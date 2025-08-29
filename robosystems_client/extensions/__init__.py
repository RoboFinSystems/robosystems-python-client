"""RoboSystems Client Extensions for Python

Enhanced clients with SSE support for the RoboSystems API.
Provides seamless integration with streaming operations, queue management,
and advanced query capabilities.
"""

from .sse_client import SSEClient, EventType, SSEEvent, SSEConfig
from .query_client import (
  QueryClient,
  QueryResult,
  QueuedQueryResponse,
  QueryRequest,
  QueryOptions,
  QueuedQueryError,
)
from .operation_client import (
  OperationClient,
  OperationStatus,
  OperationProgress,
  OperationResult,
)
from .copy_client import (
  CopyClient,
  AsyncCopyClient,
  CopySourceType,
  CopyOptions,
  CopyResult,
  CopyStatistics,
)
from .extensions import (
  RoboSystemsExtensions,
  RoboSystemsExtensionConfig,
  AsyncRoboSystemsExtensions,
)
from .utils import (
  QueryBuilder,
  ResultProcessor,
  CacheManager,
  ProgressTracker,
  DataBatcher,
  QueryStats,
  ConnectionInfo,
  estimate_query_cost,
  format_duration,
  validate_cypher_query,
)
from .auth_integration import (
  AuthenticatedExtensions,
  CookieAuthExtensions,
  TokenExtensions,
  create_extensions,
  create_production_extensions,
  create_development_extensions,
)

__all__ = [
  # Core extension classes
  "RoboSystemsExtensions",
  "RoboSystemsExtensionConfig",
  "AsyncRoboSystemsExtensions",
  # SSE Client
  "SSEClient",
  "EventType",
  "SSEEvent",
  "SSEConfig",
  # Query Client
  "QueryClient",
  "QueryResult",
  "QueuedQueryResponse",
  "QueryRequest",
  "QueryOptions",
  "QueuedQueryError",
  # Operation Client
  "OperationClient",
  "OperationStatus",
  "OperationProgress",
  "OperationResult",
  # Copy Client
  "CopyClient",
  "AsyncCopyClient",
  "CopySourceType",
  "CopyOptions",
  "CopyResult",
  "CopyStatistics",
  # Utilities
  "QueryBuilder",
  "ResultProcessor",
  "CacheManager",
  "ProgressTracker",
  "DataBatcher",
  "QueryStats",
  "ConnectionInfo",
  "estimate_query_cost",
  "format_duration",
  "validate_cypher_query",
  # Authentication Integration
  "AuthenticatedExtensions",
  "CookieAuthExtensions",
  "TokenExtensions",
  "create_extensions",
  "create_production_extensions",
  "create_development_extensions",
]

# Create a default extensions instance
extensions = RoboSystemsExtensions()


# Export convenience functions
def monitor_operation(operation_id: str, on_progress=None):
  """Monitor an operation using the default extensions instance"""
  return extensions.monitor_operation(operation_id, on_progress)


def execute_query(graph_id: str, query: str, parameters=None):
  """Execute a query using the default extensions instance"""
  return extensions.query.query(graph_id, query, parameters)


def stream_query(graph_id: str, query: str, parameters=None, chunk_size=None):
  """Stream a query using the default extensions instance"""
  return extensions.query.stream_query(graph_id, query, parameters, chunk_size)


def copy_from_s3(
  graph_id: str,
  table_name: str,
  s3_path: str,
  access_key_id: str,
  secret_access_key: str,
  **kwargs,
):
  """Copy data from S3 using the default extensions instance"""
  return extensions.copy_from_s3(
    graph_id, table_name, s3_path, access_key_id, secret_access_key, **kwargs
  )
