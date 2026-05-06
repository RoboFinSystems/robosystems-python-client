"""Graph Management Client

Provides high-level graph management and lifecycle operations with
automatic operation monitoring. Supports both SSE (Server-Sent Events)
for real-time updates and polling fallback.

Graph lifecycle operations (create-subgraph, delete-subgraph, create-backup,
restore-backup, change-tier, materialize) all go through the operations
surface at ``POST /v1/graphs/{graph_id}/operations/{op_name}`` and return
an ``OperationEnvelope``.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable
import time
import json
import logging

import httpx

from .operation_client import OperationClient, OperationProgress, MonitorOptions

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class GraphMetadata:
  """Graph metadata for creation"""

  graph_name: str
  description: Optional[str] = None
  schema_extensions: Optional[list] = None
  tags: Optional[list] = None


@dataclass
class InitialEntityData:
  """Initial entity data for graph creation"""

  name: str
  uri: str
  category: Optional[str] = None
  sic: Optional[str] = None
  sic_description: Optional[str] = None


@dataclass
class GraphInfo:
  """Information about a graph"""

  graph_id: str
  graph_name: str
  description: Optional[str] = None
  schema_extensions: Optional[list] = None
  tags: Optional[list] = None
  created_at: Optional[str] = None
  status: Optional[str] = None


@dataclass
class MaterializationOptions:
  """Options for graph materialization operations"""

  ignore_errors: bool = True
  rebuild: bool = False
  force: bool = False
  materialize_embeddings: bool = False
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


class GraphClient:
  """Client for graph management and lifecycle operations.

  Covers graph creation, info retrieval, and all graph lifecycle
  operations (materialize, subgraphs, backups, tier changes).
  """

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

  def _get_authenticated_client(self):
    """Build an AuthenticatedClient for API calls."""
    from ..client import AuthenticatedClient

    if not self.token:
      raise ValueError("No API key provided. Set X-API-Key in headers.")

    return AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

  # ---------------------------------------------------------------------------
  # Graph creation
  # ---------------------------------------------------------------------------

  def create_graph_and_wait(
    self,
    metadata: GraphMetadata,
    initial_entity: InitialEntityData,
    create_entity: bool = True,
    timeout: int = 60,
    poll_interval: int = 2,
    on_progress: Optional[Callable[[str], None]] = None,
    use_sse: bool = True,
  ) -> str:
    """
    Create a graph and wait for completion.

    Uses SSE (Server-Sent Events) for real-time progress updates with
    automatic fallback to polling if SSE connection fails.

    Args:
        metadata: Graph metadata
        initial_entity: Initial entity data (required — entity graphs must have an entity)
        create_entity: Whether to populate entity data on creation (default True).
            Set False to defer population for file-based ingestion workflows.
        timeout: Maximum time to wait in seconds
        poll_interval: Time between status checks in seconds (for polling fallback)
        on_progress: Callback for progress updates
        use_sse: Whether to try SSE first (default True).

    Returns:
        graph_id when creation completes
    """
    from ..api.graphs.create_graph import sync_detailed as create_graph
    from ..models.create_graph_request import CreateGraphRequest
    from ..models.graph_metadata import GraphMetadata as APIGraphMetadata

    client = self._get_authenticated_client()

    api_metadata = APIGraphMetadata(
      graph_name=metadata.graph_name,
      description=metadata.description,
      schema_extensions=metadata.schema_extensions or [],
      tags=metadata.tags or [],
    )

    initial_entity_dict = None
    if initial_entity:
      initial_entity_dict = {
        "name": initial_entity.name,
        "uri": initial_entity.uri,
      }
      if initial_entity.category:
        initial_entity_dict["category"] = initial_entity.category
      if initial_entity.sic:
        initial_entity_dict["sic"] = initial_entity.sic
      if initial_entity.sic_description:
        initial_entity_dict["sic_description"] = initial_entity.sic_description

    graph_create = CreateGraphRequest(
      metadata=api_metadata,
      initial_entity=initial_entity_dict,
      create_entity=create_entity,
    )

    if on_progress:
      on_progress(f"Creating graph: {metadata.graph_name}")

    response = create_graph(client=client, body=graph_create)

    if not response.parsed:
      raise RuntimeError(f"Failed to create graph: {response.status_code}")

    if isinstance(response.parsed, dict):
      graph_id = response.parsed.get("graph_id")
      operation_id = response.parsed.get("operation_id")
    else:
      graph_id = getattr(response.parsed, "graph_id", None)
      operation_id = getattr(response.parsed, "operation_id", None)

    if graph_id:
      if on_progress:
        on_progress(f"Graph created: {graph_id}")
      return graph_id

    if not operation_id:
      raise RuntimeError("No graph_id or operation_id in response")

    if on_progress:
      on_progress(f"Graph creation queued (operation: {operation_id})")

    if use_sse:
      try:
        return self._wait_with_sse(operation_id, timeout, on_progress)
      except Exception as e:
        logger.debug(f"SSE connection failed, falling back to polling: {e}")
        if on_progress:
          on_progress("SSE unavailable, using polling...")

    return self._wait_with_polling(
      operation_id, timeout, poll_interval, on_progress, client
    )

  # ---------------------------------------------------------------------------
  # Graph info
  # ---------------------------------------------------------------------------

  def get_graph_info(self, graph_id: str) -> GraphInfo:
    """
    Get information about a graph.

    Args:
        graph_id: The graph ID

    Returns:
        GraphInfo with graph details
    """
    from ..api.graphs.get_graphs import sync_detailed as get_graphs

    client = self._get_authenticated_client()
    response = get_graphs(client=client)

    if not response.parsed:
      raise RuntimeError(f"Failed to get graphs: {response.status_code}")

    data = response.parsed
    graphs = None

    if isinstance(data, dict):
      graphs = data.get("graphs", [])
    elif hasattr(data, "additional_properties"):
      graphs = data.additional_properties.get("graphs", [])
    elif hasattr(data, "graphs"):
      graphs = data.graphs
    else:
      raise RuntimeError("Unexpected response format from get_graphs")

    graph_data = None
    for graph in graphs:
      if isinstance(graph, dict):
        if graph.get("graph_id") == graph_id or graph.get("id") == graph_id:
          graph_data = graph
          break
      elif hasattr(graph, "graph_id"):
        if graph.graph_id == graph_id or getattr(graph, "id", None) == graph_id:
          graph_data = graph
          break

    if not graph_data:
      raise ValueError(f"Graph not found: {graph_id}")

    if isinstance(graph_data, dict):
      return GraphInfo(
        graph_id=graph_data.get("graph_id") or graph_data.get("id", graph_id),
        graph_name=graph_data.get("graph_name") or graph_data.get("name", ""),
        description=graph_data.get("description"),
        schema_extensions=graph_data.get("schema_extensions"),
        tags=graph_data.get("tags"),
        created_at=graph_data.get("created_at"),
        status=graph_data.get("status"),
      )
    else:
      return GraphInfo(
        graph_id=getattr(graph_data, "graph_id", None)
        or getattr(graph_data, "id", graph_id),
        graph_name=getattr(graph_data, "graph_name", None)
        or getattr(graph_data, "name", ""),
        description=getattr(graph_data, "description", None),
        schema_extensions=getattr(graph_data, "schema_extensions", None),
        tags=getattr(graph_data, "tags", None),
        created_at=getattr(graph_data, "created_at", None),
        status=getattr(graph_data, "status", None),
      )

  # ---------------------------------------------------------------------------
  # Materialize
  # ---------------------------------------------------------------------------

  def materialize(
    self,
    graph_id: str,
    options: Optional[MaterializationOptions] = None,
  ) -> MaterializationResult:
    """
    Materialize graph from staging tables or extensions OLTP.

    Submits a materialization job and monitors progress via SSE.
    The operation runs asynchronously on the server but this method waits
    for completion and returns the final result.

    Args:
        graph_id: Graph database identifier
        options: Materialization options (ignore_errors, rebuild, force, timeout)

    Returns:
        MaterializationResult with detailed execution information
    """
    from ..api.graph_operations.op_materialize import (
      sync_detailed as materialize_graph,
    )

    options = options or MaterializationOptions()

    try:
      if options.on_progress:
        options.on_progress("Submitting materialization job...")

      client = self._get_authenticated_client()

      from ..models.materialize_op import MaterializeOp

      response = materialize_graph(
        graph_id=graph_id,
        client=client,
        body=MaterializeOp(
          ignore_errors=options.ignore_errors,
          rebuild=options.rebuild,
          force=options.force,
          materialize_embeddings=options.materialize_embeddings,
        ),
      )

      # Handle non-success status codes
      if response.status_code not in (200, 202) or not response.parsed:
        error_msg = f"Materialization failed: {response.status_code}"
        if hasattr(response, "content"):
          try:
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

      # Get the operation_id from the envelope
      result_data = response.parsed
      operation_id = getattr(result_data, "operation_id", None)

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

      if op_result.status.value == "completed":
        sse_result = op_result.result or {}

        if options.on_progress:
          tables = sse_result.get("tables_materialized", [])
          rows = sse_result.get("total_rows", 0)
          time_ms = sse_result.get("execution_time_ms", 0)
          options.on_progress(
            f"Materialization complete: {len(tables)} tables, "
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

  # ---------------------------------------------------------------------------
  # Tier change
  # ---------------------------------------------------------------------------

  def change_tier(
    self,
    graph_id: str,
    new_tier: str,
    timeout: int = 600,
    on_progress: Optional[Callable[[str], None]] = None,
  ) -> None:
    """
    Change the infrastructure tier of a graph (upgrade or downgrade).

    Submits an async tier change operation and monitors progress via SSE
    until the migration completes.

    Args:
        graph_id: Graph database identifier
        new_tier: Target tier — "ladybug-standard", "ladybug-large", or "ladybug-xlarge"
        timeout: Maximum time to wait in seconds (default 600 — EBS migrations can be slow)
        on_progress: Callback for progress updates

    Raises:
        RuntimeError: If the tier change fails or the operation errors out
        TimeoutError: If the operation does not complete within timeout
    """
    from ..api.graph_operations.op_change_tier import sync_detailed as change_tier_op
    from ..models.change_tier_op import ChangeTierOp

    client = self._get_authenticated_client()

    if on_progress:
      on_progress(f"Submitting tier change to {new_tier}...")

    response = change_tier_op(
      graph_id=graph_id,
      client=client,
      body=ChangeTierOp(new_tier=new_tier),  # type: ignore[arg-type]
    )

    if response.status_code not in (200, 202) or not response.parsed:
      error_msg = f"Tier change failed: HTTP {response.status_code}"
      if hasattr(response, "content"):
        try:
          error_data = json.loads(response.content)
          error_msg = error_data.get("detail", error_msg)
        except Exception:
          pass
      raise RuntimeError(error_msg)

    operation_id = getattr(response.parsed, "operation_id", None)
    if not operation_id:
      raise RuntimeError("No operation_id in tier change response")

    if on_progress:
      on_progress(f"Tier change queued (operation: {operation_id})")

    def on_sse_progress(progress: OperationProgress) -> None:
      if on_progress:
        msg = progress.message
        if progress.percentage is not None:
          msg += f" ({progress.percentage:.0f}%)"
        on_progress(msg)

    op_result = self.operation_client.monitor_operation(
      operation_id,
      MonitorOptions(on_progress=on_sse_progress, timeout=timeout),
    )

    if op_result.status.value == "completed":
      if on_progress:
        on_progress(f"Tier changed to {new_tier} successfully")
      return

    raise RuntimeError(
      f"Tier change {op_result.status.value}: {op_result.error or 'unknown error'}"
    )

  # ---------------------------------------------------------------------------
  # SSE / polling helpers (used by create_graph_and_wait)
  # ---------------------------------------------------------------------------

  def _wait_with_sse(
    self,
    operation_id: str,
    timeout: int,
    on_progress: Optional[Callable[[str], None]],
  ) -> str:
    """Wait for operation completion using SSE stream."""
    stream_url = f"{self.base_url}/v1/operations/{operation_id}/stream"
    headers = {"X-API-Key": self.token, "Accept": "text/event-stream"}

    with httpx.Client(timeout=httpx.Timeout(timeout + 5.0)) as http_client:
      with http_client.stream("GET", stream_url, headers=headers) as response:
        if response.status_code != 200:
          raise RuntimeError(f"SSE connection failed: {response.status_code}")

        start_time = time.time()
        event_type = None
        event_data = ""

        for line in response.iter_lines():
          if time.time() - start_time > timeout:
            raise TimeoutError(f"Graph creation timed out after {timeout}s")

          line = line.strip()

          if not line:
            if event_type and event_data:
              result = self._process_sse_event(event_type, event_data, on_progress)
              if result is not None:
                return result
            event_type = None
            event_data = ""
            continue

          if line.startswith("event:"):
            event_type = line[6:].strip()
          elif line.startswith("data:"):
            event_data = line[5:].strip()

    raise TimeoutError(f"SSE stream ended without completion after {timeout}s")

  def _process_sse_event(
    self,
    event_type: str,
    event_data: str,
    on_progress: Optional[Callable[[str], None]],
  ) -> Optional[str]:
    """Process a single SSE event. Returns graph_id if completed."""
    try:
      data = json.loads(event_data)
    except json.JSONDecodeError:
      logger.debug(f"Failed to parse SSE event data: {event_data}")
      return None

    if event_type == "operation_progress":
      if on_progress:
        message = data.get("message", "Processing...")
        percent = data.get("progress_percent")
        if percent is not None:
          on_progress(f"{message} ({percent:.0f}%)")
        else:
          on_progress(message)
      return None

    elif event_type == "operation_completed":
      result = data.get("result", {})
      graph_id = result.get("graph_id") if isinstance(result, dict) else None

      if graph_id:
        if on_progress:
          on_progress(f"Graph created: {graph_id}")
        return graph_id
      else:
        raise RuntimeError("Operation completed but no graph_id in result")

    elif event_type == "operation_error":
      error = data.get("error", "Unknown error")
      raise RuntimeError(f"Graph creation failed: {error}")

    elif event_type == "operation_cancelled":
      reason = data.get("reason", "Operation was cancelled")
      raise RuntimeError(f"Graph creation cancelled: {reason}")

    return None

  def _wait_with_polling(
    self,
    operation_id: str,
    timeout: int,
    poll_interval: int,
    on_progress: Optional[Callable[[str], None]],
    client: Any,
  ) -> str:
    """Wait for operation completion using polling."""
    from ..api.operations.get_operation_status import sync_detailed as get_status

    max_attempts = timeout // poll_interval
    for attempt in range(max_attempts):
      time.sleep(poll_interval)

      status_response = get_status(operation_id=operation_id, client=client)

      if not status_response.parsed:
        continue

      status_data = status_response.parsed
      if isinstance(status_data, dict):
        status = status_data.get("status")
      else:
        if hasattr(status_data, "additional_properties"):
          status = status_data.additional_properties.get("status")
        else:
          status = getattr(status_data, "status", None)

      if on_progress:
        on_progress(f"Status: {status} (attempt {attempt + 1}/{max_attempts})")

      if status == "completed":
        if isinstance(status_data, dict):
          result = status_data.get("result", {})
        elif hasattr(status_data, "additional_properties"):
          result = status_data.additional_properties.get("result", {})
        else:
          result = getattr(status_data, "result", {})

        if isinstance(result, dict):
          graph_id = result.get("graph_id")
        else:
          graph_id = getattr(result, "graph_id", None)

        if graph_id:
          if on_progress:
            on_progress(f"Graph created: {graph_id}")
          return graph_id
        else:
          raise RuntimeError("Operation completed but no graph_id in result")

      elif status == "failed":
        if isinstance(status_data, dict):
          error = (
            status_data.get("error") or status_data.get("message") or "Unknown error"
          )
        elif hasattr(status_data, "additional_properties"):
          props = status_data.additional_properties
          error = props.get("error") or props.get("message") or "Unknown error"
        else:
          error = getattr(status_data, "message", "Unknown error")
        raise RuntimeError(f"Graph creation failed: {error}")

    raise TimeoutError(f"Graph creation timed out after {timeout}s")

  def delete_graph(
    self,
    graph_id: str,
    at_period_end: bool = False,
    on_progress: Optional[Callable[[str], None]] = None,
  ) -> Dict[str, Any]:
    """
    Permanently delete a graph by canceling its subscription and triggering
    deprovisioning.

    Two modes:

    - **Immediate** (default, ``at_period_end=False``): subscription canceled
      now and fast-path deprovisioning fires within ~10 minutes.
    - **At period end** (``at_period_end=True``): graph stays usable through
      the current billing period; suspend → deprovision pipeline tears it
      down at the period boundary.

    Args:
        graph_id: Graph database identifier (must be a user graph — shared
            repositories cannot be deleted)
        at_period_end: If True, defer cancellation and teardown to the end
            of the current billing period.
        on_progress: Optional callback for progress updates.

    Returns:
        The ``result`` field of the operation envelope. For immediate:
        ``{"graph_id", "subscription_id", "status": "deprovisioning_queued",
        "message"}``. For period-end: includes ``ends_at`` instead.

    Raises:
        RuntimeError: If the deletion request fails.
    """
    from ..api.graph_operations.op_delete_graph import (
      sync_detailed as op_delete_graph,
    )
    from ..models.delete_graph_op import DeleteGraphOp

    client = self._get_authenticated_client()

    if on_progress:
      mode = "at period end" if at_period_end else "immediately"
      on_progress(f"Deleting graph {graph_id} ({mode})...")

    response = op_delete_graph(
      graph_id=graph_id,
      client=client,
      body=DeleteGraphOp(confirm=graph_id, at_period_end=at_period_end),
    )

    if response.status_code not in (200, 202) or not response.parsed:
      error_msg = f"Graph deletion failed: HTTP {response.status_code}"
      if hasattr(response, "content"):
        try:
          error_data = json.loads(response.content)
          error_msg = error_data.get("detail", error_msg)
        except Exception:
          pass
      raise RuntimeError(error_msg)

    envelope = response.parsed
    result = getattr(envelope, "result", None)
    if isinstance(result, dict):
      result_dict = result
    elif hasattr(result, "additional_properties"):
      result_dict = dict(result.additional_properties)
    else:
      result_dict = {}

    if on_progress:
      on_progress(result_dict.get("message", "Graph deletion submitted."))

    return result_dict

  def close(self):
    """Clean up resources."""
    pass
