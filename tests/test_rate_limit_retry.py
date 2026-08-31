"""Unit tests for the 429 replay behavior shared by every facade.

The API answers an exhausted category budget with 429 from a request
dependency that runs before the endpoint handler, so the rejected call
had no effect and replaying it is safe. A bulk backfill loop — a year of
history through per-event writes — sits at the category budget for
minutes, and before this the rejections surfaced to callers as ordinary
failures.
"""

import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Iterator

import httpx
import pytest

from robosystems_client.clients.ledger_client import LedgerClient
from robosystems_client.clients.operation_client import OperationClient
from robosystems_client.clients.query_client import QueryClient
from robosystems_client.clients.retry import (
  RetryingClient,
  backoff_seconds,
  retry_after_seconds,
  retrying_authenticated_client,
  retrying_client,
)


class _Stub:
  """A server that rejects the first ``fail_first`` requests with 429."""

  def __init__(self, fail_first: int, body: bytes = b"{}") -> None:
    self.calls = 0
    self.paths: list[str] = []
    self.fail_first = fail_first
    self.body = body
    stub = self

    class Handler(BaseHTTPRequestHandler):
      def _respond(self) -> None:
        stub.calls += 1
        stub.paths.append(self.path)
        length = int(self.headers.get("content-length", 0))
        if length:
          _ = self.rfile.read(length)
        if stub.calls <= stub.fail_first:
          payload = b'{"detail":"Rate limit exceeded for extensions write operations."}'
          self.send_response(429)
          # The window, not a usable delay — see backoff_seconds.
          self.send_header("Retry-After", "60")
          self.send_header("Content-Type", "application/json")
          self.send_header("Content-Length", str(len(payload)))
          self.end_headers()
          _ = self.wfile.write(payload)
          return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(stub.body)))
        self.end_headers()
        _ = self.wfile.write(stub.body)

      do_GET = _respond
      do_POST = _respond

      def log_message(self, *args: Any) -> None:
        pass

    self._server = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=self._server.serve_forever, daemon=True).start()

  @property
  def base_url(self) -> str:
    return f"http://127.0.0.1:{self._server.server_port}"

  def close(self) -> None:
    self._server.shutdown()


@pytest.fixture
def stub() -> Iterator[_Stub]:
  server = _Stub(fail_first=0)
  yield server
  server.close()


@pytest.mark.unit
class TestBackoff:
  def test_retry_after_is_a_ceiling_not_the_sleep(self):
    # The limiter is a sliding window, so Retry-After reports the whole
    # window. Obeying it literally turns a few rejections into minutes.
    assert backoff_seconds(0, 1000, 60.0) <= 1.0
    assert backoff_seconds(4, 1000, 2.0) <= 2.0

  def test_backoff_grows_but_stays_bounded(self):
    assert backoff_seconds(0, 1000, None) <= 1.0
    assert backoff_seconds(4, 1000, None) <= 16.0
    assert backoff_seconds(20, 1000, None) <= 30.0

  def test_retry_after_parsing(self):
    def response(value: str | None):
      headers = httpx.Headers({"Retry-After": value} if value is not None else {})
      return type("R", (), {"headers": headers})()

    assert retry_after_seconds(response("60")) == 60.0
    assert retry_after_seconds(response(None)) is None
    # The HTTP-date form is ignored rather than mis-parsed.
    assert retry_after_seconds(response("Wed, 21 Oct 2026 07:28:00 GMT")) is None


@pytest.mark.unit
class TestRetryingClient:
  def test_replays_until_accepted(self, stub: _Stub):
    stub.fail_first = 3
    with RetryingClient(max_retries=5, retry_delay_ms=1) as client:
      response = client.post(f"{stub.base_url}/x", json={"event": "invoice_issued"})

    assert response.status_code == 200
    assert stub.calls == 4

  def test_surfaces_the_429_once_retries_are_exhausted(self, stub: _Stub):
    stub.fail_first = 99
    with RetryingClient(max_retries=2, retry_delay_ms=1) as client:
      response = client.post(f"{stub.base_url}/x", json={})

    assert response.status_code == 429
    assert stub.calls == 3
    assert "Rate limit exceeded" in response.text

  def test_zero_retries_sends_once(self, stub: _Stub):
    stub.fail_first = 99
    with RetryingClient(max_retries=0, retry_delay_ms=1) as client:
      response = client.post(f"{stub.base_url}/x", json={})

    assert response.status_code == 429
    assert stub.calls == 1

  def test_streamed_body_is_not_replayed(self, stub: _Stub):
    # httpx leaves a streaming body unread, so the first attempt consumes
    # it and a replay would post nothing.
    stub.fail_first = 99

    def body() -> Iterator[bytes]:
      yield b'{"a": 1}'

    with RetryingClient(max_retries=3, retry_delay_ms=1) as client:
      response = client.post(f"{stub.base_url}/x", content=body())

    assert response.status_code == 429
    assert stub.calls == 1

  def test_other_statuses_are_returned_untouched(self, stub: _Stub):
    stub.fail_first = 0
    with RetryingClient(max_retries=5, retry_delay_ms=1) as client:
      response = client.get(f"{stub.base_url}/x")

    assert response.status_code == 200
    assert stub.calls == 1


@pytest.mark.unit
class TestFacadeWiring:
  def test_authenticated_client_carries_the_credential_and_retries(self, stub: _Stub):
    stub.fail_first = 2
    client = retrying_authenticated_client(
      base_url=stub.base_url,
      token="rfs_test",
      headers={"X-Trace": "1"},
      config={"max_retries": 5, "retry_delay": 1},
    )
    http = client.get_httpx_client()
    response = http.post("/x", json={})

    assert response.status_code == 200
    assert stub.calls == 3
    assert http.headers["X-API-Key"] == "rfs_test"
    assert http.headers["X-Trace"] == "1"

  def test_ledger_write_survives_a_rate_limit_burst(self, stub: _Stub):
    # The end-to-end shape the demo backfill hits: create-event-block
    # rejected mid-loop, then accepted on replay.
    stub.fail_first = 2
    stub.body = (
      b'{"operation": "create-event-block", "operationId": "op_1",'
      b' "status": "completed", "at": "2026-02-12T00:00:00+00:00",'
      b' "result": {"id": "evt_1", "event_type": "invoice_issued",'
      b' "event_category": "sales", "status": "posted",'
      b' "occurred_at": "2026-02-12T00:00:00+00:00", "source": "manual",'
      b' "currency": "USD", "metadata": {}, "dimension_ids": [],'
      b' "event_class": "economic",'
      b' "created_at": "2026-02-12T00:00:00+00:00", "created_by": "demo"}}'
    )
    ledger = LedgerClient(
      {
        "base_url": stub.base_url,
        "token": "rfs_test",
        "headers": {},
        "max_retries": 5,
        "retry_delay": 1,
      }
    )

    result = ledger.create_event_block(
      "kg_test",
      {
        "event_type": "invoice_issued",
        "event_category": "sales",
        "source": "manual",
        "occurred_at": "2026-02-12T00:00:00+00:00",
        "metadata": {"memo": "demo"},
      },
    )

    assert stub.calls == 3
    assert result.id == "evt_1"
    assert all(p.endswith("/operations/create-event-block") for p in stub.paths)


@pytest.mark.unit
class TestUnauthenticatedFacadeWiring:
  """The facades that resolve their own credential and pass it in headers.

  query / operator / operations build a plain ``Client`` rather than an
  ``AuthenticatedClient``, so they were missed by the first pass. Their
  endpoints carry their own category budgets — Cypher queries, operator
  runs, operation-status polls — and need the same replay.
  """

  def test_plain_client_retries_and_keeps_its_headers(self, stub: _Stub):
    stub.fail_first = 2
    client = retrying_client(
      base_url=stub.base_url,
      headers={"X-API-Key": "rfs_test", "X-Trace": "1"},
      config={"max_retries": 5, "retry_delay": 1},
    )
    http = client.get_httpx_client()
    response = http.post("/x", json={})

    assert response.status_code == 200
    assert stub.calls == 3
    assert http.headers["X-API-Key"] == "rfs_test"
    assert http.headers["X-Trace"] == "1"

  def test_operation_status_poll_survives_a_rate_limit_burst(self, stub: _Stub):
    # Polling a long-running operation in a loop is exactly the shape
    # that exhausts a category budget.
    #
    # Asserts the replay, not the returned payload: `get_operation_status`
    # reads `parsed.status` off a model that only carries
    # `additional_properties`, so it raises AttributeError on every
    # response and its `except Exception` shapes that into
    # `{"status": "error"}`. That defect predates this change and is
    # deliberately untouched here — `operator_client._poll_for_completion`
    # shows the working pattern (`parsed.to_dict()`).
    stub.fail_first = 2
    stub.body = b'{"operation_id": "op_1", "status": "completed", "progress": 100}'
    client = OperationClient(
      {
        "base_url": stub.base_url,
        "token": "rfs_test",
        "headers": {},
        "max_retries": 5,
        "retry_delay": 1,
      }
    )

    client.get_operation_status("op_1")

    assert stub.calls == 3
    assert all(p.endswith("/v1/operations/op_1/status") for p in stub.paths)

  def test_query_client_builds_a_retrying_rest_client(self, stub: _Stub):
    client = QueryClient(
      {
        "base_url": stub.base_url,
        "token": "rfs_test",
        "headers": {},
        "max_retries": 3,
        "retry_delay": 1,
      }
    )
    http = client._rest_client().get_httpx_client()

    assert isinstance(http, RetryingClient)
    assert http.headers["X-API-Key"] == "rfs_test"
