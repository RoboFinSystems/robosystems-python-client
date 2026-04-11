"""Unit tests for QueryClient operational logic.

Covers: execute_query (sync dict response, attrs response, queued response,
NDJSON streaming, error handling), _parse_ndjson_response,
_wait_for_query_completion, query convenience, query_batch, stream_query.

Dataclass tests already exist in tests/test_query_client.py.
"""

import pytest
from unittest.mock import Mock, patch
from robosystems_client.extensions.query_client import (
  QueryClient,
  QueryRequest,
  QueryOptions,
  QueryResult,
  QueuedQueryError,
)


# ── execute_query — sync dict response ───────────────────────────────


@pytest.mark.unit
class TestExecuteQuerySync:
  """Test execute_query with immediate sync responses."""

  @patch("robosystems_client.extensions.query_client.execute_cypher_query")
  def test_dict_response(self, mock_exec, mock_config, graph_id):
    """Test execute_query with a dict response."""
    mock_resp = Mock()
    mock_resp.parsed = {
      "data": [{"name": "ACME"}],
      "columns": ["name"],
      "row_count": 1,
      "execution_time_ms": 42,
      "timestamp": "2025-01-15T10:00:00Z",
    }
    # No NDJSON headers
    mock_resp.headers = {"content-type": "application/json"}
    mock_resp.status_code = 200
    mock_exec.return_value = mock_resp

    client = QueryClient(mock_config)
    request = QueryRequest(query="MATCH (n) RETURN n.name")
    result = client.execute_query(graph_id, request)

    assert isinstance(result, QueryResult)
    assert result.data == [{"name": "ACME"}]
    assert result.columns == ["name"]
    assert result.row_count == 1
    assert result.execution_time_ms == 42
    assert result.graph_id == graph_id

  @patch("robosystems_client.extensions.query_client.execute_cypher_query")
  def test_attrs_response(self, mock_exec, mock_config, graph_id):
    """Test execute_query with an attrs object response."""
    mock_data_item = Mock()
    mock_data_item.to_dict.return_value = {"name": "Beta Corp"}

    mock_parsed = Mock()
    mock_parsed.data = [mock_data_item]
    mock_parsed.columns = ["name"]
    mock_parsed.row_count = 1
    mock_parsed.execution_time_ms = 30
    mock_parsed.timestamp = "2025-01-15T10:00:00Z"

    mock_resp = Mock()
    mock_resp.parsed = mock_parsed
    mock_resp.headers = {"content-type": "application/json"}
    mock_resp.status_code = 200
    mock_exec.return_value = mock_resp

    client = QueryClient(mock_config)
    request = QueryRequest(query="MATCH (n) RETURN n.name")
    result = client.execute_query(graph_id, request)

    assert isinstance(result, QueryResult)
    assert result.data == [{"name": "Beta Corp"}]

  @patch("robosystems_client.extensions.query_client.execute_cypher_query")
  def test_attrs_with_additional_properties(self, mock_exec, mock_config, graph_id):
    """Test attrs response items using additional_properties fallback."""
    mock_data_item = Mock(spec=[])
    mock_data_item.additional_properties = {"ticker": "ACM"}
    # No to_dict method

    mock_parsed = Mock()
    mock_parsed.data = [mock_data_item]
    mock_parsed.columns = ["ticker"]
    mock_parsed.row_count = 1
    mock_parsed.execution_time_ms = 10
    mock_parsed.timestamp = "2025-01-15T10:00:00Z"

    mock_resp = Mock()
    mock_resp.parsed = mock_parsed
    mock_resp.headers = {"content-type": "application/json"}
    mock_resp.status_code = 200
    mock_exec.return_value = mock_resp

    client = QueryClient(mock_config)
    request = QueryRequest(query="MATCH (n) RETURN n.ticker")
    result = client.execute_query(graph_id, request)

    assert result.data == [{"ticker": "ACM"}]


# ── execute_query — queued response ──────────────────────────────────


@pytest.mark.unit
class TestExecuteQueryQueued:
  """Test execute_query with queued responses."""

  @patch("robosystems_client.extensions.query_client.execute_cypher_query")
  def test_queued_max_wait_zero_raises(self, mock_exec, mock_config, graph_id):
    """Test queued response with max_wait=0 raises QueuedQueryError."""
    mock_resp = Mock()
    mock_resp.parsed = {
      "status": "queued",
      "operation_id": "op-q1",
      "queue_position": 3,
      "estimated_wait_seconds": 15,
      "message": "Query queued",
    }
    mock_resp.headers = {"content-type": "application/json"}
    mock_resp.status_code = 200
    mock_exec.return_value = mock_resp

    client = QueryClient(mock_config)
    request = QueryRequest(query="MATCH (n) RETURN n")
    options = QueryOptions(max_wait=0)

    with pytest.raises(QueuedQueryError) as exc_info:
      client.execute_query(graph_id, request, options)

    assert exc_info.value.queue_info.operation_id == "op-q1"
    assert exc_info.value.queue_info.queue_position == 3

  @patch("robosystems_client.extensions.query_client.execute_cypher_query")
  def test_queued_calls_queue_update_callback(self, mock_exec, mock_config, graph_id):
    """Test queued response invokes on_queue_update."""
    mock_resp = Mock()
    mock_resp.parsed = {
      "status": "queued",
      "operation_id": "op-q2",
      "queue_position": 5,
      "estimated_wait_seconds": 30,
      "message": "Queued",
    }
    mock_resp.headers = {"content-type": "application/json"}
    mock_resp.status_code = 200
    mock_exec.return_value = mock_resp

    queue_updates = []
    options = QueryOptions(
      max_wait=0,
      on_queue_update=lambda pos, wait: queue_updates.append((pos, wait)),
    )

    client = QueryClient(mock_config)
    request = QueryRequest(query="MATCH (n) RETURN n")

    with pytest.raises(QueuedQueryError):
      client.execute_query(graph_id, request, options)

    assert queue_updates == [(5, 30)]


# ── execute_query — error handling ───────────────────────────────────


@pytest.mark.unit
class TestExecuteQueryErrors:
  """Test error handling in execute_query."""

  def test_no_token_raises(self, mock_config, graph_id):
    """Test execute_query fails without token."""
    mock_config["token"] = None
    client = QueryClient(mock_config)
    request = QueryRequest(query="MATCH (n) RETURN n")

    with pytest.raises(Exception, match="Authentication failed|No API key"):
      client.execute_query(graph_id, request)

  @patch("robosystems_client.extensions.query_client.execute_cypher_query")
  def test_auth_error_wrapped(self, mock_exec, mock_config, graph_id):
    """Test 401/403 errors are wrapped as auth errors."""
    mock_exec.side_effect = Exception("401 Unauthorized")

    client = QueryClient(mock_config)
    request = QueryRequest(query="MATCH (n) RETURN n")

    with pytest.raises(Exception, match="Authentication failed"):
      client.execute_query(graph_id, request)

  @patch("robosystems_client.extensions.query_client.execute_cypher_query")
  def test_generic_error_wrapped(self, mock_exec, mock_config, graph_id):
    """Test generic errors are wrapped."""
    mock_exec.side_effect = Exception("Connection timeout")

    client = QueryClient(mock_config)
    request = QueryRequest(query="MATCH (n) RETURN n")

    with pytest.raises(Exception, match="Query execution failed"):
      client.execute_query(graph_id, request)

  @patch("robosystems_client.extensions.query_client.execute_cypher_query")
  def test_http_error_response(self, mock_exec, mock_config, graph_id):
    """Test HTTP 4xx/5xx with error body."""
    mock_resp = Mock()
    mock_resp.parsed = None
    mock_resp.status_code = 400
    mock_resp.headers = {"content-type": "application/json"}
    mock_resp.content = b'{"detail": "Invalid query syntax"}'
    mock_exec.return_value = mock_resp

    client = QueryClient(mock_config)
    request = QueryRequest(query="BAD QUERY")

    with pytest.raises(Exception, match="Invalid query syntax"):
      client.execute_query(graph_id, request)


# ── NDJSON parsing ───────────────────────────────────────────────────


@pytest.mark.unit
class TestNDJSON:
  """Test _parse_ndjson_response."""

  def test_single_chunk(self, mock_config, graph_id):
    """Test parsing a single NDJSON chunk."""
    content = '{"columns": ["name"], "rows": [["ACME"]], "execution_time_ms": 10}\n'

    mock_resp = Mock()
    mock_resp.content = content.encode()

    client = QueryClient(mock_config)
    result = client._parse_ndjson_response(mock_resp, graph_id)

    assert result.columns == ["name"]
    assert result.data == [["ACME"]]
    assert result.row_count == 1
    assert result.execution_time_ms == 10

  def test_multiple_chunks(self, mock_config, graph_id):
    """Test parsing multiple NDJSON chunks."""
    content = (
      '{"columns": ["id"], "rows": [[1], [2]], "execution_time_ms": 5}\n'
      '{"rows": [[3], [4]], "execution_time_ms": 12}\n'
    )

    mock_resp = Mock()
    mock_resp.content = content.encode()

    client = QueryClient(mock_config)
    result = client._parse_ndjson_response(mock_resp, graph_id)

    assert result.columns == ["id"]
    assert result.data == [[1], [2], [3], [4]]
    assert result.row_count == 4
    assert result.execution_time_ms == 12  # max of 5, 12

  def test_data_key_fallback(self, mock_config, graph_id):
    """Test NDJSON with 'data' key instead of 'rows'."""
    content = '{"columns": ["x"], "data": [{"x": 1}], "execution_time_ms": 3}\n'

    mock_resp = Mock()
    mock_resp.content = content.encode()

    client = QueryClient(mock_config)
    result = client._parse_ndjson_response(mock_resp, graph_id)

    assert result.data == [{"x": 1}]

  def test_empty_lines_skipped(self, mock_config, graph_id):
    """Test that empty lines in NDJSON are skipped."""
    content = '{"columns": ["a"], "rows": [[1]]}\n\n\n'

    mock_resp = Mock()
    mock_resp.content = content.encode()

    client = QueryClient(mock_config)
    result = client._parse_ndjson_response(mock_resp, graph_id)

    assert result.row_count == 1

  def test_invalid_json_raises(self, mock_config, graph_id):
    """Test invalid JSON in NDJSON raises error."""
    content = "not json at all\n"

    mock_resp = Mock()
    mock_resp.content = content.encode()

    client = QueryClient(mock_config)

    with pytest.raises(Exception, match="Failed to parse NDJSON"):
      client._parse_ndjson_response(mock_resp, graph_id)

  def test_no_columns_defaults_to_empty(self, mock_config, graph_id):
    """Test NDJSON without columns field defaults to empty list."""
    content = '{"rows": [[1]]}\n'

    mock_resp = Mock()
    mock_resp.content = content.encode()

    client = QueryClient(mock_config)
    result = client._parse_ndjson_response(mock_resp, graph_id)

    assert result.columns == []


# ── NDJSON detection in execute_query ────────────────────────────────


@pytest.mark.unit
class TestNDJSONDetection:
  """Test that NDJSON responses are detected and parsed."""

  @patch("robosystems_client.extensions.query_client.execute_cypher_query")
  def test_ndjson_content_type_detected(self, mock_exec, mock_config, graph_id):
    """Test NDJSON response detected by content-type header."""
    mock_resp = Mock()
    mock_resp.parsed = None
    mock_resp.status_code = 200
    mock_resp.headers = {"content-type": "application/x-ndjson"}
    mock_resp.content = b'{"columns": ["n"], "rows": [["x"]]}\n'
    mock_exec.return_value = mock_resp

    client = QueryClient(mock_config)
    request = QueryRequest(query="MATCH (n) RETURN n")
    result = client.execute_query(graph_id, request)

    assert isinstance(result, QueryResult)
    assert result.data == [["x"]]

  @patch("robosystems_client.extensions.query_client.execute_cypher_query")
  def test_ndjson_stream_format_header(self, mock_exec, mock_config, graph_id):
    """Test NDJSON detected by x-stream-format header."""
    mock_resp = Mock()
    mock_resp.parsed = None
    mock_resp.status_code = 200
    mock_resp.headers = {
      "content-type": "application/json",
      "x-stream-format": "ndjson",
    }
    mock_resp.content = b'{"columns": ["a"], "rows": [[1]]}\n'
    mock_exec.return_value = mock_resp

    client = QueryClient(mock_config)
    request = QueryRequest(query="MATCH (n) RETURN n")
    result = client.execute_query(graph_id, request)

    assert result.data == [[1]]


# ── query convenience ────────────────────────────────────────────────


@pytest.mark.unit
class TestQueryConvenience:
  """Test query() convenience method."""

  @patch.object(QueryClient, "execute_query")
  def test_query_returns_result(self, mock_exec, mock_config, graph_id):
    """Test query() returns QueryResult directly."""
    mock_exec.return_value = QueryResult(
      data=[{"n": 1}], columns=["n"], row_count=1, execution_time_ms=5
    )

    client = QueryClient(mock_config)
    result = client.query(graph_id, "MATCH (n) RETURN n")

    assert result.row_count == 1

  @patch.object(QueryClient, "execute_query")
  def test_query_collects_iterator(self, mock_exec, mock_config, graph_id):
    """Test query() collects iterator results into QueryResult."""
    mock_exec.return_value = iter([{"n": 1}, {"n": 2}])

    client = QueryClient(mock_config)
    result = client.query(graph_id, "MATCH (n) RETURN n")

    assert result.row_count == 2
    assert result.data == [{"n": 1}, {"n": 2}]

  @patch.object(QueryClient, "execute_query")
  def test_query_passes_parameters(self, mock_exec, mock_config, graph_id):
    """Test query() forwards parameters."""
    mock_exec.return_value = QueryResult(
      data=[], columns=[], row_count=0, execution_time_ms=0
    )

    client = QueryClient(mock_config)
    client.query(graph_id, "MATCH (n) WHERE n.x > $v RETURN n", {"v": 10})

    call_args = mock_exec.call_args
    assert call_args[0][1].parameters == {"v": 10}


# ── query_batch ──────────────────────────────────────────────────────


@pytest.mark.unit
class TestQueryBatch:
  """Test query_batch method."""

  @patch.object(QueryClient, "query")
  def test_batch_success(self, mock_query, mock_config, graph_id):
    """Test batch execution of multiple queries."""
    mock_query.side_effect = [
      QueryResult(
        data=[{"count": 5}], columns=["count"], row_count=1, execution_time_ms=10
      ),
      QueryResult(
        data=[{"count": 3}], columns=["count"], row_count=1, execution_time_ms=8
      ),
    ]

    client = QueryClient(mock_config)
    results = client.query_batch(
      graph_id,
      ["MATCH (n:Person) RETURN count(n)", "MATCH (c:Company) RETURN count(c)"],
    )

    assert len(results) == 2
    assert all(isinstance(r, QueryResult) for r in results)

  @patch.object(QueryClient, "query")
  def test_batch_with_error(self, mock_query, mock_config, graph_id):
    """Test batch handles individual query failures."""
    mock_query.side_effect = [
      QueryResult(data=[], columns=[], row_count=0, execution_time_ms=0),
      Exception("Query 2 failed"),
    ]

    client = QueryClient(mock_config)
    results = client.query_batch(graph_id, ["query1", "query2"])

    assert isinstance(results[0], QueryResult)
    assert isinstance(results[1], dict)
    assert "error" in results[1]

  def test_batch_length_mismatch(self, mock_config, graph_id):
    """Test batch raises on mismatched query/params lengths."""
    client = QueryClient(mock_config)

    with pytest.raises(ValueError, match="same length"):
      client.query_batch(graph_id, ["q1", "q2"], [{"a": 1}])

  @patch.object(QueryClient, "query")
  def test_batch_with_parameters(self, mock_query, mock_config, graph_id):
    """Test batch passes parameters per query."""
    mock_query.return_value = QueryResult(
      data=[], columns=[], row_count=0, execution_time_ms=0
    )

    client = QueryClient(mock_config)
    client.query_batch(
      graph_id,
      ["MATCH (n) WHERE n.x > $v RETURN n", "MATCH (n) WHERE n.y = $w RETURN n"],
      [{"v": 10}, {"w": "abc"}],
    )

    assert mock_query.call_count == 2
    assert mock_query.call_args_list[0][0][2] == {"v": 10}
    assert mock_query.call_args_list[1][0][2] == {"w": "abc"}


# ── stream_query ─────────────────────────────────────────────────────


@pytest.mark.unit
class TestStreamQuery:
  """Test stream_query method."""

  @patch.object(QueryClient, "execute_query")
  def test_stream_yields_from_iterator(self, mock_exec, mock_config, graph_id):
    """Test stream_query yields items from iterator result."""
    mock_exec.return_value = iter([{"id": 1}, {"id": 2}, {"id": 3}])

    client = QueryClient(mock_config)
    items = list(client.stream_query(graph_id, "MATCH (n) RETURN n"))

    assert items == [{"id": 1}, {"id": 2}, {"id": 3}]

  @patch.object(QueryClient, "execute_query")
  def test_stream_yields_from_query_result(self, mock_exec, mock_config, graph_id):
    """Test stream_query yields items when result is QueryResult."""
    mock_exec.return_value = QueryResult(
      data=[{"id": 1}, {"id": 2}],
      columns=["id"],
      row_count=2,
      execution_time_ms=10,
    )

    client = QueryClient(mock_config)
    items = list(client.stream_query(graph_id, "MATCH (n) RETURN n"))

    assert items == [{"id": 1}, {"id": 2}]

  @patch.object(QueryClient, "execute_query")
  def test_stream_calls_progress(self, mock_exec, mock_config, graph_id):
    """Test stream_query calls on_progress callback."""
    mock_exec.return_value = QueryResult(
      data=[{"id": i} for i in range(5)],
      columns=["id"],
      row_count=5,
      execution_time_ms=10,
    )

    progress_calls = []
    client = QueryClient(mock_config)
    list(
      client.stream_query(
        graph_id,
        "MATCH (n) RETURN n",
        on_progress=lambda cur, tot: progress_calls.append((cur, tot)),
      )
    )

    assert len(progress_calls) == 5
    assert progress_calls[-1] == (5, 5)
