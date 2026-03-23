"""Document Client for RoboSystems API

Upload, search, list, and delete text documents indexed in OpenSearch.
Documents are sectioned on markdown headings, embedded for semantic search,
and searchable alongside structured graph data.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import httpx
import logging

logger = logging.getLogger(__name__)


@dataclass
class DocumentUploadResult:
  """Result from document upload."""

  document_id: str
  sections_indexed: int
  total_content_length: int
  section_ids: List[str]
  success: bool = True
  error: Optional[str] = None


@dataclass
class DocumentSearchHit:
  """A single search result."""

  document_id: str
  score: float
  source_type: str
  snippet: str
  section_label: Optional[str] = None
  document_title: Optional[str] = None
  entity_ticker: Optional[str] = None
  form_type: Optional[str] = None
  filing_date: Optional[str] = None
  tags: Optional[List[str]] = None
  folder: Optional[str] = None


@dataclass
class DocumentSearchResult:
  """Result from document search."""

  total: int
  hits: List[DocumentSearchHit]
  query: str
  graph_id: str


@dataclass
class DocumentInfo:
  """Information about an indexed document."""

  document_title: str
  section_count: int
  source_type: str
  folder: Optional[str] = None
  tags: Optional[List[str]] = None
  last_indexed: Optional[str] = None


@dataclass
class DocumentListResult:
  """Result from listing documents."""

  total: int
  documents: List[DocumentInfo]
  graph_id: str


class DocumentClient:
  """Client for document upload, search, and management."""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.timeout = config.get("timeout", 60)
    self._http_client = httpx.Client(
      timeout=self.timeout,
      headers=self.headers,
    )

  def _url(self, graph_id: str, path: str = "") -> str:
    return f"{self.base_url}/v1/graphs/{graph_id}/documents{path}"

  def _search_url(self, graph_id: str, path: str = "") -> str:
    return f"{self.base_url}/v1/graphs/{graph_id}/search{path}"

  def upload(
    self,
    graph_id: str,
    title: str,
    content: str,
    tags: Optional[List[str]] = None,
    folder: Optional[str] = None,
    external_id: Optional[str] = None,
  ) -> DocumentUploadResult:
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
        DocumentUploadResult with section IDs and counts.
    """
    payload: Dict[str, Any] = {"title": title, "content": content}
    if tags is not None:
      payload["tags"] = tags
    if folder is not None:
      payload["folder"] = folder
    if external_id is not None:
      payload["external_id"] = external_id

    response = self._http_client.post(self._url(graph_id), json=payload)

    if response.status_code == 200:
      data = response.json()
      return DocumentUploadResult(
        document_id=data["document_id"],
        sections_indexed=data["sections_indexed"],
        total_content_length=data["total_content_length"],
        section_ids=data["section_ids"],
      )
    else:
      error_detail = response.text
      try:
        error_detail = response.json().get("detail", response.text)
      except Exception:
        pass
      return DocumentUploadResult(
        document_id="",
        sections_indexed=0,
        total_content_length=0,
        section_ids=[],
        success=False,
        error=f"{response.status_code}: {error_detail}",
      )

  def upload_file(
    self,
    graph_id: str,
    file_path: str | Path,
    title: Optional[str] = None,
    tags: Optional[List[str]] = None,
    folder: Optional[str] = None,
    external_id: Optional[str] = None,
  ) -> DocumentUploadResult:
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
      # Try frontmatter title, fall back to filename
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
  ) -> List[DocumentUploadResult]:
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
    semantic: bool = False,
    size: int = 10,
  ) -> DocumentSearchResult:
    """Search documents with full-text or semantic search.

    Args:
        graph_id: Target graph ID.
        query: Search query string.
        source_type: Filter by source type (uploaded_doc, memory, etc.).
        entity: Filter by entity ticker/CIK/name.
        form_type: Filter by SEC form type.
        section: Filter by section ID.
        semantic: Enable semantic (vector) search.
        size: Max results to return.

    Returns:
        DocumentSearchResult with ranked hits.
    """
    payload: Dict[str, Any] = {"query": query, "size": size}
    if source_type is not None:
      payload["source_type"] = source_type
    if entity is not None:
      payload["entity"] = entity
    if form_type is not None:
      payload["form_type"] = form_type
    if section is not None:
      payload["section"] = section
    if semantic:
      payload["semantic"] = True

    response = self._http_client.post(self._search_url(graph_id), json=payload)
    response.raise_for_status()
    data = response.json()

    hits = [
      DocumentSearchHit(
        document_id=h["document_id"],
        score=h["score"],
        source_type=h["source_type"],
        snippet=h["snippet"],
        section_label=h.get("section_label"),
        document_title=h.get("document_title"),
        entity_ticker=h.get("entity_ticker"),
        form_type=h.get("form_type"),
        filing_date=h.get("filing_date"),
        tags=h.get("tags"),
        folder=h.get("folder"),
      )
      for h in data.get("hits", [])
    ]

    return DocumentSearchResult(
      total=data["total"],
      hits=hits,
      query=data["query"],
      graph_id=data["graph_id"],
    )

  def get_section(self, graph_id: str, document_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve the full text of a document section by ID.

    Args:
        graph_id: Target graph ID.
        document_id: Document section ID.

    Returns:
        Dict with full section content and metadata, or None if not found.
    """
    response = self._http_client.get(self._search_url(graph_id, f"/{document_id}"))
    if response.status_code == 404:
      return None
    response.raise_for_status()
    return response.json()

  def list(
    self, graph_id: str, source_type: Optional[str] = None
  ) -> DocumentListResult:
    """List indexed documents for a graph.

    Args:
        graph_id: Target graph ID.
        source_type: Optional filter by source type.

    Returns:
        DocumentListResult with document inventory.
    """
    params = {}
    if source_type is not None:
      params["source_type"] = source_type

    response = self._http_client.get(self._url(graph_id), params=params)
    response.raise_for_status()
    data = response.json()

    documents = [
      DocumentInfo(
        document_title=d["document_title"],
        section_count=d["section_count"],
        source_type=d["source_type"],
        folder=d.get("folder"),
        tags=d.get("tags"),
        last_indexed=d.get("last_indexed"),
      )
      for d in data.get("documents", [])
    ]

    return DocumentListResult(
      total=data["total"],
      documents=documents,
      graph_id=data["graph_id"],
    )

  def delete(self, graph_id: str, document_id: str) -> bool:
    """Delete a document and all its sections.

    Args:
        graph_id: Target graph ID.
        document_id: Document ID to delete.

    Returns:
        True if deleted, False if not found.
    """
    response = self._http_client.delete(self._url(graph_id, f"/{document_id}"))
    if response.status_code == 204:
      return True
    if response.status_code == 404:
      return False
    response.raise_for_status()
    return False

  def close(self):
    """Close the HTTP client."""
    self._http_client.close()
