"""Operation Client for monitoring long-running operations

Provides comprehensive operation monitoring with SSE support.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable, List
from datetime import datetime
from enum import Enum

from .sse_client import SSEClient, AsyncSSEClient, SSEConfig, EventType


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


class OperationClient:
  """Client for monitoring operations via SSE"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    # Get token from config if passed by parent
    self.token = config.get("token")
    self.active_operations: Dict[str, SSEClient] = {}
    # Thread safety for operations tracking
    import threading

    self._lock = threading.Lock()

  def monitor_operation(
    self, operation_id: str, options: MonitorOptions = None
  ) -> OperationResult:
    """Monitor a single operation until completion"""
    if options is None:
      options = MonitorOptions()

    result = OperationResult(operation_id=operation_id, status=OperationStatus.PENDING)
    completed = False
    error = None

    # Set up SSE connection
    sse_config = SSEConfig(base_url=self.base_url)
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

    # Register event handlers
    sse_client.on(EventType.OPERATION_STARTED.value, on_operation_started)
    sse_client.on(EventType.OPERATION_PROGRESS.value, on_operation_progress)
    sse_client.on(EventType.QUEUE_UPDATE.value, on_queue_update)
    sse_client.on(EventType.OPERATION_COMPLETED.value, on_operation_completed)
    sse_client.on(EventType.OPERATION_ERROR.value, on_operation_error)
    sse_client.on(EventType.OPERATION_CANCELLED.value, on_operation_cancelled)

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
    from ..client import Client

    # Use regular Client with headers instead of AuthenticatedClient
    client = Client(base_url=self.base_url, headers=self.headers)
    try:
      kwargs = {"operation_id": operation_id, "client": client}
      # Only add token if it's a valid string
      if self.token and isinstance(self.token, str) and self.token.strip():
        kwargs["token"] = self.token
      response = get_operation_status(**kwargs)
      if response.parsed:
        return {
          "operation_id": operation_id,
          "status": response.parsed.status,
          "progress": getattr(response.parsed, "progress", None),
          "result": getattr(response.parsed, "result", None),
          "error": getattr(response.parsed, "error", None),
        }
    except Exception as e:
      return {"operation_id": operation_id, "status": "error", "error": str(e)}

    return {"operation_id": operation_id, "status": "unknown"}

  def cancel_operation(self, operation_id: str) -> bool:
    """Cancel an operation"""
    # This would use the generated SDK to call /v1/operations/{operation_id}/cancel
    from ..api.operations.cancel_operation import sync_detailed as cancel_operation
    from ..client import Client

    # Use regular Client with headers instead of AuthenticatedClient
    client = Client(base_url=self.base_url, headers=self.headers)
    try:
      kwargs = {"operation_id": operation_id, "client": client}
      # Only add token if it's a valid string
      if self.token and isinstance(self.token, str) and self.token.strip():
        kwargs["token"] = self.token
      response = cancel_operation(**kwargs)
      if response.parsed:
        return response.parsed.cancelled or False
    except Exception as e:
      print(f"Failed to cancel operation {operation_id}: {e}")
      return False

    # Also close any active SSE connection with thread safety
    with self._lock:
      if operation_id in self.active_operations:
        self.active_operations[operation_id].close()
        del self.active_operations[operation_id]

    return False

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

    # Set up SSE connection
    sse_config = SSEConfig(base_url=self.base_url)
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

    # Register event handlers
    sse_client.on(EventType.OPERATION_STARTED.value, on_operation_started)
    sse_client.on(EventType.OPERATION_PROGRESS.value, on_operation_progress)
    sse_client.on(EventType.QUEUE_UPDATE.value, on_queue_update)
    sse_client.on(EventType.OPERATION_COMPLETED.value, on_operation_completed)
    sse_client.on(EventType.OPERATION_ERROR.value, on_operation_error)
    sse_client.on(EventType.OPERATION_CANCELLED.value, on_operation_cancelled)

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
