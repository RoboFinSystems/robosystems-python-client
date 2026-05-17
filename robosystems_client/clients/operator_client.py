"""Enhanced AI Operator Client with SSE support

Provides intelligent operator execution with automatic strategy selection.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable
from datetime import datetime

from ..api.operator.auto_select_operator import sync_detailed as auto_select_operator
from ..api.operator.execute_specific_operator import (
  sync_detailed as execute_specific_operator,
)
from ..models.operator_request import OperatorRequest
from ..models.operator_message import OperatorMessage
from .sse_client import SSEClient, SSEConfig, EventType


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


@dataclass
class QueuedOperatorResponse:
  """Response when operator execution is queued"""

  status: str
  operation_id: str
  message: str
  sse_endpoint: Optional[str] = None


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

    # Execute through the generated client
    from ..client import AuthenticatedClient

    if not self.token:
      raise Exception("No API key provided. Set X-API-Key in headers.")

    client = AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

    try:
      response = auto_select_operator(
        graph_id=graph_id,
        client=client,
        body=operator_request,
      )

      # Check response type and handle accordingly
      if hasattr(response, "parsed") and response.parsed:
        response_data = response.parsed

        # Handle both dict and attrs object responses
        if isinstance(response_data, dict):
          data = response_data
        else:
          # Response is an attrs object
          data = response_data

        # Check if this is an immediate response (sync or SSE execution)
        has_content = False
        if isinstance(data, dict):
          has_content = "content" in data and "operator_used" in data
        else:
          has_content = hasattr(data, "content") and hasattr(data, "operator_used")

        if has_content:
          # Extract data from either dict or attrs object
          if isinstance(data, dict):
            return OperatorResult(
              content=data["content"],
              operator_used=data["operator_used"],
              mode_used=data["mode_used"],
              metadata=data.get("metadata"),
              tokens_used=data.get("tokens_used"),
              confidence_score=data.get("confidence_score"),
              execution_time=data.get("execution_time"),
              timestamp=data.get("timestamp", datetime.now().isoformat()),
            )
          else:
            # attrs object - access attributes directly
            from ..types import UNSET

            return OperatorResult(
              content=data.content if data.content is not UNSET else "",
              operator_used=data.operator_used
              if data.operator_used is not UNSET
              else "unknown",
              mode_used=data.mode_used.value
              if hasattr(data.mode_used, "value")
              else data.mode_used
              if data.mode_used is not UNSET
              else "standard",
              metadata=data.metadata if data.metadata is not UNSET else None,
              tokens_used=data.tokens_used if data.tokens_used is not UNSET else None,
              confidence_score=data.confidence_score
              if data.confidence_score is not UNSET
              else None,
              execution_time=data.execution_time
              if data.execution_time is not UNSET
              else None,
              timestamp=data.timestamp
              if hasattr(data, "timestamp") and data.timestamp is not UNSET
              else datetime.now().isoformat(),
            )

        # Check if this is a queued response (async background task execution)
        is_queued = False
        queued_response = None

        if isinstance(data, dict):
          is_queued = "operation_id" in data
          if is_queued:
            queued_response = QueuedOperatorResponse(
              status=data.get("status", "queued"),
              operation_id=data["operation_id"],
              message=data.get("message", "Operator execution queued"),
              sse_endpoint=data.get("sse_endpoint"),
            )
        else:
          is_queued = hasattr(data, "operation_id")
          if is_queued:
            from ..types import UNSET

            queued_response = QueuedOperatorResponse(
              status=data.status if hasattr(data, "status") else "queued",
              operation_id=data.operation_id,
              message=data.message
              if hasattr(data, "message") and data.message is not UNSET
              else "Operator execution queued",
              sse_endpoint=data.sse_endpoint
              if hasattr(data, "sse_endpoint") and data.sse_endpoint is not UNSET
              else None,
            )

        if is_queued and queued_response:
          # If user doesn't want to wait, raise with queue info
          if options.max_wait == 0:
            raise QueuedOperatorError(queued_response)

          # Use SSE to monitor the operation
          return self._wait_for_operator_completion(
            queued_response.operation_id, options
          )

    except Exception as e:
      if isinstance(e, QueuedOperatorError):
        raise

      error_msg = str(e)
      # Check for authentication errors
      if (
        "401" in error_msg or "403" in error_msg or "unauthorized" in error_msg.lower()
      ):
        raise Exception(f"Authentication failed during operator execution: {error_msg}")
      else:
        raise Exception(f"Operator execution failed: {error_msg}")

    # Unexpected response format
    raise Exception("Unexpected response format from operator endpoint")

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

    # Execute through the generated client
    from ..client import AuthenticatedClient

    if not self.token:
      raise Exception("No API key provided. Set X-API-Key in headers.")

    client = AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

    try:
      response = execute_specific_operator(
        graph_id=graph_id,
        operator_type=operator_type,
        client=client,
        body=operator_request,
      )

      # Check response type and handle accordingly
      if hasattr(response, "parsed") and response.parsed:
        response_data = response.parsed

        # Handle both dict and attrs object responses
        if isinstance(response_data, dict):
          data = response_data
        else:
          data = response_data

        # Check if this is an immediate response
        has_content = False
        if isinstance(data, dict):
          has_content = "content" in data and "operator_used" in data
        else:
          has_content = hasattr(data, "content") and hasattr(data, "operator_used")

        if has_content:
          # Extract data from either dict or attrs object
          if isinstance(data, dict):
            return OperatorResult(
              content=data["content"],
              operator_used=data["operator_used"],
              mode_used=data["mode_used"],
              metadata=data.get("metadata"),
              tokens_used=data.get("tokens_used"),
              confidence_score=data.get("confidence_score"),
              execution_time=data.get("execution_time"),
              timestamp=data.get("timestamp", datetime.now().isoformat()),
            )
          else:
            # attrs object
            from ..types import UNSET

            return OperatorResult(
              content=data.content if data.content is not UNSET else "",
              operator_used=data.operator_used
              if data.operator_used is not UNSET
              else "unknown",
              mode_used=data.mode_used.value
              if hasattr(data.mode_used, "value")
              else data.mode_used
              if data.mode_used is not UNSET
              else "standard",
              metadata=data.metadata if data.metadata is not UNSET else None,
              tokens_used=data.tokens_used if data.tokens_used is not UNSET else None,
              confidence_score=data.confidence_score
              if data.confidence_score is not UNSET
              else None,
              execution_time=data.execution_time
              if data.execution_time is not UNSET
              else None,
              timestamp=data.timestamp
              if hasattr(data, "timestamp") and data.timestamp is not UNSET
              else datetime.now().isoformat(),
            )

        # Check if this is a queued response
        is_queued = False
        queued_response = None

        if isinstance(data, dict):
          is_queued = "operation_id" in data
          if is_queued:
            queued_response = QueuedOperatorResponse(
              status=data.get("status", "queued"),
              operation_id=data["operation_id"],
              message=data.get("message", "Operator execution queued"),
              sse_endpoint=data.get("sse_endpoint"),
            )
        else:
          is_queued = hasattr(data, "operation_id")
          if is_queued:
            from ..types import UNSET

            queued_response = QueuedOperatorResponse(
              status=data.status if hasattr(data, "status") else "queued",
              operation_id=data.operation_id,
              message=data.message
              if hasattr(data, "message") and data.message is not UNSET
              else "Operator execution queued",
              sse_endpoint=data.sse_endpoint
              if hasattr(data, "sse_endpoint") and data.sse_endpoint is not UNSET
              else None,
            )

        if is_queued and queued_response:
          # If user doesn't want to wait, raise with queue info
          if options.max_wait == 0:
            raise QueuedOperatorError(queued_response)

          # Use SSE to monitor the operation
          return self._wait_for_operator_completion(
            queued_response.operation_id, options
          )

    except Exception as e:
      if isinstance(e, QueuedOperatorError):
        raise

      error_msg = str(e)
      if (
        "401" in error_msg or "403" in error_msg or "unauthorized" in error_msg.lower()
      ):
        raise Exception(f"Authentication failed during operator execution: {error_msg}")
      else:
        raise Exception(f"Operator execution failed: {error_msg}")

    # Unexpected response format
    raise Exception("Unexpected response format from operator endpoint")

  def _wait_for_operator_completion(
    self, operation_id: str, options: OperatorOptions
  ) -> OperatorResult:
    """Wait for operator completion and return final result"""
    result = None
    error = None
    completed = False

    # Set up SSE connection
    sse_config = SSEConfig(base_url=self.base_url, headers=self.headers)
    sse_client = SSEClient(sse_config)

    def on_progress(data):
      if options.on_progress:
        options.on_progress(
          data.get("message", "Processing..."), data.get("percentage")
        )

    def on_operator_started(data):
      if options.on_progress:
        options.on_progress(f"Agent {data.get('operator_type')} started", 0)

    def on_operator_initialized(data):
      if options.on_progress:
        options.on_progress(f"{data.get('operator_name')} initialized", 10)

    def on_operator_completed(data):
      nonlocal result, completed
      result = OperatorResult(
        content=data.get("content", ""),
        operator_used=data.get("operator_used", "unknown"),
        mode_used=data.get("mode_used", "standard"),
        metadata=data.get("metadata"),
        tokens_used=data.get("tokens_used"),
        confidence_score=data.get("confidence_score"),
        execution_time=data.get("execution_time"),
        timestamp=data.get("timestamp", datetime.now().isoformat()),
      )
      completed = True

    def on_completed(data):
      nonlocal result, completed
      if not result:
        # Fallback to generic completion event
        operator_result = data.get("result", data)
        result = OperatorResult(
          content=operator_result.get("content", ""),
          operator_used=operator_result.get("operator_used", "unknown"),
          mode_used=operator_result.get("mode_used", "standard"),
          metadata=operator_result.get("metadata"),
          tokens_used=operator_result.get("tokens_used"),
          confidence_score=operator_result.get("confidence_score"),
          execution_time=operator_result.get("execution_time"),
          timestamp=operator_result.get("timestamp", datetime.now().isoformat()),
        )
        completed = True

    def on_error(err):
      nonlocal error, completed
      error = Exception(err.get("message", err.get("error", "Unknown error")))
      completed = True

    def on_cancelled():
      nonlocal error, completed
      error = Exception("Operator execution cancelled")
      completed = True

    # Register event handlers
    sse_client.on(EventType.OPERATION_PROGRESS.value, on_progress)
    sse_client.on("operator_started", on_operator_started)
    sse_client.on("operator_initialized", on_operator_initialized)
    sse_client.on("progress", on_progress)
    sse_client.on("operator_completed", on_operator_completed)
    sse_client.on(EventType.OPERATION_COMPLETED.value, on_completed)
    sse_client.on(EventType.OPERATION_ERROR.value, on_error)
    sse_client.on("error", on_error)
    sse_client.on(EventType.OPERATION_CANCELLED.value, on_cancelled)

    # Connect and wait
    sse_client.connect(operation_id)

    # Wait for completion
    import time

    while not completed:
      if error:
        sse_client.close()
        raise error
      time.sleep(0.1)

    sse_client.close()
    return result

  def query(
    self, graph_id: str, message: str, context: Dict[str, Any] = None
  ) -> OperatorResult:
    """Convenience method for simple operator queries with auto-selection"""
    request = OperatorQueryRequest(message=message, context=context)
    return self.execute_query(graph_id, request, OperatorOptions(mode="auto"))

  def analyze_financials(
    self,
    graph_id: str,
    message: str,
    on_progress: Optional[Callable[[str, Optional[int]], None]] = None,
  ) -> OperatorResult:
    """Execute financial operator for financial analysis"""
    request = OperatorQueryRequest(message=message)
    return self.execute_operator(
      graph_id, "financial", request, OperatorOptions(on_progress=on_progress)
    )

  def research(
    self,
    graph_id: str,
    message: str,
    on_progress: Optional[Callable[[str, Optional[int]], None]] = None,
  ) -> OperatorResult:
    """Execute research operator for deep research"""
    request = OperatorQueryRequest(message=message)
    return self.execute_operator(
      graph_id, "research", request, OperatorOptions(on_progress=on_progress)
    )

  def rag(
    self,
    graph_id: str,
    message: str,
    on_progress: Optional[Callable[[str, Optional[int]], None]] = None,
  ) -> OperatorResult:
    """Execute RAG operator for fast retrieval"""
    request = OperatorQueryRequest(message=message)
    return self.execute_operator(
      graph_id, "rag", request, OperatorOptions(on_progress=on_progress)
    )

  def close(self):
    """Cancel any active SSE connections"""
    if self.sse_client:
      self.sse_client.close()
      self.sse_client = None
