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
    from ..client import AuthenticatedClient

    # Create authenticated client with X-API-Key
    if not self.token:
      raise Exception("No API key provided. Set X-API-Key in headers.")

    client = AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

    try:
      kwargs = {
        "graph_id": graph_id,
        "client": client,
        "body": query_request,
        "mode": options.mode if options.mode else None,
        "chunk_size": options.chunk_size if options.chunk_size else 1000,
        "test_mode": options.test_mode if options.test_mode else False,
      }
      response = execute_cypher_query(**kwargs)

      # Check if this is an NDJSON streaming response (parsed will be None for NDJSON)
      if (
        hasattr(response, "headers")
        and (
          "application/x-ndjson" in response.headers.get("content-type", "")
          or response.headers.get("x-stream-format") == "ndjson"
        )
      ) or (
        hasattr(response, "parsed")
        and response.parsed is None
        and response.status_code == 200
      ):
        return self._parse_ndjson_response(response, graph_id)

      # Check response type and handle accordingly
      if hasattr(response, "parsed") and response.parsed:
        response_data = response.parsed

        # Handle both dict and attrs object responses
        if isinstance(response_data, dict):
          # Response is a plain dict
          data = response_data
          has_data = "data" in data and "columns" in data
        else:
          # Response is an attrs object - check for attributes directly
          data = response_data
          has_data = hasattr(data, "data") and hasattr(data, "columns")

        # Check if this is an immediate response
        if has_data:
          # Extract data from either dict or attrs object
          if isinstance(data, dict):
            result_data = data["data"]
            result_columns = data["columns"]
            result_row_count = data.get("row_count", len(data["data"]))
            result_execution_time = data.get("execution_time_ms", 0)
            result_timestamp = data.get("timestamp", datetime.now().isoformat())
          else:
            # attrs object - access attributes directly
            from ..types import UNSET

            raw_data = data.data if data.data is not UNSET else []
            # Convert data items to dicts if they're objects
            result_data = []
            for item in raw_data:
              if hasattr(item, "to_dict"):
                result_data.append(item.to_dict())
              elif hasattr(item, "additional_properties"):
                result_data.append(item.additional_properties)
              else:
                result_data.append(item)
            result_columns = data.columns if data.columns is not UNSET else []
            result_row_count = (
              data.row_count if data.row_count is not UNSET else len(result_data)
            )
            result_execution_time = (
              data.execution_time_ms if data.execution_time_ms is not UNSET else 0
            )
            result_timestamp = (
              data.timestamp
              if data.timestamp is not UNSET
              else datetime.now().isoformat()
            )

          return QueryResult(
            data=result_data,
            columns=result_columns,
            row_count=result_row_count,
            execution_time_ms=result_execution_time,
            graph_id=graph_id,
            timestamp=result_timestamp,
          )

        # Check if this is a queued response
        is_queued = False
        queued_response = None

        if isinstance(data, dict):
          is_queued = data.get("status") == "queued" and "operation_id" in data
          if is_queued:
            queued_response = QueuedQueryResponse(
              status=data["status"],
              operation_id=data["operation_id"],
              queue_position=data.get("queue_position", 0),
              estimated_wait_seconds=data.get("estimated_wait_seconds", 0),
              message=data.get("message", "Query queued"),
            )
        else:
          is_queued = (
            hasattr(data, "status")
            and hasattr(data, "operation_id")
            and getattr(data, "status", None) == "queued"
          )
          if is_queued:
            from ..types import UNSET

            queued_response = QueuedQueryResponse(
              status=data.status,
              operation_id=data.operation_id,
              queue_position=data.queue_position
              if hasattr(data, "queue_position") and data.queue_position is not UNSET
              else 0,
              estimated_wait_seconds=data.estimated_wait_seconds
              if hasattr(data, "estimated_wait_seconds")
              and data.estimated_wait_seconds is not UNSET
              else 0,
              message=data.message
              if hasattr(data, "message") and data.message is not UNSET
              else "Query queued",
            )

        if is_queued and queued_response:
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

  def _parse_ndjson_response(self, response, graph_id: str) -> QueryResult:
    """Parse NDJSON streaming response and aggregate into QueryResult"""
    import json

    all_data = []
    columns = None
    total_rows = 0
    execution_time_ms = 0

    # Parse NDJSON line by line
    content = (
      response.content.decode("utf-8")
      if isinstance(response.content, bytes)
      else response.content
    )

    for line in content.strip().split("\n"):
      if not line.strip():
        continue

      try:
        chunk = json.loads(line)

        # Extract columns from first chunk
        if columns is None and "columns" in chunk:
          columns = chunk["columns"]

        # Aggregate data rows (NDJSON uses "rows", regular JSON uses "data")
        if "rows" in chunk:
          all_data.extend(chunk["rows"])
          total_rows += len(chunk["rows"])
        elif "data" in chunk:
          all_data.extend(chunk["data"])
          total_rows += len(chunk["data"])

        # Track execution time (use max from all chunks)
        if "execution_time_ms" in chunk:
          execution_time_ms = max(execution_time_ms, chunk["execution_time_ms"])

      except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse NDJSON line: {e}")

    # Return aggregated result
    return QueryResult(
      data=all_data,
      columns=columns or [],
      row_count=total_rows,
      execution_time_ms=execution_time_ms,
      graph_id=graph_id,
      timestamp=datetime.now().isoformat(),
    )

  def _stream_query_results(
    self, operation_id: str, options: QueryOptions
  ) -> Iterator[Any]:
    """Stream query results using SSE"""
    buffer = []
    completed = False
    error = None

    # Set up SSE connection
    sse_config = SSEConfig(base_url=self.base_url, headers=self.headers)
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
    parameters_list: Optional[List[Optional[Dict[str, Any]]]] = None,
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
      # Create a list of None values for each query
      parameters_list = [None for _ in queries]

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
