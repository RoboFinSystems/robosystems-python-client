"""Enhanced Query Client with SSE support

Provides intelligent query execution with automatic strategy selection.
"""

import json
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

from ..api.query.execute_cypher import sync_detailed as execute_cypher_query
from ..api.query.execute_cypher import asyncio_detailed as execute_cypher_query_async
from ..models.cypher_statement_request import CypherStatementRequest
from ..client import Client
from .retry import retrying_client
from .sse_client import (
  SSEClient,
  AsyncSSEClient,
  SSEConfig,
  EventType,
  event_error_message,
)
from .token_utils import has_auth_header, resolve_auth_headers, resolve_config_token
from ..types import UNSET


def _status_code(response: Any) -> Optional[int]:
  """The HTTP status of a generated-client response, when it carries one."""
  code = getattr(response, "status_code", None)
  return int(code) if isinstance(code, int) else None


def _json_body(response: Any) -> Optional[Dict[str, Any]]:
  """The raw JSON body of a response as a dict, or ``None``."""
  content = getattr(response, "content", None)
  if not isinstance(content, (bytes, str)) or not content:
    return None
  try:
    body = json.loads(content)
  except ValueError:
    return None
  return body if isinstance(body, dict) else None


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


class _QueryFailed(Exception):
  """A definitive answer from the endpoint that is not a result: raised as is."""


def _cypher_kwargs(
  graph_id: str, client: Any, body: CypherStatementRequest, options: QueryOptions
) -> Dict[str, Any]:
  return {
    "graph_id": graph_id,
    "client": client,
    "body": body,
    "mode": options.mode if options.mode else None,
    "chunk_size": options.chunk_size if options.chunk_size else 1000,
    "test_mode": options.test_mode if options.test_mode else False,
  }


def _wrap_query_error(error: Exception) -> Exception:
  error_msg = str(error)
  if "401" in error_msg or "403" in error_msg or "unauthorized" in error_msg.lower():
    return Exception(f"Authentication failed during query execution: {error_msg}")
  return Exception(f"Query execution failed: {error_msg}")


def _notify_queued(queued: QueuedQueryResponse, options: QueryOptions) -> None:
  """Report the queue position, and stop here when the caller will not wait."""
  if options.on_queue_update:
    options.on_queue_update(queued.queue_position, queued.estimated_wait_seconds)
  if options.max_wait == 0:
    raise QueuedQueryError(queued)


def _interpret_response(
  response: Any, graph_id: str
) -> Union[QueryResult, QueuedQueryResponse]:
  """Classify a `/query/cypher` response: a result, or a queued query.

  Raises :class:`_QueryFailed` for an error status or an unreadable body.
  """
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
    return _parse_ndjson_response(response, graph_id)

  # A queued query answers 202, which the generated parser yields as None;
  # its body (operation id, queue position) is on the raw response.
  data = getattr(response, "parsed", None)
  if data is None and _status_code(response) == 202:
    data = _json_body(response)

  if data:
    if isinstance(data, dict):
      if "data" in data and "columns" in data:
        return QueryResult(
          data=data["data"],
          columns=data["columns"],
          row_count=data.get("row_count", len(data["data"])),
          execution_time_ms=data.get("execution_time_ms", 0),
          graph_id=graph_id,
          timestamp=data.get("timestamp", datetime.now().isoformat()),
        )
      if data.get("status") == "queued" and "operation_id" in data:
        return QueuedQueryResponse(
          status=data["status"],
          operation_id=data["operation_id"],
          queue_position=data.get("queue_position", 0),
          estimated_wait_seconds=data.get("estimated_wait_seconds", 0),
          message=data.get("message", "Query queued"),
        )
    elif hasattr(data, "data") and hasattr(data, "columns"):
      # attrs object - access attributes directly
      raw_data = data.data if data.data is not UNSET else []
      result_data = []
      for item in raw_data:
        if hasattr(item, "to_dict"):
          result_data.append(item.to_dict())
        elif hasattr(item, "additional_properties"):
          result_data.append(item.additional_properties)
        else:
          result_data.append(item)
      return QueryResult(
        data=result_data,
        columns=data.columns if data.columns is not UNSET else [],
        row_count=data.row_count if data.row_count is not UNSET else len(result_data),
        execution_time_ms=(
          data.execution_time_ms if data.execution_time_ms is not UNSET else 0
        ),
        graph_id=graph_id,
        timestamp=(
          data.timestamp if data.timestamp is not UNSET else datetime.now().isoformat()
        ),
      )
    elif (
      hasattr(data, "status")
      and hasattr(data, "operation_id")
      and getattr(data, "status", None) == "queued"
    ):
      return QueuedQueryResponse(
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

  # Error responses (4xx/5xx)
  code = _status_code(response)
  if code is not None and code >= 400:
    detail: Any = f"HTTP {code}"
    try:
      body = (
        response.content.decode("utf-8")
        if isinstance(response.content, bytes)
        else str(response.content)
      )
      error_data = json.loads(body)
      detail = error_data.get("detail", error_data.get("message", body))
    except Exception:
      pass
    raise _QueryFailed(f"Query failed ({code}): {detail}")

  raise _QueryFailed("Unexpected response format from query endpoint")


def _parse_ndjson_response(response: Any, graph_id: str) -> QueryResult:
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


class QueryClient:
  """Enhanced query client with SSE streaming support"""

  def __init__(self, config: Dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    # Get token from config if passed by parent
    self.token = config.get("token")
    self.sse_client: Optional[SSEClient] = None

  def _rest_client(self) -> Client:
    """A REST client for one call, carrying the credential current now."""
    if not resolve_config_token(self.config):
      raise Exception("No API key provided. Set X-API-Key in headers.")
    return retrying_client(
      base_url=self.base_url,
      headers=resolve_auth_headers(self.config),
      config=self.config,
    )

  def _sse_config(self) -> SSEConfig:
    """Stream config for one connect; headers carry the credential current now."""
    return SSEConfig(base_url=self.base_url, headers=resolve_auth_headers(self.config))

  def execute_query(
    self, graph_id: str, request: QueryRequest, options: QueryOptions = None
  ) -> Union[QueryResult, Iterator[Any]]:
    """Execute a query with intelligent strategy selection"""
    if options is None:
      options = QueryOptions()

    # Build request data
    query_request = CypherStatementRequest(
      query=request.query, parameters=request.parameters or {}
    )

    # Execute the query through the generated client, with the credential
    # current now (`token_provider` wins over the static token).
    client = self._rest_client()

    try:
      response = execute_cypher_query(
        **_cypher_kwargs(graph_id, client, query_request, options)
      )
      outcome = _interpret_response(response, graph_id)
      if isinstance(outcome, QueryResult):
        return outcome

      _notify_queued(outcome, options)
      if options.mode == "stream":
        return self._stream_query_results(outcome.operation_id, options)
      return self._wait_for_query_completion(outcome.operation_id, options)

    except (QueuedQueryError, _QueryFailed):
      raise
    except Exception as e:
      raise _wrap_query_error(e) from e

  def _parse_ndjson_response(self, response, graph_id: str) -> QueryResult:
    """Parse NDJSON streaming response and aggregate into QueryResult"""
    return _parse_ndjson_response(response, graph_id)

  def _stream_query_results(
    self, operation_id: str, options: QueryOptions
  ) -> Iterator[Any]:
    """Stream query results using SSE"""
    buffer = []
    completed = False
    error = None

    # Set up SSE connection; headers resolved per connect so a rotated JWT
    # reaches the stream.
    self.sse_client = SSEClient(self._sse_config())

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
      # Terminal events carry dicts; a stream that could not open (or whose
      # reconnects ran out) emits the transport Exception itself.
      nonlocal error, completed
      error = err if isinstance(err, Exception) else Exception(event_error_message(err))
      completed = True

    # Register event handlers
    self.sse_client.on(EventType.DATA_CHUNK.value, on_data_chunk)
    self.sse_client.on(EventType.QUEUE_UPDATE.value, on_queue_update)
    self.sse_client.on(EventType.OPERATION_PROGRESS.value, on_progress)
    self.sse_client.on(EventType.OPERATION_COMPLETED.value, on_completed)
    self.sse_client.on(EventType.OPERATION_ERROR.value, on_error)
    # Transport failures (bad status, retries exhausted) must end the wait too.
    self.sse_client.on("error", on_error)
    self.sse_client.on("max_retries_exceeded", on_error)

    # Connect and start streaming. connect() is blocking: the stream has
    # ended (or never opened) by the time it returns.
    self.sse_client.connect(operation_id)

    # No terminal event means no verdict — say so rather than spin below.
    if not completed and error is None:
      error = Exception(
        f"Query stream for operation {operation_id} ended before a result"
      )
      completed = True
    if error is not None:
      self.sse_client.close()
      self.sse_client = None
      raise error

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

    # Set up SSE connection. Headers carry the auth SSEClient.connect merges in;
    # omitting them made this stream anonymous, so every queued query 401'd.
    # Resolved per connect so a rotated JWT reaches the stream.
    sse_client = SSEClient(self._sse_config())

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
      # Terminal events carry dicts; a stream that could not open (or whose
      # reconnects ran out) emits the transport Exception itself.
      nonlocal error, completed
      error = err if isinstance(err, Exception) else Exception(event_error_message(err))
      completed = True

    def on_cancelled(_data=None):
      nonlocal error, completed
      error = Exception("Query cancelled")
      completed = True

    # Register event handlers
    sse_client.on(EventType.QUEUE_UPDATE.value, on_queue_update)
    sse_client.on(EventType.OPERATION_PROGRESS.value, on_progress)
    sse_client.on(EventType.OPERATION_COMPLETED.value, on_completed)
    sse_client.on(EventType.OPERATION_ERROR.value, on_error)
    sse_client.on(EventType.OPERATION_CANCELLED.value, on_cancelled)
    # Transport failures (bad status, retries exhausted) must end the wait too.
    sse_client.on("error", on_error)
    sse_client.on("max_retries_exceeded", on_error)

    # Connect and wait. connect() is blocking: the stream has ended (or
    # never opened) by the time it returns, so the verdict is in by now.
    try:
      sse_client.connect(operation_id)
    finally:
      sse_client.close()

    if error is not None:
      raise error
    if result is None:
      # No terminal event means no verdict — say so rather than return None.
      raise Exception(
        f"Query stream for operation {operation_id} ended before a result"
      )
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
    self.headers = config.get("headers", {})
    self.token = config.get("token")
    self.sse_client: Optional[AsyncSSEClient] = None

  def _rest_client(self) -> Client:
    """A REST client for one call, carrying the credential current now."""
    headers = resolve_auth_headers(self.config)
    if not has_auth_header(headers):
      raise Exception("No API key provided. Set X-API-Key in headers.")
    return Client(base_url=self.base_url, headers=headers)

  def _sse_config(self) -> SSEConfig:
    """Stream config for one connect; headers carry the credential current now."""
    return SSEConfig(base_url=self.base_url, headers=resolve_auth_headers(self.config))

  async def execute_query(
    self, graph_id: str, request: QueryRequest, options: QueryOptions = None
  ) -> Union[QueryResult, AsyncIterator[Any]]:
    """Execute a query asynchronously.

    Same contract as :meth:`QueryClient.execute_query`: a result, or for a
    queued query (202) the SSE-followed result — an async iterator of rows
    under ``mode="stream"``.
    """
    if options is None:
      options = QueryOptions()

    query_request = CypherStatementRequest(
      query=request.query, parameters=request.parameters or {}
    )

    try:
      async with self._rest_client() as client:
        response = await execute_cypher_query_async(
          **_cypher_kwargs(graph_id, client, query_request, options)
        )
      outcome = _interpret_response(response, graph_id)
      if isinstance(outcome, QueryResult):
        return outcome

      _notify_queued(outcome, options)
      if options.mode == "stream":
        return self._stream_query_results(outcome.operation_id, options)
      return await self._wait_for_query_completion(outcome.operation_id, options)

    except (QueuedQueryError, _QueryFailed):
      raise
    except Exception as e:
      raise _wrap_query_error(e) from e

  async def _follow(self, operation_id: str, options: QueryOptions) -> Dict[str, Any]:
    """Follow a queued query's stream to its end; the verdict and any rows."""
    state: Dict[str, Any] = {"rows": [], "result": None, "error": None}

    def on_data_chunk(data):
      if isinstance(data.get("rows"), list):
        state["rows"].extend(data["rows"])
      elif isinstance(data.get("data"), list):
        state["rows"].extend(data["data"])

    def on_queue_update(data):
      if options.on_queue_update:
        options.on_queue_update(
          data.get("position", 0), data.get("estimated_wait_seconds", 0)
        )

    def on_progress(data):
      if options.on_progress:
        options.on_progress(data.get("message", "Processing..."))

    def on_completed(data):
      state["result"] = data.get("result", data) or {}

    def on_error(err):
      state["error"] = (
        err if isinstance(err, Exception) else Exception(event_error_message(err))
      )

    def on_cancelled(_data=None):
      state["error"] = Exception("Query cancelled")

    sse_client = AsyncSSEClient(self._sse_config())
    self.sse_client = sse_client
    sse_client.on(EventType.DATA_CHUNK.value, on_data_chunk)
    sse_client.on(EventType.QUEUE_UPDATE.value, on_queue_update)
    sse_client.on(EventType.OPERATION_PROGRESS.value, on_progress)
    sse_client.on(EventType.OPERATION_COMPLETED.value, on_completed)
    sse_client.on(EventType.OPERATION_ERROR.value, on_error)
    sse_client.on(EventType.OPERATION_CANCELLED.value, on_cancelled)
    sse_client.on("error", on_error)
    sse_client.on("max_retries_exceeded", on_error)

    # connect() returns once the stream has ended (or never opened).
    try:
      await sse_client.connect(operation_id)
    finally:
      await sse_client.close()
      if self.sse_client is sse_client:
        self.sse_client = None

    if state["error"] is not None:
      raise state["error"]
    if state["result"] is None:
      raise Exception(
        f"Query stream for operation {operation_id} ended before a result"
      )
    return state

  async def _wait_for_query_completion(
    self, operation_id: str, options: QueryOptions
  ) -> QueryResult:
    """Wait for a queued query's completion and return its result."""
    state = await self._follow(operation_id, options)
    query_result = state["result"]
    return QueryResult(
      data=query_result.get("data", []),
      columns=query_result.get("columns", []),
      row_count=query_result.get("row_count", 0),
      execution_time_ms=query_result.get("execution_time_ms", 0),
      graph_id=query_result.get("graph_id"),
      timestamp=query_result.get("timestamp", datetime.now().isoformat()),
    )

  async def _stream_query_results(
    self, operation_id: str, options: QueryOptions
  ) -> AsyncIterator[Any]:
    """Yield a queued query's rows once its stream has ended."""
    state = await self._follow(operation_id, options)
    for item in state["rows"]:
      yield item
    for item in state["result"].get("data") or []:
      yield item

  async def query(
    self, graph_id: str, cypher: str, parameters: Dict[str, Any] = None
  ) -> QueryResult:
    """Async convenience method for simple queries"""
    request = QueryRequest(query=cypher, parameters=parameters)
    result = await self.execute_query(graph_id, request, QueryOptions(mode="auto"))
    if isinstance(result, QueryResult):
      return result
    data = [item async for item in result]
    return QueryResult(
      data=data,
      columns=[],
      row_count=len(data),
      execution_time_ms=0,
      graph_id=graph_id,
      timestamp=datetime.now().isoformat(),
    )

  async def stream_query(
    self,
    graph_id: str,
    cypher: str,
    parameters: Dict[str, Any] = None,
    chunk_size: int = 1000,
  ) -> AsyncIterator[Any]:
    """Async streaming query for large results.

    Rows are yielded once the query's stream has ended — the same
    buffering :meth:`QueryClient.stream_query` does — or straight from the
    result when the query answered inline.
    """
    request = QueryRequest(query=cypher, parameters=parameters)
    result = await self.execute_query(
      graph_id, request, QueryOptions(mode="stream", chunk_size=chunk_size)
    )
    if isinstance(result, QueryResult):
      for item in result.data:
        yield item
    else:
      async for item in result:
        yield item

  async def close(self):
    """Cancel any active SSE connections"""
    if self.sse_client:
      await self.sse_client.close()
      self.sse_client = None
