"""RoboSystems Client Extensions - Main entry point

Enhanced clients with SSE support for the RoboSystems API.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable

from .query_client import QueryClient
from .agent_client import AgentClient
from .operation_client import OperationClient
from .table_ingest_client import TableIngestClient
from .graph_client import GraphClient
from .sse_client import SSEClient


@dataclass
class RoboSystemsExtensionConfig:
  """Configuration for RoboSystems extensions"""

  base_url: Optional[str] = None
  headers: Optional[Dict[str, str]] = None
  max_retries: int = 5
  retry_delay: int = 1000
  timeout: int = 30


class RoboSystemsExtensions:
  """Main extensions class providing enhanced RoboSystems API functionality"""

  def __init__(self, config: RoboSystemsExtensionConfig = None):
    if config is None:
      config = RoboSystemsExtensionConfig()

    # Get base URL from config or use default
    self.config = {
      "base_url": config.base_url or "http://localhost:8000",
      "headers": config.headers or {},
      "max_retries": config.max_retries,
      "retry_delay": config.retry_delay,
      "timeout": config.timeout,
    }

    # Extract token from headers if it was set by auth classes
    # The auth classes should set the token in a standard way
    token = None
    if config.headers:
      # Check for Authorization Bearer token
      auth_header = config.headers.get("Authorization", "")
      if auth_header.startswith("Bearer "):
        token = auth_header[7:]
      # Check for X-API-Key
      elif config.headers.get("X-API-Key"):
        token = config.headers.get("X-API-Key")

    # Pass token to child clients if available
    if token:
      self.config["token"] = token

    # Initialize clients
    self.query = QueryClient(self.config)
    self.agent = AgentClient(self.config)
    self.operations = OperationClient(self.config)
    self.tables = TableIngestClient(self.config)
    self.graphs = GraphClient(self.config)

  def monitor_operation(
    self, operation_id: str, on_progress: Optional[Callable] = None
  ) -> Any:
    """Convenience method to monitor any operation"""
    from .operation_client import MonitorOptions

    options = MonitorOptions(on_progress=on_progress)
    return self.operations.monitor_operation(operation_id, options)

  def create_sse_client(self) -> SSEClient:
    """Create custom SSE client for advanced use cases"""
    from .sse_client import SSEConfig

    sse_config = SSEConfig(
      base_url=self.config["base_url"],
      headers=self.config["headers"],
      max_retries=self.config["max_retries"],
      retry_delay=self.config["retry_delay"],
      timeout=self.config["timeout"],
    )

    return SSEClient(sse_config)

  def close(self):
    """Clean up all active connections"""
    self.query.close()
    self.agent.close()
    self.operations.close_all()
    self.tables.close()
    self.graphs.close()

  # Convenience methods that delegate to the appropriate clients
  def execute_query(self, graph_id: str, query: str, parameters: Dict[str, Any] = None):
    """Execute a query using the query client"""
    return self.query.query(graph_id, query, parameters)

  def stream_query(
    self,
    graph_id: str,
    query: str,
    parameters: Dict[str, Any] = None,
    chunk_size: int = 1000,
  ):
    """Stream a query using the query client"""
    return self.query.stream_query(graph_id, query, parameters, chunk_size)

  def get_operation_status(self, operation_id: str):
    """Get operation status using the operation client"""
    return self.operations.get_operation_status(operation_id)

  def cancel_operation(self, operation_id: str):
    """Cancel an operation using the operation client"""
    return self.operations.cancel_operation(operation_id)


class AsyncRoboSystemsExtensions:
  """Async version of the extensions class"""

  def __init__(self, config: RoboSystemsExtensionConfig = None):
    if config is None:
      config = RoboSystemsExtensionConfig()

    self.config = {
      "base_url": config.base_url or "http://localhost:8000",
      "headers": config.headers or {},
      "max_retries": config.max_retries,
      "retry_delay": config.retry_delay,
      "timeout": config.timeout,
    }

    # Initialize async clients
    from .query_client import AsyncQueryClient
    from .operation_client import AsyncOperationClient

    self.query = AsyncQueryClient(self.config)
    self.operations = AsyncOperationClient(self.config)

  async def monitor_operation(
    self, operation_id: str, on_progress: Optional[Callable] = None
  ) -> Any:
    """Convenience method to monitor any operation (async)"""
    from .operation_client import MonitorOptions

    options = MonitorOptions(on_progress=on_progress)
    return await self.operations.monitor_operation(operation_id, options)

  def create_sse_client(self):
    """Create custom async SSE client for advanced use cases"""
    from .sse_client import AsyncSSEClient, SSEConfig

    sse_config = SSEConfig(
      base_url=self.config["base_url"],
      headers=self.config["headers"],
      max_retries=self.config["max_retries"],
      retry_delay=self.config["retry_delay"],
      timeout=self.config["timeout"],
    )

    return AsyncSSEClient(sse_config)

  async def close(self):
    """Clean up all active connections (async)"""
    await self.query.close()
    await self.operations.close_all()

  async def execute_query(
    self, graph_id: str, query: str, parameters: Dict[str, Any] = None
  ):
    """Execute a query using the async query client"""
    return await self.query.query(graph_id, query, parameters)

  async def stream_query(
    self,
    graph_id: str,
    query: str,
    parameters: Dict[str, Any] = None,
    chunk_size: int = 1000,
  ):
    """Stream a query using the async query client"""
    async for item in self.query.stream_query(graph_id, query, parameters, chunk_size):
      yield item

  async def get_operation_status(self, operation_id: str):
    """Get operation status using the async operation client"""
    return await self.operations.get_operation_status(operation_id)

  async def cancel_operation(self, operation_id: str):
    """Cancel an operation using the async operation client"""
    return await self.operations.cancel_operation(operation_id)
