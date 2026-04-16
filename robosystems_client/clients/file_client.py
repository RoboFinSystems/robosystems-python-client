"""File Client for RoboSystems API

Manages file operations as first-class resources with multi-layer status tracking.
Files are independent entities with their own lifecycle (S3 → DuckDB → Graph).
"""

from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Dict, Any, Optional, Callable, Union, BinaryIO
import logging
import httpx

from ..api.files.create_file_upload import (
  sync_detailed as create_file_upload,
)
from ..api.files.update_file import (
  sync_detailed as update_file,
)
from ..api.files.list_files import (
  sync_detailed as list_files,
)
from ..api.files.get_file import (
  sync_detailed as get_file,
)
from ..api.files.delete_file import (
  sync_detailed as delete_file,
)
from ..models.file_upload_request import FileUploadRequest
from ..models.file_status_update import FileStatusUpdate

logger = logging.getLogger(__name__)


@dataclass
class FileUploadOptions:
  """Options for file upload operations"""

  on_progress: Optional[Callable[[str], None]] = None
  ingest_to_graph: bool = False


@dataclass
class FileUploadResult:
  """Result from file upload operation"""

  file_id: str
  file_size: int
  row_count: int
  table_name: str
  file_name: str
  success: bool = True
  error: Optional[str] = None


@dataclass
class FileInfo:
  """Information about a file"""

  file_id: str
  file_name: str
  file_format: str
  size_bytes: int
  row_count: Optional[int]
  upload_status: str
  table_name: str
  created_at: Optional[str]
  uploaded_at: Optional[str]
  layers: Optional[Dict[str, Any]] = None


class FileClient:
  """Client for managing files as first-class resources"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")
    self.s3_endpoint_url = config.get(
      "s3_endpoint_url"
    )  # Optional S3 endpoint override
    self._http_client = httpx.Client(timeout=120.0)

  def upload(
    self,
    graph_id: str,
    table_name: str,
    file_or_buffer: Union[Path, str, BytesIO, BinaryIO],
    options: Optional[FileUploadOptions] = None,
  ) -> FileUploadResult:
    """
    Upload a file to a table.

    This handles the complete 3-step upload process:
    1. Get presigned upload URL
    2. Upload file to S3
    3. Mark file as 'uploaded' (triggers DuckDB staging)

    Args:
        graph_id: Graph database identifier
        table_name: Table to associate file with
        file_or_buffer: File path, Path object, BytesIO, or file-like object
        options: Upload options (progress callback, LocalStack URL fix, auto-ingest)

    Returns:
        FileUploadResult with file metadata and status
    """
    options = options or FileUploadOptions()

    try:
      # Determine file name and read content
      if isinstance(file_or_buffer, (str, Path)):
        file_path = Path(file_or_buffer)
        file_name = file_path.name
        with open(file_path, "rb") as f:
          file_content = f.read()
      elif isinstance(file_or_buffer, BytesIO):
        file_name = "data.parquet"
        file_content = file_or_buffer.getvalue()
      elif hasattr(file_or_buffer, "read"):
        file_name = getattr(file_or_buffer, "name", "data.parquet")
        file_content = file_or_buffer.read()
      else:
        raise ValueError(f"Unsupported file type: {type(file_or_buffer)}")

      # Step 1: Get presigned upload URL
      if options.on_progress:
        options.on_progress(
          f"Getting upload URL for {file_name} → table '{table_name}'..."
        )

      upload_request = FileUploadRequest(
        file_name=file_name,
        content_type="application/x-parquet",
        table_name=table_name,
      )

      from ..client import AuthenticatedClient

      if not self.token:
        raise Exception("No API key provided. Set X-API-Key in headers.")

      client = AuthenticatedClient(
        base_url=self.base_url,
        token=self.token,
        prefix="",
        auth_header_name="X-API-Key",
        headers=self.headers,
      )

      kwargs = {
        "graph_id": graph_id,
        "client": client,
        "body": upload_request,
      }

      response = create_file_upload(**kwargs)

      if response.status_code != 200 or not response.parsed:
        error_msg = f"Failed to get upload URL: {response.status_code}"
        return FileUploadResult(
          file_id="",
          file_size=0,
          row_count=0,
          table_name=table_name,
          file_name=file_name,
          success=False,
          error=error_msg,
        )

      upload_data = response.parsed
      upload_url = upload_data.upload_url
      file_id = upload_data.file_id

      # Override S3 endpoint if configured (e.g., for LocalStack)
      if self.s3_endpoint_url:
        from urllib.parse import urlparse, urlunparse

        parsed_url = urlparse(upload_url)
        override_parsed = urlparse(self.s3_endpoint_url)
        # Replace scheme, host, and port with the override endpoint
        upload_url = urlunparse(
          (
            override_parsed.scheme or parsed_url.scheme,
            override_parsed.netloc,
            parsed_url.path,
            parsed_url.params,
            parsed_url.query,
            parsed_url.fragment,
          )
        )

      # Step 2: Upload file to S3
      if options.on_progress:
        options.on_progress(f"Uploading {file_name} to S3...")

      s3_response = self._http_client.put(
        upload_url,
        content=file_content,
        headers={"Content-Type": "application/x-parquet"},
      )

      if s3_response.status_code not in [200, 204]:
        return FileUploadResult(
          file_id=file_id,
          file_size=len(file_content),
          row_count=0,
          table_name=table_name,
          file_name=file_name,
          success=False,
          error=f"S3 upload failed: {s3_response.status_code}",
        )

      # Step 3: Mark file as uploaded
      if options.on_progress:
        options.on_progress(f"Marking {file_name} as uploaded...")

      status_update = FileStatusUpdate(
        status="uploaded",
        ingest_to_graph=options.ingest_to_graph,
      )

      update_kwargs = {
        "graph_id": graph_id,
        "file_id": file_id,
        "client": client,
        "body": status_update,
      }

      update_response = update_file(**update_kwargs)

      if update_response.status_code != 200 or not update_response.parsed:
        return FileUploadResult(
          file_id=file_id,
          file_size=len(file_content),
          row_count=0,
          table_name=table_name,
          file_name=file_name,
          success=False,
          error="Failed to complete file upload",
        )

      # Extract metadata from response
      response_data = update_response.parsed
      actual_file_size = getattr(response_data, "file_size_bytes", len(file_content))
      actual_row_count = getattr(response_data, "row_count", 0)

      if options.on_progress:
        options.on_progress(
          f"✅ Uploaded {file_name} ({actual_file_size:,} bytes, {actual_row_count:,} rows)"
        )

      return FileUploadResult(
        file_id=file_id,
        file_size=actual_file_size,
        row_count=actual_row_count,
        table_name=table_name,
        file_name=file_name,
        success=True,
      )

    except Exception as e:
      logger.error(f"File upload failed: {e}")
      return FileUploadResult(
        file_id="",
        file_size=0,
        row_count=0,
        table_name=table_name,
        file_name=getattr(file_or_buffer, "name", "unknown"),
        success=False,
        error=str(e),
      )

  def list(
    self,
    graph_id: str,
    table_name: Optional[str] = None,
    status: Optional[str] = None,
  ) -> list[FileInfo]:
    """
    List files in a graph with optional filtering.

    Args:
        graph_id: Graph database identifier
        table_name: Optional table name filter
        status: Optional upload status filter (uploaded, pending, etc.)

    Returns:
        List of FileInfo objects
    """
    try:
      from ..client import AuthenticatedClient

      if not self.token:
        raise Exception("No API key provided. Set X-API-Key in headers.")

      client = AuthenticatedClient(
        base_url=self.base_url,
        token=self.token,
        prefix="",
        auth_header_name="X-API-Key",
        headers=self.headers,
      )

      kwargs = {
        "graph_id": graph_id,
        "client": client,
      }

      if table_name:
        kwargs["table_name"] = table_name
      if status:
        kwargs["status"] = status

      response = list_files(**kwargs)

      if response.status_code != 200 or not response.parsed:
        logger.error(f"Failed to list files: {response.status_code}")
        return []

      files_data = response.parsed
      files = getattr(files_data, "files", [])

      return [
        FileInfo(
          file_id=f.file_id,
          file_name=f.file_name,
          file_format=f.file_format,
          size_bytes=f.size_bytes or 0,
          row_count=f.row_count,
          upload_status=f.upload_status,
          table_name=getattr(f, "table_name", ""),
          created_at=f.created_at,
          uploaded_at=f.uploaded_at,
        )
        for f in files
      ]

    except Exception as e:
      logger.error(f"Failed to list files: {e}")
      return []

  def get(self, graph_id: str, file_id: str) -> Optional[FileInfo]:
    """
    Get detailed information about a specific file.

    Args:
        graph_id: Graph database identifier
        file_id: File ID

    Returns:
        FileInfo with multi-layer status tracking, or None if not found
    """
    try:
      from ..client import AuthenticatedClient

      if not self.token:
        raise Exception("No API key provided. Set X-API-Key in headers.")

      client = AuthenticatedClient(
        base_url=self.base_url,
        token=self.token,
        prefix="",
        auth_header_name="X-API-Key",
        headers=self.headers,
      )

      kwargs = {
        "graph_id": graph_id,
        "file_id": file_id,
        "client": client,
      }

      response = get_file(**kwargs)

      if response.status_code != 200 or not response.parsed:
        logger.error(f"Failed to get file {file_id}: {response.status_code}")
        return None

      file_data = response.parsed

      return FileInfo(
        file_id=file_data.file_id,
        file_name=file_data.file_name,
        file_format=file_data.file_format,
        size_bytes=file_data.size_bytes or 0,
        row_count=file_data.row_count,
        upload_status=file_data.upload_status,
        table_name=file_data.table_name or "",
        created_at=file_data.created_at,
        uploaded_at=file_data.uploaded_at,
        layers=getattr(file_data, "layers", None),
      )

    except Exception as e:
      logger.error(f"Failed to get file {file_id}: {e}")
      return None

  def delete(self, graph_id: str, file_id: str, cascade: bool = False) -> bool:
    """
    Delete a file from all layers.

    Args:
        graph_id: Graph database identifier
        file_id: File ID to delete
        cascade: If True, delete from all layers including DuckDB and graph

    Returns:
        True if deletion succeeded, False otherwise
    """
    try:
      from ..client import AuthenticatedClient

      if not self.token:
        raise Exception("No API key provided. Set X-API-Key in headers.")

      client = AuthenticatedClient(
        base_url=self.base_url,
        token=self.token,
        prefix="",
        auth_header_name="X-API-Key",
        headers=self.headers,
      )

      kwargs = {
        "graph_id": graph_id,
        "file_id": file_id,
        "client": client,
        "cascade": cascade,
      }

      response = delete_file(**kwargs)

      if response.status_code not in [200, 204]:
        logger.error(f"Failed to delete file {file_id}: {response.status_code}")
        return False

      return True

    except Exception as e:
      logger.error(f"Failed to delete file {file_id}: {e}")
      return False

  def __del__(self):
    """Cleanup HTTP client on deletion"""
    if hasattr(self, "_http_client"):
      self._http_client.close()
