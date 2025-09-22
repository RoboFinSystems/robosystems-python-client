"""Enhanced Query Client with SSE support

Provides intelligent query execution with automatic strategy selection.
"""

from dataclasses import dataclass
from typing import (
  Dict,
  Any,
  Optional,
  Callable,
  AsyncIterator,
  Iterator,
  Union,
  Generator,
  List,
)
from datetime import datetime

from ..api.query.execute_cypher_query import sync_detailed as execute_cypher_query
from ..models.cypher_query_request import CypherQueryRequest
from .sse_client import SSEClient, AsyncSSEClient, SSEConfig, EventType


@dataclass
class QueryRequest:
  """Request object for queries"""

  query: str
  parameters: Optional[Dict[str, Any]] = None
  timeout: Optional[int] = None


@dataclass
class QueryOptions:
  """Options for query execution"""

  mode: Optional[str] = "auto"  # 'auto', 'sync', 'async', 'stream'
  chunk_size: Optional[int] = None
  test_mode: Optional[bool] = None
  max_wait: Optional[int] = None
  on_queue_update: Optional[Callable[[int, int], None]] = None
  on_progress: Optional[Callable[[str], None]] = None


@dataclass
class QueryResult:
  """Result from query execution"""

  data: list
  columns: list
  row_count: int
  execution_time_ms: int
  graph_id: Optional[str] = None
  timestamp: Optional[str] = None


@dataclass
class QueuedQueryResponse:
  """Response when query is queued"""

  status: str
  operation_id: str
  queue_position: int
  estimated_wait_seconds: int
  message: str


class QueuedQueryError(Exception):
  """Exception thrown when query is queued and maxWait is 0"""

  def __init__(self, queue_info: QueuedQueryResponse):
    super().__init__("Query was queued")
    self.queue_info = queue_info


class QueryClient:
  """Enhanced query client with SSE streaming support"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    # Get token from config if passed by parent
    self.token = config.get("token")
    self.sse_client: Optional[SSEClient] = None

  def execute_query(
    self, graph_id: str, request: QueryRequest, options: QueryOptions = None
  ) -> Union[QueryResult, Iterator[Any]]:
    """Execute a query with intelligent strategy selection"""
    if options is None:
      options = QueryOptions()

    # Build request data
    query_request = CypherQueryRequest(
      query=request.query, parameters=request.parameters or {}
    )

    # Execute the query through the generated client
    from ..client import Client

    # Create client with headers
    client = Client(base_url=self.base_url, headers=self.headers)

    try:
      kwargs = {"graph_id": graph_id, "client": client, "body": query_request}
      # Only add token if it's a valid string
      if self.token and isinstance(self.token, str) and self.token.strip():
        kwargs["token"] = self.token
      response = execute_cypher_query(**kwargs)

      # Check response type and handle accordingly
      if hasattr(response, "parsed") and response.parsed:
        response_data = response.parsed

        # Check if this is an immediate response
        if hasattr(response_data, "data") and hasattr(response_data, "columns"):
          return QueryResult(
            data=response_data.data,
            columns=response_data.columns,
            row_count=getattr(response_data, "row_count", len(response_data.data)),
            execution_time_ms=getattr(response_data, "execution_time_ms", 0),
            graph_id=graph_id,
            timestamp=getattr(response_data, "timestamp", datetime.now().isoformat()),
          )

        # Check if this is a queued response
        if (
          hasattr(response_data, "status")
          and response_data.status == "queued"
          and hasattr(response_data, "operation_id")
        ):
          queued_response = QueuedQueryResponse(
            status=response_data.status,
            operation_id=response_data.operation_id,
            queue_position=getattr(response_data, "queue_position", 0),
            estimated_wait_seconds=getattr(response_data, "estimated_wait_seconds", 0),
            message=getattr(response_data, "message", "Query queued"),
          )

          # Notify about queue status
          if options.on_queue_update:
            options.on_queue_update(
              queued_response.queue_position, queued_response.estimated_wait_seconds
            )

          # If user doesn't want to wait, raise with queue info
          if options.max_wait == 0:
            raise QueuedQueryError(queued_response)

          # Use SSE to monitor the operation
          if options.mode == "stream":
            return self._stream_query_results(queued_response.operation_id, options)
          else:
            return self._wait_for_query_completion(
              queued_response.operation_id, options
            )

    except Exception as e:
      if isinstance(e, QueuedQueryError):
        raise

      error_msg = str(e)
      # Check for authentication errors
      if (
        "401" in error_msg or "403" in error_msg or "unauthorized" in error_msg.lower()
      ):
        raise Exception(f"Authentication failed during query execution: {error_msg}")
      else:
        raise Exception(f"Query execution failed: {error_msg}")

    # Unexpected response format
    raise Exception("Unexpected response format from query endpoint")

  def _stream_query_results(
    self, operation_id: str, options: QueryOptions
  ) -> Iterator[Any]:
    """Stream query results using SSE"""
    buffer = []
    completed = False
    error = None

    # Set up SSE connection
    sse_config = SSEConfig(base_url=self.base_url)
    self.sse_client = SSEClient(sse_config)

    # Set up event handlers
    def on_data_chunk(data):
      nonlocal buffer
      if isinstance(data.get("rows"), list):
        buffer.extend(data["rows"])
      elif isinstance(data.get("data"), list):
        buffer.extend(data["data"])

    def on_queue_update(data):
      if options.on_queue_update:
        options.on_queue_update(
          data.get("position", 0), data.get("estimated_wait_seconds", 0)
        )

    def on_progress(data):
      if options.on_progress:
        options.on_progress(data.get("message", "Processing..."))

    def on_completed(data):
      nonlocal completed, buffer
      if data.get("result", {}).get("data"):
        buffer.extend(data["result"]["data"])
      completed = True

    def on_error(err):
      nonlocal error, completed
      error = Exception(err.get("message", err.get("error", "Unknown error")))
      completed = True

    # Register event handlers
    self.sse_client.on(EventType.DATA_CHUNK.value, on_data_chunk)
    self.sse_client.on(EventType.QUEUE_UPDATE.value, on_queue_update)
    self.sse_client.on(EventType.OPERATION_PROGRESS.value, on_progress)
    self.sse_client.on(EventType.OPERATION_COMPLETED.value, on_completed)
    self.sse_client.on(EventType.OPERATION_ERROR.value, on_error)

    # Connect and start streaming
    self.sse_client.connect(operation_id)

    # Yield buffered results
    while not completed or buffer:
      if error:
        raise error

      if buffer:
        chunk_size = options.chunk_size or 100
        chunk = buffer[:chunk_size]
        buffer = buffer[chunk_size:]
        for item in chunk:
          yield item
      elif not completed:
        # Wait for more data
        import time

        time.sleep(0.1)

    # Clean up
    if self.sse_client:
      self.sse_client.close()
      self.sse_client = None

  def _wait_for_query_completion(
    self, operation_id: str, options: QueryOptions
  ) -> QueryResult:
    """Wait for query completion and return final result"""
    result = None
    error = None
    completed = False

    # Set up SSE connection
    sse_config = SSEConfig(base_url=self.base_url)
    sse_client = SSEClient(sse_config)

    def on_queue_update(data):
      if options.on_queue_update:
        options.on_queue_update(
          data.get("position", 0), data.get("estimated_wait_seconds", 0)
        )

    def on_progress(data):
      if options.on_progress:
        options.on_progress(data.get("message", "Processing..."))

    def on_completed(data):
      nonlocal result, completed
      query_result = data.get("result", data)
      result = QueryResult(
        data=query_result.get("data", []),
        columns=query_result.get("columns", []),
        row_count=query_result.get("row_count", 0),
        execution_time_ms=query_result.get("execution_time_ms", 0),
        graph_id=query_result.get("graph_id"),
        timestamp=query_result.get("timestamp", datetime.now().isoformat()),
      )
      completed = True

    def on_error(err):
      nonlocal error, completed
      error = Exception(err.get("message", err.get("error", "Unknown error")))
      completed = True

    def on_cancelled():
      nonlocal error, completed
      error = Exception("Query cancelled")
      completed = True

    # Register event handlers
    sse_client.on(EventType.QUEUE_UPDATE.value, on_queue_update)
    sse_client.on(EventType.OPERATION_PROGRESS.value, on_progress)
    sse_client.on(EventType.OPERATION_COMPLETED.value, on_completed)
    sse_client.on(EventType.OPERATION_ERROR.value, on_error)
    sse_client.on(EventType.OPERATION_CANCELLED.value, on_cancelled)

    # Connect and wait
    sse_client.connect(operation_id)

    # Wait for completion
    import time

    while not completed:
      if error:
        sse_client.close()
        raise error
      time.sleep(0.1)

    sse_client.close()
    return result

  def query(
    self, graph_id: str, cypher: str, parameters: Dict[str, Any] = None
  ) -> QueryResult:
    """Convenience method for simple queries"""
    request = QueryRequest(query=cypher, parameters=parameters)
    result = self.execute_query(graph_id, request, QueryOptions(mode="auto"))
    if isinstance(result, QueryResult):
      return result
    else:
      # If it's an iterator, collect all results
      data = list(result)
      return QueryResult(
        data=data,
        columns=[],  # Would need to extract from first chunk
        row_count=len(data),
        execution_time_ms=0,
        graph_id=graph_id,
        timestamp=datetime.now().isoformat(),
      )

  def stream_query(
    self,
    graph_id: str,
    cypher: str,
    parameters: Dict[str, Any] = None,
    chunk_size: int = 1000,
    on_progress: Optional[Callable[[int, int], None]] = None,
  ) -> Generator[Any, None, None]:
    """Stream query results for large datasets with progress tracking

    Args:
        graph_id: Graph ID to query
        cypher: Cypher query string
        parameters: Query parameters
        chunk_size: Number of records per chunk
        on_progress: Callback for progress updates (current, total)

    Yields:
        Individual records from query results

    Example:
        >>> def progress(current, total):
        ...     print(f"Processed {current}/{total} records")
        >>> for record in query_client.stream_query(
        ...     'graph_id',
        ...     'MATCH (n) RETURN n',
        ...     chunk_size=100,
        ...     on_progress=progress
        ... ):
        ...     process_record(record)
    """
    request = QueryRequest(query=cypher, parameters=parameters)
    result = self.execute_query(
      graph_id, request, QueryOptions(mode="stream", chunk_size=chunk_size)
    )

    count = 0
    if isinstance(result, Iterator):
      for item in result:
        count += 1
        if on_progress and count % chunk_size == 0:
          on_progress(count, None)  # Total unknown in streaming
        yield item
    else:
      # If not streaming, yield all results at once
      total = len(result.data)
      for item in result.data:
        count += 1
        if on_progress:
          on_progress(count, total)
        yield item

  def query_batch(
    self,
    graph_id: str,
    queries: List[str],
    parameters_list: Optional[List[Dict[str, Any]]] = None,
    parallel: bool = False,
  ) -> List[Union[QueryResult, Dict[str, Any]]]:
    """Execute multiple queries in batch

    Args:
        graph_id: Graph ID to query
        queries: List of Cypher query strings
        parameters_list: List of parameter dicts (one per query)
        parallel: Execute queries in parallel (experimental)

    Returns:
        List of QueryResult objects or error dicts

    Example:
        >>> results = query_client.query_batch('graph_id', [
        ...     'MATCH (n:Person) RETURN count(n)',
        ...     'MATCH (c:Company) RETURN count(c)'
        ... ])
    """
    if parameters_list is None:
      parameters_list = [None] * len(queries)

    if len(queries) != len(parameters_list):
      raise ValueError("queries and parameters_list must have same length")

    results = []
    for query, params in zip(queries, parameters_list):
      try:
        result = self.query(graph_id, query, params)
        results.append(result)
      except Exception as e:
        # Store error as result
        results.append({"error": str(e), "query": query})

    return results

  def close(self):
    """Cancel any active SSE connections"""
    if self.sse_client:
      self.sse_client.close()
      self.sse_client = None


class AsyncQueryClient:
  """Async version of the query client"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.sse_client: Optional[AsyncSSEClient] = None

  async def execute_query(
    self, graph_id: str, request: QueryRequest, options: QueryOptions = None
  ) -> Union[QueryResult, AsyncIterator[Any]]:
    """Execute a query asynchronously"""
    # Similar implementation to sync version but with async/await
    # Would need async version of the generated client
    pass

  async def query(
    self, graph_id: str, cypher: str, parameters: Dict[str, Any] = None
  ) -> QueryResult:
    """Async convenience method for simple queries"""
    pass

  async def stream_query(
    self,
    graph_id: str,
    cypher: str,
    parameters: Dict[str, Any] = None,
    chunk_size: int = 1000,
  ) -> AsyncIterator[Any]:
    """Async streaming query for large results"""
    pass

  async def close(self):
    """Cancel any active SSE connections"""
    if self.sse_client:
      await self.sse_client.close()
      self.sse_client = None
