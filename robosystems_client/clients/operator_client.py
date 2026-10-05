"""Enhanced AI Operator Client with SSE support

Provides intelligent operator execution with automatic strategy selection.
"""

import json
import time
from dataclasses import dataclass
from typing import Dict, Any, List, Optional, Callable, cast
from datetime import datetime

from ..api.operator.auto_select_operator import sync_detailed as auto_select_operator
from ..api.operator.execute_specific_operator import (
  sync_detailed as execute_specific_operator,
)
from ..api.operations.get_operation_status import (
  sync_detailed as get_operation_status,
)
from ..client import Client
from .retry import retrying_client
from ..models.operator_request import OperatorRequest
from ..models.operator_message import OperatorMessage
from ..models.response_mode import ResponseMode
from ..types import UNSET, Unset
from .sse_client import SSEClient, SSEConfig, EventType, event_error_message
from .token_utils import resolve_auth_headers, resolve_config_token

# Seconds between `/status` polls while following a run whose stream gave
# no verdict. Mirrors the TypeScript client's `pollIntervalMs` default.
DEFAULT_POLL_INTERVAL_SECONDS = 2.0

# Consecutive `/status` failures tolerated before the fallback gives up: one
# transient network error must not lose a run that is still going.
MAX_CONSECUTIVE_POLL_FAILURES = 3


@dataclass
class OperatorQueryRequest:
  """Request object for operator queries"""

  message: str
  history: Optional[list] = None
  context: Optional[Dict[str, Any]] = None
  mode: Optional[str] = None  # 'quick', 'standard', 'extended', 'streaming'
  enable_rag: Optional[bool] = None
  force_extended_analysis: Optional[bool] = None


@dataclass
class OperatorOptions:
  """Options for operator execution"""

  mode: Optional[str] = "auto"  # 'auto', 'sync', 'async'
  max_wait: Optional[int] = None
  on_progress: Optional[Callable[[str, Optional[int]], None]] = None
  # Seconds between `/v1/operations/{id}/status` polls while the client
  # follows a queued run its stream gave no verdict for. Only the fallback
  # path uses it; defaults to DEFAULT_POLL_INTERVAL_SECONDS.
  poll_interval: Optional[float] = None


@dataclass
class OperatorResult:
  """Result from operator execution"""

  content: str
  operator_used: str
  mode_used: str
  metadata: Optional[Dict[str, Any]] = None
  tokens_used: Optional[Dict[str, int]] = None
  confidence_score: Optional[float] = None
  execution_time: Optional[float] = None
  timestamp: Optional[str] = None
  # Present when the API reports a failed run inside an otherwise successful
  # response (credit pre-flight, operator timeouts, cancelled runs); `content`
  # then carries the explanation rather than an answer.
  error_details: Optional[Dict[str, Any]] = None


def _operator_result(data: Dict[str, Any]) -> OperatorResult:
  """Shape an operator payload into the public result.

  The `operator_completed` event, the generic completion event's `result`,
  and the `/status` `result` all carry the same fields — one mapper keeps
  them consistent.
  """
  return OperatorResult(
    content=data.get("content") or "",
    operator_used=data.get("operator_used") or "unknown",
    mode_used=data.get("mode_used") or "standard",
    metadata=data.get("metadata"),
    tokens_used=data.get("tokens_used"),
    confidence_score=data.get("confidence_score"),
    execution_time=data.get("execution_time"),
    timestamp=data.get("timestamp") or datetime.now().isoformat(),
    error_details=data.get("error_details"),
  )


@dataclass
class QueuedOperatorResponse:
  """Response when operator execution is queued"""

  status: str
  operation_id: str
  message: str
  sse_endpoint: Optional[str] = None


class _PollAbort(Exception):
  """Internal: a `/status` verdict that must not be retried."""


def _response_detail(response: Any) -> str:
  """Human-readable detail of a non-200 generated-client response."""
  parsed = getattr(response, "parsed", None)
  detail = getattr(parsed, "detail", None)
  if isinstance(detail, str) and detail:
    return detail
  content = getattr(response, "content", b"")
  if isinstance(content, bytes):
    text = content.decode("utf-8", errors="replace")
  else:
    text = str(content or "")
  return text[:200] or "empty response"


def _status_code(response: Any) -> Optional[int]:
  """The HTTP status of a generated-client response, when it carries one."""
  code = getattr(response, "status_code", None)
  return int(code) if isinstance(code, int) else None


def _response_body(response: Any) -> Optional[Dict[str, Any]]:
  """The JSON body of an operator response as a dict.

  The generated parser yields ``None`` for a 202, so its body (the queued
  operation and its links) is read off the raw content instead.
  """
  parsed = getattr(response, "parsed", None)
  if isinstance(parsed, dict):
    return parsed
  if parsed is not None and hasattr(parsed, "to_dict"):
    body = parsed.to_dict()
    if isinstance(body, dict):
      return body
  content = getattr(response, "content", None)
  if isinstance(content, (bytes, str)) and content:
    try:
      body = json.loads(content)
    except ValueError:
      return None
    return body if isinstance(body, dict) else None
  return None


def _response_mode(mode: Optional[str]) -> ResponseMode | Unset:
  """`OperatorOptions.mode` as the endpoint's `?mode=` value, when it is one."""
  try:
    return ResponseMode(mode) if mode else UNSET
  except ValueError:
    return UNSET


def _wrap_call_error(error: Exception) -> Exception:
  """A transport-level failure of the operator call, labelled for the caller."""
  error_msg = str(error)
  if "401" in error_msg or "403" in error_msg or "unauthorized" in error_msg.lower():
    return Exception(f"Authentication failed during operator execution: {error_msg}")
  return Exception(f"Operator execution failed: {error_msg}")


def _read_writes(source: Any) -> List[Dict[str, Any]]:
  """The `writes` a stopped run had already landed, from whichever payload has them."""
  writes = source.get("writes") if isinstance(source, dict) else None
  if not isinstance(writes, list):
    return []
  return [w for w in writes if isinstance(w, dict)]


class OperatorRunError(Exception):
  """A run that failed or was cancelled.

  ``writes`` lists what the run had already changed on the graph before it
  stopped, so a caller can show a receipt rather than invite a retry that
  repeats them. ``status`` is ``"failed"`` or ``"cancelled"``.
  """

  def __init__(
    self,
    message: str,
    status: str,
    writes: Optional[List[Dict[str, Any]]] = None,
    operation_id: Optional[str] = None,
  ):
    super().__init__(message)
    self.message = message
    self.status = status
    self.writes: List[Dict[str, Any]] = list(writes or [])
    self.operation_id = operation_id


class QueuedOperatorError(Exception):
  """Exception thrown when operator execution is queued and maxWait is 0"""

  def __init__(self, queue_info: QueuedOperatorResponse):
    super().__init__("Operator execution was queued")
    self.queue_info = queue_info


class OperatorClient:
  """Enhanced AI Operator client with SSE streaming support"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")
    self.sse_client: Optional[SSEClient] = None

  def _rest_client(self) -> Client:
    """A REST client for one call, carrying the credential current now.

    Resolved per call — `token_provider` wins over the static token — so a
    rotated JWT is picked up without rebuilding the facade, the same way the
    GraphQL facades do it.
    """
    if not resolve_config_token(self.config):
      raise Exception("No API key provided. Set X-API-Key in headers.")
    return retrying_client(
      base_url=self.base_url,
      headers=resolve_auth_headers(self.config),
      config=self.config,
    )

  def _sse_config(self) -> SSEConfig:
    """Stream config for one connect; headers carry the credential current now."""
    return SSEConfig(base_url=self.base_url, headers=resolve_auth_headers(self.config))

  def execute_query(
    self,
    graph_id: str,
    request: OperatorQueryRequest,
    options: OperatorOptions = None,
  ) -> OperatorResult:
    """Execute operator query with automatic operator selection"""
    if options is None:
      options = OperatorOptions()

    # Build request data
    operator_request = OperatorRequest(
      message=request.message,
      history=[
        OperatorMessage(role=msg["role"], content=msg["content"])
        for msg in (request.history or [])
      ],
      context=request.context,
      mode=request.mode,
      enable_rag=request.enable_rag,
      force_extended_analysis=request.force_extended_analysis,
    )

    # Execute through the generated client, with the credential current now
    client = self._rest_client()

    try:
      response = auto_select_operator(
        graph_id=graph_id,
        client=client,
        body=operator_request,
        mode=_response_mode(options.mode),
      )
    except Exception as e:
      raise _wrap_call_error(e) from e

    return self._settle(response, options)

  def execute_operator(
    self,
    graph_id: str,
    operator_type: str,
    request: OperatorQueryRequest,
    options: OperatorOptions = None,
  ) -> OperatorResult:
    """Execute specific operator type"""
    if options is None:
      options = OperatorOptions()

    # Build request data
    operator_request = OperatorRequest(
      message=request.message,
      history=[
        OperatorMessage(role=msg["role"], content=msg["content"])
        for msg in (request.history or [])
      ],
      context=request.context,
      mode=request.mode,
      enable_rag=request.enable_rag,
      force_extended_analysis=request.force_extended_analysis,
    )

    # Execute through the generated client, with the credential current now
    client = self._rest_client()

    try:
      response = execute_specific_operator(
        graph_id=graph_id,
        operator_type=operator_type,
        client=client,
        body=operator_request,
        mode=_response_mode(options.mode),
      )
    except Exception as e:
      raise _wrap_call_error(e) from e

    return self._settle(response, options)

  def _settle(self, response: Any, options: OperatorOptions) -> OperatorResult:
    """Resolve an operator endpoint response.

    A 200 body is the result. A 202 carries the queued operation's links
    — the generated parser yields ``None`` for it, so the body is read off
    the raw response — and is followed to completion.
    """
    code = _status_code(response)
    if code is not None and code >= 400:
      detail = _response_detail(response)
      if code in (401, 403):
        raise Exception(
          f"Authentication failed during operator execution: {code}: {detail}"
        )
      raise Exception(f"Operator execution failed: {code}: {detail}")

    data = _response_body(response)
    if data is None:
      raise Exception("Unexpected response format from operator endpoint")

    if "content" in data and "operator_used" in data:
      return _operator_result(data)

    if data.get("operation_id"):
      links = data.get("_links") or {}
      queued_response = QueuedOperatorResponse(
        status=data.get("status") or "queued",
        operation_id=data["operation_id"],
        message=data.get("message") or "Operator execution queued",
        sse_endpoint=data.get("sse_endpoint") or links.get("stream"),
      )
      if options.max_wait == 0:
        raise QueuedOperatorError(queued_response)
      return self._wait_for_operator_completion(queued_response.operation_id, options)

    raise Exception("Unexpected response format from operator endpoint")

  def _wait_for_operator_completion(
    self, operation_id: str, options: OperatorOptions
  ) -> OperatorResult:
    """Follow a queued run to its result: over the stream, else over `/status`."""
    result: Optional[OperatorResult] = None
    error: Optional[Exception] = None
    completed = False
    transport_error: Optional[Exception] = None

    # Headers are resolved per connect so a rotated JWT reaches the stream.
    sse_client = SSEClient(self._sse_config())
    self.sse_client = sse_client

    def on_progress(data):
      if options.on_progress:
        percent = data.get("progress_percent")
        if percent is None:
          percent = data.get("percentage")
        options.on_progress(data.get("message", "Processing..."), percent)

    def on_operator_started(data):
      if options.on_progress:
        options.on_progress(f"Agent {data.get('operator_type')} started", 0)

    def on_operator_initialized(data):
      if options.on_progress:
        options.on_progress(f"{data.get('operator_name')} initialized", 10)

    def on_operator_completed(data):
      nonlocal result, completed
      result = _operator_result(data)
      completed = True

    def on_completed(data):
      nonlocal result, completed
      if not result:
        # Fallback to generic completion event
        result = _operator_result(data.get("result") or data)
        completed = True

    def on_error(err):
      # The run itself failed — a verdict, not a transport problem.
      nonlocal error, completed
      details = err.get("error_details") if isinstance(err, dict) else None
      error = OperatorRunError(
        event_error_message(err), "failed", _read_writes(details), operation_id
      )
      completed = True

    def on_cancelled(_data=None):
      nonlocal error, completed
      error = OperatorRunError(
        "Operator execution cancelled", "cancelled", [], operation_id
      )
      completed = True

    def on_transport_error(err):
      # The stream could not open (401/403/404/429) or its reconnects ran
      # out. That is not a verdict on the run; `/status` gives one below.
      nonlocal transport_error
      transport_error = (
        err if isinstance(err, Exception) else Exception(event_error_message(err))
      )

    # Register event handlers
    sse_client.on(EventType.OPERATION_PROGRESS.value, on_progress)
    sse_client.on("operator_started", on_operator_started)
    sse_client.on("operator_initialized", on_operator_initialized)
    sse_client.on("progress", on_progress)
    sse_client.on("operator_completed", on_operator_completed)
    sse_client.on(EventType.OPERATION_COMPLETED.value, on_completed)
    sse_client.on(EventType.OPERATION_ERROR.value, on_error)
    sse_client.on(EventType.OPERATION_CANCELLED.value, on_cancelled)
    sse_client.on("error", on_transport_error)
    sse_client.on("max_retries_exceeded", on_transport_error)

    # connect() is blocking: it returns once the stream has ended, or right
    # away when the stream never opened.
    try:
      sse_client.connect(operation_id)
    finally:
      sse_client.close()
      if self.sse_client is sse_client:
        self.sse_client = None

    if completed and error is not None:
      raise error
    if result is not None:
      return result

    # No verdict from the stream: it never opened, its reconnects ran out, or
    # it ended before a terminal event. The run is already queued and
    # finishes regardless, so follow it over `/status` instead of losing it.
    return self._poll_for_completion(operation_id, options, transport_error)

  def _poll_for_completion(
    self,
    operation_id: str,
    options: OperatorOptions,
    stream_error: Optional[Exception],
  ) -> OperatorResult:
    """Follow a queued run over `/v1/operations/{id}/status` until it settles.

    Used when the stream gave no verdict; `stream_error` is folded into the
    failure message if polling cannot reach one either.
    """
    interval = (
      options.poll_interval
      if options.poll_interval is not None
      else DEFAULT_POLL_INTERVAL_SECONDS
    )
    stream_detail = (
      str(stream_error) if stream_error else "stream ended before a terminal event"
    )
    consecutive_failures = 0

    if options.on_progress:
      options.on_progress("Live progress unavailable — waiting for the result", None)

    while True:
      try:
        response = get_operation_status(
          operation_id=operation_id, client=self._rest_client()
        )
        code = int(response.status_code)
        parsed = response.parsed
        if code != 200 or parsed is None:
          detail = _response_detail(response)
          # A definitive 4xx (expired, not ours, unauthenticated) ends the
          # wait; anything else is treated as transient and retried below.
          if 400 <= code < 500 and code != 429:
            raise _PollAbort(
              f"Operator stream failed ({stream_detail}); "
              f"status check failed ({code}: {detail})"
            )
          raise RuntimeError(f"{code}: {detail}")
        status: Dict[str, Any] = (
          parsed.to_dict()
          if hasattr(parsed, "to_dict")
          else cast(Dict[str, Any], parsed)
        )
        consecutive_failures = 0
      except _PollAbort as abort:
        raise Exception(str(abort)) from None
      except Exception as poll_error:
        consecutive_failures += 1
        if consecutive_failures >= MAX_CONSECUTIVE_POLL_FAILURES:
          raise Exception(
            f"Operator stream failed ({stream_detail}); "
            f"status polling failed ({poll_error})"
          ) from poll_error
        time.sleep(interval)
        continue

      state = status.get("status")
      if state == "completed":
        return _operator_result(status.get("result") or {})
      if state == "failed":
        raise OperatorRunError(
          status.get("error") or status.get("message") or "Operator run failed",
          "failed",
          _read_writes(status),
          operation_id,
        )
      if state == "cancelled":
        raise OperatorRunError(
          "Operator execution cancelled",
          "cancelled",
          _read_writes(status.get("result")),
          operation_id,
        )
      if options.on_progress and status.get("message"):
        options.on_progress(status["message"], None)
      time.sleep(interval)

  def query(
    self, graph_id: str, message: str, context: Dict[str, Any] = None
  ) -> OperatorResult:
    """Convenience method for simple operator queries with auto-selection"""
    request = OperatorQueryRequest(message=message, context=context)
    return self.execute_query(graph_id, request, OperatorOptions(mode="auto"))

  def close(self):
    """Cancel any active SSE connections"""
    if self.sse_client:
      self.sse_client.close()
      self.sse_client = None
