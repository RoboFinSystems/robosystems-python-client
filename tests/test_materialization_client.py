"""Unit tests for MaterializationClient."""

import pytest
from unittest.mock import Mock, patch
from robosystems_client.extensions.materialization_client import (
  MaterializationClient,
  MaterializationOptions,
  MaterializationResult,
  MaterializationStatus,
)
from robosystems_client.extensions.operation_client import (
  OperationResult,
  OperationStatus,
)


@pytest.mark.unit
class TestMaterializationDataclasses:
  """Test suite for materialization-related dataclasses."""

  def test_materialization_options_defaults(self):
    """Test MaterializationOptions default values."""
    options = MaterializationOptions()

    assert options.ignore_errors is True
    assert options.rebuild is False
    assert options.force is False
    assert options.materialize_embeddings is False
    assert options.on_progress is None
    assert options.timeout == 600

  def test_materialization_options_custom(self):
    """Test MaterializationOptions with custom values."""
    progress_fn = Mock()
    options = MaterializationOptions(
      ignore_errors=False,
      rebuild=True,
      force=True,
      materialize_embeddings=True,
      on_progress=progress_fn,
      timeout=300,
    )

    assert options.ignore_errors is False
    assert options.rebuild is True
    assert options.force is True
    assert options.materialize_embeddings is True
    assert options.on_progress is progress_fn
    assert options.timeout == 300

  def test_materialization_result(self):
    """Test MaterializationResult dataclass."""
    result = MaterializationResult(
      status="success",
      was_stale=True,
      stale_reason="New files uploaded",
      tables_materialized=["Entity", "Transaction"],
      total_rows=1500,
      execution_time_ms=3000.0,
      message="Graph materialized successfully",
    )

    assert result.status == "success"
    assert result.was_stale is True
    assert result.stale_reason == "New files uploaded"
    assert len(result.tables_materialized) == 2
    assert result.total_rows == 1500
    assert result.execution_time_ms == 3000.0
    assert result.success is True
    assert result.error is None

  def test_materialization_result_with_error(self):
    """Test MaterializationResult with error."""
    result = MaterializationResult(
      status="failed",
      was_stale=False,
      stale_reason=None,
      tables_materialized=[],
      total_rows=0,
      execution_time_ms=0,
      message="Failed to materialize",
      success=False,
      error="Connection timeout",
    )

    assert result.success is False
    assert result.error == "Connection timeout"

  def test_materialization_status(self):
    """Test MaterializationStatus dataclass."""
    status = MaterializationStatus(
      graph_id="graph-123",
      is_stale=True,
      stale_reason="Files uploaded since last materialization",
      stale_since="2025-01-15T10:00:00Z",
      last_materialized_at="2025-01-14T08:00:00Z",
      materialization_count=5,
      hours_since_materialization=26.0,
      message="Graph is stale",
    )

    assert status.graph_id == "graph-123"
    assert status.is_stale is True
    assert status.materialization_count == 5
    assert status.hours_since_materialization == 26.0


@pytest.mark.unit
class TestMaterializationClientInit:
  """Test suite for MaterializationClient initialization."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = MaterializationClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}
    assert client._operation_client is None

  def test_operation_client_lazy_creation(self, mock_config):
    """Test that operation client is created lazily."""
    client = MaterializationClient(mock_config)

    assert client._operation_client is None
    op_client = client.operation_client
    assert op_client is not None
    # Second access returns same instance
    assert client.operation_client is op_client


@pytest.mark.unit
class TestMaterialize:
  """Test suite for MaterializationClient.materialize method."""

  @patch("robosystems_client.extensions.materialization_client.materialize_graph")
  def test_materialize_success(self, mock_mat, mock_config, graph_id):
    """Test successful materialization."""
    # Mock initial response with operation_id
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock(operation_id="op-mat-123")
    mock_mat.return_value = mock_resp

    # Mock the operation client monitoring
    op_result = OperationResult(
      operation_id="op-mat-123",
      status=OperationStatus.COMPLETED,
      result={
        "was_stale": True,
        "stale_reason": "New files",
        "tables_materialized": ["Entity"],
        "total_rows": 100,
        "execution_time_ms": 2000.0,
        "message": "Done",
      },
      execution_time_ms=2000.0,
    )

    client = MaterializationClient(mock_config)
    client._operation_client = Mock()
    client._operation_client.monitor_operation.return_value = op_result

    result = client.materialize(graph_id)

    assert result.success is True
    assert result.status == "success"
    assert result.tables_materialized == ["Entity"]
    assert result.total_rows == 100

  @patch("robosystems_client.extensions.materialization_client.materialize_graph")
  def test_materialize_api_failure(self, mock_mat, mock_config, graph_id):
    """Test materialization when API returns error."""
    mock_resp = Mock()
    mock_resp.status_code = 500
    mock_resp.parsed = None
    mock_resp.content = b'{"detail": "Internal error"}'
    mock_mat.return_value = mock_resp

    client = MaterializationClient(mock_config)
    result = client.materialize(graph_id)

    assert result.success is False
    assert result.status == "failed"

  @patch("robosystems_client.extensions.materialization_client.materialize_graph")
  def test_materialize_operation_failed(self, mock_mat, mock_config, graph_id):
    """Test materialization when operation fails."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock(operation_id="op-fail")
    mock_mat.return_value = mock_resp

    op_result = OperationResult(
      operation_id="op-fail",
      status=OperationStatus.FAILED,
      error="Dagster job failed",
      execution_time_ms=1000.0,
    )

    client = MaterializationClient(mock_config)
    client._operation_client = Mock()
    client._operation_client.monitor_operation.return_value = op_result

    result = client.materialize(graph_id)

    assert result.success is False
    assert result.error == "Dagster job failed"

  def test_materialize_no_token(self, mock_config, graph_id):
    """Test materialize fails without API key."""
    mock_config["token"] = None
    client = MaterializationClient(mock_config)

    result = client.materialize(graph_id)

    assert result.success is False
    assert "No API key" in result.error

  @patch("robosystems_client.extensions.materialization_client.materialize_graph")
  def test_materialize_with_progress(self, mock_mat, mock_config, graph_id):
    """Test materialize calls progress callback."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock(operation_id="op-progress")
    mock_mat.return_value = mock_resp

    op_result = OperationResult(
      operation_id="op-progress",
      status=OperationStatus.COMPLETED,
      result={
        "was_stale": False,
        "tables_materialized": [],
        "total_rows": 0,
        "execution_time_ms": 500.0,
        "message": "Already up to date",
      },
      execution_time_ms=500.0,
    )

    progress_messages = []
    options = MaterializationOptions(
      on_progress=lambda msg: progress_messages.append(msg)
    )

    client = MaterializationClient(mock_config)
    client._operation_client = Mock()
    client._operation_client.monitor_operation.return_value = op_result

    client.materialize(graph_id, options)

    assert len(progress_messages) >= 2  # At least "Submitting" and "queued"

  @patch("robosystems_client.extensions.materialization_client.materialize_graph")
  def test_materialize_with_rebuild(self, mock_mat, mock_config, graph_id):
    """Test materialize passes rebuild option."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock(operation_id="op-rebuild")
    mock_mat.return_value = mock_resp

    op_result = OperationResult(
      operation_id="op-rebuild",
      status=OperationStatus.COMPLETED,
      result={
        "was_stale": True,
        "tables_materialized": ["Entity"],
        "total_rows": 50,
        "execution_time_ms": 5000.0,
        "message": "Rebuilt",
      },
      execution_time_ms=5000.0,
    )

    client = MaterializationClient(mock_config)
    client._operation_client = Mock()
    client._operation_client.monitor_operation.return_value = op_result

    options = MaterializationOptions(rebuild=True, force=True)
    result = client.materialize(graph_id, options)

    assert result.success is True
    # Verify the request body had rebuild=True
    call_kwargs = mock_mat.call_args[1]
    assert call_kwargs["body"].rebuild is True
    assert call_kwargs["body"].force is True


@pytest.mark.unit
class TestMaterializationStatus:
  """Test suite for MaterializationClient.status method."""

  @patch(
    "robosystems_client.extensions.materialization_client.get_materialization_status"
  )
  def test_get_status(self, mock_status, mock_config, graph_id):
    """Test getting materialization status."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock(
      graph_id=graph_id,
      is_stale=True,
      stale_reason="New files uploaded",
      stale_since="2025-01-15T10:00:00Z",
      last_materialized_at="2025-01-14T08:00:00Z",
      materialization_count=3,
      hours_since_materialization=26.0,
      message="Graph is stale",
    )
    mock_status.return_value = mock_resp

    client = MaterializationClient(mock_config)
    status = client.status(graph_id)

    assert status is not None
    assert status.is_stale is True
    assert status.materialization_count == 3

  @patch(
    "robosystems_client.extensions.materialization_client.get_materialization_status"
  )
  def test_get_status_failure(self, mock_status, mock_config, graph_id):
    """Test status returns None on failure."""
    mock_resp = Mock()
    mock_resp.status_code = 500
    mock_resp.parsed = None
    mock_status.return_value = mock_resp

    client = MaterializationClient(mock_config)
    status = client.status(graph_id)

    assert status is None

  def test_status_no_token(self, mock_config, graph_id):
    """Test status returns None without token."""
    mock_config["token"] = None
    client = MaterializationClient(mock_config)
    status = client.status(graph_id)

    assert status is None
