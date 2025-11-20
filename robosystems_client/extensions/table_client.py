"""Table Client for RoboSystems API

Manages DuckDB staging table operations.
Tables provide SQL-queryable staging layer before graph materialization.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional
import logging

from ..api.tables.list_tables import (
  sync_detailed as list_tables,
)
from ..api.tables.query_tables import (
  sync_detailed as query_tables,
)
from ..models.table_query_request import TableQueryRequest

logger = logging.getLogger(__name__)


@dataclass
class TableInfo:
  """Information about a DuckDB staging table"""

  table_name: str
  table_type: str
  row_count: int
  file_count: int
  total_size_bytes: int


@dataclass
class QueryResult:
  """Result from SQL query execution"""

  columns: list[str]
  rows: list[list[Any]]
  row_count: int
  execution_time_ms: float
  success: bool = True
  error: Optional[str] = None


class TableClient:
  """Client for managing DuckDB staging tables"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")

  def list(self, graph_id: str) -> list[TableInfo]:
    """
    List all DuckDB staging tables in a graph.

    Args:
        graph_id: Graph database identifier

    Returns:
        List of TableInfo objects with metadata
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

      response = list_tables(**kwargs)

      if response.status_code != 200 or not response.parsed:
        logger.error(f"Failed to list tables: {response.status_code}")
        return []

      table_data = response.parsed
      tables = getattr(table_data, "tables", [])

      return [
        TableInfo(
          table_name=t.table_name,
          table_type=t.table_type,
          row_count=t.row_count,
          file_count=t.file_count or 0,
          total_size_bytes=t.total_size_bytes or 0,
        )
        for t in tables
      ]

    except Exception as e:
      logger.error(f"Failed to list tables: {e}")
      return []

  def query(
    self, graph_id: str, sql_query: str, limit: Optional[int] = None
  ) -> QueryResult:
    """
    Execute SQL query against DuckDB staging tables.

    Args:
        graph_id: Graph database identifier
        sql_query: SQL query to execute
        limit: Optional row limit

    Returns:
        QueryResult with columns and rows

    Example:
        >>> result = client.tables.query(
        ...     graph_id,
        ...     "SELECT * FROM Entity WHERE entity_type = 'CORPORATION'"
        ... )
        >>> for row in result.rows:
        ...     print(row)
    """
    try:
      final_query = sql_query
      if limit is not None:
        final_query = f"{sql_query.rstrip(';')} LIMIT {limit}"

      request = TableQueryRequest(sql=final_query)

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

      response = query_tables(**kwargs)

      if response.status_code != 200 or not response.parsed:
        error_msg = f"Query failed: {response.status_code}"
        return QueryResult(
          columns=[],
          rows=[],
          row_count=0,
          execution_time_ms=0,
          success=False,
          error=error_msg,
        )

      result_data = response.parsed

      return QueryResult(
        columns=result_data.columns,
        rows=result_data.rows,
        row_count=len(result_data.rows),
        execution_time_ms=getattr(result_data, "execution_time_ms", 0),
        success=True,
      )

    except Exception as e:
      logger.error(f"Query failed: {e}")
      return QueryResult(
        columns=[],
        rows=[],
        row_count=0,
        execution_time_ms=0,
        success=False,
        error=str(e),
      )
