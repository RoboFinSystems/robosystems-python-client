"""Operation Client for monitoring long-running operations

Provides comprehensive operation monitoring with SSE support.
"""

import logging
from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable, List, cast
from datetime import datetime
from enum import Enum

from .sse_client import SSEClient, AsyncSSEClient, SSEConfig, EventType
from .token_utils import resolve_auth_headers

logger = logging.getLogger(__name__)


class OperationStatus(Enum):
  """Standard operation statuses"""

  PENDING = "pending"
  QUEUED = "queued"
  RUNNING = "running"
  COMPLETED = "completed"
  FAILED = "failed"
  CANCELLED = "cancelled"


@dataclass
class OperationProgress:
  """Progress information for an operation"""

  message: str
  percentage: Optional[float] = None
  current_step: Optional[int] = None
  total_steps: Optional[int] = None
  timestamp: Optional[datetime] = None

  def __post_init__(self):
    if self.timestamp is None:
      self.timestamp = datetime.now()


@dataclass
class OperationResult:
  """Result from an operation"""

  operation_id: str
  status: OperationStatus
  result: Optional[Any] = None
  error: Optional[str] = None
  progress: Optional[List[OperationProgress]] = None
  started_at: Optional[datetime] = None
  completed_at: Optional[datetime] = None
  execution_time_ms: Optional[int] = None

  def __post_init__(self):
    if self.progress is None:
      self.progress = []


@dataclass
class MonitorOptions:
  """Options for operation monitoring"""

  on_progress: Optional[Callable[[OperationProgress], None]] = None
  on_queue_update: Optional[Callable[[int, int], None]] = None
  timeout: Optional[int] = None
  poll_interval: Optional[int] = None


def _parsed_dict(parsed: Any) -> Dict[str, Any] | None:
  """Body of a generated operations response as a plain dict.

  The operations endpoints are declared as free-form objects, so the
  generator emits models whose only field is ``additional_properties``
  — attribute access on them raises, whatever the payload contained.
  ``to_dict()`` is the accessor that works, and is what
  ``operator_client._poll_for_completion`` already uses.
  """
  if parsed is None:
    return None
  if hasattr(parsed, "to_dict"):
    return cast(Dict[str, Any], parsed.to_dict())
  if isinstance(parsed, dict):
    return cast(Dict[str, Any], parsed)
  return None


class OperationClient:
  """Client for monitoring operations via SSE"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = dict(config.get("headers") or {})
    # Get token from config if passed by parent
    self.token = config.get("token")
    # Propagate the API key into SSE headers — SSE requests bypass the
    # AuthenticatedClient used by the generated REST methods, so the token
    # must be injected explicitly or the /stream endpoint returns 401.
    if self.token and "X-API-Key" not in self.headers:
      self.headers["X-API-Key"] = self.token
    self.active_operations: Dict[str, SSEClient] = {}
    # Thread safety for operations tracking
    import threading

    self._lock = threading.Lock()

  def monitor_operation(
    self, operation_id: str, options: MonitorOptions = None
  ) -> OperationResult:
    """Monitor a single operation until completion

    The SSE stream will replay all events from the beginning (from_sequence=0),
    so even if the operation completed before we connected, we'll still receive
    all events including the completion event.
    """
    if options is None:
      options = MonitorOptions()

    result = OperationResult(operation_id=operation_id, status=OperationStatus.PENDING)
    completed = False
    error = None

    # Set up SSE connection with event replay from the beginning
    # This handles the race condition where the operation may have already completed.
    # Headers are resolved per connect so a rotated JWT reaches the stream.
    sse_config = SSEConfig(
      base_url=self.base_url, headers=resolve_auth_headers(self.config)
    )
    sse_client = SSEClient(sse_config)

    def on_operation_started(data):
      result.status = OperationStatus.RUNNING
      result.started_at = datetime.now()

    def on_operation_progress(data):
      progress = OperationProgress(
        message=data.get("message", "Processing..."),
        percentage=data.get("percentage"),
        current_step=data.get("current_step"),
        total_steps=data.get("total_steps"),
      )
      result.progress.append(progress)

      if options.on_progress:
        options.on_progress(progress)

    def on_queue_update(data):
      result.status = OperationStatus.QUEUED
      if options.on_queue_update:
        options.on_queue_update(
          data.get("position", 0), data.get("estimated_wait_seconds", 0)
        )

    def on_operation_completed(data):
      nonlocal completed
      result.status = OperationStatus.COMPLETED
      result.result = data.get("result")
      result.completed_at = datetime.now()
      result.execution_time_ms = data.get("execution_time_ms")
      completed = True

    def on_operation_error(err):
      nonlocal completed, error
      result.status = OperationStatus.FAILED
      result.error = err.get("message", err.get("error", "Unknown error"))
      result.completed_at = datetime.now()
      error = Exception(result.error)
      completed = True

    def on_operation_cancelled():
      nonlocal completed
      result.status = OperationStatus.CANCELLED
      result.completed_at = datetime.now()
      completed = True

    def on_connection_error(err):
      nonlocal completed, error
      result.status = OperationStatus.FAILED
      result.error = str(err)
      result.completed_at = datetime.now()
      error = err if isinstance(err, Exception) else Exception(str(err))
      completed = True

    # Register event handlers
    sse_client.on(EventType.OPERATION_STARTED.value, on_operation_started)
    sse_client.on(EventType.OPERATION_PROGRESS.value, on_operation_progress)
    sse_client.on(EventType.QUEUE_UPDATE.value, on_queue_update)
    sse_client.on(EventType.OPERATION_COMPLETED.value, on_operation_completed)
    sse_client.on(EventType.OPERATION_ERROR.value, on_operation_error)
    sse_client.on(EventType.OPERATION_CANCELLED.value, on_operation_cancelled)
    # Surface transport-level errors (bad status, dropped connection,
    # max retries exceeded) so the wait loop terminates instead of hanging.
    sse_client.on("error", on_connection_error)
    sse_client.on("max_retries_exceeded", on_connection_error)

    # Connect and monitor
    try:
      sse_client.connect(operation_id)
      with self._lock:
        self.active_operations[operation_id] = sse_client

      # Wait for completion
      import time

      start_time = datetime.now()
      while not completed:
        if error:
          raise error

        # Check timeout
        if options.timeout:
          elapsed = (datetime.now() - start_time).total_seconds()
          if elapsed > options.timeout:
            sse_client.close()
            raise TimeoutError(
              f"Operation {operation_id} timed out after {options.timeout}s"
            )

        time.sleep(options.poll_interval or 0.1)

    finally:
      # Clean up with thread safety
      with self._lock:
        if operation_id in self.active_operations:
          self.active_operations[operation_id].close()
          del self.active_operations[operation_id]

    return result

  def get_operation_status(self, operation_id: str) -> Dict[str, Any]:
    """Get current status of an operation (sync API call)"""
    # This would use the generated SDK to call /v1/operations/{operation_id}/status
    from ..api.operations.get_operation_status import (
      sync_detailed as get_operation_status,
    )
    from .retry import retrying_client

    # Plain Client with the headers current now (`token_provider` wins).
    client = retrying_client(
      base_url=self.base_url,
      headers=resolve_auth_headers(self.config),
      config=self.config,
    )
    try:
      # Auth travels in self.headers (X-API-Key / Authorization). The generated
      # function takes no `token` kwarg — passing one raised TypeError, which
      # the handler below laundered into a fake {"status": "error"} result, so
      # this call never succeeded whenever a token was configured.
      #
      # Read through `to_dict()`, not attributes: the second incarnation of
      # that same bug was `response.parsed.status` raising AttributeError on
      # an additional-properties model, laundered into the same fake result
      # for *every* response — including successful ones.
      response = get_operation_status(operation_id=operation_id, client=client)
      payload = _parsed_dict(response.parsed)
      if payload is not None:
        return {
          "operation_id": operation_id,
          "status": payload.get("status", "unknown"),
          "progress": payload.get("progress"),
          "result": payload.get("result"),
          "error": payload.get("error"),
        }
    except Exception as e:
      # Logged rather than silently shaped into a result: swallowing here is
      # what hid the TypeError above for as long as it lived.
      logger.warning("Failed to get status for operation %s: %s", operation_id, e)
      return {"operation_id": operation_id, "status": "error", "error": str(e)}

    return {"operation_id": operation_id, "status": "unknown"}

  def cancel_operation(self, operation_id: str) -> bool:
    """Cancel an operation"""
    # This would use the generated SDK to call /v1/operations/{operation_id}/cancel
    from ..api.operations.cancel_operation import sync_detailed as cancel_operation
    from .retry import retrying_client

    # Plain Client with the headers current now (`token_provider` wins).
    client = retrying_client(
      base_url=self.base_url,
      headers=resolve_auth_headers(self.config),
      config=self.config,
    )
    try:
      # See get_operation_status: no `token` kwarg, and the body is read
      # through `to_dict()` because attribute access always raises.
      response = cancel_operation(operation_id=operation_id, client=client)
      payload = _parsed_dict(response.parsed)
      cancelled = bool(payload.get("cancelled")) if payload is not None else False
    except Exception as e:
      logger.warning("Failed to cancel operation %s: %s", operation_id, e)
      return False

    # Close any active SSE connection with thread safety. This used to sit
    # after an early `return` on the success path, so the one case that
    # needs it — the cancel actually landed — was the one case that skipped
    # it, leaking the stream.
    with self._lock:
      if operation_id in self.active_operations:
        self.active_operations[operation_id].close()
        del self.active_operations[operation_id]

    return cancelled

  def list_operations(self) -> List[Dict[str, Any]]:
    """List all operations (if supported by the API)"""
    # This would be implemented if the API supports listing operations
    return []

  def close_all(self):
    """Close all active operation monitors"""
    with self._lock:
      for sse_client in self.active_operations.values():
        sse_client.close()
      self.active_operations.clear()

  def close_operation(self, operation_id: str):
    """Close monitoring for a specific operation"""
    with self._lock:
      if operation_id in self.active_operations:
        self.active_operations[operation_id].close()
        del self.active_operations[operation_id]


class AsyncOperationClient:
  """Async version of the operation client"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = dict(config.get("headers") or {})
    self.token = config.get("token")
    if self.token and "X-API-Key" not in self.headers:
      self.headers["X-API-Key"] = self.token
    self.active_operations: Dict[str, AsyncSSEClient] = {}

  async def monitor_operation(
    self, operation_id: str, options: MonitorOptions = None
  ) -> OperationResult:
    """Monitor a single operation until completion (async)"""
    if options is None:
      options = MonitorOptions()

    result = OperationResult(operation_id=operation_id, status=OperationStatus.PENDING)
    completed = False
    error = None

    # Set up SSE connection; headers resolved per connect so a rotated JWT
    # reaches the stream.
    sse_config = SSEConfig(
      base_url=self.base_url, headers=resolve_auth_headers(self.config)
    )
    sse_client = AsyncSSEClient(sse_config)

    def on_operation_started(data):
      result.status = OperationStatus.RUNNING
      result.started_at = datetime.now()

    def on_operation_progress(data):
      progress = OperationProgress(
        message=data.get("message", "Processing..."),
        percentage=data.get("percentage"),
        current_step=data.get("current_step"),
        total_steps=data.get("total_steps"),
      )
      result.progress.append(progress)

      if options.on_progress:
        options.on_progress(progress)

    def on_queue_update(data):
      result.status = OperationStatus.QUEUED
      if options.on_queue_update:
        options.on_queue_update(
          data.get("position", 0), data.get("estimated_wait_seconds", 0)
        )

    def on_operation_completed(data):
      nonlocal completed
      result.status = OperationStatus.COMPLETED
      result.result = data.get("result")
      result.completed_at = datetime.now()
      result.execution_time_ms = data.get("execution_time_ms")
      completed = True

    def on_operation_error(err):
      nonlocal completed, error
      result.status = OperationStatus.FAILED
      result.error = err.get("message", err.get("error", "Unknown error"))
      result.completed_at = datetime.now()
      error = Exception(result.error)
      completed = True

    def on_operation_cancelled():
      nonlocal completed
      result.status = OperationStatus.CANCELLED
      result.completed_at = datetime.now()
      completed = True

    def on_connection_error(err):
      nonlocal completed, error
      result.status = OperationStatus.FAILED
      result.error = str(err)
      result.completed_at = datetime.now()
      error = err if isinstance(err, Exception) else Exception(str(err))
      completed = True

    # Register event handlers
    sse_client.on(EventType.OPERATION_STARTED.value, on_operation_started)
    sse_client.on(EventType.OPERATION_PROGRESS.value, on_operation_progress)
    sse_client.on(EventType.QUEUE_UPDATE.value, on_queue_update)
    sse_client.on(EventType.OPERATION_COMPLETED.value, on_operation_completed)
    sse_client.on(EventType.OPERATION_ERROR.value, on_operation_error)
    sse_client.on(EventType.OPERATION_CANCELLED.value, on_operation_cancelled)
    # Surface transport-level errors (bad status, dropped connection,
    # max retries exceeded) so the wait loop terminates instead of hanging.
    sse_client.on("error", on_connection_error)
    sse_client.on("max_retries_exceeded", on_connection_error)

    # Connect and monitor
    try:
      await sse_client.connect(operation_id)
      self.active_operations[operation_id] = sse_client

      # Wait for completion
      import asyncio

      start_time = datetime.now()
      while not completed:
        if error:
          raise error

        # Check timeout
        if options.timeout:
          elapsed = (datetime.now() - start_time).total_seconds()
          if elapsed > options.timeout:
            await sse_client.close()
            raise TimeoutError(
              f"Operation {operation_id} timed out after {options.timeout}s"
            )

        await asyncio.sleep(options.poll_interval or 0.1)

    finally:
      # Clean up
      if operation_id in self.active_operations:
        await self.active_operations[operation_id].close()
        del self.active_operations[operation_id]

    return result

  async def get_operation_status(self, operation_id: str) -> Dict[str, Any]:
    """Get current status of an operation (async API call)"""
    # Would use async version of the generated client
    pass

  async def cancel_operation(self, operation_id: str) -> bool:
    """Cancel an operation (async)"""
    # Would use async version of the generated client
    pass

  async def close_all(self):
    """Close all active operation monitors (async)"""
    for sse_client in self.active_operations.values():
      await sse_client.close()
    self.active_operations.clear()

  async def close_operation(self, operation_id: str):
    """Close monitoring for a specific operation (async)"""
    if operation_id in self.active_operations:
      await self.active_operations[operation_id].close()
      del self.active_operations[operation_id]
