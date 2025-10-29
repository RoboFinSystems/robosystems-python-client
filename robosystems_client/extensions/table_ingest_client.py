"""Table Ingest Client for RoboSystems API

Simplifies uploading Parquet files to staging tables and ingesting them into graphs.
"""

from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Dict, Any, Optional, Callable, List, Union, BinaryIO
import json
import logging
import httpx

from ..api.tables.get_upload_url import (
  sync_detailed as get_upload_url,
)
from ..api.tables.update_file_status import (
  sync_detailed as update_file_status,
)
from ..api.tables.list_tables import (
  sync_detailed as list_tables,
)
from ..api.tables.ingest_tables import (
  sync_detailed as ingest_tables,
)
from ..models.file_upload_request import FileUploadRequest
from ..models.file_status_update import FileStatusUpdate
from ..models.bulk_ingest_request import BulkIngestRequest

logger = logging.getLogger(__name__)


@dataclass
class UploadOptions:
  """Options for file upload operations"""

  on_progress: Optional[Callable[[str], None]] = None
  fix_localstack_url: bool = True  # Auto-fix LocalStack URLs for localhost
  file_name: Optional[str] = None  # Override file name (useful for buffer uploads)


@dataclass
class IngestOptions:
  """Options for table ingestion operations"""

  ignore_errors: bool = True
  rebuild: bool = False
  on_progress: Optional[Callable[[str], None]] = None


@dataclass
class UploadResult:
  """Result from file upload operation"""

  file_id: str
  file_size: int
  row_count: int
  table_name: str
  file_name: str
  success: bool = True
  error: Optional[str] = None


@dataclass
class TableInfo:
  """Information about a staging table"""

  table_name: str
  row_count: int
  file_count: int
  total_size_bytes: int


class TableIngestClient:
  """Enhanced table ingest client with simplified upload workflow"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")
    # Create httpx client for S3 uploads
    self._http_client = httpx.Client(timeout=120.0)

  def upload_parquet_file(
    self,
    graph_id: str,
    table_name: str,
    file_or_buffer: Union[Path, str, BytesIO, BinaryIO],
    options: Optional[UploadOptions] = None,
  ) -> UploadResult:
    """
    Upload a Parquet file to a staging table.

    This method handles the complete 3-step upload process:
    1. Get presigned upload URL
    2. Upload file to S3
    3. Mark file as 'uploaded' (backend validates, calculates size/row count)

    Args:
        graph_id: The graph ID
        table_name: Name of the staging table
        file_or_buffer: Path to the Parquet file or BytesIO/BinaryIO buffer
        options: Upload options

    Returns:
        UploadResult with upload details (size/row count calculated by backend)
    """
    if options is None:
      options = UploadOptions()

    # Auto-detect if this is a file path or buffer
    is_buffer = isinstance(file_or_buffer, (BytesIO, BinaryIO)) or hasattr(
      file_or_buffer, "read"
    )

    # Initialize file_path for type checking
    file_path: Optional[Path] = None

    if is_buffer:
      # Handle buffer upload
      file_name = options.file_name or "data.parquet"
    else:
      # Handle file path upload
      file_path = Path(file_or_buffer)
      file_name = file_path.name
      if not file_path.exists():
        return UploadResult(
          file_id="",
          file_size=0,
          row_count=0,
          table_name=table_name,
          file_name=file_name,
          success=False,
          error=f"File not found: {file_path}",
        )

    try:
      # Import client here to avoid circular imports
      from ..client import AuthenticatedClient

      # Create authenticated client with X-API-Key
      # The token is extracted from X-API-Key header in extensions.py
      if not self.token:
        return UploadResult(
          file_id="",
          file_size=0,
          row_count=0,
          table_name=table_name,
          file_name=file_name,
          success=False,
          error="No API key provided. Set X-API-Key in headers.",
        )

      client = AuthenticatedClient(
        base_url=self.base_url,
        token=self.token,
        prefix="",  # No prefix for X-API-Key
        auth_header_name="X-API-Key",  # Use X-API-Key header instead of Authorization
        headers=self.headers,
      )

      # Step 1: Get presigned upload URL
      if options.on_progress:
        options.on_progress(
          f"Getting upload URL for {file_name} -> table '{table_name}'..."
        )

      upload_request = FileUploadRequest(
        file_name=file_name, content_type="application/x-parquet"
      )

      kwargs = {
        "graph_id": graph_id,
        "table_name": table_name,
        "client": client,
        "body": upload_request,
      }

      response = get_upload_url(**kwargs)

      if not response.parsed:
        error_msg = f"Failed to get upload URL (status: {response.status_code})"
        if hasattr(response, "content"):
          try:
            error_detail = json.loads(response.content)
            error_msg = f"{error_msg}: {error_detail}"
          except (json.JSONDecodeError, ValueError):
            error_msg = f"{error_msg}: {response.content[:200]}"

        return UploadResult(
          file_id="",
          file_size=0,
          row_count=0,
          table_name=table_name,
          file_name=file_name,
          success=False,
          error=error_msg,
        )

      upload_url = response.parsed.upload_url
      file_id = response.parsed.file_id

      # Fix LocalStack URL if needed
      if options.fix_localstack_url and "localstack:4566" in upload_url:
        upload_url = upload_url.replace("localstack:4566", "localhost:4566")
        logger.debug("Fixed LocalStack URL for localhost access")

      # Step 2: Upload file to S3
      if options.on_progress:
        options.on_progress(f"Uploading {file_name} to S3...")

      # Read file content - handle both paths and buffers
      if is_buffer:
        # Read from buffer
        if hasattr(file_or_buffer, "getvalue"):
          file_content = file_or_buffer.getvalue()
        else:
          # BinaryIO or file-like object
          file_or_buffer.seek(0)
          file_content = file_or_buffer.read()
      else:
        # Read from file path
        if file_path is None:
          raise ValueError("file_path should not be None when not using buffer")
        with open(file_path, "rb") as f:
          file_content = f.read()

      s3_response = self._http_client.put(
        upload_url,
        content=file_content,
        headers={"Content-Type": "application/x-parquet"},
      )
      s3_response.raise_for_status()

      # Step 3: Mark file as uploaded (backend validates and calculates size/row count)
      if options.on_progress:
        options.on_progress(f"Marking {file_name} as uploaded...")

      status_update = FileStatusUpdate(status="uploaded")

      kwargs = {
        "graph_id": graph_id,
        "file_id": file_id,
        "client": client,
        "body": status_update,
      }

      update_response = update_file_status(**kwargs)

      if not update_response.parsed:
        logger.error(
          f"No parsed response from update_file_status. Status code: {update_response.status_code}"
        )
        return UploadResult(
          file_id=file_id,
          file_size=0,
          row_count=0,
          table_name=table_name,
          file_name=file_name,
          success=False,
          error="Failed to complete file upload",
        )

      response_data = update_response.parsed

      if isinstance(response_data, dict):
        file_size = response_data.get("file_size_bytes", 0)
        row_count = response_data.get("row_count", 0)
      elif hasattr(response_data, "additional_properties"):
        file_size = response_data.additional_properties.get("file_size_bytes", 0)
        row_count = response_data.additional_properties.get("row_count", 0)
      else:
        file_size = getattr(response_data, "file_size_bytes", 0)
        row_count = getattr(response_data, "row_count", 0)

      if options.on_progress:
        options.on_progress(
          f"✅ Uploaded {file_name} ({file_size:,} bytes, {row_count:,} rows)"
        )

      return UploadResult(
        file_id=file_id,
        file_size=file_size,
        row_count=row_count,
        table_name=table_name,
        file_name=file_name,
        success=True,
      )

    except Exception as e:
      logger.error(f"Upload failed for {file_name}: {e}")
      return UploadResult(
        file_id="",
        file_size=0,
        row_count=0,
        table_name=table_name,
        file_name=file_name,
        success=False,
        error=str(e),
      )

  def list_staging_tables(self, graph_id: str) -> List[TableInfo]:
    """
    List all staging tables in a graph.

    Args:
        graph_id: The graph ID

    Returns:
        List of TableInfo objects
    """
    try:
      from ..client import AuthenticatedClient

      if not self.token:
        logger.error("No API key provided")
        return []

      client = AuthenticatedClient(
        base_url=self.base_url,
        token=self.token,
        prefix="",
        auth_header_name="X-API-Key",
        headers=self.headers,
      )

      kwargs = {"graph_id": graph_id, "client": client}

      response = list_tables(**kwargs)

      if not response.parsed:
        logger.error("Failed to list tables")
        return []

      tables = []
      for table_data in response.parsed.tables:
        tables.append(
          TableInfo(
            table_name=table_data.table_name,
            row_count=table_data.row_count,
            file_count=table_data.file_count,
            total_size_bytes=table_data.total_size_bytes,
          )
        )

      return tables

    except Exception as e:
      logger.error(f"Failed to list tables: {e}")
      return []

  def ingest_all_tables(
    self, graph_id: str, options: Optional[IngestOptions] = None
  ) -> Dict[str, Any]:
    """
    Ingest all staging tables into the graph.

    Args:
        graph_id: The graph ID
        options: Ingest options

    Returns:
        Dictionary with ingestion results
    """
    if options is None:
      options = IngestOptions()

    try:
      from ..client import AuthenticatedClient

      if not self.token:
        return {"success": False, "error": "No API key provided"}

      client = AuthenticatedClient(
        base_url=self.base_url,
        token=self.token,
        prefix="",
        auth_header_name="X-API-Key",
        headers=self.headers,
      )

      if options.on_progress:
        options.on_progress("Starting table ingestion...")

      ingest_request = BulkIngestRequest(
        ignore_errors=options.ignore_errors, rebuild=options.rebuild
      )

      kwargs = {
        "graph_id": graph_id,
        "client": client,
        "body": ingest_request,
      }

      response = ingest_tables(**kwargs)

      if not response.parsed:
        return {"success": False, "error": "Failed to ingest tables"}

      result = {
        "success": True,
        "operation_id": getattr(response.parsed, "operation_id", None),
        "message": getattr(response.parsed, "message", "Ingestion started"),
      }

      if options.on_progress:
        options.on_progress("✅ Table ingestion completed")

      return result

    except Exception as e:
      logger.error(f"Failed to ingest tables: {e}")
      return {"success": False, "error": str(e)}

  def upload_and_ingest(
    self,
    graph_id: str,
    table_name: str,
    file_path: Path,
    upload_options: Optional[UploadOptions] = None,
    ingest_options: Optional[IngestOptions] = None,
  ) -> Dict[str, Any]:
    """
    Convenience method to upload a file and immediately ingest it.

    Args:
        graph_id: The graph ID
        table_name: Name of the staging table
        file_path: Path to the Parquet file
        upload_options: Upload options
        ingest_options: Ingest options

    Returns:
        Dictionary with upload and ingest results
    """
    # Upload the file
    upload_result = self.upload_parquet_file(
      graph_id, table_name, file_path, upload_options
    )

    if not upload_result.success:
      return {
        "success": False,
        "upload": upload_result,
        "ingest": None,
        "error": upload_result.error,
      }

    # Ingest the table
    ingest_result = self.ingest_all_tables(graph_id, ingest_options)

    return {
      "success": upload_result.success and ingest_result.get("success", False),
      "upload": upload_result,
      "ingest": ingest_result,
    }

  def close(self):
    """Close HTTP client connections"""
    if self._http_client:
      self._http_client.close()
