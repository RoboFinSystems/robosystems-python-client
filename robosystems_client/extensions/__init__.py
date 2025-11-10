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
from .agent_client import (
  AgentClient,
  AgentResult,
  QueuedAgentResponse,
  AgentQueryRequest,
  AgentOptions,
  QueuedAgentError,
)
from .operation_client import (
  OperationClient,
  OperationStatus,
  OperationProgress,
  OperationResult,
)
from .table_ingest_client import (
  TableIngestClient,
  UploadOptions,
  IngestOptions,
  UploadResult,
  TableInfo,
)
from .graph_client import (
  GraphClient,
  GraphMetadata,
  InitialEntityData,
  GraphInfo,
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

# JWT Token utilities
from .token_utils import (
  validate_jwt_format,
  extract_jwt_from_header,
  decode_jwt_payload,
  is_jwt_expired,
  get_jwt_claims,
  get_jwt_expiration,
  extract_token_from_environment,
  extract_token_from_cookie,
  find_valid_token,
  TokenManager,
  TokenSource,
)

# DataFrame utilities (optional - requires pandas)
try:
  from .dataframe_utils import (
    query_result_to_dataframe,
    DataFrameQueryClient,
    HAS_PANDAS,
  )

  # Re-export the imported functions for module API
  from .dataframe_utils import (
    parse_datetime_columns,
    stream_to_dataframe as _stream_to_dataframe,
    dataframe_to_cypher_params,
    export_query_to_csv,
    compare_dataframes,
  )
except ImportError:
  HAS_PANDAS = False
  DataFrameQueryClient = None
  # Set placeholders for optional functions
  query_result_to_dataframe = None
  parse_datetime_columns = None
  _stream_to_dataframe = None
  dataframe_to_cypher_params = None
  export_query_to_csv = None
  compare_dataframes = None

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
  # Agent Client
  "AgentClient",
  "AgentResult",
  "QueuedAgentResponse",
  "AgentQueryRequest",
  "AgentOptions",
  "QueuedAgentError",
  # Operation Client
  "OperationClient",
  "OperationStatus",
  "OperationProgress",
  "OperationResult",
  # Table Ingest Client
  "TableIngestClient",
  "UploadOptions",
  "IngestOptions",
  "UploadResult",
  "TableInfo",
  # Graph Client
  "GraphClient",
  "GraphMetadata",
  "InitialEntityData",
  "GraphInfo",
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
  # JWT Token utilities
  "validate_jwt_format",
  "extract_jwt_from_header",
  "decode_jwt_payload",
  "is_jwt_expired",
  "get_jwt_claims",
  "get_jwt_expiration",
  "extract_token_from_environment",
  "extract_token_from_cookie",
  "find_valid_token",
  "TokenManager",
  "TokenSource",
  # DataFrame utilities (optional)
  "HAS_PANDAS",
  "DataFrameQueryClient",
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


def agent_query(graph_id: str, message: str, context=None):
  """Execute an agent query using the default extensions instance"""
  return extensions.agent.query(graph_id, message, context)


def analyze_financials(graph_id: str, message: str, on_progress=None):
  """Execute financial agent using the default extensions instance"""
  return extensions.agent.analyze_financials(graph_id, message, on_progress)


# DataFrame convenience functions (if pandas is available)
if (
  HAS_PANDAS
  and query_result_to_dataframe is not None
  and _stream_to_dataframe is not None
):

  def query_to_dataframe(graph_id: str, query: str, parameters=None, **kwargs):
    """Execute query and return results as pandas DataFrame"""
    assert query_result_to_dataframe is not None
    result = execute_query(graph_id, query, parameters)
    return query_result_to_dataframe(result, **kwargs)

  def stream_to_dataframe(graph_id: str, query: str, parameters=None, chunk_size=10000):
    """Stream query results and return as pandas DataFrame"""
    assert _stream_to_dataframe is not None
    stream = stream_query(graph_id, query, parameters, chunk_size)
    return _stream_to_dataframe(stream, chunk_size)
