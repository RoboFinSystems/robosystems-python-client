"""Unit tests for QueryClient's SSE-backed waits.

The stream's terminal events carry dicts, but a stream that cannot open (a
revoked JWT answers 401) or whose reconnects run out emits the transport
Exception itself. Handlers that assumed a dict raised inside `emit` — which
only logs — and left the wait loop spinning forever with no verdict.
"""

from unittest.mock import MagicMock, patch

import pytest

from robosystems_client.clients.query_client import QueryClient, QueryOptions
from robosystems_client.clients.sse_client import SSEClient


def _fake_sse(script):
  fake = MagicMock(spec=SSEClient)
  listeners = {}
  fake.on.side_effect = lambda event, handler: listeners.__setitem__(event, handler)
  fake.connect.side_effect = lambda op_id: script(listeners)
  return fake


@pytest.mark.unit
@patch("time.sleep")
@patch("robosystems_client.clients.query_client.SSEClient")
class TestWaitForQueryCompletion:
  def test_completed_event_returns_result(self, MockSSE, mock_sleep, mock_config):
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["operation_completed"](
        {"result": {"data": [{"n": 1}], "columns": ["n"], "row_count": 1}}
      )
    )

    result = QueryClient(mock_config)._wait_for_query_completion("op-1", QueryOptions())

    assert result.data == [{"n": 1}]
    assert result.columns == ["n"]

  def test_transport_error_object_raises_instead_of_hanging(
    self, MockSSE, mock_sleep, mock_config
  ):
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["error"](RuntimeError("SSE connection failed: HTTP 401"))
    )

    with pytest.raises(RuntimeError, match="HTTP 401"):
      QueryClient(mock_config)._wait_for_query_completion("op-1", QueryOptions())

  def test_retries_exhausted_raises(self, MockSSE, mock_sleep, mock_config):
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["max_retries_exceeded"](ConnectionError("connection reset"))
    )

    with pytest.raises(ConnectionError, match="connection reset"):
      QueryClient(mock_config)._wait_for_query_completion("op-1", QueryOptions())

  def test_stream_ending_without_verdict_raises(self, MockSSE, mock_sleep, mock_config):
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["operation_progress"]({"message": "Working"})
    )

    with pytest.raises(Exception, match="ended before a result"):
      QueryClient(mock_config)._wait_for_query_completion("op-1", QueryOptions())

  def test_cancelled_event_raises(self, MockSSE, mock_sleep, mock_config):
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["operation_cancelled"]({"message": "Cancelled by user"})
    )

    with pytest.raises(Exception, match="Query cancelled"):
      QueryClient(mock_config)._wait_for_query_completion("op-1", QueryOptions())

  def test_stream_headers_resolved_from_provider_at_connect(
    self, MockSSE, mock_sleep, mock_config
  ):
    current = {"jwt": "jwt-old"}
    config = {
      **mock_config,
      "headers": {"Authorization": "Bearer jwt-old"},
      "token": "jwt-old",
      "token_provider": lambda: current["jwt"],
    }
    client = QueryClient(config)
    current["jwt"] = "jwt-rotated"
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["operation_completed"]({"result": {"data": []}})
    )

    client._wait_for_query_completion("op-1", QueryOptions())

    assert MockSSE.call_args[0][0].headers == {"Authorization": "Bearer jwt-rotated"}


@pytest.mark.unit
@patch("time.sleep")
@patch("robosystems_client.clients.query_client.SSEClient")
class TestStreamQueryResults:
  def test_yields_buffered_rows(self, MockSSE, mock_sleep, mock_config):
    MockSSE.return_value = _fake_sse(
      lambda ls: (
        ls["data_chunk"]({"rows": [{"n": 1}, {"n": 2}]}),
        ls["operation_completed"]({"result": {}}),
      )
    )

    rows = list(QueryClient(mock_config)._stream_query_results("op-1", QueryOptions()))

    assert rows == [{"n": 1}, {"n": 2}]

  def test_transport_error_object_raises_instead_of_hanging(
    self, MockSSE, mock_sleep, mock_config
  ):
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["error"](RuntimeError("SSE connection failed: HTTP 401"))
    )

    with pytest.raises(RuntimeError, match="HTTP 401"):
      list(QueryClient(mock_config)._stream_query_results("op-1", QueryOptions()))

  def test_stream_ending_without_verdict_raises(self, MockSSE, mock_sleep, mock_config):
    MockSSE.return_value = _fake_sse(lambda ls: None)

    with pytest.raises(Exception, match="ended before a result"):
      list(QueryClient(mock_config)._stream_query_results("op-1", QueryOptions()))
