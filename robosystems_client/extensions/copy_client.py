"""Enhanced Copy Client with SSE support

Provides intelligent data copy operations with progress monitoring.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable, Union, List
from enum import Enum
import time
import logging

from ..api.copy.copy_data_to_graph import sync_detailed as copy_data_to_graph
from ..models.s3_copy_request import S3CopyRequest
from ..models.url_copy_request import URLCopyRequest
from ..models.data_frame_copy_request import DataFrameCopyRequest
from ..models.copy_response import CopyResponse
from ..models.copy_response_status import CopyResponseStatus
from ..models.s3_copy_request_file_format import S3CopyRequestFileFormat
from .sse_client import SSEClient, AsyncSSEClient, SSEConfig, EventType

logger = logging.getLogger(__name__)


class CopySourceType(Enum):
  """Types of copy sources"""

  S3 = "s3"
  URL = "url"
  DATAFRAME = "dataframe"


@dataclass
class CopyOptions:
  """Options for copy operations"""

  on_progress: Optional[Callable[[str, Optional[float]], None]] = None
  on_queue_update: Optional[Callable[[int, int], None]] = None
  on_warning: Optional[Callable[[str], None]] = None
  timeout: Optional[int] = None
  test_mode: Optional[bool] = None


@dataclass
class CopyResult:
  """Result from copy operation"""

  status: str  # 'completed', 'failed', 'partial', 'accepted'
  rows_imported: Optional[int] = None
  rows_skipped: Optional[int] = None
  bytes_processed: Optional[int] = None
  execution_time_ms: Optional[float] = None
  warnings: Optional[List[str]] = None
  error: Optional[str] = None
  operation_id: Optional[str] = None
  sse_url: Optional[str] = None
  message: Optional[str] = None


@dataclass
class CopyStatistics:
  """Statistics from copy operation"""

  total_rows: int
  imported_rows: int
  skipped_rows: int
  bytes_processed: int
  duration: float  # seconds
  throughput: float  # rows per second


class CopyClient:
  """Enhanced copy client with SSE streaming support"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    # Get token from config if passed by parent
    self.token = config.get("token")
    self.sse_client: Optional[SSEClient] = None

  def copy_from_s3(
    self, graph_id: str, request: S3CopyRequest, options: Optional[CopyOptions] = None
  ) -> CopyResult:
    """Copy data from S3 to graph database"""
    return self._execute_copy(graph_id, request, CopySourceType.S3, options)

  def copy_from_url(
    self, graph_id: str, request: URLCopyRequest, options: Optional[CopyOptions] = None
  ) -> CopyResult:
    """Copy data from URL to graph database (when available)"""
    return self._execute_copy(graph_id, request, CopySourceType.URL, options)

  def copy_from_dataframe(
    self,
    graph_id: str,
    request: DataFrameCopyRequest,
    options: Optional[CopyOptions] = None,
  ) -> CopyResult:
    """Copy data from DataFrame to graph database (when available)"""
    return self._execute_copy(graph_id, request, CopySourceType.DATAFRAME, options)

  def _execute_copy(
    self,
    graph_id: str,
    request: Union[S3CopyRequest, URLCopyRequest, DataFrameCopyRequest],
    source_type: CopySourceType,
    options: Optional[CopyOptions] = None,
  ) -> CopyResult:
    """Execute copy operation with automatic SSE monitoring for long-running operations"""
    if options is None:
      options = CopyOptions()

    start_time = time.time()

    # Import client here to avoid circular imports
    from ..client import Client

    # Create client with headers
    client = Client(base_url=self.base_url, headers=self.headers)

    try:
      # Execute the copy request with token if available
      kwargs = {"graph_id": graph_id, "client": client, "body": request}
      # Only add token if it's a valid string
      if self.token and isinstance(self.token, str) and self.token.strip():
        kwargs["token"] = self.token
      response = copy_data_to_graph(**kwargs)

      if response.parsed:
        response_data: CopyResponse = response.parsed

        # Check if this is an accepted (async) operation
        if (
          response_data.status == CopyResponseStatus.ACCEPTED
          and response_data.operation_id
        ):
          # This is a long-running operation with SSE monitoring
          if options.on_progress:
            options.on_progress("Copy operation started. Monitoring progress...", None)

          # If SSE URL is provided, use it for monitoring
          if response_data.sse_url:
            return self._monitor_copy_operation(
              response_data.operation_id, options, start_time
            )

          # Otherwise return the accepted response
          return CopyResult(
            status="accepted",
            operation_id=response_data.operation_id,
            sse_url=response_data.sse_url,
            message=response_data.message,
          )

        # This is a synchronous response - operation completed immediately
        return self._build_copy_result(response_data, time.time() - start_time)
      else:
        return CopyResult(
          status="failed",
          error="No response data received",
          execution_time_ms=(time.time() - start_time) * 1000,
        )

    except Exception as e:
      error_msg = str(e)
      # Check for authentication errors
      if (
        "401" in error_msg or "403" in error_msg or "unauthorized" in error_msg.lower()
      ):
        logger.error(f"Authentication failed during copy operation: {e}")
        return CopyResult(
          status="failed",
          error=f"Authentication failed: {error_msg}",
          execution_time_ms=(time.time() - start_time) * 1000,
        )
      else:
        logger.error(f"Copy operation failed: {e}")
        return CopyResult(
          status="failed",
          error=error_msg,
          execution_time_ms=(time.time() - start_time) * 1000,
        )

  def _monitor_copy_operation(
    self, operation_id: str, options: CopyOptions, start_time: float
  ) -> CopyResult:
    """Monitor a copy operation using SSE"""
    timeout_ms = options.timeout or 3600000  # Default 1 hour for copy operations
    timeout_time = time.time() + (timeout_ms / 1000)

    result = CopyResult(status="failed")
    warnings: List[str] = []

    # Set up SSE connection
    sse_config = SSEConfig(base_url=self.base_url, timeout=timeout_ms // 1000)
    sse_client = SSEClient(sse_config)

    try:
      sse_client.connect(operation_id)

      # Set up event handlers
      def on_queue_update(data):
        if options.on_queue_update:
          position = data.get("position", data.get("queue_position", 0))
          wait_time = data.get("estimated_wait_seconds", 0)
          options.on_queue_update(position, wait_time)

      def on_progress(data):
        if options.on_progress:
          message = data.get("message", data.get("status", "Processing..."))
          progress_percent = data.get("progress_percent", data.get("progress"))
          options.on_progress(message, progress_percent)

        # Check for warnings in progress updates
        if "warnings" in data and data["warnings"]:
          warnings.extend(data["warnings"])
          if options.on_warning:
            for warning in data["warnings"]:
              options.on_warning(warning)

      def on_completed(data):
        nonlocal result
        completion_data = data.get("result", data)
        result = CopyResult(
          status=completion_data.get("status", "completed"),
          rows_imported=completion_data.get("rows_imported"),
          rows_skipped=completion_data.get("rows_skipped"),
          bytes_processed=completion_data.get("bytes_processed"),
          execution_time_ms=(time.time() - start_time) * 1000,
          warnings=warnings if warnings else completion_data.get("warnings"),
          message=completion_data.get("message"),
        )

      def on_error(data):
        nonlocal result
        result = CopyResult(
          status="failed",
          error=data.get("message", data.get("error", "Copy operation failed")),
          execution_time_ms=(time.time() - start_time) * 1000,
          warnings=warnings if warnings else None,
        )

      def on_cancelled(data):
        nonlocal result
        result = CopyResult(
          status="failed",
          error="Copy operation cancelled",
          execution_time_ms=(time.time() - start_time) * 1000,
          warnings=warnings if warnings else None,
        )

      # Register event handlers
      sse_client.on(EventType.QUEUE_UPDATE.value, on_queue_update)
      sse_client.on(EventType.OPERATION_PROGRESS.value, on_progress)
      sse_client.on(EventType.OPERATION_COMPLETED.value, on_completed)
      sse_client.on(EventType.OPERATION_ERROR.value, on_error)
      sse_client.on(EventType.OPERATION_CANCELLED.value, on_cancelled)

      # Listen for events until completion or timeout
      while time.time() < timeout_time:
        sse_client.listen(timeout=1)  # Process events for 1 second

        # Check if operation is complete
        if result.status in ["completed", "failed", "partial"]:
          break

      if time.time() >= timeout_time:
        result = CopyResult(
          status="failed",
          error=f"Copy operation timeout after {timeout_ms}ms",
          execution_time_ms=(time.time() - start_time) * 1000,
        )

    finally:
      sse_client.close()

    return result

  def _build_copy_result(
    self, response_data: CopyResponse, execution_time: float
  ) -> CopyResult:
    """Build copy result from response data"""
    return CopyResult(
      status=response_data.status.value,
      rows_imported=response_data.rows_imported,
      rows_skipped=response_data.rows_skipped,
      bytes_processed=response_data.bytes_processed,
      execution_time_ms=response_data.execution_time_ms or (execution_time * 1000),
      warnings=response_data.warnings,
      message=response_data.message,
      error=str(response_data.error_details) if response_data.error_details else None,
    )

  def calculate_statistics(self, result: CopyResult) -> Optional[CopyStatistics]:
    """Calculate copy statistics from result"""
    if result.status == "failed" or not result.rows_imported:
      return None

    total_rows = (result.rows_imported or 0) + (result.rows_skipped or 0)
    duration = (result.execution_time_ms or 0) / 1000  # Convert to seconds
    throughput = (result.rows_imported or 0) / duration if duration > 0 else 0

    return CopyStatistics(
      total_rows=total_rows,
      imported_rows=result.rows_imported or 0,
      skipped_rows=result.rows_skipped or 0,
      bytes_processed=result.bytes_processed or 0,
      duration=duration,
      throughput=throughput,
    )

  def copy_s3(
    self,
    graph_id: str,
    table_name: str,
    s3_path: str,
    access_key_id: str,
    secret_access_key: str,
    region: str = "us-east-1",
    file_format: Optional[str] = None,
    ignore_errors: bool = False,
  ) -> CopyResult:
    """Convenience method for simple S3 copy with default options"""

    # Map string format to enum
    format_enum = S3CopyRequestFileFormat.PARQUET
    if file_format:
      format_map = {
        "csv": S3CopyRequestFileFormat.CSV,
        "parquet": S3CopyRequestFileFormat.PARQUET,
        "json": S3CopyRequestFileFormat.JSON,
        "delta": S3CopyRequestFileFormat.DELTA,
        "iceberg": S3CopyRequestFileFormat.ICEBERG,
      }
      format_enum = format_map.get(file_format.lower(), S3CopyRequestFileFormat.PARQUET)

    request = S3CopyRequest(
      table_name=table_name,
      s3_path=s3_path,
      s3_access_key_id=access_key_id,
      s3_secret_access_key=secret_access_key,
      s3_region=region,
      file_format=format_enum,
      ignore_errors=ignore_errors,
    )

    return self.copy_from_s3(graph_id, request)

  def monitor_multiple_copies(
    self, operation_ids: List[str], options: Optional[CopyOptions] = None
  ) -> Dict[str, CopyResult]:
    """Monitor multiple copy operations concurrently"""
    results = {}
    for operation_id in operation_ids:
      result = self._monitor_copy_operation(
        operation_id, options or CopyOptions(), time.time()
      )
      results[operation_id] = result
    return results

  def batch_copy_from_s3(
    self, graph_id: str, copies: List[Dict[str, Any]]
  ) -> List[CopyResult]:
    """Batch copy multiple tables from S3"""
    results = []
    for copy_config in copies:
      request = copy_config.get("request")
      options = copy_config.get("options")
      if request:
        result = self.copy_from_s3(graph_id, request, options)
        results.append(result)
    return results

  def copy_with_retry(
    self,
    graph_id: str,
    request: Union[S3CopyRequest, URLCopyRequest, DataFrameCopyRequest],
    source_type: CopySourceType,
    max_retries: int = 3,
    options: Optional[CopyOptions] = None,
  ) -> CopyResult:
    """Copy with retry logic for transient failures"""
    if options is None:
      options = CopyOptions()

    last_error: Optional[Exception] = None
    attempt = 0

    while attempt < max_retries:
      attempt += 1

      try:
        result = self._execute_copy(graph_id, request, source_type, options)

        # If successful or partially successful, return
        if result.status in ["completed", "partial"]:
          return result

        # If failed, check if it's retryable
        if result.status == "failed":
          is_retryable = self._is_retryable_error(result.error)
          if not is_retryable or attempt == max_retries:
            return result

          # Wait before retry with exponential backoff
          wait_time = min(1000 * (2 ** (attempt - 1)), 30000) / 1000
          if options.on_progress:
            options.on_progress(
              f"Retrying copy operation (attempt {attempt}/{max_retries}) in {wait_time}s...",
              None,
            )
          time.sleep(wait_time)

      except Exception as e:
        last_error = e

        if attempt == max_retries:
          raise last_error

        # Wait before retry
        wait_time = min(1000 * (2 ** (attempt - 1)), 30000) / 1000
        if options.on_progress:
          options.on_progress(
            f"Retrying after error (attempt {attempt}/{max_retries}) in {wait_time}s...",
            None,
          )
        time.sleep(wait_time)

    raise last_error or Exception("Copy operation failed after all retries")

  def _is_retryable_error(self, error: Optional[str]) -> bool:
    """Check if an error is retryable"""
    if not error:
      return False

    retryable_patterns = [
      "timeout",
      "network",
      "connection",
      "temporary",
      "unavailable",
      "rate limit",
      "throttl",
    ]

    lower_error = error.lower()
    return any(pattern in lower_error for pattern in retryable_patterns)

  def close(self):
    """Cancel any active SSE connections"""
    if self.sse_client:
      self.sse_client.close()
      self.sse_client = None


class AsyncCopyClient:
  """Async version of CopyClient for async/await usage"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.sse_client: Optional[AsyncSSEClient] = None
    # Get token from config if passed by parent
    self.token = config.get("token")

  async def copy_from_s3(
    self, graph_id: str, request: S3CopyRequest, options: Optional[CopyOptions] = None
  ) -> CopyResult:
    """Copy data from S3 to graph database asynchronously"""
    # Async implementation would go here
    # For now, this is a placeholder
    raise NotImplementedError("Async copy client not yet implemented")

  async def close(self):
    """Close any active connections"""
    if self.sse_client:
      await self.sse_client.close()
      self.sse_client = None
