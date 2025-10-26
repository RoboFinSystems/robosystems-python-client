"""Unit tests for OperationClient."""

import pytest
from datetime import datetime
from robosystems_client.extensions.operation_client import (
  OperationClient,
  OperationStatus,
  OperationProgress,
  OperationResult,
  MonitorOptions,
)


@pytest.mark.unit
class TestOperationClient:
  """Test suite for OperationClient."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = OperationClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}
    assert client.active_operations == {}
    assert client._lock is not None

  def test_operation_status_enum(self):
    """Test OperationStatus enum values."""
    assert OperationStatus.PENDING.value == "pending"
    assert OperationStatus.QUEUED.value == "queued"
    assert OperationStatus.RUNNING.value == "running"
    assert OperationStatus.COMPLETED.value == "completed"
    assert OperationStatus.FAILED.value == "failed"
    assert OperationStatus.CANCELLED.value == "cancelled"

  def test_operation_progress_dataclass(self):
    """Test OperationProgress dataclass creation."""
    progress = OperationProgress(
      message="Processing step 1", percentage=25.0, current_step=1, total_steps=4
    )

    assert progress.message == "Processing step 1"
    assert progress.percentage == 25.0
    assert progress.current_step == 1
    assert progress.total_steps == 4
    assert isinstance(progress.timestamp, datetime)

  def test_operation_progress_defaults(self):
    """Test OperationProgress with defaults."""
    progress = OperationProgress(message="Processing")

    assert progress.message == "Processing"
    assert progress.percentage is None
    assert progress.current_step is None
    assert progress.total_steps is None
    assert isinstance(progress.timestamp, datetime)

  def test_operation_result_dataclass(self, operation_id):
    """Test OperationResult dataclass creation."""
    result = OperationResult(
      operation_id=operation_id,
      status=OperationStatus.COMPLETED,
      result={"rows_processed": 1000},
      execution_time_ms=5000,
    )

    assert result.operation_id == operation_id
    assert result.status == OperationStatus.COMPLETED
    assert result.result == {"rows_processed": 1000}
    assert result.execution_time_ms == 5000
    assert result.progress == []  # Default empty list
    assert result.error is None

  def test_operation_result_with_error(self, operation_id):
    """Test OperationResult with error."""
    result = OperationResult(
      operation_id=operation_id,
      status=OperationStatus.FAILED,
      error="Operation failed",
    )

    assert result.status == OperationStatus.FAILED
    assert result.error == "Operation failed"
    assert result.result is None

  def test_monitor_options_defaults(self):
    """Test MonitorOptions with default values."""
    options = MonitorOptions()

    assert options.on_progress is None
    assert options.on_queue_update is None
    assert options.timeout is None
    assert options.poll_interval is None

  def test_monitor_options_with_timeout(self):
    """Test MonitorOptions with timeout."""
    options = MonitorOptions(timeout=30000, poll_interval=1000)

    assert options.timeout == 30000
    assert options.poll_interval == 1000

  def test_close_all_empty(self, mock_config):
    """Test close_all when no active operations."""
    client = OperationClient(mock_config)

    # Should not raise any exceptions
    client.close_all()

    assert len(client.active_operations) == 0

  def test_thread_safety(self, mock_config):
    """Test that client uses threading lock for safety."""
    client = OperationClient(mock_config)

    # Verify lock exists
    assert hasattr(client, "_lock")
    assert client._lock is not None

    # Lock should be acquirable
    acquired = client._lock.acquire(blocking=False)
    assert acquired is True
    client._lock.release()
