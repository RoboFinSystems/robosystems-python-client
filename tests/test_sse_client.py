"""Unit tests for SSEClient operational logic.

Covers: connection, event processing, reconnection/retry, heartbeat,
completion-event auto-close, and close/cleanup. Dataclass and listener
tests already exist in extensions/tests/test_unit.py.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from robosystems_client.extensions.sse_client import (
  SSEClient,
  SSEConfig,
)


@pytest.fixture
def sse_config():
  return SSEConfig(
    base_url="http://localhost:8000",
    headers={"X-API-Key": "test-key"},
    max_retries=3,
    retry_delay=100,
    timeout=10,
  )


@pytest.fixture
def sse_client(sse_config):
  return SSEClient(sse_config)


# ── Event processing ────────────────────────────────────────────────


@pytest.mark.unit
class TestProcessEvents:
  """Test _process_events with mocked SSE streams."""

  def _make_client_with_lines(self, sse_config, lines):
    """Create an SSEClient with a fake response that yields lines."""
    client = SSEClient(sse_config)
    mock_response = Mock()
    mock_response.iter_lines.return_value = iter(lines)
    client._response = mock_response
    client.closed = False
    return client

  def test_simple_event(self, sse_config):
    """Test processing a single complete event."""
    lines = [
      "event: operation_progress",
      'data: {"message": "Working"}',
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    events = []
    client.on("operation_progress", lambda d: events.append(d))

    client._process_events()

    assert len(events) == 1
    assert events[0] == {"message": "Working"}

  def test_multiline_data(self, sse_config):
    """Test multiline data is joined with newlines."""
    lines = [
      "event: data_chunk",
      'data: {"rows": [',
      'data:   {"id": 1}',
      "data: ]}",
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    events = []
    client.on("data_chunk", lambda d: events.append(d))

    client._process_events()

    assert len(events) == 1
    assert events[0] == {"rows": [{"id": 1}]}

  def test_comment_lines_skipped(self, sse_config):
    """Test that comment lines (starting with :) are skipped."""
    lines = [
      ": this is a comment",
      "event: operation_progress",
      'data: {"message": "hello"}',
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    events = []
    client.on("operation_progress", lambda d: events.append(d))

    client._process_events()

    assert len(events) == 1

  def test_id_field_tracked(self, sse_config):
    """Test that id field is tracked for reconnection."""
    lines = [
      "event: operation_progress",
      'data: {"message": "step 1"}',
      "id: 42",
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    client._process_events()

    assert client.last_event_id == "42"

  def test_retry_field_parsed(self, sse_config):
    """Test retry field is parsed from events."""
    lines = [
      "event: operation_progress",
      'data: {"message": "retry test"}',
      "retry: 5000",
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    # The retry value is parsed in the event buffer but not stored on client
    # Just verify it doesn't crash
    client._process_events()

  def test_invalid_retry_ignored(self, sse_config):
    """Test invalid retry value is silently ignored."""
    lines = [
      "event: operation_progress",
      'data: {"message": "test"}',
      "retry: not-a-number",
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    client._process_events()  # Should not raise

  def test_multiple_events(self, sse_config):
    """Test processing multiple events in sequence."""
    lines = [
      "event: operation_progress",
      'data: {"message": "step 1"}',
      "",
      "event: operation_progress",
      'data: {"message": "step 2"}',
      "",
      "event: operation_completed",
      'data: {"result": {"done": true}}',
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    progress = []
    completed = []
    client.on("operation_progress", lambda d: progress.append(d))
    client.on("operation_completed", lambda d: completed.append(d))

    client._process_events()

    assert len(progress) == 2
    assert len(completed) == 1

  def test_default_event_type_is_message(self, sse_config):
    """Test events without event: field default to 'message'."""
    lines = [
      'data: {"hello": "world"}',
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    events = []
    client.on("message", lambda d: events.append(d))

    client._process_events()

    assert len(events) == 1
    assert events[0] == {"hello": "world"}

  def test_non_json_data_kept_as_string(self, sse_config):
    """Test that non-JSON data is kept as a string."""
    lines = [
      "event: operation_progress",
      "data: plain text message",
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    events = []
    client.on("operation_progress", lambda d: events.append(d))

    client._process_events()

    assert events[0] == "plain text message"

  def test_final_event_without_trailing_newline(self, sse_config):
    """Test that a final event is dispatched even without trailing empty line."""
    lines = [
      "event: operation_completed",
      'data: {"result": {}}',
    ]
    client = self._make_client_with_lines(sse_config, lines)
    events = []
    client.on("operation_completed", lambda d: events.append(d))

    client._process_events()

    assert len(events) == 1

  def test_closed_flag_stops_processing(self, sse_config):
    """Test that setting closed=True mid-stream stops processing."""
    call_count = 0

    def close_on_second(data):
      nonlocal call_count
      call_count += 1

    lines = [
      "event: operation_progress",
      'data: {"message": "first"}',
      "",
      "event: operation_progress",
      'data: {"message": "second"}',
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    client.on("operation_progress", close_on_second)

    # Close after first event dispatch
    original_dispatch = client._dispatch_event

    def dispatch_and_close(buf):
      original_dispatch(buf)
      client.closed = True

    client._dispatch_event = dispatch_and_close
    client._process_events()

    assert call_count == 1

  def test_data_field_with_no_value(self, sse_config):
    """Test 'data' line without colon appends empty string."""
    lines = [
      "event: operation_progress",
      "data",
      "",
    ]
    client = self._make_client_with_lines(sse_config, lines)
    events = []
    client.on("operation_progress", lambda d: events.append(d))

    client._process_events()

    assert len(events) == 1
    assert events[0] == ""  # Empty string, not JSON


# ── Completion auto-close ────────────────────────────────────────────


@pytest.mark.unit
class TestCompletionAutoClose:
  """Test that terminal events set closed flag."""

  def _dispatch(self, sse_config, event_type):
    client = SSEClient(sse_config)
    buf = {"event": event_type, "data": ["{}"], "id": None, "retry": None}
    client._dispatch_event(buf)
    return client.closed

  def test_completed_sets_closed(self, sse_config):
    assert self._dispatch(sse_config, "operation_completed") is True

  def test_error_sets_closed(self, sse_config):
    assert self._dispatch(sse_config, "operation_error") is True

  def test_cancelled_sets_closed(self, sse_config):
    assert self._dispatch(sse_config, "operation_cancelled") is True

  def test_progress_does_not_close(self, sse_config):
    assert self._dispatch(sse_config, "operation_progress") is False

  def test_data_chunk_does_not_close(self, sse_config):
    assert self._dispatch(sse_config, "data_chunk") is False


# ── Reconnection / retry ────────────────────────────────────────────


@pytest.mark.unit
class TestReconnection:
  """Test _handle_error retry logic."""

  @patch("robosystems_client.extensions.sse_client.time.sleep")
  @patch("robosystems_client.extensions.sse_client.httpx")
  def test_retry_with_backoff(self, mock_httpx, mock_sleep, sse_config):
    """Test exponential backoff on retry."""
    # Make httpx.Client always raise to trigger retry chain
    mock_httpx.Client.side_effect = Exception("connection refused")

    client = SSEClient(sse_config)

    reconnect_events = []
    exceeded_events = []
    client.on("reconnecting", lambda d: reconnect_events.append(d))
    client.on("max_retries_exceeded", lambda d: exceeded_events.append(d))

    # connect → fail → _handle_error → retry connect → fail → ... → max retries
    client.connect("op-1")

    # Should have attempted max_retries reconnections
    assert len(reconnect_events) == sse_config.max_retries
    assert len(exceeded_events) == 1

    # Verify backoff: delays should double each time
    # retry_delay=100ms, so: 100ms, 200ms, 400ms → sleep(0.1), sleep(0.2), sleep(0.4)
    sleep_calls = [call.args[0] for call in mock_sleep.call_args_list]
    assert sleep_calls[0] == pytest.approx(0.1)
    assert sleep_calls[1] == pytest.approx(0.2)
    assert sleep_calls[2] == pytest.approx(0.4)

  def test_max_retries_exceeded_emits_event(self, sse_config):
    """Test that exceeding max retries emits event and closes."""
    sse_config.max_retries = 0  # No retries allowed
    client = SSEClient(sse_config)

    exceeded_events = []
    client.on("max_retries_exceeded", lambda d: exceeded_events.append(d))

    client._handle_error(Exception("fail"), "op-1", 0)

    assert len(exceeded_events) == 1
    assert client.closed is True

  @patch("robosystems_client.extensions.sse_client.time.sleep")
  def test_resume_from_last_event_id(self, mock_sleep, sse_config):
    """Test reconnection resumes from last_event_id."""
    sse_config.max_retries = 1
    client = SSEClient(sse_config)
    client.last_event_id = "10"

    connect_calls = []
    # Make connect succeed (no-op) to stop recursion
    with patch.object(
      client, "connect", side_effect=lambda op, seq: connect_calls.append((op, seq))
    ):
      client._handle_error(Exception("lost"), "op-1", 0)

    assert connect_calls == [("op-1", 11)]  # last_event_id + 1

  @patch("robosystems_client.extensions.sse_client.time.sleep")
  def test_resume_with_non_numeric_event_id(self, mock_sleep, sse_config):
    """Test reconnection falls back to from_sequence for non-numeric IDs."""
    sse_config.max_retries = 1
    client = SSEClient(sse_config)
    client.last_event_id = "not-a-number"

    connect_calls = []
    with patch.object(
      client, "connect", side_effect=lambda op, seq: connect_calls.append((op, seq))
    ):
      client._handle_error(Exception("lost"), "op-1", 5)

    assert connect_calls == [("op-1", 5)]  # Falls back to from_sequence

  def test_no_retry_when_closed(self, sse_config):
    """Test no retry when client is already closed."""
    client = SSEClient(sse_config)
    client.closed = True

    reconnect_events = []
    client.on("reconnecting", lambda d: reconnect_events.append(d))

    client._handle_error(Exception("fail"), "op-1", 0)

    assert len(reconnect_events) == 0


# ── Connect ──────────────────────────────────────────────────────────


@pytest.mark.unit
class TestConnect:
  """Test connect method."""

  @patch("robosystems_client.extensions.sse_client.httpx")
  def test_connect_sets_up_stream(self, mock_httpx, sse_config):
    """Test connect creates httpx client and starts streaming."""
    mock_http_client = MagicMock()
    mock_context = MagicMock()
    mock_response = MagicMock()
    mock_response.iter_lines.return_value = iter(
      [
        "event: operation_completed",
        'data: {"result": {}}',
        "",
      ]
    )
    mock_context.__enter__ = Mock(return_value=mock_response)
    mock_http_client.stream.return_value = mock_context
    mock_httpx.Client.return_value = mock_http_client

    client = SSEClient(sse_config)
    connected_events = []
    client.on("connected", lambda d: connected_events.append(d))

    client.connect("op-123")

    assert len(connected_events) == 1
    assert client.reconnect_attempts == 0

  @patch("robosystems_client.extensions.sse_client.httpx")
  def test_connect_error_triggers_retry(self, mock_httpx, sse_config):
    """Test that connection error triggers _handle_error."""
    sse_config.max_retries = 0  # Don't actually retry
    mock_httpx.Client.side_effect = Exception("Connection refused")

    client = SSEClient(sse_config)
    exceeded = []
    client.on("max_retries_exceeded", lambda d: exceeded.append(d))

    client.connect("op-123")

    assert len(exceeded) == 1


# ── Close / cleanup ─────────────────────────────────────────────────


@pytest.mark.unit
class TestClose:
  """Test close and cleanup."""

  def test_close_clears_listeners(self, sse_config):
    """Test close removes all listeners."""
    client = SSEClient(sse_config)
    client.on("test", lambda d: None)
    assert len(client.listeners) > 0

    client.close()

    assert len(client.listeners) == 0
    assert client.closed is True

  def test_close_emits_closed_event(self, sse_config):
    """Test close emits 'closed' event before clearing listeners."""
    client = SSEClient(sse_config)
    closed_events = []
    client.on("closed", lambda d: closed_events.append(d))

    client.close()

    assert len(closed_events) == 1

  def test_close_cleans_up_http_client(self, sse_config):
    """Test close closes the httpx client."""
    client = SSEClient(sse_config)
    mock_http = Mock()
    client.client = mock_http

    client.close()

    mock_http.close.assert_called_once()
    assert client.client is None

  def test_close_cleans_up_context_manager(self, sse_config):
    """Test close exits the stream context manager."""
    client = SSEClient(sse_config)
    mock_ctx = MagicMock()
    client._context_manager = mock_ctx

    client.close()

    mock_ctx.__exit__.assert_called_once_with(None, None, None)

  def test_is_connected(self, sse_config):
    """Test is_connected reflects state."""
    client = SSEClient(sse_config)
    assert client.is_connected() is False

    client.client = Mock()
    assert client.is_connected() is True

    client.closed = True
    assert client.is_connected() is False


# ── Listener error handling ──────────────────────────────────────────


@pytest.mark.unit
class TestListenerErrors:
  """Test that listener errors don't break other listeners."""

  def test_error_in_listener_doesnt_stop_others(self, sse_config):
    """Test that a failing listener doesn't prevent others from running."""
    client = SSEClient(sse_config)

    results = []
    client.on("test", lambda d: (_ for _ in ()).throw(ValueError("boom")))
    client.on("test", lambda d: results.append(d))

    client.emit("test", "data")

    assert results == ["data"]

  def test_emit_to_nonexistent_event_is_noop(self, sse_config):
    """Test emitting to an event with no listeners doesn't raise."""
    client = SSEClient(sse_config)
    client.emit("nonexistent", "data")  # Should not raise
