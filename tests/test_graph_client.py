"""Unit tests for GraphClient."""

import pytest
from unittest.mock import Mock, MagicMock, patch
from robosystems_client.extensions.graph_client import (
  GraphClient,
  GraphMetadata,
  InitialEntityData,
  GraphInfo,
)


@pytest.mark.unit
class TestGraphClient:
  """Test suite for GraphClient."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = GraphClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}

  def test_graph_metadata_dataclass(self):
    """Test GraphMetadata dataclass."""
    metadata = GraphMetadata(
      graph_name="Test Graph",
      description="A test graph",
      schema_extensions=["custom_prop"],
      tags=["test", "demo"],
    )

    assert metadata.graph_name == "Test Graph"
    assert metadata.description == "A test graph"
    assert metadata.schema_extensions == ["custom_prop"]
    assert metadata.tags == ["test", "demo"]

  def test_graph_metadata_defaults(self):
    """Test GraphMetadata default values."""
    metadata = GraphMetadata(graph_name="Simple Graph")

    assert metadata.graph_name == "Simple Graph"
    assert metadata.description is None
    assert metadata.schema_extensions is None
    assert metadata.tags is None

  def test_initial_entity_data_dataclass(self):
    """Test InitialEntityData dataclass."""
    entity = InitialEntityData(
      name="ACME Corp",
      uri="https://example.com/acme",
      category="Technology",
      sic="7372",
      sic_description="Prepackaged Software",
    )

    assert entity.name == "ACME Corp"
    assert entity.uri == "https://example.com/acme"
    assert entity.category == "Technology"
    assert entity.sic == "7372"
    assert entity.sic_description == "Prepackaged Software"

  def test_initial_entity_data_defaults(self):
    """Test InitialEntityData default values."""
    entity = InitialEntityData(name="Basic Entity", uri="https://example.com")

    assert entity.name == "Basic Entity"
    assert entity.uri == "https://example.com"
    assert entity.category is None
    assert entity.sic is None
    assert entity.sic_description is None

  def test_graph_info_dataclass(self):
    """Test GraphInfo dataclass."""
    info = GraphInfo(
      graph_id="graph-123",
      graph_name="Production Graph",
      description="Production knowledge graph",
      schema_extensions=["prop1", "prop2"],
      tags=["prod"],
      created_at="2024-01-15T10:30:00Z",
      status="active",
    )

    assert info.graph_id == "graph-123"
    assert info.graph_name == "Production Graph"
    assert info.description == "Production knowledge graph"
    assert info.schema_extensions == ["prop1", "prop2"]
    assert info.tags == ["prod"]
    assert info.created_at == "2024-01-15T10:30:00Z"
    assert info.status == "active"

  def test_graph_info_minimal(self):
    """Test GraphInfo with minimal data."""
    info = GraphInfo(graph_id="graph-456", graph_name="Minimal Graph")

    assert info.graph_id == "graph-456"
    assert info.graph_name == "Minimal Graph"
    assert info.description is None
    assert info.schema_extensions is None
    assert info.tags is None
    assert info.created_at is None
    assert info.status is None

  def test_close_method(self, mock_config):
    """Test that close method exists and can be called."""
    client = GraphClient(mock_config)

    # Should not raise any exceptions
    client.close()


@pytest.mark.unit
class TestProcessSSEEvent:
  """Test suite for _process_sse_event method."""

  def test_operation_progress_with_percent(self, mock_config):
    """Test processing progress event with percentage."""
    client = GraphClient(mock_config)
    progress_messages = []

    result = client._process_sse_event(
      "operation_progress",
      '{"message": "Processing data", "progress_percent": 50}',
      lambda msg: progress_messages.append(msg),
    )

    assert result is None  # Should continue waiting
    assert progress_messages == ["Processing data (50%)"]

  def test_operation_progress_without_percent(self, mock_config):
    """Test processing progress event without percentage."""
    client = GraphClient(mock_config)
    progress_messages = []

    result = client._process_sse_event(
      "operation_progress",
      '{"message": "Initializing..."}',
      lambda msg: progress_messages.append(msg),
    )

    assert result is None
    assert progress_messages == ["Initializing..."]

  def test_operation_progress_default_message(self, mock_config):
    """Test progress event with missing message uses default."""
    client = GraphClient(mock_config)
    progress_messages = []

    result = client._process_sse_event(
      "operation_progress",
      "{}",
      lambda msg: progress_messages.append(msg),
    )

    assert result is None
    assert progress_messages == ["Processing..."]

  def test_operation_progress_no_callback(self, mock_config):
    """Test progress event without callback doesn't error."""
    client = GraphClient(mock_config)

    result = client._process_sse_event(
      "operation_progress",
      '{"message": "Processing", "progress_percent": 75}',
      None,
    )

    assert result is None

  def test_operation_completed_returns_graph_id(self, mock_config):
    """Test completed event returns graph_id."""
    client = GraphClient(mock_config)
    progress_messages = []

    result = client._process_sse_event(
      "operation_completed",
      '{"result": {"graph_id": "graph-123"}}',
      lambda msg: progress_messages.append(msg),
    )

    assert result == "graph-123"
    assert progress_messages == ["Graph created: graph-123"]

  def test_operation_completed_no_graph_id_raises(self, mock_config):
    """Test completed event without graph_id raises error."""
    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="no graph_id in result"):
      client._process_sse_event(
        "operation_completed",
        '{"result": {}}',
        None,
      )

  def test_operation_completed_empty_result_raises(self, mock_config):
    """Test completed event with empty result raises error."""
    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="no graph_id in result"):
      client._process_sse_event(
        "operation_completed",
        "{}",
        None,
      )

  def test_operation_error_raises(self, mock_config):
    """Test error event raises RuntimeError with message."""
    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="Graph creation failed: Database error"):
      client._process_sse_event(
        "operation_error",
        '{"error": "Database error"}',
        None,
      )

  def test_operation_error_default_message(self, mock_config):
    """Test error event with missing error uses default."""
    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="Graph creation failed: Unknown error"):
      client._process_sse_event(
        "operation_error",
        "{}",
        None,
      )

  def test_operation_cancelled_raises(self, mock_config):
    """Test cancelled event raises RuntimeError with reason."""
    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="Graph creation cancelled: User requested"):
      client._process_sse_event(
        "operation_cancelled",
        '{"reason": "User requested"}',
        None,
      )

  def test_operation_cancelled_default_reason(self, mock_config):
    """Test cancelled event with missing reason uses default."""
    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="Operation was cancelled"):
      client._process_sse_event(
        "operation_cancelled",
        "{}",
        None,
      )

  def test_unknown_event_type_ignored(self, mock_config):
    """Test unknown event types are ignored."""
    client = GraphClient(mock_config)

    result = client._process_sse_event(
      "keepalive",
      "{}",
      None,
    )

    assert result is None

  def test_invalid_json_ignored(self, mock_config):
    """Test invalid JSON is gracefully ignored."""
    client = GraphClient(mock_config)

    result = client._process_sse_event(
      "operation_progress",
      "not valid json",
      None,
    )

    assert result is None

  def test_operation_completed_non_dict_result(self, mock_config):
    """Test completed event with non-dict result raises error."""
    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="no graph_id in result"):
      client._process_sse_event(
        "operation_completed",
        '{"result": "some string"}',
        None,
      )


@pytest.mark.unit
class TestWaitWithSSE:
  """Test suite for _wait_with_sse method."""

  def _create_mock_response(self, lines, status_code=200):
    """Helper to create a mock streaming response."""
    mock_response = MagicMock()
    mock_response.status_code = status_code
    mock_response.iter_lines.return_value = iter(lines)
    mock_response.__enter__ = Mock(return_value=mock_response)
    mock_response.__exit__ = Mock(return_value=False)
    return mock_response

  def _create_mock_client(self, mock_response):
    """Helper to create a mock httpx client."""
    mock_client = MagicMock()
    mock_client.stream.return_value = mock_response
    mock_client.__enter__ = Mock(return_value=mock_client)
    mock_client.__exit__ = Mock(return_value=False)
    return mock_client

  @patch("robosystems_client.extensions.graph_client.httpx.Client")
  def test_sse_successful_completion(self, mock_httpx_client, mock_config):
    """Test SSE stream completes successfully with graph_id."""
    sse_lines = [
      "event: operation_progress",
      'data: {"message": "Starting", "progress_percent": 0}',
      "",
      "event: operation_progress",
      'data: {"message": "Processing", "progress_percent": 50}',
      "",
      "event: operation_completed",
      'data: {"result": {"graph_id": "graph-456"}}',
      "",
    ]

    mock_response = self._create_mock_response(sse_lines)
    mock_client = self._create_mock_client(mock_response)
    mock_httpx_client.return_value = mock_client

    client = GraphClient(mock_config)
    progress_messages = []

    result = client._wait_with_sse(
      "op-123",
      timeout=60,
      on_progress=lambda msg: progress_messages.append(msg),
    )

    assert result == "graph-456"
    assert "Starting (0%)" in progress_messages
    assert "Processing (50%)" in progress_messages
    assert "Graph created: graph-456" in progress_messages

  @patch("robosystems_client.extensions.graph_client.httpx.Client")
  def test_sse_connection_failure(self, mock_httpx_client, mock_config):
    """Test SSE raises error on non-200 response."""
    mock_response = self._create_mock_response([], status_code=503)
    mock_client = self._create_mock_client(mock_response)
    mock_httpx_client.return_value = mock_client

    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="SSE connection failed: 503"):
      client._wait_with_sse("op-123", timeout=60, on_progress=None)

  @patch("robosystems_client.extensions.graph_client.httpx.Client")
  def test_sse_operation_error(self, mock_httpx_client, mock_config):
    """Test SSE handles operation error event."""
    sse_lines = [
      "event: operation_error",
      'data: {"error": "Validation failed"}',
      "",
    ]

    mock_response = self._create_mock_response(sse_lines)
    mock_client = self._create_mock_client(mock_response)
    mock_httpx_client.return_value = mock_client

    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="Graph creation failed: Validation failed"):
      client._wait_with_sse("op-123", timeout=60, on_progress=None)

  @patch("robosystems_client.extensions.graph_client.httpx.Client")
  def test_sse_stream_ends_without_completion(self, mock_httpx_client, mock_config):
    """Test SSE raises timeout if stream ends without completion."""
    sse_lines = [
      "event: operation_progress",
      'data: {"message": "Processing"}',
      "",
    ]

    mock_response = self._create_mock_response(sse_lines)
    mock_client = self._create_mock_client(mock_response)
    mock_httpx_client.return_value = mock_client

    client = GraphClient(mock_config)

    with pytest.raises(TimeoutError, match="SSE stream ended without completion"):
      client._wait_with_sse("op-123", timeout=60, on_progress=None)

  @patch("robosystems_client.extensions.graph_client.httpx.Client")
  @patch("robosystems_client.extensions.graph_client.time.time")
  def test_sse_timeout_during_stream(self, mock_time, mock_httpx_client, mock_config):
    """Test SSE raises timeout during long stream."""
    # Simulate time passing: start at 0, then jump past timeout
    mock_time.side_effect = [0, 0, 0, 100]  # Start, then timeout check fails

    sse_lines = [
      "event: operation_progress",
      'data: {"message": "Processing"}',
      "",
      "event: operation_progress",  # This line triggers timeout check
      'data: {"message": "Still going"}',
      "",
    ]

    mock_response = self._create_mock_response(sse_lines)
    mock_client = self._create_mock_client(mock_response)
    mock_httpx_client.return_value = mock_client

    client = GraphClient(mock_config)

    with pytest.raises(TimeoutError, match="timed out after"):
      client._wait_with_sse("op-123", timeout=60, on_progress=None)

  @patch("robosystems_client.extensions.graph_client.httpx.Client")
  def test_sse_ignores_comments_and_other_lines(self, mock_httpx_client, mock_config):
    """Test SSE ignores comment lines and other non-event lines."""
    sse_lines = [
      ": this is a comment",
      "id: 12345",
      "retry: 5000",
      "event: operation_completed",
      'data: {"result": {"graph_id": "graph-789"}}',
      "",
    ]

    mock_response = self._create_mock_response(sse_lines)
    mock_client = self._create_mock_client(mock_response)
    mock_httpx_client.return_value = mock_client

    client = GraphClient(mock_config)

    result = client._wait_with_sse("op-123", timeout=60, on_progress=None)

    assert result == "graph-789"

  @patch("robosystems_client.extensions.graph_client.httpx.Client")
  def test_sse_uses_correct_url_and_headers(self, mock_httpx_client, mock_config):
    """Test SSE constructs correct URL and headers."""
    sse_lines = [
      "event: operation_completed",
      'data: {"result": {"graph_id": "graph-test"}}',
      "",
    ]

    mock_response = self._create_mock_response(sse_lines)
    mock_client = self._create_mock_client(mock_response)
    mock_httpx_client.return_value = mock_client

    client = GraphClient(mock_config)
    client._wait_with_sse("op-999", timeout=60, on_progress=None)

    # Verify stream was called with correct URL and headers
    mock_client.stream.assert_called_once_with(
      "GET",
      "http://localhost:8000/v1/operations/op-999/stream",
      headers={"X-API-Key": "test-api-key", "Accept": "text/event-stream"},
    )


@pytest.mark.unit
class TestWaitWithPolling:
  """Test suite for _wait_with_polling method."""

  def _create_mock_status_response(self, status, result=None, error=None):
    """Helper to create a mock status response."""
    mock_response = Mock()
    mock_response.parsed = {
      "status": status,
      "result": result or {},
    }
    if error:
      mock_response.parsed["error"] = error
    return mock_response

  @patch("robosystems_client.extensions.graph_client.time.sleep")
  def test_polling_successful_completion(self, mock_sleep, mock_config):
    """Test polling completes successfully on completed status."""
    mock_client = Mock()

    with patch(
      "robosystems_client.extensions.graph_client.GraphClient._wait_with_polling"
    ) as original:
      # Call the real method but mock the API call
      original.side_effect = lambda *args, **kwargs: "graph-poll-123"

      client = GraphClient(mock_config)
      result = client._wait_with_polling(
        "op-123", timeout=60, poll_interval=2, on_progress=None, client=mock_client
      )

      assert result == "graph-poll-123"

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  @patch("robosystems_client.extensions.graph_client.time.sleep")
  def test_polling_with_dict_response(self, mock_sleep, mock_get_status, mock_config):
    """Test polling handles dict response format."""
    mock_client = Mock()

    # First call: pending, second call: completed
    mock_get_status.side_effect = [
      Mock(parsed={"status": "pending"}),
      Mock(parsed={"status": "completed", "result": {"graph_id": "graph-dict-123"}}),
    ]

    client = GraphClient(mock_config)
    progress_messages = []

    result = client._wait_with_polling(
      "op-123",
      timeout=60,
      poll_interval=2,
      on_progress=lambda msg: progress_messages.append(msg),
      client=mock_client,
    )

    assert result == "graph-dict-123"
    assert mock_sleep.call_count == 2
    assert any("completed" in msg.lower() for msg in progress_messages)

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  @patch("robosystems_client.extensions.graph_client.time.sleep")
  def test_polling_failed_status(self, mock_sleep, mock_get_status, mock_config):
    """Test polling raises error on failed status."""
    mock_client = Mock()

    mock_get_status.return_value = Mock(
      parsed={"status": "failed", "error": "Processing error"}
    )

    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="Graph creation failed: Processing error"):
      client._wait_with_polling(
        "op-123", timeout=60, poll_interval=2, on_progress=None, client=mock_client
      )

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  @patch("robosystems_client.extensions.graph_client.time.sleep")
  def test_polling_timeout(self, mock_sleep, mock_get_status, mock_config):
    """Test polling raises timeout after max attempts."""
    mock_client = Mock()

    # Always return pending
    mock_get_status.return_value = Mock(parsed={"status": "pending"})

    client = GraphClient(mock_config)

    with pytest.raises(TimeoutError, match="timed out after"):
      client._wait_with_polling(
        "op-123", timeout=6, poll_interval=2, on_progress=None, client=mock_client
      )

    # Should have made 3 attempts (6 // 2)
    assert mock_get_status.call_count == 3

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  @patch("robosystems_client.extensions.graph_client.time.sleep")
  def test_polling_completed_no_graph_id(
    self, mock_sleep, mock_get_status, mock_config
  ):
    """Test polling raises error when completed but no graph_id."""
    mock_client = Mock()

    mock_get_status.return_value = Mock(parsed={"status": "completed", "result": {}})

    client = GraphClient(mock_config)

    with pytest.raises(RuntimeError, match="no graph_id in result"):
      client._wait_with_polling(
        "op-123", timeout=60, poll_interval=2, on_progress=None, client=mock_client
      )

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  @patch("robosystems_client.extensions.graph_client.time.sleep")
  def test_polling_skips_empty_response(self, mock_sleep, mock_get_status, mock_config):
    """Test polling continues when response.parsed is None."""
    mock_client = Mock()

    mock_get_status.side_effect = [
      Mock(parsed=None),  # Empty response, should continue
      Mock(parsed={"status": "completed", "result": {"graph_id": "graph-skip-123"}}),
    ]

    client = GraphClient(mock_config)

    result = client._wait_with_polling(
      "op-123", timeout=60, poll_interval=2, on_progress=None, client=mock_client
    )

    assert result == "graph-skip-123"
    assert mock_get_status.call_count == 2

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  @patch("robosystems_client.extensions.graph_client.time.sleep")
  def test_polling_with_object_response(self, mock_sleep, mock_get_status, mock_config):
    """Test polling handles object response with additional_properties."""
    mock_client = Mock()

    # Create object-like response
    mock_parsed = Mock()
    mock_parsed.additional_properties = {
      "status": "completed",
      "result": {"graph_id": "graph-obj-123"},
    }
    del mock_parsed.status  # Ensure it uses additional_properties path

    mock_get_status.return_value = Mock(parsed=mock_parsed)

    client = GraphClient(mock_config)

    result = client._wait_with_polling(
      "op-123", timeout=60, poll_interval=2, on_progress=None, client=mock_client
    )

    assert result == "graph-obj-123"


@pytest.mark.unit
class TestSSEFallback:
  """Test suite for SSE fallback behavior in create_graph_and_wait."""

  @patch.object(GraphClient, "_wait_with_polling")
  @patch.object(GraphClient, "_wait_with_sse")
  @patch("robosystems_client.client.AuthenticatedClient")
  @patch("robosystems_client.api.graphs.create_graph.sync_detailed")
  def test_sse_failure_falls_back_to_polling(
    self, mock_create, mock_auth_client, mock_sse, mock_polling, mock_config
  ):
    """Test that SSE failure triggers fallback to polling."""
    # Setup create_graph to return operation_id
    mock_response = Mock()
    mock_response.parsed = Mock()
    mock_response.parsed.graph_id = None
    mock_response.parsed.operation_id = "op-fallback-123"
    mock_create.return_value = mock_response

    # SSE fails
    mock_sse.side_effect = RuntimeError("SSE connection refused")

    # Polling succeeds
    mock_polling.return_value = "graph-fallback-456"

    client = GraphClient(mock_config)
    progress_messages = []

    result = client.create_graph_and_wait(
      metadata=GraphMetadata(graph_name="Test Graph"),
      on_progress=lambda msg: progress_messages.append(msg),
    )

    assert result == "graph-fallback-456"
    mock_sse.assert_called_once()
    mock_polling.assert_called_once()
    assert any("polling" in msg.lower() for msg in progress_messages)

  @patch.object(GraphClient, "_wait_with_polling")
  @patch.object(GraphClient, "_wait_with_sse")
  @patch("robosystems_client.client.AuthenticatedClient")
  @patch("robosystems_client.api.graphs.create_graph.sync_detailed")
  def test_use_sse_false_skips_sse(
    self, mock_create, mock_auth_client, mock_sse, mock_polling, mock_config
  ):
    """Test that use_sse=False skips SSE entirely."""
    mock_response = Mock()
    mock_response.parsed = Mock()
    mock_response.parsed.graph_id = None
    mock_response.parsed.operation_id = "op-no-sse-123"
    mock_create.return_value = mock_response

    mock_polling.return_value = "graph-no-sse-456"

    client = GraphClient(mock_config)

    result = client.create_graph_and_wait(
      metadata=GraphMetadata(graph_name="Test Graph"),
      use_sse=False,
    )

    assert result == "graph-no-sse-456"
    mock_sse.assert_not_called()
    mock_polling.assert_called_once()

  @patch.object(GraphClient, "_wait_with_polling")
  @patch.object(GraphClient, "_wait_with_sse")
  @patch("robosystems_client.client.AuthenticatedClient")
  @patch("robosystems_client.api.graphs.create_graph.sync_detailed")
  def test_sse_success_does_not_call_polling(
    self, mock_create, mock_auth_client, mock_sse, mock_polling, mock_config
  ):
    """Test that successful SSE does not trigger polling."""
    mock_response = Mock()
    mock_response.parsed = Mock()
    mock_response.parsed.graph_id = None
    mock_response.parsed.operation_id = "op-sse-only-123"
    mock_create.return_value = mock_response

    mock_sse.return_value = "graph-sse-only-456"

    client = GraphClient(mock_config)

    result = client.create_graph_and_wait(
      metadata=GraphMetadata(graph_name="Test Graph"),
    )

    assert result == "graph-sse-only-456"
    mock_sse.assert_called_once()
    mock_polling.assert_not_called()

  @patch("robosystems_client.client.AuthenticatedClient")
  @patch("robosystems_client.api.graphs.create_graph.sync_detailed")
  def test_immediate_graph_id_skips_waiting(
    self, mock_create, mock_auth_client, mock_config
  ):
    """Test that immediate graph_id in response skips SSE/polling."""
    mock_response = Mock()
    mock_response.parsed = Mock()
    mock_response.parsed.graph_id = "graph-immediate-789"
    mock_response.parsed.operation_id = None
    mock_create.return_value = mock_response

    client = GraphClient(mock_config)
    progress_messages = []

    result = client.create_graph_and_wait(
      metadata=GraphMetadata(graph_name="Test Graph"),
      on_progress=lambda msg: progress_messages.append(msg),
    )

    assert result == "graph-immediate-789"
    assert "Graph created: graph-immediate-789" in progress_messages
