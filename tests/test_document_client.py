"""Unit tests for DocumentClient."""

import pytest
from http import HTTPStatus
from unittest.mock import Mock, patch
from robosystems_client.clients.document_client import DocumentClient


@pytest.mark.unit
class TestDocumentClientInit:
  """Test suite for DocumentClient initialization."""

  def test_client_initialization(self, mock_config):
    """Test that client initializes correctly with config."""
    client = DocumentClient(mock_config)

    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}
    assert client.timeout == 60

  def test_client_custom_timeout(self, mock_config):
    """Test client with custom timeout."""
    mock_config["timeout"] = 120
    client = DocumentClient(mock_config)

    assert client.timeout == 120

  def test_get_client_no_token(self, mock_config):
    """Test _get_client raises without token."""
    mock_config["token"] = None
    client = DocumentClient(mock_config)

    with pytest.raises(Exception, match="No API key"):
      client._get_client()

  def test_close_is_noop(self, mock_config):
    """Test close method doesn't raise."""
    client = DocumentClient(mock_config)
    client.close()  # Should not raise


@pytest.mark.unit
class TestDocumentUpload:
  """Test suite for DocumentClient.upload method."""

  @patch("robosystems_client.clients.document_client.upload_document")
  def test_upload_document(self, mock_upload, mock_config, graph_id):
    """Test uploading a markdown document."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(document_id="doc-123", section_count=3)
    mock_upload.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.upload(
      graph_id=graph_id,
      title="Test Document",
      content="# Heading\n\nSome content.",
      tags=["test", "demo"],
      folder="reports",
    )

    assert result.document_id == "doc-123"
    assert result.section_count == 3
    mock_upload.assert_called_once()

  @patch("robosystems_client.clients.document_client.upload_document")
  def test_upload_document_failure(self, mock_upload, mock_config, graph_id):
    """Test upload failure raises exception."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    mock_resp.content = b"Server error"
    mock_upload.return_value = mock_resp

    client = DocumentClient(mock_config)

    with pytest.raises(Exception, match="Document upload failed"):
      client.upload(graph_id=graph_id, title="Bad", content="content")

  @patch("robosystems_client.clients.document_client.upload_document")
  def test_upload_minimal(self, mock_upload, mock_config, graph_id):
    """Test upload with only required fields."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(document_id="doc-min", section_count=1)
    mock_upload.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.upload(graph_id=graph_id, title="Minimal", content="Just text.")

    assert result.document_id == "doc-min"


@pytest.mark.unit
class TestDocumentGet:
  """Test suite for DocumentClient.get method."""

  @patch("robosystems_client.clients.document_client.get_document")
  def test_get_document(self, mock_get, mock_config, graph_id):
    """Test getting a document by ID."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(
      document_id="doc-456", title="Found Document", content="# Content"
    )
    mock_get.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.get(graph_id=graph_id, document_id="doc-456")

    assert result is not None
    assert result.title == "Found Document"

  @patch("robosystems_client.clients.document_client.get_document")
  def test_get_document_not_found(self, mock_get, mock_config, graph_id):
    """Test getting a document that doesn't exist."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NOT_FOUND
    mock_get.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.get(graph_id=graph_id, document_id="nonexistent")

    assert result is None

  @patch("robosystems_client.clients.document_client.get_document")
  def test_get_document_server_error(self, mock_get, mock_config, graph_id):
    """Test get raises on server error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    mock_resp.content = b"Internal error"
    mock_get.return_value = mock_resp

    client = DocumentClient(mock_config)

    with pytest.raises(Exception, match="Get document failed"):
      client.get(graph_id=graph_id, document_id="doc-err")


@pytest.mark.unit
class TestDocumentUpdate:
  """Test suite for DocumentClient.update method."""

  @patch("robosystems_client.clients.document_client.update_document")
  def test_update_document(self, mock_update, mock_config, graph_id):
    """Test updating a document."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(document_id="doc-upd", section_count=5)
    mock_update.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.update(
      graph_id=graph_id,
      document_id="doc-upd",
      title="Updated Title",
      content="# Updated\n\nNew content.",
    )

    assert result.section_count == 5

  @patch("robosystems_client.clients.document_client.update_document")
  def test_update_document_failure(self, mock_update, mock_config, graph_id):
    """Test update failure raises exception."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.BAD_REQUEST
    mock_resp.content = b"Bad request"
    mock_update.return_value = mock_resp

    client = DocumentClient(mock_config)

    with pytest.raises(Exception, match="Update document failed"):
      client.update(graph_id=graph_id, document_id="doc-bad", title="Bad")


@pytest.mark.unit
class TestDocumentSearch:
  """Test suite for DocumentClient.search method."""

  @patch("robosystems_client.clients.document_client.search_documents")
  def test_search_documents(self, mock_search, mock_config, graph_id):
    """Test searching documents."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(total=2, hits=[Mock(), Mock()])
    mock_search.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.search(graph_id=graph_id, query="revenue growth")

    assert result.total == 2
    assert len(result.hits) == 2

  @patch("robosystems_client.clients.document_client.search_documents")
  def test_search_with_filters(self, mock_search, mock_config, graph_id):
    """Test searching with filters."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(total=1, hits=[Mock()])
    mock_search.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.search(
      graph_id=graph_id,
      query="risk factors",
      source_type="xbrl_textblock",
      form_type="10-K",
      entity="AAPL",
      fiscal_year=2024,
      size=5,
    )

    assert result.total == 1
    mock_search.assert_called_once()

  @patch("robosystems_client.clients.document_client.search_documents")
  def test_search_failure(self, mock_search, mock_config, graph_id):
    """Test search failure raises exception."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    mock_resp.content = b"Search error"
    mock_search.return_value = mock_resp

    client = DocumentClient(mock_config)

    with pytest.raises(Exception, match="Document search failed"):
      client.search(graph_id=graph_id, query="test")


@pytest.mark.unit
class TestDocumentList:
  """Test suite for DocumentClient.list method."""

  @patch("robosystems_client.clients.document_client.list_documents")
  def test_list_documents(self, mock_list, mock_config, graph_id):
    """Test listing documents."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(total=3, documents=[Mock(), Mock(), Mock()])
    mock_list.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.list(graph_id=graph_id)

    assert result.total == 3

  @patch("robosystems_client.clients.document_client.list_documents")
  def test_list_documents_with_filter(self, mock_list, mock_config, graph_id):
    """Test listing with source type filter."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(total=1, documents=[Mock()])
    mock_list.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.list(graph_id=graph_id, source_type="uploaded_doc")

    assert result.total == 1


@pytest.mark.unit
class TestDocumentDelete:
  """Test suite for DocumentClient.delete method."""

  @patch("robosystems_client.clients.document_client.delete_document")
  def test_delete_document(self, mock_delete, mock_config, graph_id):
    """Test deleting a document."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NO_CONTENT
    mock_delete.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.delete(graph_id=graph_id, document_id="doc-del")

    assert result is True

  @patch("robosystems_client.clients.document_client.delete_document")
  def test_delete_document_not_found(self, mock_delete, mock_config, graph_id):
    """Test deleting a document that doesn't exist."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NOT_FOUND
    mock_delete.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.delete(graph_id=graph_id, document_id="doc-missing")

    assert result is False

  @patch("robosystems_client.clients.document_client.delete_document")
  def test_delete_document_server_error(self, mock_delete, mock_config, graph_id):
    """Test delete raises on server error."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    mock_resp.content = b"Delete error"
    mock_delete.return_value = mock_resp

    client = DocumentClient(mock_config)

    with pytest.raises(Exception, match="Delete document failed"):
      client.delete(graph_id=graph_id, document_id="doc-err")


@pytest.mark.unit
class TestDocumentSection:
  """Test suite for DocumentClient.get_section method."""

  @patch("robosystems_client.clients.document_client.get_document_section")
  def test_get_section(self, mock_get_section, mock_config, graph_id):
    """Test getting a document section."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(
      section_id="sec-1", title="Revenue", content="Revenue was $1B."
    )
    mock_get_section.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.get_section(graph_id=graph_id, document_id="sec-1")

    assert result is not None
    assert result.title == "Revenue"

  @patch("robosystems_client.clients.document_client.get_document_section")
  def test_get_section_not_found(self, mock_get_section, mock_config, graph_id):
    """Test getting a section that doesn't exist."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.NOT_FOUND
    mock_get_section.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.get_section(graph_id=graph_id, document_id="nonexistent")

    assert result is None


@pytest.mark.unit
class TestDocumentBulkUpload:
  """Test suite for DocumentClient.upload_bulk method."""

  @patch("robosystems_client.clients.document_client.upload_documents_bulk")
  def test_upload_bulk(self, mock_bulk, mock_config, graph_id):
    """Test bulk uploading documents."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(total=2, succeeded=2, failed=0, results=[Mock(), Mock()])
    mock_bulk.return_value = mock_resp

    client = DocumentClient(mock_config)
    docs = [
      {"title": "Doc 1", "content": "Content 1"},
      {"title": "Doc 2", "content": "Content 2", "tags": ["tag1"]},
    ]
    result = client.upload_bulk(graph_id=graph_id, documents=docs)

    assert result.total == 2
    assert result.succeeded == 2

  @patch("robosystems_client.clients.document_client.upload_documents_bulk")
  def test_upload_bulk_failure(self, mock_bulk, mock_config, graph_id):
    """Test bulk upload failure raises exception."""
    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.BAD_REQUEST
    mock_resp.content = b"Bulk upload error"
    mock_bulk.return_value = mock_resp

    client = DocumentClient(mock_config)

    with pytest.raises(Exception, match="Bulk upload failed"):
      client.upload_bulk(graph_id=graph_id, documents=[{"title": "x", "content": "y"}])


@pytest.mark.unit
class TestDocumentUploadFile:
  """Test suite for DocumentClient.upload_file method."""

  @patch("robosystems_client.clients.document_client.upload_document")
  def test_upload_file(self, mock_upload, mock_config, graph_id, tmp_path):
    """Test uploading a file from disk."""
    md_file = tmp_path / "test-doc.md"
    md_file.write_text("# Test\n\nContent here.")

    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(document_id="doc-file", section_count=2)
    mock_upload.return_value = mock_resp

    client = DocumentClient(mock_config)
    result = client.upload_file(graph_id=graph_id, file_path=md_file)

    assert result.document_id == "doc-file"

  @patch("robosystems_client.clients.document_client.upload_document")
  def test_upload_file_title_from_filename(
    self, mock_upload, mock_config, graph_id, tmp_path
  ):
    """Test that title is derived from filename when not provided."""
    md_file = tmp_path / "revenue-analysis.md"
    md_file.write_text("# Revenue\n\nAnalysis content.")

    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(document_id="doc-title", section_count=1)
    mock_upload.return_value = mock_resp

    client = DocumentClient(mock_config)
    client.upload_file(graph_id=graph_id, file_path=md_file)

    # Verify the body was created with title derived from filename
    call_kwargs = mock_upload.call_args[1]
    assert call_kwargs["body"].title == "Revenue Analysis"


@pytest.mark.unit
class TestDocumentUploadDirectory:
  """Test suite for DocumentClient.upload_directory method."""

  @patch("robosystems_client.clients.document_client.upload_document")
  def test_upload_directory(self, mock_upload, mock_config, graph_id, tmp_path):
    """Test uploading all markdown files from a directory."""
    (tmp_path / "doc1.md").write_text("# Doc 1")
    (tmp_path / "doc2.md").write_text("# Doc 2")
    (tmp_path / "not-md.txt").write_text("Skip this")

    mock_resp = Mock()
    mock_resp.status_code = HTTPStatus.OK
    mock_resp.parsed = Mock(document_id="doc-dir", section_count=1)
    mock_upload.return_value = mock_resp

    client = DocumentClient(mock_config)
    results = client.upload_directory(graph_id=graph_id, directory=tmp_path)

    assert len(results) == 2  # Only .md files
