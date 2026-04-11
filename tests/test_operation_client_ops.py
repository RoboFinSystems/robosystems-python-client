"""Unit tests for OperationClient operational logic.

Covers: monitor_operation (SSE event handling, completion, error, cancel,
timeout, progress callbacks, queue updates), get_operation_status,
cancel_operation, close_operation, close_all.

Dataclass and enum tests already exist in tests/test_operation_client.py.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from robosystems_client.extensions.operation_client import (
  OperationClient,
  OperationStatus,
  OperationProgress,
  MonitorOptions,
)
from robosystems_client.extensions.sse_client import SSEClient


# ── Helpers ──────────────────────────────────────────────────────────


def _fire_events(sse_client_instance, events):
  """Simulate SSE events by directly calling registered listeners.

  Each event is a (event_type, data) tuple.
  """
  for event_type, data in events:
    sse_client_instance.emit(event_type, data)


# ── monitor_operation ────────────────────────────────────────────────


@pytest.mark.unit
class TestMonitorOperation:
  """Test OperationClient.monitor_operation via mocked SSE."""

  @patch("robosystems_client.extensions.operation_client.SSEClient")
  @patch("time.sleep")
  def test_monitor_completed(self, mock_sleep, MockSSE, mock_config):
    """Test monitoring an operation that completes successfully."""
    fake_sse = MagicMock(spec=SSEClient)
    listeners = {}

    def capture_on(event, handler):
      listeners[event] = handler

    fake_sse.on.side_effect = capture_on

    def fake_connect(op_id):
      # Simulate: started → progress → completed
      listeners["operation_started"]({"agent": "financial"})
      listeners["operation_progress"]({"message": "Processing", "percentage": 50})
      listeners["operation_completed"](
        {"result": {"rows": 100}, "execution_time_ms": 2000}
      )

    fake_sse.connect.side_effect = fake_connect
    MockSSE.return_value = fake_sse

    client = OperationClient(mock_config)
    result = client.monitor_operation("op-123")

    assert result.status == OperationStatus.COMPLETED
    assert result.result == {"rows": 100}
    assert result.execution_time_ms == 2000
    assert len(result.progress) == 1
    assert result.progress[0].message == "Processing"
    assert result.progress[0].percentage == 50

  @patch("robosystems_client.extensions.operation_client.SSEClient")
  @patch("time.sleep")
  def test_monitor_failed(self, mock_sleep, MockSSE, mock_config):
    """Test monitoring an operation that fails."""
    fake_sse = MagicMock(spec=SSEClient)
    listeners = {}

    def capture_on(event, handler):
      listeners[event] = handler

    fake_sse.on.side_effect = capture_on

    def fake_connect(op_id):
      listeners["operation_error"]({"message": "Database connection lost"})

    fake_sse.connect.side_effect = fake_connect
    MockSSE.return_value = fake_sse

    client = OperationClient(mock_config)
    result = client.monitor_operation("op-fail")

    assert result.status == OperationStatus.FAILED
    assert result.error == "Database connection lost"

  @patch("robosystems_client.extensions.operation_client.SSEClient")
  @patch("time.sleep")
  def test_monitor_cancelled(self, mock_sleep, MockSSE, mock_config):
    """Test monitoring a cancelled operation."""
    fake_sse = MagicMock(spec=SSEClient)
    listeners = {}

    def capture_on(event, handler):
      listeners[event] = handler

    fake_sse.on.side_effect = capture_on

    def fake_connect(op_id):
      listeners["operation_cancelled"]()

    fake_sse.connect.side_effect = fake_connect
    MockSSE.return_value = fake_sse

    client = OperationClient(mock_config)
    result = client.monitor_operation("op-cancel")

    assert result.status == OperationStatus.CANCELLED

  @patch("robosystems_client.extensions.operation_client.SSEClient")
  @patch("time.sleep")
  def test_monitor_with_progress_callback(self, mock_sleep, MockSSE, mock_config):
    """Test that progress callback is invoked."""
    fake_sse = MagicMock(spec=SSEClient)
    listeners = {}

    def capture_on(event, handler):
      listeners[event] = handler

    fake_sse.on.side_effect = capture_on

    def fake_connect(op_id):
      listeners["operation_progress"](
        {"message": "Step 1", "percentage": 25, "current_step": 1, "total_steps": 4}
      )
      listeners["operation_progress"](
        {"message": "Step 2", "percentage": 50, "current_step": 2, "total_steps": 4}
      )
      listeners["operation_completed"]({"result": {}})

    fake_sse.connect.side_effect = fake_connect
    MockSSE.return_value = fake_sse

    progress_updates = []
    options = MonitorOptions(on_progress=lambda p: progress_updates.append(p))

    client = OperationClient(mock_config)
    client.monitor_operation("op-progress", options)

    assert len(progress_updates) == 2
    assert isinstance(progress_updates[0], OperationProgress)
    assert progress_updates[0].message == "Step 1"
    assert progress_updates[1].current_step == 2

  @patch("robosystems_client.extensions.operation_client.SSEClient")
  @patch("time.sleep")
  def test_monitor_with_queue_update(self, mock_sleep, MockSSE, mock_config):
    """Test queue update callback."""
    fake_sse = MagicMock(spec=SSEClient)
    listeners = {}

    def capture_on(event, handler):
      listeners[event] = handler

    fake_sse.on.side_effect = capture_on

    def fake_connect(op_id):
      listeners["queue_update"]({"position": 3, "estimated_wait_seconds": 15})
      listeners["operation_completed"]({"result": {}})

    fake_sse.connect.side_effect = fake_connect
    MockSSE.return_value = fake_sse

    queue_updates = []
    options = MonitorOptions(
      on_queue_update=lambda pos, wait: queue_updates.append((pos, wait))
    )

    client = OperationClient(mock_config)
    result = client.monitor_operation("op-queue", options)

    assert queue_updates == [(3, 15)]
    assert result.status == OperationStatus.COMPLETED

  @patch("robosystems_client.extensions.operation_client.SSEClient")
  @patch("time.sleep")
  def test_monitor_error_uses_fallback_key(self, mock_sleep, MockSSE, mock_config):
    """Test error event falls back to 'error' key when 'message' absent."""
    fake_sse = MagicMock(spec=SSEClient)
    listeners = {}

    def capture_on(event, handler):
      listeners[event] = handler

    fake_sse.on.side_effect = capture_on

    def fake_connect(op_id):
      listeners["operation_error"]({"error": "Timeout exceeded"})

    fake_sse.connect.side_effect = fake_connect
    MockSSE.return_value = fake_sse

    client = OperationClient(mock_config)
    result = client.monitor_operation("op-err")

    assert result.status == OperationStatus.FAILED
    assert result.error == "Timeout exceeded"

  @patch("robosystems_client.extensions.operation_client.SSEClient")
  @patch("time.sleep")
  def test_monitor_cleanup_on_completion(self, mock_sleep, MockSSE, mock_config):
    """Test that SSE client is cleaned up after completion."""
    fake_sse = MagicMock(spec=SSEClient)
    listeners = {}

    def capture_on(event, handler):
      listeners[event] = handler

    fake_sse.on.side_effect = capture_on

    def fake_connect(op_id):
      listeners["operation_completed"]({"result": {}})

    fake_sse.connect.side_effect = fake_connect
    MockSSE.return_value = fake_sse

    client = OperationClient(mock_config)
    client.monitor_operation("op-cleanup")

    # Operation should be removed from active_operations
    assert "op-cleanup" not in client.active_operations
    # SSE client should have been closed
    fake_sse.close.assert_called()


# ── get_operation_status ─────────────────────────────────────────────


@pytest.mark.unit
class TestGetOperationStatus:
  """Test OperationClient.get_operation_status."""

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  def test_get_status_success(self, mock_get, mock_config):
    """Test successful status retrieval."""
    mock_resp = Mock()
    mock_resp.parsed = Mock()
    mock_resp.parsed.status = "running"
    mock_resp.parsed.progress = 50
    mock_resp.parsed.result = None
    mock_resp.parsed.error = None
    mock_get.return_value = mock_resp

    client = OperationClient(mock_config)
    status = client.get_operation_status("op-status")

    assert status["status"] == "running"
    assert status["progress"] == 50

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  def test_get_status_error(self, mock_get, mock_config):
    """Test status retrieval on error."""
    mock_get.side_effect = Exception("Network error")

    client = OperationClient(mock_config)
    status = client.get_operation_status("op-err")

    assert status["status"] == "error"
    assert "Network error" in status["error"]

  @patch("robosystems_client.api.operations.get_operation_status.sync_detailed")
  def test_get_status_no_parsed(self, mock_get, mock_config):
    """Test status when response has no parsed data."""
    mock_resp = Mock()
    mock_resp.parsed = None
    mock_get.return_value = mock_resp

    client = OperationClient(mock_config)
    status = client.get_operation_status("op-none")

    assert status["status"] == "unknown"


# ── cancel_operation ─────────────────────────────────────────────────


@pytest.mark.unit
class TestCancelOperation:
  """Test OperationClient.cancel_operation."""

  @patch("robosystems_client.api.operations.cancel_operation.sync_detailed")
  def test_cancel_success(self, mock_cancel, mock_config):
    """Test successful cancellation."""
    mock_resp = Mock()
    mock_resp.parsed = Mock()
    mock_resp.parsed.cancelled = True
    mock_cancel.return_value = mock_resp

    client = OperationClient(mock_config)
    result = client.cancel_operation("op-cancel")

    assert result is True

  @patch("robosystems_client.api.operations.cancel_operation.sync_detailed")
  def test_cancel_failure(self, mock_cancel, mock_config):
    """Test cancellation failure."""
    mock_cancel.side_effect = Exception("Not found")

    client = OperationClient(mock_config)
    result = client.cancel_operation("op-missing")

    assert result is False


# ── close_operation / close_all ──────────────────────────────────────


@pytest.mark.unit
class TestCloseOperations:
  """Test close_operation and close_all."""

  def test_close_operation(self, mock_config):
    """Test closing a specific operation monitor."""
    client = OperationClient(mock_config)
    mock_sse = Mock()
    client.active_operations["op-1"] = mock_sse

    client.close_operation("op-1")

    mock_sse.close.assert_called_once()
    assert "op-1" not in client.active_operations

  def test_close_operation_nonexistent(self, mock_config):
    """Test closing a nonexistent operation is a no-op."""
    client = OperationClient(mock_config)
    client.close_operation("op-missing")  # Should not raise

  def test_close_all_multiple(self, mock_config):
    """Test closing all active operations."""
    client = OperationClient(mock_config)
    mock_sse1 = Mock()
    mock_sse2 = Mock()
    client.active_operations["op-1"] = mock_sse1
    client.active_operations["op-2"] = mock_sse2

    client.close_all()

    mock_sse1.close.assert_called_once()
    mock_sse2.close.assert_called_once()
    assert len(client.active_operations) == 0
