"""Document Client for RoboSystems API

Upload, search, list, and delete text documents indexed in OpenSearch.
Documents are sectioned on markdown headings, embedded for semantic search,
and searchable alongside structured graph data.
"""

from http import HTTPStatus
from pathlib import Path
from typing import Any, Dict, List, Optional

from ..api.documents.delete_document import sync_detailed as delete_document
from ..api.documents.list_documents import sync_detailed as list_documents
from ..api.documents.upload_document import sync_detailed as upload_document
from ..api.search.get_document_section import sync_detailed as get_document_section
from ..api.search.search_documents import sync_detailed as search_documents
from ..client import AuthenticatedClient
from ..models.document_list_response import DocumentListResponse
from ..models.document_section import DocumentSection
from ..models.document_upload_request import DocumentUploadRequest
from ..models.document_upload_response import DocumentUploadResponse
from ..models.search_request import SearchRequest
from ..models.search_response import SearchResponse
from ..types import UNSET


class DocumentClient:
  """Client for document upload, search, and management."""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")
    self.timeout = config.get("timeout", 60)

  def _get_client(self) -> AuthenticatedClient:
    if not self.token:
      raise Exception("No API key provided. Set X-API-Key in headers.")
    return AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

  def upload(
    self,
    graph_id: str,
    title: str,
    content: str,
    tags: Optional[List[str]] = None,
    folder: Optional[str] = None,
    external_id: Optional[str] = None,
  ) -> DocumentUploadResponse:
    """Upload a markdown document for text indexing.

    The document is sectioned on headings, embedded, and indexed
    into OpenSearch for full-text and semantic search.

    Args:
        graph_id: Target graph ID.
        title: Document title.
        content: Markdown content (may include YAML frontmatter).
        tags: Optional tags for filtering.
        folder: Optional folder/category.
        external_id: Optional external ID for upsert behavior.

    Returns:
        DocumentUploadResponse with section IDs and counts.
    """
    body = DocumentUploadRequest(
      title=title,
      content=content,
      tags=tags if tags is not None else UNSET,
      folder=folder if folder is not None else UNSET,
      external_id=external_id if external_id is not None else UNSET,
    )

    client = self._get_client()
    response = upload_document(graph_id=graph_id, client=client, body=body)
    if response.status_code != HTTPStatus.OK:
      raise Exception(
        f"Document upload failed ({response.status_code}): {response.content.decode()}"
      )
    return response.parsed

  def upload_file(
    self,
    graph_id: str,
    file_path: str | Path,
    title: Optional[str] = None,
    tags: Optional[List[str]] = None,
    folder: Optional[str] = None,
    external_id: Optional[str] = None,
  ) -> DocumentUploadResponse:
    """Upload a markdown file by path.

    Reads the file, optionally extracts title from filename,
    and uploads via the document API.

    Args:
        graph_id: Target graph ID.
        file_path: Path to markdown file.
        title: Document title (defaults to filename).
        tags: Optional tags.
        folder: Optional folder.
        external_id: Optional external ID.
    """
    path = Path(file_path)
    content = path.read_text()

    if title is None:
      title = path.stem.replace("-", " ").replace("_", " ").title()

    return self.upload(
      graph_id=graph_id,
      title=title,
      content=content,
      tags=tags,
      folder=folder,
      external_id=external_id,
    )

  def upload_directory(
    self,
    graph_id: str,
    directory: str | Path,
    pattern: str = "*.md",
    folder: Optional[str] = None,
  ) -> List[DocumentUploadResponse]:
    """Upload all markdown files from a directory.

    Args:
        graph_id: Target graph ID.
        directory: Path to directory containing markdown files.
        pattern: Glob pattern for file matching (default: *.md).
        folder: Optional folder to apply to all documents.

    Returns:
        List of upload results, one per file.
    """
    dir_path = Path(directory)
    results = []

    for md_file in sorted(dir_path.glob(pattern)):
      result = self.upload_file(
        graph_id=graph_id,
        file_path=md_file,
        folder=folder,
      )
      results.append(result)

    return results

  def search(
    self,
    graph_id: str,
    query: str,
    source_type: Optional[str] = None,
    entity: Optional[str] = None,
    form_type: Optional[str] = None,
    section: Optional[str] = None,
    element: Optional[str] = None,
    fiscal_year: Optional[int] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    size: int = 10,
  ) -> SearchResponse:
    """Search documents with hybrid (BM25 + KNN) search.

    Args:
        graph_id: Target graph ID.
        query: Search query string.
        source_type: Filter by source type (xbrl_textblock, narrative_section,
            ixbrl_disclosure, uploaded_doc, memory).
        entity: Filter by entity ticker/CIK/name.
        form_type: Filter by SEC form type (10-K, 10-Q).
        section: Filter by section ID (item_1, item_1a, item_7, etc.).
        element: Filter by XBRL element qname (e.g., us-gaap:Goodwill).
        fiscal_year: Filter by fiscal year.
        date_from: Filter filings on or after date (YYYY-MM-DD).
        date_to: Filter filings on or before date (YYYY-MM-DD).
        size: Max results to return.

    Returns:
        SearchResponse with ranked hits.
    """
    body = SearchRequest(
      query=query,
      source_type=source_type if source_type is not None else UNSET,
      entity=entity if entity is not None else UNSET,
      form_type=form_type if form_type is not None else UNSET,
      section=section if section is not None else UNSET,
      element=element if element is not None else UNSET,
      fiscal_year=fiscal_year if fiscal_year is not None else UNSET,
      date_from=date_from if date_from is not None else UNSET,
      date_to=date_to if date_to is not None else UNSET,
      size=size,
    )

    client = self._get_client()
    response = search_documents(graph_id=graph_id, client=client, body=body)
    if response.status_code != HTTPStatus.OK:
      raise Exception(
        f"Document search failed ({response.status_code}): {response.content.decode()}"
      )
    return response.parsed

  def get_section(self, graph_id: str, document_id: str) -> Optional[DocumentSection]:
    """Retrieve the full text of a document section by ID.

    Args:
        graph_id: Target graph ID.
        document_id: Document section ID.

    Returns:
        DocumentSection with full content and metadata, or None if not found.
    """
    client = self._get_client()
    response = get_document_section(
      graph_id=graph_id, document_id=document_id, client=client
    )
    if response.status_code == HTTPStatus.NOT_FOUND:
      return None
    if response.status_code != HTTPStatus.OK:
      raise Exception(
        f"Get section failed ({response.status_code}): {response.content.decode()}"
      )
    return response.parsed

  def list(
    self, graph_id: str, source_type: Optional[str] = None
  ) -> DocumentListResponse:
    """List indexed documents for a graph.

    Args:
        graph_id: Target graph ID.
        source_type: Optional filter by source type.

    Returns:
        DocumentListResponse with document inventory.
    """
    client = self._get_client()
    response = list_documents(
      graph_id=graph_id,
      client=client,
      source_type=source_type if source_type is not None else UNSET,
    )
    if response.status_code != HTTPStatus.OK:
      raise Exception(
        f"List documents failed ({response.status_code}): {response.content.decode()}"
      )
    return response.parsed

  def delete(self, graph_id: str, document_id: str) -> bool:
    """Delete a document and all its sections.

    Args:
        graph_id: Target graph ID.
        document_id: Document ID to delete.

    Returns:
        True if deleted, False if not found.
    """
    client = self._get_client()
    response = delete_document(
      graph_id=graph_id, document_id=document_id, client=client
    )
    if response.status_code == HTTPStatus.NO_CONTENT:
      return True
    if response.status_code == HTTPStatus.NOT_FOUND:
      return False
    raise Exception(
      f"Delete document failed ({response.status_code}): {response.content.decode()}"
    )

  def close(self):
    """Close the client (no-op, AuthenticatedClient is created per-call)."""
    pass
