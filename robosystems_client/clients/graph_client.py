"""Graph Management Client

Provides high-level graph management operations with automatic operation monitoring.
Supports both SSE (Server-Sent Events) for real-time updates and polling fallback.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable
import time
import json
import logging

import httpx

logger = logging.getLogger(__name__)


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


class GraphClient:
  """Client for graph management operations"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")

  def create_graph_and_wait(
    self,
    metadata: GraphMetadata,
    initial_entity: Optional[InitialEntityData] = None,
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
        initial_entity: Optional initial entity data
        create_entity: Whether to create the entity node and upload initial data.
            Only applies when initial_entity is provided. Set to False to create
            graph without populating entity data (useful for file-based ingestion).
        timeout: Maximum time to wait in seconds
        poll_interval: Time between status checks in seconds (for polling fallback)
        on_progress: Callback for progress updates
        use_sse: Whether to try SSE first (default True). Falls back to polling on failure.

    Returns:
        graph_id when creation completes

    Raises:
        Exception: If creation fails or times out
    """
    from ..client import AuthenticatedClient
    from ..api.graphs.create_graph import sync_detailed as create_graph
    from ..models.create_graph_request import CreateGraphRequest
    from ..models.graph_metadata import GraphMetadata as APIGraphMetadata

    if not self.token:
      raise ValueError("No API key provided. Set X-API-Key in headers.")

    client = AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

    # Build API metadata
    api_metadata = APIGraphMetadata(
      graph_name=metadata.graph_name,
      description=metadata.description,
      schema_extensions=metadata.schema_extensions or [],
      tags=metadata.tags or [],
    )

    # Build initial entity if provided
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

    # Create graph request
    graph_create = CreateGraphRequest(
      metadata=api_metadata,
      initial_entity=initial_entity_dict,
      create_entity=create_entity,
    )

    if on_progress:
      on_progress(f"Creating graph: {metadata.graph_name}")

    # Execute create request
    response = create_graph(client=client, body=graph_create)

    if not response.parsed:
      raise RuntimeError(f"Failed to create graph: {response.status_code}")

    # Extract graph_id or operation_id
    if isinstance(response.parsed, dict):
      graph_id = response.parsed.get("graph_id")
      operation_id = response.parsed.get("operation_id")
    else:
      graph_id = getattr(response.parsed, "graph_id", None)
      operation_id = getattr(response.parsed, "operation_id", None)

    # If graph_id returned immediately, we're done
    if graph_id:
      if on_progress:
        on_progress(f"Graph created: {graph_id}")
      return graph_id

    # Otherwise, wait for operation to complete
    if not operation_id:
      raise RuntimeError("No graph_id or operation_id in response")

    if on_progress:
      on_progress(f"Graph creation queued (operation: {operation_id})")

    # Try SSE first, fall back to polling
    if use_sse:
      try:
        return self._wait_with_sse(operation_id, timeout, on_progress)
      except Exception as e:
        logger.debug(f"SSE connection failed, falling back to polling: {e}")
        if on_progress:
          on_progress("SSE unavailable, using polling...")

    # Fallback to polling
    return self._wait_with_polling(
      operation_id, timeout, poll_interval, on_progress, client
    )

  def _wait_with_sse(
    self,
    operation_id: str,
    timeout: int,
    on_progress: Optional[Callable[[str], None]],
  ) -> str:
    """
    Wait for operation completion using SSE stream.

    Args:
        operation_id: Operation ID to monitor
        timeout: Maximum time to wait in seconds
        on_progress: Callback for progress updates

    Returns:
        graph_id when operation completes

    Raises:
        RuntimeError: If operation fails
        TimeoutError: If operation times out
    """
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
          # Check timeout
          if time.time() - start_time > timeout:
            raise TimeoutError(f"Graph creation timed out after {timeout}s")

          line = line.strip()

          if not line:
            # Empty line = end of event, process it
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
          # Ignore other lines (comments, id, retry, etc.)

    raise TimeoutError(f"SSE stream ended without completion after {timeout}s")

  def _process_sse_event(
    self,
    event_type: str,
    event_data: str,
    on_progress: Optional[Callable[[str], None]],
  ) -> Optional[str]:
    """
    Process a single SSE event.

    Returns:
        graph_id if operation completed, None to continue waiting

    Raises:
        RuntimeError: If operation failed
    """
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

    # Ignore other event types (keepalive, etc.)
    return None

  def _wait_with_polling(
    self,
    operation_id: str,
    timeout: int,
    poll_interval: int,
    on_progress: Optional[Callable[[str], None]],
    client: Any,
  ) -> str:
    """
    Wait for operation completion using polling.

    Args:
        operation_id: Operation ID to monitor
        timeout: Maximum time to wait in seconds
        poll_interval: Time between status checks
        on_progress: Callback for progress updates
        client: Authenticated HTTP client

    Returns:
        graph_id when operation completes

    Raises:
        RuntimeError: If operation fails
        TimeoutError: If operation times out
    """
    from ..api.operations.get_operation_status import sync_detailed as get_status

    max_attempts = timeout // poll_interval
    for attempt in range(max_attempts):
      time.sleep(poll_interval)

      status_response = get_status(operation_id=operation_id, client=client)

      if not status_response.parsed:
        continue

      # Handle both dict and object responses
      status_data = status_response.parsed
      if isinstance(status_data, dict):
        status = status_data.get("status")
      else:
        # Check for additional_properties first (common in generated clients)
        if hasattr(status_data, "additional_properties"):
          status = status_data.additional_properties.get("status")
        else:
          status = getattr(status_data, "status", None)

      if on_progress:
        on_progress(f"Status: {status} (attempt {attempt + 1}/{max_attempts})")

      if status == "completed":
        # Extract graph_id from result
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
        # Extract error message
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

  def get_graph_info(self, graph_id: str) -> GraphInfo:
    """
    Get information about a graph.

    Args:
        graph_id: The graph ID

    Returns:
        GraphInfo with graph details

    Raises:
        ValueError: If graph not found
    """
    from ..client import AuthenticatedClient
    from ..api.graphs.get_graphs import sync_detailed as get_graphs

    if not self.token:
      raise ValueError("No API key provided. Set X-API-Key in headers.")

    client = AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

    # Use get_graphs and filter for the specific graph
    response = get_graphs(client=client)

    if not response.parsed:
      raise RuntimeError(f"Failed to get graphs: {response.status_code}")

    data = response.parsed
    graphs = None

    # Extract graphs list from response
    if isinstance(data, dict):
      graphs = data.get("graphs", [])
    elif hasattr(data, "additional_properties"):
      graphs = data.additional_properties.get("graphs", [])
    elif hasattr(data, "graphs"):
      graphs = data.graphs
    else:
      raise RuntimeError("Unexpected response format from get_graphs")

    # Find the specific graph by ID
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

    # Build GraphInfo from the found graph
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

  def delete_graph(self, graph_id: str) -> None:
    """
    Delete a graph.

    Note: This method is not yet available as the delete_graph endpoint
    is not included in the generated SDK. This will be implemented when
    the endpoint is added to the API specification.

    Args:
        graph_id: The graph ID to delete

    Raises:
        NotImplementedError: This feature is not yet available
    """
    raise NotImplementedError(
      "Graph deletion is not yet available. "
      "The delete_graph endpoint needs to be added to the API specification."
    )

  def close(self):
    """Clean up resources (placeholder for consistency)"""
    pass
