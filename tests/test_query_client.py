"""Unit tests for QueryClient."""

import pytest
from robosystems_client.extensions.query_client import (
  QueryClient,
  QueryRequest,
  QueryOptions,
  QueryResult,
  QueuedQueryResponse,
  QueuedQueryError,
)


@pytest.mark.unit
class TestQueryClient:
  """Test suite for QueryClient."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = QueryClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}
    assert client.sse_client is None

  def test_query_result_dataclass(self):
    """Test QueryResult dataclass creation."""
    result = QueryResult(
      data=[{"name": "test"}],
      columns=["name"],
      row_count=1,
      execution_time_ms=100,
      graph_id="graph-123",
    )

    assert result.data == [{"name": "test"}]
    assert result.columns == ["name"]
    assert result.row_count == 1
    assert result.execution_time_ms == 100
    assert result.graph_id == "graph-123"

  def test_query_request_dataclass(self):
    """Test QueryRequest dataclass creation."""
    request = QueryRequest(
      query="MATCH (n) RETURN n", parameters={"limit": 10}, timeout=5000
    )

    assert request.query == "MATCH (n) RETURN n"
    assert request.parameters == {"limit": 10}
    assert request.timeout == 5000

  def test_query_request_defaults(self):
    """Test QueryRequest with default values."""
    request = QueryRequest(query="MATCH (n) RETURN n")

    assert request.query == "MATCH (n) RETURN n"
    assert request.parameters is None
    assert request.timeout is None

  def test_query_options_defaults(self):
    """Test QueryOptions with default values."""
    options = QueryOptions()

    assert options.mode == "auto"
    assert options.chunk_size is None
    assert options.test_mode is None
    assert options.max_wait is None

  def test_query_options_custom(self):
    """Test QueryOptions with custom values."""
    options = QueryOptions(mode="sync", chunk_size=100, test_mode=True, max_wait=5000)

    assert options.mode == "sync"
    assert options.chunk_size == 100
    assert options.test_mode is True
    assert options.max_wait == 5000

  def test_queued_query_response_dataclass(self):
    """Test QueuedQueryResponse dataclass."""
    response = QueuedQueryResponse(
      status="queued",
      operation_id="op-123",
      queue_position=5,
      estimated_wait_seconds=30,
      message="Query queued",
    )

    assert response.status == "queued"
    assert response.operation_id == "op-123"
    assert response.queue_position == 5
    assert response.estimated_wait_seconds == 30
    assert response.message == "Query queued"

  def test_queued_query_error(self):
    """Test QueuedQueryError exception."""
    queue_info = QueuedQueryResponse(
      status="queued",
      operation_id="op-123",
      queue_position=3,
      estimated_wait_seconds=15,
      message="Query queued",
    )

    error = QueuedQueryError(queue_info)

    assert error.queue_info.queue_position == 3
    assert error.queue_info.estimated_wait_seconds == 15
    assert str(error) == "Query was queued"

  def test_close_without_sse_client(self, mock_config):
    """Test that close works when no SSE client exists."""
    client = QueryClient(mock_config)

    # Should not raise any exceptions
    client.close()
