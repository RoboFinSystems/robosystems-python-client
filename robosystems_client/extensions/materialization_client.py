"""Materialization Client for RoboSystems API

Manages graph materialization from DuckDB staging tables.
Treats the graph database as a materialized view of the mutable DuckDB data lake.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable
import logging

from ..api.materialize.materialize_graph import (
  sync_detailed as materialize_graph,
)
from ..api.materialize.get_materialization_status import (
  sync_detailed as get_materialization_status,
)
from ..models.materialize_request import MaterializeRequest
from .operation_client import OperationClient, OperationProgress, MonitorOptions

logger = logging.getLogger(__name__)


@dataclass
class MaterializationOptions:
  """Options for graph materialization operations"""

  ignore_errors: bool = True
  rebuild: bool = False
  force: bool = False
  on_progress: Optional[Callable[[str], None]] = None
  timeout: Optional[int] = 600  # 10 minute default timeout


@dataclass
class MaterializationResult:
  """Result from materialization operation"""

  status: str
  was_stale: bool
  stale_reason: Optional[str]
  tables_materialized: list[str]
  total_rows: int
  execution_time_ms: float
  message: str
  success: bool = True
  error: Optional[str] = None


@dataclass
class MaterializationStatus:
  """Status information about graph materialization"""

  graph_id: str
  is_stale: bool
  stale_reason: Optional[str]
  stale_since: Optional[str]
  last_materialized_at: Optional[str]
  materialization_count: int
  hours_since_materialization: Optional[float]
  message: str


class MaterializationClient:
  """Client for managing graph materialization operations"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")
    self._operation_client = None

  @property
  def operation_client(self) -> OperationClient:
    """Get or create the operation client for SSE monitoring."""
    if self._operation_client is None:
      self._operation_client = OperationClient(self.config)
    return self._operation_client

  def materialize(
    self,
    graph_id: str,
    options: Optional[MaterializationOptions] = None,
  ) -> MaterializationResult:
    """
    Materialize graph from DuckDB staging tables.

    Submits a materialization job to Dagster and monitors progress via SSE.
    The operation runs asynchronously on the server but this method waits
    for completion and returns the final result.

    Args:
        graph_id: Graph database identifier
        options: Materialization options (ignore_errors, rebuild, force, timeout)

    Returns:
        MaterializationResult with detailed execution information

    When to use:
        - After batch uploads (files uploaded with ingest_to_graph=false)
        - After cascade file deletions (graph marked stale)
        - Periodic full refresh to ensure consistency
        - Recovery from partial materialization failures
    """
    options = options or MaterializationOptions()

    try:
      if options.on_progress:
        options.on_progress("Submitting materialization job...")

      request = MaterializeRequest(
        ignore_errors=options.ignore_errors,
        rebuild=options.rebuild,
        force=options.force,
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
        "body": request,
      }

      response = materialize_graph(**kwargs)

      # Handle non-200 status codes
      if response.status_code != 200 or not response.parsed:
        error_msg = f"Materialization failed: {response.status_code}"
        if hasattr(response, "content"):
          try:
            import json

            error_data = json.loads(response.content)
            error_msg = error_data.get("detail", error_msg)
          except Exception:
            pass

        return MaterializationResult(
          status="failed",
          was_stale=False,
          stale_reason=None,
          tables_materialized=[],
          total_rows=0,
          execution_time_ms=0,
          message=error_msg,
          success=False,
          error=error_msg,
        )

      # Get the operation_id from the queued response
      result_data = response.parsed
      operation_id = result_data.operation_id

      if options.on_progress:
        options.on_progress(f"Materialization queued (operation: {operation_id})")

      # Monitor the operation via SSE until completion
      def on_sse_progress(progress: OperationProgress):
        if options.on_progress:
          msg = progress.message
          if progress.percentage is not None:
            msg += f" ({progress.percentage:.0f}%)"
          options.on_progress(msg)

      monitor_options = MonitorOptions(
        on_progress=on_sse_progress,
        timeout=options.timeout,
      )

      op_result = self.operation_client.monitor_operation(operation_id, monitor_options)

      # Convert operation result to materialization result
      if op_result.status.value == "completed":
        # Extract details from SSE completion event result
        sse_result = op_result.result or {}

        if options.on_progress:
          tables = sse_result.get("tables_materialized", [])
          rows = sse_result.get("total_rows", 0)
          time_ms = sse_result.get("execution_time_ms", 0)
          options.on_progress(
            f"✅ Materialization complete: {len(tables)} tables, "
            f"{rows:,} rows in {time_ms:.2f}ms"
          )

        return MaterializationResult(
          status="success",
          was_stale=sse_result.get("was_stale", False),
          stale_reason=sse_result.get("stale_reason"),
          tables_materialized=sse_result.get("tables_materialized", []),
          total_rows=sse_result.get("total_rows", 0),
          execution_time_ms=sse_result.get(
            "execution_time_ms", op_result.execution_time_ms or 0
          ),
          message=sse_result.get("message", "Graph materialized successfully"),
          success=True,
        )
      else:
        # Operation failed or was cancelled
        return MaterializationResult(
          status=op_result.status.value,
          was_stale=False,
          stale_reason=None,
          tables_materialized=[],
          total_rows=0,
          execution_time_ms=op_result.execution_time_ms or 0,
          message=op_result.error or f"Operation {op_result.status.value}",
          success=False,
          error=op_result.error,
        )

    except Exception as e:
      logger.error(f"Materialization failed: {e}")
      return MaterializationResult(
        status="failed",
        was_stale=False,
        stale_reason=None,
        tables_materialized=[],
        total_rows=0,
        execution_time_ms=0,
        message=str(e),
        success=False,
        error=str(e),
      )

  def status(self, graph_id: str) -> Optional[MaterializationStatus]:
    """
    Get current materialization status for the graph.

    Shows whether the graph is stale (DuckDB has changes not yet in graph database),
    when it was last materialized, and how long since last materialization.

    Args:
        graph_id: Graph database identifier

    Returns:
        MaterializationStatus with staleness and timing information
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

      response = get_materialization_status(**kwargs)

      if response.status_code != 200 or not response.parsed:
        logger.error(f"Failed to get materialization status: {response.status_code}")
        return None

      status_data = response.parsed

      return MaterializationStatus(
        graph_id=status_data.graph_id,
        is_stale=status_data.is_stale,
        stale_reason=status_data.stale_reason,
        stale_since=status_data.stale_since,
        last_materialized_at=status_data.last_materialized_at,
        materialization_count=status_data.materialization_count,
        hours_since_materialization=status_data.hours_since_materialization,
        message=status_data.message,
      )

    except Exception as e:
      logger.error(f"Failed to get materialization status: {e}")
      return None
