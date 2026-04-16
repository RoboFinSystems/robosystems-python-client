"""Unit tests for FileClient."""

import pytest
from io import BytesIO
from unittest.mock import Mock, patch
from robosystems_client.clients.file_client import (
  FileClient,
  FileUploadOptions,
  FileUploadResult,
  FileInfo,
)


@pytest.mark.unit
class TestFileClientInit:
  """Test suite for FileClient initialization."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = FileClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}
    assert client.s3_endpoint_url is None

  def test_client_with_s3_override(self, mock_config):
    """Test client with S3 endpoint override."""
    mock_config["s3_endpoint_url"] = "http://localhost:4566"
    client = FileClient(mock_config)

    assert client.s3_endpoint_url == "http://localhost:4566"

  def test_client_cleanup(self, mock_config):
    """Test that cleanup closes HTTP client."""
    client = FileClient(mock_config)
    assert hasattr(client, "_http_client")
    client.__del__()


@pytest.mark.unit
class TestFileDataclasses:
  """Test suite for file-related dataclasses."""

  def test_file_upload_options_defaults(self):
    """Test FileUploadOptions default values."""
    options = FileUploadOptions()

    assert options.on_progress is None
    assert options.ingest_to_graph is False

  def test_file_upload_options_custom(self):
    """Test FileUploadOptions with custom values."""
    progress_fn = Mock()
    options = FileUploadOptions(on_progress=progress_fn, ingest_to_graph=True)

    assert options.on_progress is progress_fn
    assert options.ingest_to_graph is True

  def test_file_upload_result(self):
    """Test FileUploadResult dataclass creation."""
    result = FileUploadResult(
      file_id="file-123",
      file_size=50000,
      row_count=100,
      table_name="Entity",
      file_name="data.parquet",
      success=True,
    )

    assert result.file_id == "file-123"
    assert result.file_size == 50000
    assert result.row_count == 100
    assert result.table_name == "Entity"
    assert result.file_name == "data.parquet"
    assert result.success is True
    assert result.error is None

  def test_file_upload_result_with_error(self):
    """Test FileUploadResult with error."""
    result = FileUploadResult(
      file_id="",
      file_size=0,
      row_count=0,
      table_name="Entity",
      file_name="bad.parquet",
      success=False,
      error="Upload failed",
    )

    assert result.success is False
    assert result.error == "Upload failed"

  def test_file_info(self):
    """Test FileInfo dataclass creation."""
    info = FileInfo(
      file_id="file-456",
      file_name="transactions.parquet",
      file_format="parquet",
      size_bytes=120000,
      row_count=500,
      upload_status="uploaded",
      table_name="Transaction",
      created_at="2025-01-15T10:00:00Z",
      uploaded_at="2025-01-15T10:01:00Z",
    )

    assert info.file_id == "file-456"
    assert info.file_name == "transactions.parquet"
    assert info.file_format == "parquet"
    assert info.size_bytes == 120000
    assert info.row_count == 500
    assert info.upload_status == "uploaded"
    assert info.table_name == "Transaction"
    assert info.layers is None

  def test_file_info_with_layers(self):
    """Test FileInfo with layer tracking."""
    layers = {"s3": "uploaded", "duckdb": "staged", "graph": "pending"}
    info = FileInfo(
      file_id="file-789",
      file_name="data.parquet",
      file_format="parquet",
      size_bytes=1000,
      row_count=10,
      upload_status="uploaded",
      table_name="Entity",
      created_at=None,
      uploaded_at=None,
      layers=layers,
    )

    assert info.layers == layers


@pytest.mark.unit
class TestFileUpload:
  """Test suite for FileClient.upload method."""

  @patch("robosystems_client.clients.file_client.update_file")
  @patch("robosystems_client.clients.file_client.create_file_upload")
  def test_upload_bytesio(self, mock_create, mock_update, mock_config, graph_id):
    """Test uploading a BytesIO buffer."""
    # Mock presigned URL response
    mock_create_resp = Mock()
    mock_create_resp.status_code = 200
    mock_create_resp.parsed = Mock()
    mock_create_resp.parsed.upload_url = "http://s3.localhost/bucket/file.parquet"
    mock_create_resp.parsed.file_id = "file-new-123"
    mock_create.return_value = mock_create_resp

    # Mock update response
    mock_update_resp = Mock()
    mock_update_resp.status_code = 200
    mock_update_resp.parsed = Mock()
    mock_update_resp.parsed.file_size_bytes = 1234
    mock_update_resp.parsed.row_count = 10
    mock_update.return_value = mock_update_resp

    client = FileClient(mock_config)
    # Mock the S3 PUT
    client._http_client = Mock()
    client._http_client.put.return_value = Mock(status_code=200)

    buf = BytesIO(b"fake parquet data")
    result = client.upload(graph_id, "Entity", buf)

    assert result.success is True
    assert result.file_id == "file-new-123"
    assert result.file_size == 1234
    assert result.row_count == 10
    assert result.table_name == "Entity"

  @patch("robosystems_client.clients.file_client.create_file_upload")
  def test_upload_presigned_url_failure(self, mock_create, mock_config, graph_id):
    """Test upload failure when presigned URL request fails."""
    mock_create_resp = Mock()
    mock_create_resp.status_code = 500
    mock_create_resp.parsed = None
    mock_create.return_value = mock_create_resp

    client = FileClient(mock_config)
    result = client.upload(graph_id, "Entity", BytesIO(b"data"))

    assert result.success is False
    assert "Failed to get upload URL" in result.error

  @patch("robosystems_client.clients.file_client.create_file_upload")
  def test_upload_s3_failure(self, mock_create, mock_config, graph_id):
    """Test upload failure when S3 PUT fails."""
    mock_create_resp = Mock()
    mock_create_resp.status_code = 200
    mock_create_resp.parsed = Mock()
    mock_create_resp.parsed.upload_url = "http://s3.localhost/bucket/file.parquet"
    mock_create_resp.parsed.file_id = "file-s3-fail"
    mock_create.return_value = mock_create_resp

    client = FileClient(mock_config)
    client._http_client = Mock()
    client._http_client.put.return_value = Mock(status_code=500)

    result = client.upload(graph_id, "Entity", BytesIO(b"data"))

    assert result.success is False
    assert "S3 upload failed" in result.error

  @patch("robosystems_client.clients.file_client.update_file")
  @patch("robosystems_client.clients.file_client.create_file_upload")
  def test_upload_status_update_failure(
    self, mock_create, mock_update, mock_config, graph_id
  ):
    """Test upload failure when status update fails."""
    mock_create_resp = Mock()
    mock_create_resp.status_code = 200
    mock_create_resp.parsed = Mock()
    mock_create_resp.parsed.upload_url = "http://s3.localhost/bucket/file.parquet"
    mock_create_resp.parsed.file_id = "file-update-fail"
    mock_create.return_value = mock_create_resp

    mock_update_resp = Mock()
    mock_update_resp.status_code = 500
    mock_update_resp.parsed = None
    mock_update.return_value = mock_update_resp

    client = FileClient(mock_config)
    client._http_client = Mock()
    client._http_client.put.return_value = Mock(status_code=200)

    result = client.upload(graph_id, "Entity", BytesIO(b"data"))

    assert result.success is False
    assert "Failed to complete file upload" in result.error

  def test_upload_no_token(self, mock_config, graph_id):
    """Test upload fails without API key."""
    mock_config["token"] = None
    client = FileClient(mock_config)

    result = client.upload(graph_id, "Entity", BytesIO(b"data"))

    assert result.success is False
    assert "No API key" in result.error

  def test_upload_unsupported_type(self, mock_config, graph_id):
    """Test upload fails with unsupported file type."""
    client = FileClient(mock_config)

    result = client.upload(graph_id, "Entity", 12345)

    assert result.success is False
    assert "Unsupported file type" in result.error

  @patch("robosystems_client.clients.file_client.update_file")
  @patch("robosystems_client.clients.file_client.create_file_upload")
  def test_upload_with_progress_callback(
    self, mock_create, mock_update, mock_config, graph_id
  ):
    """Test upload calls progress callback at each step."""
    mock_create_resp = Mock()
    mock_create_resp.status_code = 200
    mock_create_resp.parsed = Mock()
    mock_create_resp.parsed.upload_url = "http://s3.localhost/bucket/file.parquet"
    mock_create_resp.parsed.file_id = "file-progress"
    mock_create.return_value = mock_create_resp

    mock_update_resp = Mock()
    mock_update_resp.status_code = 200
    mock_update_resp.parsed = Mock()
    mock_update_resp.parsed.file_size_bytes = 100
    mock_update_resp.parsed.row_count = 5
    mock_update.return_value = mock_update_resp

    client = FileClient(mock_config)
    client._http_client = Mock()
    client._http_client.put.return_value = Mock(status_code=200)

    progress_messages = []
    options = FileUploadOptions(on_progress=lambda msg: progress_messages.append(msg))

    client.upload(graph_id, "Entity", BytesIO(b"data"), options)

    assert len(progress_messages) >= 3  # URL, upload, mark uploaded

  @patch("robosystems_client.clients.file_client.update_file")
  @patch("robosystems_client.clients.file_client.create_file_upload")
  def test_upload_with_s3_endpoint_override(
    self, mock_create, mock_update, mock_config, graph_id
  ):
    """Test upload rewrites S3 URL when s3_endpoint_url is set."""
    mock_config["s3_endpoint_url"] = "http://localhost:4566"

    mock_create_resp = Mock()
    mock_create_resp.status_code = 200
    mock_create_resp.parsed = Mock()
    mock_create_resp.parsed.upload_url = (
      "https://s3.amazonaws.com/bucket/file.parquet?sig=abc"
    )
    mock_create_resp.parsed.file_id = "file-s3-override"
    mock_create.return_value = mock_create_resp

    mock_update_resp = Mock()
    mock_update_resp.status_code = 200
    mock_update_resp.parsed = Mock()
    mock_update_resp.parsed.file_size_bytes = 100
    mock_update_resp.parsed.row_count = 5
    mock_update.return_value = mock_update_resp

    client = FileClient(mock_config)
    client._http_client = Mock()
    client._http_client.put.return_value = Mock(status_code=200)

    client.upload(graph_id, "Entity", BytesIO(b"data"))

    # Verify S3 PUT was called with overridden URL
    put_url = client._http_client.put.call_args[0][0]
    assert "localhost:4566" in put_url


@pytest.mark.unit
class TestFileList:
  """Test suite for FileClient.list method."""

  @patch("robosystems_client.clients.file_client.list_files")
  def test_list_files(self, mock_list, mock_config, graph_id):
    """Test listing files returns FileInfo objects."""
    mock_file = Mock()
    mock_file.file_id = "file-1"
    mock_file.file_name = "data.parquet"
    mock_file.file_format = "parquet"
    mock_file.size_bytes = 5000
    mock_file.row_count = 50
    mock_file.upload_status = "uploaded"
    mock_file.table_name = "Entity"
    mock_file.created_at = "2025-01-01T00:00:00Z"
    mock_file.uploaded_at = "2025-01-01T00:01:00Z"

    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = Mock()
    mock_resp.parsed.files = [mock_file]
    mock_list.return_value = mock_resp

    client = FileClient(mock_config)
    files = client.list(graph_id)

    assert len(files) == 1
    assert files[0].file_id == "file-1"
    assert files[0].file_name == "data.parquet"
    assert files[0].size_bytes == 5000

  @patch("robosystems_client.clients.file_client.list_files")
  def test_list_files_failure(self, mock_list, mock_config, graph_id):
    """Test listing files returns empty list on failure."""
    mock_resp = Mock()
    mock_resp.status_code = 500
    mock_resp.parsed = None
    mock_list.return_value = mock_resp

    client = FileClient(mock_config)
    files = client.list(graph_id)

    assert files == []

  def test_list_files_no_token(self, mock_config, graph_id):
    """Test listing files returns empty list without token."""
    mock_config["token"] = None
    client = FileClient(mock_config)
    files = client.list(graph_id)

    assert files == []


@pytest.mark.unit
class TestFileGet:
  """Test suite for FileClient.get method."""

  @patch("robosystems_client.clients.file_client.get_file")
  def test_get_file(self, mock_get, mock_config, graph_id):
    """Test getting a specific file."""
    mock_file_data = Mock()
    mock_file_data.file_id = "file-detail"
    mock_file_data.file_name = "detail.parquet"
    mock_file_data.file_format = "parquet"
    mock_file_data.size_bytes = 8000
    mock_file_data.row_count = 80
    mock_file_data.upload_status = "uploaded"
    mock_file_data.table_name = "Entity"
    mock_file_data.created_at = "2025-01-01T00:00:00Z"
    mock_file_data.uploaded_at = "2025-01-01T00:01:00Z"
    mock_file_data.layers = {"s3": "uploaded", "duckdb": "staged"}

    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.parsed = mock_file_data
    mock_get.return_value = mock_resp

    client = FileClient(mock_config)
    info = client.get(graph_id, "file-detail")

    assert info is not None
    assert info.file_id == "file-detail"
    assert info.layers == {"s3": "uploaded", "duckdb": "staged"}

  @patch("robosystems_client.clients.file_client.get_file")
  def test_get_file_not_found(self, mock_get, mock_config, graph_id):
    """Test getting a file that doesn't exist."""
    mock_resp = Mock()
    mock_resp.status_code = 404
    mock_resp.parsed = None
    mock_get.return_value = mock_resp

    client = FileClient(mock_config)
    info = client.get(graph_id, "nonexistent")

    assert info is None


@pytest.mark.unit
class TestFileDelete:
  """Test suite for FileClient.delete method."""

  @patch("robosystems_client.clients.file_client.delete_file")
  def test_delete_file(self, mock_delete, mock_config, graph_id):
    """Test deleting a file."""
    mock_resp = Mock()
    mock_resp.status_code = 204
    mock_delete.return_value = mock_resp

    client = FileClient(mock_config)
    result = client.delete(graph_id, "file-to-delete")

    assert result is True

  @patch("robosystems_client.clients.file_client.delete_file")
  def test_delete_file_failure(self, mock_delete, mock_config, graph_id):
    """Test delete failure returns False."""
    mock_resp = Mock()
    mock_resp.status_code = 500
    mock_delete.return_value = mock_resp

    client = FileClient(mock_config)
    result = client.delete(graph_id, "file-to-delete")

    assert result is False

  @patch("robosystems_client.clients.file_client.delete_file")
  def test_delete_file_with_cascade(self, mock_delete, mock_config, graph_id):
    """Test cascade delete passes parameter."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_delete.return_value = mock_resp

    client = FileClient(mock_config)
    result = client.delete(graph_id, "file-cascade", cascade=True)

    assert result is True
    call_kwargs = mock_delete.call_args[1]
    assert call_kwargs["cascade"] is True
