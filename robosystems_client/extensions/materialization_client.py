"""Materialization Client for RoboSystems API

Manages graph materialization from DuckDB staging tables.
Treats the graph database as a materialized view of the mutable DuckDB data lake.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable
import logging

from ..api.materialization.materialize_graph import (
  sync_detailed as materialize_graph,
)
from ..api.materialization.get_materialization_status import (
  sync_detailed as get_materialization_status,
)
from ..models.materialize_request import MaterializeRequest

logger = logging.getLogger(__name__)


@dataclass
class MaterializationOptions:
  """Options for graph materialization operations"""

  ignore_errors: bool = True
  rebuild: bool = False
  force: bool = False
  on_progress: Optional[Callable[[str], None]] = None


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

  def materialize(
    self,
    graph_id: str,
    options: Optional[MaterializationOptions] = None,
  ) -> MaterializationResult:
    """
    Materialize graph from DuckDB staging tables.

    Rebuilds the complete graph database from the current state of DuckDB
    staging tables. Automatically discovers all tables, materializes them in
    the correct order (nodes before relationships), and clears the staleness flag.

    Args:
        graph_id: Graph database identifier
        options: Materialization options (ignore_errors, rebuild, force)

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
        options.on_progress("Starting graph materialization...")

      request = MaterializeRequest(
        ignore_errors=options.ignore_errors,
        rebuild=options.rebuild,
        force=options.force,
      )

      kwargs = {
        "graph_id": graph_id,
        "client": self.config.get("client"),
        "body": request,
      }

      response = materialize_graph(**kwargs)

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

      result_data = response.parsed

      if options.on_progress:
        options.on_progress(
          f"✅ Materialization complete: {len(result_data.tables_materialized)} tables, "
          f"{result_data.total_rows:,} rows in {result_data.execution_time_ms:.2f}ms"
        )

      return MaterializationResult(
        status=result_data.status,
        was_stale=result_data.was_stale,
        stale_reason=result_data.stale_reason,
        tables_materialized=result_data.tables_materialized,
        total_rows=result_data.total_rows,
        execution_time_ms=result_data.execution_time_ms,
        message=result_data.message,
        success=True,
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
      kwargs = {
        "graph_id": graph_id,
        "client": self.config.get("client"),
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
