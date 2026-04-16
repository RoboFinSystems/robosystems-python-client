"""Unit tests for AgentClient."""

import pytest
from unittest.mock import Mock, patch
from robosystems_client.clients.agent_client import (
  AgentClient,
  AgentQueryRequest,
  AgentOptions,
  AgentResult,
  QueuedAgentResponse,
  QueuedAgentError,
)


@pytest.mark.unit
class TestAgentDataclasses:
  """Test suite for agent-related dataclasses."""

  def test_agent_query_request(self):
    """Test AgentQueryRequest dataclass."""
    request = AgentQueryRequest(
      message="What is the revenue?",
      history=[{"role": "user", "content": "Hello"}],
      context={"fiscal_year": 2024},
      mode="standard",
      enable_rag=True,
      force_extended_analysis=False,
    )

    assert request.message == "What is the revenue?"
    assert len(request.history) == 1
    assert request.context == {"fiscal_year": 2024}
    assert request.mode == "standard"
    assert request.enable_rag is True
    assert request.force_extended_analysis is False

  def test_agent_query_request_defaults(self):
    """Test AgentQueryRequest default values."""
    request = AgentQueryRequest(message="Simple query")

    assert request.message == "Simple query"
    assert request.history is None
    assert request.context is None
    assert request.mode is None
    assert request.enable_rag is None
    assert request.force_extended_analysis is None

  def test_agent_options_defaults(self):
    """Test AgentOptions default values."""
    options = AgentOptions()

    assert options.mode == "auto"
    assert options.max_wait is None
    assert options.on_progress is None

  def test_agent_options_custom(self):
    """Test AgentOptions with custom values."""
    progress_fn = Mock()
    options = AgentOptions(mode="sync", max_wait=30, on_progress=progress_fn)

    assert options.mode == "sync"
    assert options.max_wait == 30
    assert options.on_progress is progress_fn

  def test_agent_result(self):
    """Test AgentResult dataclass."""
    result = AgentResult(
      content="Revenue is $1B",
      agent_used="financial",
      mode_used="standard",
      metadata={"graph_id": "g-123"},
      tokens_used={"input": 100, "output": 50},
      confidence_score=0.95,
      execution_time=1.5,
      timestamp="2025-01-15T10:00:00Z",
    )

    assert result.content == "Revenue is $1B"
    assert result.agent_used == "financial"
    assert result.mode_used == "standard"
    assert result.confidence_score == 0.95
    assert result.execution_time == 1.5

  def test_agent_result_defaults(self):
    """Test AgentResult with minimal fields."""
    result = AgentResult(content="Answer", agent_used="rag", mode_used="quick")

    assert result.metadata is None
    assert result.tokens_used is None
    assert result.confidence_score is None
    assert result.execution_time is None
    assert result.timestamp is None

  def test_queued_agent_response(self):
    """Test QueuedAgentResponse dataclass."""
    response = QueuedAgentResponse(
      status="queued",
      operation_id="op-agent-1",
      message="Agent execution queued",
      sse_endpoint="/v1/operations/op-agent-1/stream",
    )

    assert response.status == "queued"
    assert response.operation_id == "op-agent-1"
    assert response.message == "Agent execution queued"
    assert response.sse_endpoint == "/v1/operations/op-agent-1/stream"

  def test_queued_agent_response_defaults(self):
    """Test QueuedAgentResponse defaults."""
    response = QueuedAgentResponse(
      status="queued", operation_id="op-1", message="Queued"
    )

    assert response.sse_endpoint is None

  def test_queued_agent_error(self):
    """Test QueuedAgentError exception."""
    queue_info = QueuedAgentResponse(
      status="queued", operation_id="op-err", message="Queued"
    )
    error = QueuedAgentError(queue_info)

    assert str(error) == "Agent execution was queued"
    assert error.queue_info.operation_id == "op-err"


@pytest.mark.unit
class TestAgentClientInit:
  """Test suite for AgentClient initialization."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = AgentClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}
    assert client.sse_client is None

  def test_close_without_sse(self, mock_config):
    """Test close when no SSE client exists."""
    client = AgentClient(mock_config)
    client.close()  # Should not raise

  def test_close_with_sse(self, mock_config):
    """Test close cleans up SSE client."""
    client = AgentClient(mock_config)
    client.sse_client = Mock()
    client.close()

    assert client.sse_client is None


@pytest.mark.unit
class TestAgentExecuteQuery:
  """Test suite for AgentClient.execute_query method."""

  @patch("robosystems_client.clients.agent_client.auto_select_agent")
  def test_execute_query_dict_response(self, mock_auto, mock_config, graph_id):
    """Test execute_query with dict response."""
    mock_resp = Mock()
    mock_resp.parsed = {
      "content": "Revenue is $1B for FY2024.",
      "agent_used": "financial",
      "mode_used": "standard",
      "metadata": {},
      "tokens_used": {"input": 100, "output": 50},
      "confidence_score": 0.9,
      "execution_time": 2.5,
      "timestamp": "2025-01-15T10:00:00Z",
    }
    mock_auto.return_value = mock_resp

    client = AgentClient(mock_config)
    request = AgentQueryRequest(message="What is revenue?")
    result = client.execute_query(graph_id, request)

    assert result.content == "Revenue is $1B for FY2024."
    assert result.agent_used == "financial"
    assert result.confidence_score == 0.9

  @patch("robosystems_client.clients.agent_client.auto_select_agent")
  def test_execute_query_queued_max_wait_zero(self, mock_auto, mock_config, graph_id):
    """Test execute_query raises QueuedAgentError when max_wait=0."""
    mock_resp = Mock()
    mock_resp.parsed = {
      "operation_id": "op-queued",
      "status": "queued",
      "message": "Agent execution queued",
    }
    mock_auto.return_value = mock_resp

    client = AgentClient(mock_config)
    request = AgentQueryRequest(message="Complex query")
    options = AgentOptions(max_wait=0)

    with pytest.raises(QueuedAgentError) as exc_info:
      client.execute_query(graph_id, request, options)

    assert exc_info.value.queue_info.operation_id == "op-queued"

  @patch("robosystems_client.clients.agent_client.auto_select_agent")
  def test_execute_query_no_token(self, mock_auto, mock_config, graph_id):
    """Test execute_query fails without token."""
    mock_config["token"] = None
    client = AgentClient(mock_config)
    request = AgentQueryRequest(message="test")

    with pytest.raises(Exception, match="Authentication failed|No API key"):
      client.execute_query(graph_id, request)

  @patch("robosystems_client.clients.agent_client.auto_select_agent")
  def test_execute_query_auth_error(self, mock_auto, mock_config, graph_id):
    """Test execute_query wraps 401 errors."""
    mock_auto.side_effect = Exception("401 Unauthorized")

    client = AgentClient(mock_config)
    request = AgentQueryRequest(message="test")

    with pytest.raises(Exception, match="Authentication failed"):
      client.execute_query(graph_id, request)

  @patch("robosystems_client.clients.agent_client.auto_select_agent")
  def test_execute_query_generic_error(self, mock_auto, mock_config, graph_id):
    """Test execute_query wraps generic errors."""
    mock_auto.side_effect = Exception("Connection timeout")

    client = AgentClient(mock_config)
    request = AgentQueryRequest(message="test")

    with pytest.raises(Exception, match="Agent execution failed"):
      client.execute_query(graph_id, request)


@pytest.mark.unit
class TestAgentExecuteSpecific:
  """Test suite for AgentClient.execute_agent method."""

  @patch("robosystems_client.clients.agent_client.execute_specific_agent")
  def test_execute_specific_agent(self, mock_exec, mock_config, graph_id):
    """Test executing a specific agent type."""
    mock_resp = Mock()
    mock_resp.parsed = {
      "content": "Deep analysis of financials.",
      "agent_used": "financial",
      "mode_used": "extended",
    }
    mock_exec.return_value = mock_resp

    client = AgentClient(mock_config)
    request = AgentQueryRequest(message="Analyze financials")
    result = client.execute_agent(graph_id, "financial", request)

    assert result.content == "Deep analysis of financials."
    assert result.agent_used == "financial"

  @patch("robosystems_client.clients.agent_client.execute_specific_agent")
  def test_execute_specific_agent_queued(self, mock_exec, mock_config, graph_id):
    """Test specific agent returns queued response."""
    mock_resp = Mock()
    mock_resp.parsed = {
      "operation_id": "op-specific-queued",
      "status": "queued",
      "message": "Queued for processing",
    }
    mock_exec.return_value = mock_resp

    client = AgentClient(mock_config)
    request = AgentQueryRequest(message="Heavy analysis")
    options = AgentOptions(max_wait=0)

    with pytest.raises(QueuedAgentError) as exc_info:
      client.execute_agent(graph_id, "research", request, options)

    assert exc_info.value.queue_info.operation_id == "op-specific-queued"


@pytest.mark.unit
class TestAgentConvenienceMethods:
  """Test suite for convenience methods."""

  @patch.object(AgentClient, "execute_query")
  def test_query_convenience(self, mock_exec, mock_config, graph_id):
    """Test query() convenience method."""
    mock_exec.return_value = AgentResult(
      content="Answer", agent_used="rag", mode_used="quick"
    )

    client = AgentClient(mock_config)
    result = client.query(graph_id, "What is X?")

    assert result.content == "Answer"
    mock_exec.assert_called_once()

  @patch.object(AgentClient, "execute_agent")
  def test_analyze_financials_convenience(self, mock_exec, mock_config, graph_id):
    """Test analyze_financials() convenience method."""
    mock_exec.return_value = AgentResult(
      content="Financial analysis", agent_used="financial", mode_used="standard"
    )

    client = AgentClient(mock_config)
    result = client.analyze_financials(graph_id, "Analyze revenue trends")

    assert result.agent_used == "financial"
    call_args = mock_exec.call_args
    assert call_args[0][1] == "financial"  # agent_type

  @patch.object(AgentClient, "execute_agent")
  def test_research_convenience(self, mock_exec, mock_config, graph_id):
    """Test research() convenience method."""
    mock_exec.return_value = AgentResult(
      content="Research results", agent_used="research", mode_used="extended"
    )

    client = AgentClient(mock_config)
    result = client.research(graph_id, "Deep dive into market")

    assert result.agent_used == "research"
    call_args = mock_exec.call_args
    assert call_args[0][1] == "research"

  @patch.object(AgentClient, "execute_agent")
  def test_rag_convenience(self, mock_exec, mock_config, graph_id):
    """Test rag() convenience method."""
    mock_exec.return_value = AgentResult(
      content="RAG answer", agent_used="rag", mode_used="quick"
    )

    client = AgentClient(mock_config)
    result = client.rag(graph_id, "Quick lookup")

    assert result.agent_used == "rag"
    call_args = mock_exec.call_args
    assert call_args[0][1] == "rag"
