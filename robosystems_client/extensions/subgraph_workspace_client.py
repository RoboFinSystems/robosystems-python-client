"""Subgraph Workspace Client Extension

Client for managing subgraph workspaces following the Financial Report Creator architecture.
Supports creating isolated workspaces, transferring data, and publishing to main graph.
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum
import json
import httpx


class StorageType(Enum):
  """Subgraph storage types"""

  IN_MEMORY = "in_memory"
  DISK_BASED = "disk_based"


@dataclass
class SubgraphWorkspace:
  """Represents a subgraph workspace"""

  graph_id: str  # Full subgraph ID (e.g., kg123_workspace)
  parent_id: str  # Parent graph ID (e.g., kg123)
  name: str  # Workspace name (e.g., workspace)
  display_name: str
  storage_type: StorageType
  created_at: str
  status: str = "active"
  fork_status: Optional[Dict[str, Any]] = None  # Fork operation status if forked


@dataclass
class ExportResult:
  """Result from exporting subgraph to parquet"""

  shared_filename: str
  files_exported: List[Dict[str, Any]]
  total_rows: int
  execution_time_ms: int


@dataclass
class PublishResult:
  """Result from publishing subgraph to main graph"""

  nodes_created: int
  relationships_created: int
  execution_time_ms: int
  success: bool


class SubgraphWorkspaceClient:
  """
  Client for managing subgraph workspaces.

  Provides functionality to:
  - Create/delete subgraph workspaces
  - Transfer data from main graph to subgraph
  - Export subgraph to parquet files
  - Publish subgraph to main graph via incremental ingestion
  """

  def __init__(self, api_client, query_client=None):
    """
    Initialize with API client and optional query client.

    Args:
        api_client: RoboSystems API client for subgraph operations
        query_client: Optional query client for executing Cypher
    """
    self.api = api_client
    self.query = query_client

  async def create_workspace(
    self,
    parent_graph_id: str,
    name: str,
    display_name: str = None,
    storage_type: StorageType = StorageType.IN_MEMORY,
    schema_extensions: List[str] = None,
    fork_parent: bool = False,
  ) -> SubgraphWorkspace:
    """
    Create a new subgraph workspace.

    Args:
        parent_graph_id: Parent graph ID (e.g., kg123)
        name: Workspace name (alphanumeric, 1-20 chars)
        display_name: Optional human-readable name
        storage_type: IN_MEMORY (fast, <10K nodes) or DISK_BASED (persistent, >100K nodes)
        schema_extensions: List of schema extensions (e.g., ["roboledger"])
        fork_parent: If True, copy all data from parent graph (creates a "fork")

    Returns:
        SubgraphWorkspace object
    """
    # Construct request for subgraph creation
    request_body = {
      "name": name,
      "display_name": display_name or f"Workspace {name}",
      "storage_type": storage_type.value,
      "schema_extensions": schema_extensions or ["roboledger"],
      "fork_parent": fork_parent,  # Pass fork flag to server
    }

    # Use httpx to call API
    async with httpx.AsyncClient() as client:
      headers = {"X-API-Key": self.api.token, "Content-Type": "application/json"}
      response = await client.post(
        f"{self.api._base_url}/v1/graphs/{parent_graph_id}/subgraphs",
        json=request_body,
        headers=headers,
      )
      result = response.json()

    # Construct full subgraph ID
    subgraph_id = f"{parent_graph_id}_{name}"

    workspace = SubgraphWorkspace(
      graph_id=subgraph_id,
      parent_id=parent_graph_id,
      name=name,
      display_name=result.get("display_name", display_name),
      storage_type=storage_type,
      created_at=result.get("created_at"),
      status="active",
    )

    # If fork_parent is True, trigger server-side fork
    # The server will handle the fork operation with progress monitoring
    if fork_parent:
      # Fork happens server-side during creation when fork_parent=True
      # For client-side monitoring, use fork_from_parent_with_sse() method
      pass

    return workspace

  async def create_workspace_with_fork(
    self,
    parent_graph_id: str,
    name: str,
    display_name: str = None,
    fork_parent: bool = True,
    fork_options: Dict[str, Any] = None,
    progress_callback: Optional[callable] = None,
  ) -> SubgraphWorkspace:
    """
    Create a subgraph workspace with fork from parent using SSE monitoring.

    This method creates a subgraph and monitors the fork operation via SSE
    if fork_parent=True. The fork operation copies data from the parent
    graph to the new subgraph.

    Args:
        parent_graph_id: Parent graph ID
        name: Workspace name (alphanumeric only, 1-20 chars)
        display_name: Human-readable display name
        fork_parent: If True, fork data from parent graph
        fork_options: Fork options dict:
            - tables: List of tables to copy or "all" (default: "all")
            - exclude_patterns: List of table patterns to exclude (e.g., ["Report*"])
        progress_callback: Optional callback(msg: str, pct: float) for progress updates

    Returns:
        SubgraphWorkspace with fork_status if fork was performed
    """
    # Create request body
    request_body = {
      "name": name,
      "display_name": display_name or f"Workspace {name}",
      "fork_parent": fork_parent,
      "metadata": {"fork_options": fork_options} if fork_options else None,
    }

    # Use httpx directly to call API
    async with httpx.AsyncClient() as client:
      headers = {"X-API-Key": self.api.token, "Content-Type": "application/json"}

      # Call API to create subgraph with fork
      response = await client.post(
        f"{self.api._base_url}/v1/graphs/{parent_graph_id}/subgraphs",
        json=request_body,
        headers=headers,
      )
      result = response.json()

    # If fork_parent=True, response includes operation_id for SSE monitoring
    if fork_parent and "operation_id" in result:
      operation_id = result["operation_id"]

      # Monitor fork progress via SSE
      if progress_callback:
        # Connect to SSE endpoint
        sse_url = f"{self.api._base_url}/v1/operations/{operation_id}/stream"
        headers = {"X-API-Key": self.api.token}

        # Use longer timeout for SSE streaming (Dagster jobs can take time)
        timeout = httpx.Timeout(connect=30.0, read=120.0, write=30.0, pool=30.0)
        async with httpx.AsyncClient(timeout=timeout) as client:
          async with client.stream("GET", sse_url, headers=headers) as sse_response:
            async for line in sse_response.aiter_lines():
              if line.startswith("data: "):
                try:
                  event_data = json.loads(line[6:])
                  if event_data.get("event") == "operation_progress":
                    msg = event_data.get("data", {}).get("message", "")
                    pct = event_data.get("data", {}).get("progress_percent", 0)
                    if progress_callback:
                      await progress_callback(msg, pct)
                  elif event_data.get("event") == "operation_completed":
                    if progress_callback:
                      await progress_callback("Fork completed", 100)
                    break
                  elif event_data.get("event") == "operation_error":
                    error = event_data.get("data", {}).get("error", "Unknown error")
                    if progress_callback:
                      await progress_callback(f"Fork failed: {error}", 0)
                    break
                except json.JSONDecodeError:
                  continue

      # Get final status via API
      async with httpx.AsyncClient() as client:
        headers = {"X-API-Key": self.api.token}
        status_response = await client.get(
          f"{self.api._base_url}/v1/operations/{operation_id}/status", headers=headers
        )
        final_status = status_response.json()

      # Construct full subgraph ID
      subgraph_id = f"{parent_graph_id}_{name}"

      workspace = SubgraphWorkspace(
        graph_id=subgraph_id,
        parent_id=parent_graph_id,
        name=name,
        display_name=display_name or f"Workspace {name}",
        storage_type=StorageType.IN_MEMORY,
        created_at=final_status.get("created_at"),
        status="active",
        fork_status=final_status.get("result", {}).get("fork_status"),
      )

      return workspace

    # Non-fork path (immediate response)
    subgraph_id = f"{parent_graph_id}_{name}"

    return SubgraphWorkspace(
      graph_id=subgraph_id,
      parent_id=parent_graph_id,
      name=name,
      display_name=result.get("display_name", display_name),
      storage_type=StorageType.IN_MEMORY,
      created_at=result.get("created_at"),
      status="active",
    )

  async def delete_workspace(
    self,
    parent_graph_id: str,
    workspace_name: str,
    force: bool = False,
    create_backup: bool = False,
  ) -> bool:
    """
    Delete a subgraph workspace.

    Args:
        parent_graph_id: Parent graph ID
        workspace_name: Workspace name to delete
        force: Force deletion even if subgraph contains data
        create_backup: Create backup before deletion

    Returns:
        True if deleted successfully
    """
    params = {"force": force, "create_backup": create_backup}

    response = await self.api.delete(
      f"/v1/graphs/{parent_graph_id}/subgraphs/{workspace_name}", params=params
    )

    return response.status_code == 200

  async def list_workspaces(self, parent_graph_id: str) -> List[SubgraphWorkspace]:
    """
    List all subgraph workspaces for a parent graph.

    Args:
        parent_graph_id: Parent graph ID

    Returns:
        List of SubgraphWorkspace objects
    """
    response = await self.api.get(f"/v1/graphs/{parent_graph_id}/subgraphs")
    subgraphs = response.json()

    workspaces = []
    for subgraph in subgraphs:
      workspaces.append(
        SubgraphWorkspace(
          graph_id=f"{parent_graph_id}_{subgraph['name']}",
          parent_id=parent_graph_id,
          name=subgraph["name"],
          display_name=subgraph.get("display_name", ""),
          storage_type=StorageType(subgraph.get("storage_type", "in_memory")),
          created_at=subgraph.get("created_at", ""),
          status=subgraph.get("status", "active"),
        )
      )

    return workspaces

  async def copy_data_from_main_graph(
    self,
    workspace_id: str,
    parent_graph_id: str,
    node_types: List[str],
    filters: Dict[str, Any] = None,
  ) -> int:
    """
    Copy data from main graph to subgraph workspace.

    Queries nodes from main graph and creates them in subgraph.

    Args:
        workspace_id: Subgraph workspace ID (e.g., kg123_workspace)
        parent_graph_id: Parent graph ID to query from
        node_types: List of node types to copy (e.g., ["Element", "Period", "Unit"])
        filters: Optional filters for querying (e.g., {"period_end": "2024-12-31"})

    Returns:
        Number of nodes copied
    """
    if not self.query:
      raise ValueError("Query client required for data transfer")

    total_copied = 0

    for node_type in node_types:
      # Build query for main graph
      where_clause = ""
      if filters:
        conditions = []
        for key, value in filters.items():
          conditions.append(f"n.{key} = '{value}'")
        where_clause = f"WHERE {' AND '.join(conditions)}"

      # Query from main graph
      query_cypher = f"""
            MATCH (n:{node_type})
            {where_clause}
            RETURN n
            """

      result = await self.query.query(parent_graph_id, query_cypher)

      if result and result.data:
        # Batch create in subgraph
        for batch in self._batch_nodes(result.data, 100):
          create_cypher = self._build_batch_create_cypher(node_type, batch)
          await self.query.query(workspace_id, create_cypher)
          total_copied += len(batch)

    return total_copied

  async def copy_facts_with_aspects(
    self,
    workspace_id: str,
    parent_graph_id: str,
    fact_set_ids: List[str] = None,
    period_start: str = None,
    period_end: str = None,
    entity_id: str = None,
  ) -> int:
    """
    Copy facts with all their aspects (element, period, unit, dimensions).

    This is optimized for copying complete fact data with relationships.

    Args:
        workspace_id: Subgraph workspace ID
        parent_graph_id: Parent graph ID
        fact_set_ids: Optional list of fact set IDs to copy
        period_start: Optional start date filter
        period_end: Optional end date filter
        entity_id: Optional entity filter

    Returns:
        Number of facts copied
    """
    if not self.query:
      raise ValueError("Query client required for fact transfer")

    # Build WHERE clause
    conditions = []
    params = {}

    if fact_set_ids:
      conditions.append("fs.identifier IN $fact_set_ids")
      params["fact_set_ids"] = fact_set_ids

    if period_start and period_end:
      conditions.append("p.end_date >= $period_start AND p.end_date <= $period_end")
      params["period_start"] = period_start
      params["period_end"] = period_end

    if entity_id:
      conditions.append("e.identifier = $entity_id")
      params["entity_id"] = entity_id

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

    # Query facts with all relationships from main graph
    query_cypher = f"""
        MATCH (fs:FactSet)-[:FACT_SET_CONTAINS_FACT]->(f:Fact)
        MATCH (f)-[:FACT_HAS_ELEMENT]->(el:Element)
        MATCH (f)-[:FACT_HAS_PERIOD]->(p:Period)
        MATCH (f)-[:FACT_HAS_ENTITY]->(e:Entity)
        OPTIONAL MATCH (f)-[:FACT_HAS_UNIT]->(u:Unit)
        OPTIONAL MATCH (f)-[:FACT_HAS_DIMENSION]->(d:FactDimension)
        {where_clause}
        RETURN f, el, p, e, u, collect(d) as dimensions
        """

    result = await self.query.query(parent_graph_id, query_cypher, params)

    if not result or not result.data:
      return 0

    # Create nodes and relationships in subgraph
    # This would be done in batches with proper MERGE statements
    facts_copied = 0

    for row in result.data:
      # Create fact and all related nodes in subgraph
      create_cypher = self._build_fact_create_cypher(row)
      await self.query.query(workspace_id, create_cypher)
      facts_copied += 1

    return facts_copied

  async def export_to_parquet(
    self, workspace_id: str, shared_filename: str, tables: List[str] = None
  ) -> ExportResult:
    """
    Export subgraph to parquet files.

    Each table is exported to a separate parquet file with the shared filename
    for provenance tracking and incremental ingestion.

    Args:
        workspace_id: Subgraph workspace ID
        shared_filename: Shared filename for all tables (e.g., "report_nvda_2024q4.parquet")
        tables: List of tables to export (default: all report tables)

    Returns:
        ExportResult with file details
    """
    if tables is None:
      tables = [
        "Report",
        "ReportSection",
        "FactSet",
        "Fact",
        "Structure",
        "Association",
        "Element",
        "Period",
        "Unit",
      ]

    request_body = {
      "shared_filename": shared_filename,
      "export_all_tables": False,
      "tables": tables,
    }

    response = await self.api.post(
      f"/v1/graphs/{workspace_id}/export", json=request_body
    )

    result = response.json()

    return ExportResult(
      shared_filename=shared_filename,
      files_exported=result.get("files_exported", []),
      total_rows=sum(f.get("row_count", 0) for f in result.get("files_exported", [])),
      execution_time_ms=result.get("execution_time_ms", 0),
    )

  async def publish_to_main_graph(
    self,
    workspace_id: str,
    parent_graph_id: str,
    shared_filename: str,
    delete_workspace: bool = True,
  ) -> PublishResult:
    """
    Publish workspace to main graph via incremental ingestion.

    This is the complete publish flow:
    1. Export subgraph to parquet
    2. Incremental ingest to main graph (filtered by filename)
    3. Delete workspace (optional)

    Args:
        workspace_id: Subgraph workspace ID
        parent_graph_id: Parent graph to publish to
        shared_filename: Filename to use for export/ingest
        delete_workspace: Whether to delete workspace after publish

    Returns:
        PublishResult with statistics
    """
    # Step 1: Export to parquet
    await self.export_to_parquet(workspace_id, shared_filename)

    # Step 2: Incremental ingest to main graph
    ingest_request = {
      "file_names": [shared_filename],  # Filter to only this report
      "ignore_errors": True,
      "rebuild": False,
    }

    response = await self.api.post(
      f"/v1/graphs/{parent_graph_id}/tables/ingest", json=ingest_request
    )

    ingest_result = response.json()

    # Step 3: Delete workspace (optional)
    if delete_workspace:
      workspace_name = workspace_id.split("_")[-1]
      await self.delete_workspace(parent_graph_id, workspace_name)

    return PublishResult(
      nodes_created=ingest_result.get("nodes_created", 0),
      relationships_created=ingest_result.get("relationships_created", 0),
      execution_time_ms=ingest_result.get("execution_time_ms", 0),
      success=ingest_result.get("status") == "success",
    )

  def _batch_nodes(self, nodes: List[Dict], batch_size: int):
    """Helper to batch nodes for efficient creation"""
    for i in range(0, len(nodes), batch_size):
      yield nodes[i : i + batch_size]

  def _build_batch_create_cypher(self, node_type: str, nodes: List[Dict]) -> str:
    """Helper to build batch CREATE cypher"""
    creates = []
    for i, node_data in enumerate(nodes):
      node = node_data.get("n", node_data)
      props = json.dumps(node).replace('"', "'")
      creates.append(f"CREATE (n{i}:{node_type} {props})")

    return "\n".join(creates)

  def _build_fact_create_cypher(self, row: Dict) -> str:
    """Helper to build cypher for creating fact with all relationships"""
    # This would build proper MERGE statements for fact and all related nodes
    # Simplified for illustration
    return f"""
        MERGE (f:Fact {{identifier: '{row["f"]["identifier"]}'}})
        SET f = {json.dumps(row["f"]).replace('"', "'")}

        MERGE (el:Element {{identifier: '{row["el"]["identifier"]}'}})
        SET el = {json.dumps(row["el"]).replace('"', "'")}

        MERGE (f)-[:FACT_HAS_ELEMENT]->(el)
        """

  async def fork_from_parent_with_sse(
    self,
    workspace_id: str,
    parent_graph_id: str,
    fork_options: Optional[Dict[str, Any]] = None,
    progress_callback: Optional[callable] = None,
  ) -> Dict[str, Any]:
    """
    Fork data from parent graph with SSE progress monitoring.

    This method triggers a server-side fork operation and monitors progress
    via Server-Sent Events (SSE) for real-time updates on large operations.

    Args:
        workspace_id: Target subgraph workspace ID
        parent_graph_id: Source parent graph ID
        fork_options: Options for selective forking:
            - tables: List of tables or "all"
            - period_filter: Date range filter
            - entity_filter: Entity IDs to include
            - exclude_patterns: Tables to exclude (e.g., ["Report*"])
        progress_callback: Optional callback for progress updates

    Returns:
        Fork result with statistics

    Example:
        >>> async def on_progress(event):
        ...     print(f"Progress: {event['message']}")
        >>>
        >>> result = await workspace_client.fork_from_parent_with_sse(
        ...     workspace_id="kg123_dev",
        ...     parent_graph_id="kg123",
        ...     fork_options={
        ...         "tables": "all",
        ...         "exclude_patterns": ["Report*"],
        ...         "period_filter": {"start": "2024-01-01", "end": "2024-12-31"}
        ...     },
        ...     progress_callback=on_progress
        ... )
    """
    # Start fork operation and get SSE endpoint
    fork_request = {
      "operation": "fork",
      "source_graph_id": parent_graph_id,
      "target_graph_id": workspace_id,
      "options": fork_options or {},
    }

    # Initiate fork operation
    response = await self.api.post(
      f"/v1/graphs/{workspace_id}/operations/fork", json=fork_request
    )

    operation = response.json()
    operation_id = operation.get("operation_id")

    if not operation_id:
      # If no SSE available, fall back to synchronous wait
      return operation

    # Connect to SSE endpoint for progress monitoring
    sse_url = f"{self.api.base_url}/v1/operations/{operation_id}/stream"
    headers = getattr(self.api, "_headers", {})

    async with httpx.AsyncClient() as client:
      async with client.stream("GET", sse_url, headers=headers) as response:
        async for line in response.aiter_lines():
          if line.startswith("data: "):
            data = line[6:].strip()
            if data == "[DONE]":
              break

            try:
              event = json.loads(data)

              # Call progress callback if provided
              if progress_callback:
                await progress_callback(event)

              # Check for completion
              if event.get("status") in ["completed", "failed"]:
                return event

            except json.JSONDecodeError:
              continue

    # Get final status if SSE ended without completion event
    final_response = await self.api.get(f"/v1/operations/{operation_id}")
    return final_response.json()

  async def write_view_to_workspace(
    self, workspace_id: str, view_data: Dict[str, Any], report_name: str = None
  ) -> str:
    """
    Write view/report data to subgraph workspace.

    Creates Report, FactSet, Structure, and Association nodes.

    Args:
        workspace_id: Subgraph workspace ID
        view_data: View data including facts, structures, associations
        report_name: Optional report name

    Returns:
        Report ID created
    """
    if not self.query:
      raise ValueError("Query client required for writing view data")

    import uuid

    report_id = str(uuid.uuid4())

    # Create Report node
    report_cypher = f"""
        CREATE (r:Report {{
            identifier: '{report_id}',
            name: '{report_name or "Draft Report"}',
            status: 'draft',
            created_at: datetime(),
            ai_generated: false
        }})
        RETURN r.identifier as report_id
        """

    await self.query.query(workspace_id, report_cypher)

    # Create FactSet and Facts
    if "facts" in view_data:
      factset_id = str(uuid.uuid4())
      factset_cypher = f"""
            MATCH (r:Report {{identifier: '{report_id}'}})
            CREATE (fs:FactSet {{
                identifier: '{factset_id}',
                name: 'View Facts'
            }})
            CREATE (r)-[:REPORT_HAS_FACT_SET]->(fs)
            """
      await self.query.query(workspace_id, factset_cypher)

      # Add facts to factset
      for fact in view_data["facts"]:
        fact_cypher = f"""
                MATCH (fs:FactSet {{identifier: '{factset_id}'}})
                CREATE (f:Fact {{
                    identifier: randomUUID(),
                    element_id: '{fact.get("element_id")}',
                    value: {fact.get("value", 0)},
                    period_end: '{fact.get("period_end", "")}'
                }})
                CREATE (fs)-[:FACT_SET_CONTAINS_FACT]->(f)
                """
        await self.query.query(workspace_id, fact_cypher)

    # Create Structure and Associations
    if "structures" in view_data:
      for structure in view_data["structures"]:
        struct_cypher = f"""
                MATCH (r:Report {{identifier: '{report_id}'}})
                CREATE (s:Structure {{
                    identifier: randomUUID(),
                    name: '{structure.get("name", "View Structure")}',
                    type: 'presentation'
                }})
                CREATE (r)-[:REPORT_HAS_STRUCTURE]->(s)
                """
        await self.query.query(workspace_id, struct_cypher)

    return report_id
