"""Unit tests for OperatorClient queued-run handling.

Covers: following a queued run over the SSE stream, per-connect credential
resolution (token_provider), and the `/status` polling fallback that takes
over when the stream gives no verdict — it never opened (a revoked JWT
answers 401), its reconnects ran out, or it ended before a terminal event.

Dataclass and sync-response tests live in tests/test_operator_client.py.
"""

from http import HTTPStatus
from unittest.mock import MagicMock, Mock, patch

import pytest

from robosystems_client.clients.operator_client import (
  OperatorClient,
  OperatorOptions,
  OperatorQueryRequest,
)
from robosystems_client.clients.sse_client import SSEClient


COMPLETED_RESULT = {
  "content": "Burn is ~$1,500/month.",
  "operator_used": "analyst",
  "mode_used": "standard",
  "metadata": {"sources": ["ledger"]},
  "tokens_used": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
  "execution_time": 21.2,
}


def _queued(operation_id: str = "op-1") -> Mock:
  resp = Mock()
  resp.parsed = {"operation_id": operation_id, "status": "queued", "message": "Queued"}
  return resp


def _status(code: int, payload=None, detail: str = "") -> Mock:
  """A generated-client `Response` for `/status`: `parsed.to_dict()` is the body."""
  resp = Mock()
  resp.status_code = HTTPStatus(code)
  resp.content = detail.encode()
  parsed = Mock()
  parsed.to_dict = Mock(return_value=payload or {})
  parsed.detail = detail
  resp.parsed = parsed
  return resp


def _fake_sse(script):
  """A mocked SSEClient whose connect() fires `script(listeners)`."""
  fake = MagicMock(spec=SSEClient)
  listeners = {}
  fake.on.side_effect = lambda event, handler: listeners.__setitem__(event, handler)
  fake.connect.side_effect = lambda op_id: script(listeners)
  return fake


def _run(client, graph_id, options=None):
  return client.execute_query(
    graph_id, OperatorQueryRequest(message="burn rate?"), options
  )


@pytest.mark.unit
@patch("time.sleep")
@patch("robosystems_client.clients.operator_client.get_operation_status")
@patch("robosystems_client.clients.operator_client.SSEClient")
@patch("robosystems_client.clients.operator_client.auto_select_operator")
class TestOperatorQueuedRuns:
  def test_stream_completion_returns_result(
    self, mock_auto, MockSSE, mock_status, mock_sleep, mock_config, graph_id
  ):
    mock_auto.return_value = _queued()
    MockSSE.return_value = _fake_sse(
      lambda ls: (
        ls["operation_progress"]({"message": "Working", "percentage": 40}),
        ls["operation_completed"]({"message": "done", "result": COMPLETED_RESULT}),
      )
    )
    progress = []

    result = _run(
      OperatorClient(mock_config),
      graph_id,
      OperatorOptions(on_progress=lambda m, p: progress.append((m, p))),
    )

    assert result.content == COMPLETED_RESULT["content"]
    assert result.operator_used == "analyst"
    assert result.execution_time == 21.2
    assert result.error_details is None
    assert progress == [("Working", 40)]
    # The stream delivered the verdict — no polling.
    mock_status.assert_not_called()

  def test_stream_headers_resolved_from_provider_at_connect(
    self, mock_auto, MockSSE, mock_status, mock_sleep, mock_config, graph_id
  ):
    current = {"jwt": "jwt-captured"}
    config = {
      **mock_config,
      "headers": {"Authorization": "Bearer jwt-captured"},
      "token": "jwt-captured",
      "token_provider": lambda: current["jwt"],
    }
    client = OperatorClient(config)
    # The session rotates after construction, before the run is submitted.
    current["jwt"] = "jwt-rotated"
    mock_auto.return_value = _queued()
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["operation_completed"]({"result": COMPLETED_RESULT})
    )

    _run(client, graph_id)

    sse_config = MockSSE.call_args[0][0]
    assert sse_config.headers == {"Authorization": "Bearer jwt-rotated"}
    rest_client = mock_auto.call_args.kwargs["client"]
    assert rest_client._headers["Authorization"] == "Bearer jwt-rotated"

  def test_stream_that_cannot_open_falls_back_to_status_polling(
    self, mock_auto, MockSSE, mock_status, mock_sleep, mock_config, graph_id
  ):
    mock_auto.return_value = _queued()
    # A 401 on the stream URL surfaces as the transport Exception itself.
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["error"](RuntimeError("SSE connection failed: HTTP 401"))
    )
    mock_status.side_effect = [
      _status(
        200, {"status": "running", "message": "Operation is currently executing"}
      ),
      _status(200, {"status": "completed", "result": COMPLETED_RESULT}),
    ]
    progress = []

    result = _run(
      OperatorClient(mock_config),
      graph_id,
      OperatorOptions(on_progress=lambda m, p: progress.append(m), poll_interval=0),
    )

    assert result.content == COMPLETED_RESULT["content"]
    assert result.operator_used == "analyst"
    assert mock_status.call_count == 2
    assert mock_status.call_args.kwargs["operation_id"] == "op-1"
    assert progress == [
      "Live progress unavailable — waiting for the result",
      "Operation is currently executing",
    ]

  def test_stream_ending_without_verdict_falls_back_to_polling(
    self, mock_auto, MockSSE, mock_status, mock_sleep, mock_config, graph_id
  ):
    mock_auto.return_value = _queued()
    # Progress arrived, then the stream ended with no terminal event.
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["operation_progress"]({"message": "Working"})
    )
    mock_status.return_value = _status(
      200, {"status": "completed", "result": COMPLETED_RESULT}
    )

    result = _run(
      OperatorClient(mock_config), graph_id, OperatorOptions(poll_interval=0)
    )

    assert result.content == COMPLETED_RESULT["content"]
    mock_status.assert_called_once()

  def test_run_error_event_raises_without_polling(
    self, mock_auto, MockSSE, mock_status, mock_sleep, mock_config, graph_id
  ):
    mock_auto.return_value = _queued()
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["operation_error"]({"message": "model timeout"})
    )

    with pytest.raises(Exception, match="model timeout"):
      _run(OperatorClient(mock_config), graph_id)
    mock_status.assert_not_called()

  def test_cancelled_event_raises_without_hanging(
    self, mock_auto, MockSSE, mock_status, mock_sleep, mock_config, graph_id
  ):
    mock_auto.return_value = _queued()
    # The stream dispatches cancellation with a payload, like every event.
    MockSSE.return_value = _fake_sse(
      lambda ls: ls["operation_cancelled"]({"message": "Cancelled by user"})
    )

    with pytest.raises(Exception, match="cancelled"):
      _run(OperatorClient(mock_config), graph_id)
    mock_status.assert_not_called()

  def test_polling_surfaces_failed_run(
    self, mock_auto, MockSSE, mock_status, mock_sleep, mock_config, graph_id
  ):
    mock_auto.return_value = _queued()
    MockSSE.return_value = _fake_sse(lambda ls: ls["error"](RuntimeError("HTTP 401")))
    mock_status.return_value = _status(
      200, {"status": "failed", "error": "Operator run failed: model timeout"}
    )

    with pytest.raises(Exception, match="model timeout"):
      _run(OperatorClient(mock_config), graph_id, OperatorOptions(poll_interval=0))

  def test_polling_stops_on_definitive_4xx(
    self, mock_auto, MockSSE, mock_status, mock_sleep, mock_config, graph_id
  ):
    mock_auto.return_value = _queued()
    MockSSE.return_value = _fake_sse(lambda ls: ls["error"](RuntimeError("HTTP 401")))
    mock_status.return_value = _status(
      404, detail="Operation not found. It may have expired or been cancelled."
    )

    with pytest.raises(Exception, match=r"404: Operation not found"):
      _run(OperatorClient(mock_config), graph_id, OperatorOptions(poll_interval=0))
    # A definitive answer is not retried.
    mock_status.assert_called_once()

  def test_polling_rides_out_transient_failure(
    self, mock_auto, MockSSE, mock_status, mock_sleep, mock_config, graph_id
  ):
    mock_auto.return_value = _queued()
    MockSSE.return_value = _fake_sse(lambda ls: ls["error"](RuntimeError("HTTP 401")))
    mock_status.side_effect = [
      ConnectionError("network down"),
      _status(503, detail="upstream unavailable"),
      _status(200, {"status": "completed", "result": COMPLETED_RESULT}),
    ]

    result = _run(
      OperatorClient(mock_config), graph_id, OperatorOptions(poll_interval=0)
    )

    assert result.content == COMPLETED_RESULT["content"]
    assert mock_status.call_count == 3

  def test_polling_gives_up_after_repeated_failures(
    self, mock_auto, MockSSE, mock_status, mock_sleep, mock_config, graph_id
  ):
    mock_auto.return_value = _queued()
    MockSSE.return_value = _fake_sse(lambda ls: ls["error"](RuntimeError("HTTP 401")))
    mock_status.side_effect = ConnectionError("network down")

    with pytest.raises(Exception, match=r"status polling failed \(network down\)"):
      _run(OperatorClient(mock_config), graph_id, OperatorOptions(poll_interval=0))
    assert mock_status.call_count == 3


@pytest.mark.unit
class TestOperatorSyncResponse:
  @patch("robosystems_client.clients.operator_client.auto_select_operator")
  def test_error_details_pass_through(self, mock_auto, mock_config, graph_id):
    resp = Mock()
    resp.parsed = {
      "content": "Not enough credits to perform AI analysis",
      "operator_used": "analyst",
      "mode_used": "standard",
      "error_details": {
        "code": "INSUFFICIENT_CREDITS",
        "message": "Not enough credits",
      },
    }
    mock_auto.return_value = resp

    result = _run(OperatorClient(mock_config), graph_id)

    assert result.error_details == {
      "code": "INSUFFICIENT_CREDITS",
      "message": "Not enough credits",
    }

  @patch("robosystems_client.clients.operator_client.auto_select_operator")
  def test_rest_client_uses_provider_credential(self, mock_auto, mock_config, graph_id):
    config = {
      **mock_config,
      "headers": {"X-API-Key": "stale"},
      "token": "stale",
      "token_provider": lambda: "rfs_fresh",
    }
    resp = Mock()
    resp.parsed = {"content": "ok", "operator_used": "analyst", "mode_used": "quick"}
    mock_auto.return_value = resp

    _run(OperatorClient(config), graph_id)

    rest_client = mock_auto.call_args.kwargs["client"]
    assert rest_client._headers == {"X-API-Key": "rfs_fresh"}
