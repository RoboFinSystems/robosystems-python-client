"""Unit tests for TableIngestClient."""

import pytest
from robosystems_client.extensions.table_ingest_client import (
  TableIngestClient,
  UploadOptions,
  IngestOptions,
  UploadResult,
  TableInfo,
)


@pytest.mark.unit
class TestTableIngestClient:
  """Test suite for TableIngestClient."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = TableIngestClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}

  def test_upload_options_dataclass(self):
    """Test UploadOptions dataclass."""
    options = UploadOptions(
      on_progress=lambda msg: print(msg),
      fix_localstack_url=True,
      file_name="test.parquet",
    )

    assert options.fix_localstack_url is True
    assert options.file_name == "test.parquet"
    assert options.on_progress is not None

  def test_ingest_options_dataclass(self):
    """Test IngestOptions dataclass."""
    options = IngestOptions(
      ignore_errors=False, rebuild=True, on_progress=lambda msg: print(msg)
    )

    assert options.ignore_errors is False
    assert options.rebuild is True
    assert options.on_progress is not None

  def test_upload_result_dataclass(self):
    """Test UploadResult dataclass."""
    result = UploadResult(
      file_id="file-123",
      file_size=5000,
      row_count=100,
      table_name="Entity",
      file_name="data.parquet",
      success=True,
    )

    assert result.file_id == "file-123"
    assert result.file_size == 5000
    assert result.row_count == 100
    assert result.table_name == "Entity"
    assert result.success is True
    assert result.error is None

  def test_upload_result_with_error(self):
    """Test UploadResult with error."""
    result = UploadResult(
      file_id="",
      file_size=0,
      row_count=0,
      table_name="Entity",
      file_name="data.parquet",
      success=False,
      error="Upload failed",
    )

    assert result.success is False
    assert result.error == "Upload failed"

  def test_table_info_dataclass(self):
    """Test TableInfo dataclass."""
    info = TableInfo(
      table_name="Entity", row_count=1000, file_count=5, total_size_bytes=50000
    )

    assert info.table_name == "Entity"
    assert info.row_count == 1000
    assert info.file_count == 5
    assert info.total_size_bytes == 50000

  def test_close_method(self, mock_config):
    """Test that close method exists and can be called."""
    client = TableIngestClient(mock_config)

    # Should not raise any exceptions
    client.close()

  def test_default_upload_options(self):
    """Test default UploadOptions values."""
    options = UploadOptions()

    assert options.on_progress is None
    assert options.fix_localstack_url is True
    assert options.file_name is None

  def test_default_ingest_options(self):
    """Test default IngestOptions values."""
    options = IngestOptions()

    assert options.ignore_errors is True
    assert options.rebuild is False
    assert options.on_progress is None
