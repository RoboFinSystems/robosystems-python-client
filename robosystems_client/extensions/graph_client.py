"""Graph Management Client

Provides high-level graph management operations with automatic operation monitoring.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable
import time
import logging

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
    timeout: int = 60,
    poll_interval: int = 2,
    on_progress: Optional[Callable[[str], None]] = None,
  ) -> str:
    """
    Create a graph and wait for completion.

    Args:
        metadata: Graph metadata
        initial_entity: Optional initial entity data
        timeout: Maximum time to wait in seconds
        poll_interval: Time between status checks in seconds
        on_progress: Callback for progress updates

    Returns:
        graph_id when creation completes

    Raises:
        Exception: If creation fails or times out
    """
    from ..client import AuthenticatedClient
    from ..api.graphs.create_graph import sync_detailed as create_graph
    from ..api.operations.get_operation_status import sync_detailed as get_status
    from ..models.create_graph_request import CreateGraphRequest
    from ..models.graph_metadata import GraphMetadata as APIGraphMetadata

    if not self.token:
      raise Exception("No API key provided. Set X-API-Key in headers.")

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
    )

    if on_progress:
      on_progress(f"Creating graph: {metadata.graph_name}")

    # Execute create request
    response = create_graph(client=client, body=graph_create)

    if not response.parsed:
      raise Exception(f"Failed to create graph: {response.status_code}")

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

    # Otherwise, poll operation until complete
    if not operation_id:
      raise Exception("No graph_id or operation_id in response")

    if on_progress:
      on_progress(f"Graph creation queued (operation: {operation_id})")

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
          raise Exception("Operation completed but no graph_id in result")

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
        raise Exception(f"Graph creation failed: {error}")

    raise Exception(f"Graph creation timed out after {timeout}s")

  def get_graph_info(self, graph_id: str) -> GraphInfo:
    """
    Get information about a graph.

    Args:
        graph_id: The graph ID

    Returns:
        GraphInfo with graph details
    """
    from ..client import AuthenticatedClient
    from ..api.graphs.get_graph import sync_detailed as get_graph

    if not self.token:
      raise Exception("No API key provided. Set X-API-Key in headers.")

    client = AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

    response = get_graph(graph_id=graph_id, client=client)

    if not response.parsed:
      raise Exception(f"Failed to get graph info: {response.status_code}")

    data = response.parsed
    if isinstance(data, dict):
      return GraphInfo(
        graph_id=data.get("graph_id", graph_id),
        graph_name=data.get("graph_name", ""),
        description=data.get("description"),
        schema_extensions=data.get("schema_extensions"),
        tags=data.get("tags"),
        created_at=data.get("created_at"),
        status=data.get("status"),
      )
    else:
      return GraphInfo(
        graph_id=getattr(data, "graph_id", graph_id),
        graph_name=getattr(data, "graph_name", ""),
        description=getattr(data, "description", None),
        schema_extensions=getattr(data, "schema_extensions", None),
        tags=getattr(data, "tags", None),
        created_at=getattr(data, "created_at", None),
        status=getattr(data, "status", None),
      )

  def delete_graph(self, graph_id: str) -> None:
    """
    Delete a graph.

    Args:
        graph_id: The graph ID to delete
    """
    from ..client import AuthenticatedClient
    from ..api.graphs.delete_graph import sync_detailed as delete_graph

    if not self.token:
      raise Exception("No API key provided. Set X-API-Key in headers.")

    client = AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

    response = delete_graph(graph_id=graph_id, client=client)

    if response.status_code not in [200, 204]:
      raise Exception(f"Failed to delete graph: {response.status_code}")

  def close(self):
    """Clean up resources (placeholder for consistency)"""
    pass
