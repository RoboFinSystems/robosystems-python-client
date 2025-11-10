"""Enhanced Agent Client with SSE support

Provides intelligent agent execution with automatic strategy selection.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable
from datetime import datetime

from ..api.agent.auto_select_agent import sync_detailed as auto_select_agent
from ..api.agent.execute_specific_agent import sync_detailed as execute_specific_agent
from ..models.agent_request import AgentRequest
from ..models.agent_message import AgentMessage
from .sse_client import SSEClient, SSEConfig, EventType


@dataclass
class AgentQueryRequest:
  """Request object for agent queries"""

  message: str
  history: Optional[list] = None
  context: Optional[Dict[str, Any]] = None
  mode: Optional[str] = None  # 'quick', 'standard', 'extended', 'streaming'
  enable_rag: Optional[bool] = None
  force_extended_analysis: Optional[bool] = None


@dataclass
class AgentOptions:
  """Options for agent execution"""

  mode: Optional[str] = "auto"  # 'auto', 'sync', 'async'
  max_wait: Optional[int] = None
  on_progress: Optional[Callable[[str, Optional[int]], None]] = None


@dataclass
class AgentResult:
  """Result from agent execution"""

  content: str
  agent_used: str
  mode_used: str
  metadata: Optional[Dict[str, Any]] = None
  tokens_used: Optional[Dict[str, int]] = None
  confidence_score: Optional[float] = None
  execution_time: Optional[float] = None
  timestamp: Optional[str] = None


@dataclass
class QueuedAgentResponse:
  """Response when agent execution is queued"""

  status: str
  operation_id: str
  message: str
  sse_endpoint: Optional[str] = None


class QueuedAgentError(Exception):
  """Exception thrown when agent execution is queued and maxWait is 0"""

  def __init__(self, queue_info: QueuedAgentResponse):
    super().__init__("Agent execution was queued")
    self.queue_info = queue_info


class AgentClient:
  """Enhanced agent client with SSE streaming support"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")
    self.sse_client: Optional[SSEClient] = None

  def execute_query(
    self,
    graph_id: str,
    request: AgentQueryRequest,
    options: AgentOptions = None,
  ) -> AgentResult:
    """Execute agent query with automatic agent selection"""
    if options is None:
      options = AgentOptions()

    # Build request data
    agent_request = AgentRequest(
      message=request.message,
      history=[
        AgentMessage(role=msg["role"], content=msg["content"])
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
      response = auto_select_agent(
        graph_id=graph_id,
        client=client,
        body=agent_request,
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
          has_content = "content" in data and "agent_used" in data
        else:
          has_content = hasattr(data, "content") and hasattr(data, "agent_used")

        if has_content:
          # Extract data from either dict or attrs object
          if isinstance(data, dict):
            return AgentResult(
              content=data["content"],
              agent_used=data["agent_used"],
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

            return AgentResult(
              content=data.content if data.content is not UNSET else "",
              agent_used=data.agent_used if data.agent_used is not UNSET else "unknown",
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

        # Check if this is a queued response (async Celery execution)
        is_queued = False
        queued_response = None

        if isinstance(data, dict):
          is_queued = "operation_id" in data
          if is_queued:
            queued_response = QueuedAgentResponse(
              status=data.get("status", "queued"),
              operation_id=data["operation_id"],
              message=data.get("message", "Agent execution queued"),
              sse_endpoint=data.get("sse_endpoint"),
            )
        else:
          is_queued = hasattr(data, "operation_id")
          if is_queued:
            from ..types import UNSET

            queued_response = QueuedAgentResponse(
              status=data.status if hasattr(data, "status") else "queued",
              operation_id=data.operation_id,
              message=data.message
              if hasattr(data, "message") and data.message is not UNSET
              else "Agent execution queued",
              sse_endpoint=data.sse_endpoint
              if hasattr(data, "sse_endpoint") and data.sse_endpoint is not UNSET
              else None,
            )

        if is_queued and queued_response:
          # If user doesn't want to wait, raise with queue info
          if options.max_wait == 0:
            raise QueuedAgentError(queued_response)

          # Use SSE to monitor the operation
          return self._wait_for_agent_completion(queued_response.operation_id, options)

    except Exception as e:
      if isinstance(e, QueuedAgentError):
        raise

      error_msg = str(e)
      # Check for authentication errors
      if (
        "401" in error_msg or "403" in error_msg or "unauthorized" in error_msg.lower()
      ):
        raise Exception(f"Authentication failed during agent execution: {error_msg}")
      else:
        raise Exception(f"Agent execution failed: {error_msg}")

    # Unexpected response format
    raise Exception("Unexpected response format from agent endpoint")

  def execute_agent(
    self,
    graph_id: str,
    agent_type: str,
    request: AgentQueryRequest,
    options: AgentOptions = None,
  ) -> AgentResult:
    """Execute specific agent type"""
    if options is None:
      options = AgentOptions()

    # Build request data
    agent_request = AgentRequest(
      message=request.message,
      history=[
        AgentMessage(role=msg["role"], content=msg["content"])
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
      response = execute_specific_agent(
        graph_id=graph_id,
        agent_type=agent_type,
        client=client,
        body=agent_request,
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
          has_content = "content" in data and "agent_used" in data
        else:
          has_content = hasattr(data, "content") and hasattr(data, "agent_used")

        if has_content:
          # Extract data from either dict or attrs object
          if isinstance(data, dict):
            return AgentResult(
              content=data["content"],
              agent_used=data["agent_used"],
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

            return AgentResult(
              content=data.content if data.content is not UNSET else "",
              agent_used=data.agent_used if data.agent_used is not UNSET else "unknown",
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
            queued_response = QueuedAgentResponse(
              status=data.get("status", "queued"),
              operation_id=data["operation_id"],
              message=data.get("message", "Agent execution queued"),
              sse_endpoint=data.get("sse_endpoint"),
            )
        else:
          is_queued = hasattr(data, "operation_id")
          if is_queued:
            from ..types import UNSET

            queued_response = QueuedAgentResponse(
              status=data.status if hasattr(data, "status") else "queued",
              operation_id=data.operation_id,
              message=data.message
              if hasattr(data, "message") and data.message is not UNSET
              else "Agent execution queued",
              sse_endpoint=data.sse_endpoint
              if hasattr(data, "sse_endpoint") and data.sse_endpoint is not UNSET
              else None,
            )

        if is_queued and queued_response:
          # If user doesn't want to wait, raise with queue info
          if options.max_wait == 0:
            raise QueuedAgentError(queued_response)

          # Use SSE to monitor the operation
          return self._wait_for_agent_completion(queued_response.operation_id, options)

    except Exception as e:
      if isinstance(e, QueuedAgentError):
        raise

      error_msg = str(e)
      if (
        "401" in error_msg or "403" in error_msg or "unauthorized" in error_msg.lower()
      ):
        raise Exception(f"Authentication failed during agent execution: {error_msg}")
      else:
        raise Exception(f"Agent execution failed: {error_msg}")

    # Unexpected response format
    raise Exception("Unexpected response format from agent endpoint")

  def _wait_for_agent_completion(
    self, operation_id: str, options: AgentOptions
  ) -> AgentResult:
    """Wait for agent completion and return final result"""
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

    def on_agent_started(data):
      if options.on_progress:
        options.on_progress(f"Agent {data.get('agent_type')} started", 0)

    def on_agent_initialized(data):
      if options.on_progress:
        options.on_progress(f"{data.get('agent_name')} initialized", 10)

    def on_agent_completed(data):
      nonlocal result, completed
      result = AgentResult(
        content=data.get("content", ""),
        agent_used=data.get("agent_used", "unknown"),
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
        agent_result = data.get("result", data)
        result = AgentResult(
          content=agent_result.get("content", ""),
          agent_used=agent_result.get("agent_used", "unknown"),
          mode_used=agent_result.get("mode_used", "standard"),
          metadata=agent_result.get("metadata"),
          tokens_used=agent_result.get("tokens_used"),
          confidence_score=agent_result.get("confidence_score"),
          execution_time=agent_result.get("execution_time"),
          timestamp=agent_result.get("timestamp", datetime.now().isoformat()),
        )
        completed = True

    def on_error(err):
      nonlocal error, completed
      error = Exception(err.get("message", err.get("error", "Unknown error")))
      completed = True

    def on_cancelled():
      nonlocal error, completed
      error = Exception("Agent execution cancelled")
      completed = True

    # Register event handlers
    sse_client.on(EventType.OPERATION_PROGRESS.value, on_progress)
    sse_client.on("agent_started", on_agent_started)
    sse_client.on("agent_initialized", on_agent_initialized)
    sse_client.on("progress", on_progress)
    sse_client.on("agent_completed", on_agent_completed)
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
  ) -> AgentResult:
    """Convenience method for simple agent queries with auto-selection"""
    request = AgentQueryRequest(message=message, context=context)
    return self.execute_query(graph_id, request, AgentOptions(mode="auto"))

  def analyze_financials(
    self,
    graph_id: str,
    message: str,
    on_progress: Optional[Callable[[str, Optional[int]], None]] = None,
  ) -> AgentResult:
    """Execute financial agent for financial analysis"""
    request = AgentQueryRequest(message=message)
    return self.execute_agent(
      graph_id, "financial", request, AgentOptions(on_progress=on_progress)
    )

  def research(
    self,
    graph_id: str,
    message: str,
    on_progress: Optional[Callable[[str, Optional[int]], None]] = None,
  ) -> AgentResult:
    """Execute research agent for deep research"""
    request = AgentQueryRequest(message=message)
    return self.execute_agent(
      graph_id, "research", request, AgentOptions(on_progress=on_progress)
    )

  def rag(
    self,
    graph_id: str,
    message: str,
    on_progress: Optional[Callable[[str, Optional[int]], None]] = None,
  ) -> AgentResult:
    """Execute RAG agent for fast retrieval"""
    request = AgentQueryRequest(message=message)
    return self.execute_agent(
      graph_id, "rag", request, AgentOptions(on_progress=on_progress)
    )

  def close(self):
    """Cancel any active SSE connections"""
    if self.sse_client:
      self.sse_client.close()
      self.sse_client = None
