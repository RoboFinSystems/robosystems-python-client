"""Facade behaviour against the API's real responses.

Each test answers the facade with the status code and JSON body the server
actually sends (`robosystems` routers, cited per test), through the real
generated `api/` parsers — mocked 200s are how a 202 the generated layer
parses as ``None``, or a body shape the facade misread, went unnoticed.
"""

import json
import re

import pytest

from robosystems_client.clients import OperatorRunError
from robosystems_client.clients.auth_integration import AuthenticatedClients
from robosystems_client.clients.facade import (
  AsyncRoboSystemsClients,
  RoboSystemsClientConfig,
)
from robosystems_client.clients.file_client import FileClient
from robosystems_client.clients.graph_client import GraphClient
from robosystems_client.clients.ledger_client import LedgerClient
from robosystems_client.clients.operation_client import (
  AsyncOperationClient,
  MonitorOptions,
  OperationClient,
  OperationStatus,
)
from robosystems_client.clients.operator_client import (
  OperatorClient,
  OperatorOptions,
  OperatorQueryRequest,
  QueuedOperatorError,
)
from robosystems_client.clients.query_client import (
  AsyncQueryClient,
  QueryClient,
  QueryOptions,
  QueryRequest,
  QueryResult,
  QueuedQueryError,
)
from robosystems_client.clients.table_client import TableClient

BASE = "http://localhost:8000"
GRAPH = "kg_test"
OP = "op_01J0000000000000000000000A"
CONFIG = {"base_url": BASE, "token": "rfs_test", "headers": {}, "max_retries": 1}


def _sse(*events: tuple[str, dict]) -> bytes:
  return "".join(
    f"id: {i}\nevent: {name}\ndata: {json.dumps(data)}\n\n"
    for i, (name, data) in enumerate(events)
  ).encode()


def _stream_url(op_id: str = OP) -> re.Pattern:
  return re.compile(rf"{BASE}/v1/operations/{op_id}/stream\?from_sequence=\d+")


# Body of `enqueue_task` / `create_operation_response` — what the operator
# endpoint returns with its 202 (routers/graphs/operator/execute.py `_dispatch`).
OPERATOR_QUEUED = {
  "operation_id": OP,
  "status": "pending",
  "operation_type": "operator",
  "created_at": "2026-10-05T00:00:00+00:00",
  "graph_id": GRAPH,
  "_links": {
    "stream": f"/v1/operations/{OP}/stream",
    "status": f"/v1/operations/{OP}/status",
    "cancel": f"/v1/operations/{OP}",
  },
  "message": "Operation operator queued. Connect to stream endpoint for real-time updates.",
}

OPERATOR_RESULT = {
  "content": "Burn is ~$1,500/month.",
  "operator_used": "analyst",
  "mode_used": "standard",
  "metadata": {},
  "execution_time": 2.1,
}

# routers/graphs/query/execute.py — the queued 202.
QUERY_QUEUED = {
  "status": "queued",
  "query_id": "q_1",
  "operation_id": OP,
  "queue_position": 2,
  "estimated_wait_seconds": 10,
  "message": "Query has been queued for execution",
  "_links": {"self": "...", "monitor": f"/v1/operations/{OP}/stream"},
}

QUERY_ROWS = {
  "data": [{"n": 1}],
  "columns": ["n"],
  "row_count": 1,
  "execution_time_ms": 5,
  "graph_id": GRAPH,
}

OPERATOR_URL = re.compile(rf"{BASE}/v1/graphs/{GRAPH}/operator(\?.*)?$")
QUERY_URL = re.compile(rf"{BASE}/v1/graphs/{GRAPH}/query/cypher(\?.*)?$")


# ── Operator runs ────────────────────────────────────────────────────


@pytest.mark.unit
class TestOperatorQueuedRun:
  def test_202_is_followed_over_the_stream(self, httpx_mock):
    httpx_mock.add_response(
      method="POST", url=OPERATOR_URL, status_code=202, json=OPERATOR_QUEUED
    )
    httpx_mock.add_response(
      url=_stream_url(),
      headers={"content-type": "text/event-stream"},
      content=_sse(
        ("operation_progress", {"message": "Thinking", "progress_percent": 40}),
        ("operation_completed", {"message": "done", "result": OPERATOR_RESULT}),
      ),
    )
    progress = []

    result = OperatorClient(CONFIG).execute_query(
      GRAPH,
      OperatorQueryRequest(message="burn?"),
      OperatorOptions(on_progress=lambda msg, pct: progress.append((msg, pct))),
    )

    assert result.content == "Burn is ~$1,500/month."
    assert result.operator_used == "analyst"
    assert ("Thinking", 40) in progress

  def test_specific_operator_202_is_followed(self, httpx_mock):
    httpx_mock.add_response(
      method="POST",
      url=f"{BASE}/v1/graphs/{GRAPH}/operator/analyst?mode=auto",
      status_code=202,
      json=OPERATOR_QUEUED,
    )
    httpx_mock.add_response(
      url=_stream_url(),
      content=_sse(("operation_completed", {"result": OPERATOR_RESULT})),
    )

    result = OperatorClient(CONFIG).execute_operator(
      GRAPH, "analyst", OperatorQueryRequest(message="burn?")
    )

    assert result.operator_used == "analyst"

  def test_202_with_max_wait_zero_hands_back_the_links(self, httpx_mock):
    httpx_mock.add_response(
      method="POST", url=OPERATOR_URL, status_code=202, json=OPERATOR_QUEUED
    )

    with pytest.raises(QueuedOperatorError) as exc_info:
      OperatorClient(CONFIG).execute_query(
        GRAPH, OperatorQueryRequest(message="burn?"), OperatorOptions(max_wait=0)
      )

    info = exc_info.value.queue_info
    assert info.operation_id == OP
    assert info.status == "pending"
    assert info.sse_endpoint == f"/v1/operations/{OP}/stream"

  def test_failed_run_raises_operator_run_error_with_writes(self, httpx_mock):
    writes = [{"op": "create-event-block", "id": "evt_1"}]
    httpx_mock.add_response(
      method="POST", url=OPERATOR_URL, status_code=202, json=OPERATOR_QUEUED
    )
    httpx_mock.add_response(
      url=_stream_url(),
      content=_sse(
        (
          "operation_error",
          {"error": "Tool budget exhausted", "error_details": {"writes": writes}},
        )
      ),
    )

    with pytest.raises(OperatorRunError) as exc_info:
      OperatorClient(CONFIG).execute_query(GRAPH, OperatorQueryRequest(message="x"))

    err = exc_info.value
    assert str(err) == "Tool budget exhausted"
    assert err.status == "failed"
    assert err.writes == writes
    assert err.operation_id == OP

  def test_cancelled_run_raises_operator_run_error(self, httpx_mock):
    httpx_mock.add_response(
      method="POST", url=OPERATOR_URL, status_code=202, json=OPERATOR_QUEUED
    )
    httpx_mock.add_response(
      url=_stream_url(),
      content=_sse(("operation_cancelled", {"reason": "Cancelled by user request"})),
    )

    with pytest.raises(OperatorRunError) as exc_info:
      OperatorClient(CONFIG).execute_query(GRAPH, OperatorQueryRequest(message="x"))

    assert exc_info.value.status == "cancelled"

  def test_polled_failure_carries_writes(self, httpx_mock):
    writes = [{"op": "update-entity"}]
    httpx_mock.add_response(
      method="POST", url=OPERATOR_URL, status_code=202, json=OPERATOR_QUEUED
    )
    # The stream ends with no terminal event, so the run is followed over
    # `/status` — whose failed body carries the landed writes.
    httpx_mock.add_response(url=_stream_url(), content=b": keepalive\n\n")
    httpx_mock.add_response(
      url=f"{BASE}/v1/operations/{OP}/status",
      json={
        "operation_id": OP,
        "operation_type": "operator",
        "status": "failed",
        "error": "Operator crashed",
        "writes": writes,
        "_links": {"stream": f"/v1/operations/{OP}/stream"},
      },
    )

    with pytest.raises(OperatorRunError) as exc_info:
      OperatorClient(CONFIG).execute_query(
        GRAPH, OperatorQueryRequest(message="x"), OperatorOptions(poll_interval=0)
      )

    assert exc_info.value.writes == writes


@pytest.mark.unit
class TestOperatorSyncResponse:
  def test_sync_mode_is_sent_and_a_200_returns_the_result(self, httpx_mock):
    httpx_mock.add_response(
      method="POST",
      url=f"{BASE}/v1/graphs/{GRAPH}/operator?mode=sync",
      json={**OPERATOR_RESULT, "operation_id": OP, "is_partial": False},
    )

    result = OperatorClient(CONFIG).execute_query(
      GRAPH, OperatorQueryRequest(message="x"), OperatorOptions(mode="sync")
    )

    assert result.content == "Burn is ~$1,500/month."
    assert result.metadata == {}

  def test_cancelled_sync_run_returns_error_details(self, httpx_mock):
    # `_response_from_operation`: a cancelled run is a 200 whose
    # `error_details` describe it and whose `content` is the explanation.
    httpx_mock.add_response(
      method="POST",
      url=f"{BASE}/v1/graphs/{GRAPH}/operator?mode=sync",
      json={
        "content": "Operator run was cancelled",
        "operator_used": "analyst",
        "mode_used": "standard",
        "metadata": {},
        "error_details": {
          "code": "OPERATOR_CANCELLED",
          "message": "Operator run was cancelled",
        },
        "operation_id": OP,
        "is_partial": False,
      },
    )

    result = OperatorClient(CONFIG).execute_query(
      GRAPH, OperatorQueryRequest(message="x"), OperatorOptions(mode="sync")
    )

    assert result.content == "Operator run was cancelled"
    assert result.error_details == {
      "code": "OPERATOR_CANCELLED",
      "message": "Operator run was cancelled",
    }

  def test_402_reports_the_status(self, httpx_mock):
    httpx_mock.add_response(
      method="POST",
      url=OPERATOR_URL,
      status_code=402,
      json={"detail": {"code": "INSUFFICIENT_CREDITS"}},
    )

    with pytest.raises(Exception, match="Operator execution failed: 402"):
      OperatorClient(CONFIG).execute_query(GRAPH, OperatorQueryRequest(message="x"))


# ── Cypher queries ───────────────────────────────────────────────────


@pytest.mark.unit
class TestQueuedQuery:
  def test_202_is_followed_over_the_stream(self, httpx_mock):
    httpx_mock.add_response(
      method="POST", url=QUERY_URL, status_code=202, json=QUERY_QUEUED
    )
    httpx_mock.add_response(
      url=_stream_url(),
      content=_sse(("operation_completed", {"result": QUERY_ROWS})),
    )

    result = QueryClient(CONFIG).execute_query(GRAPH, QueryRequest(query="RETURN 1"))

    assert isinstance(result, QueryResult)
    assert result.data == [{"n": 1}]

  def test_202_with_max_wait_zero_raises_queued(self, httpx_mock):
    httpx_mock.add_response(
      method="POST", url=QUERY_URL, status_code=202, json=QUERY_QUEUED
    )
    positions = []

    with pytest.raises(QueuedQueryError) as exc_info:
      QueryClient(CONFIG).execute_query(
        GRAPH,
        QueryRequest(query="RETURN 1"),
        QueryOptions(max_wait=0, on_queue_update=lambda p, w: positions.append(p)),
      )

    assert exc_info.value.queue_info.operation_id == OP
    assert exc_info.value.queue_info.queue_position == 2
    assert positions == [2]

  def test_authenticated_clients_cypher_reads_the_dict_body(self, httpx_mock):
    httpx_mock.add_response(
      method="POST", url=QUERY_URL, json={"success": True, **QUERY_ROWS}
    )

    clients = AuthenticatedClients("rfs_test", base_url=BASE)
    result = clients.execute_cypher_query(GRAPH, "RETURN 1")

    assert result == {
      "data": [{"n": 1}],
      "columns": ["n"],
      "row_count": 1,
      "execution_time_ms": 5,
    }

  def test_authenticated_clients_cypher_follows_a_202(self, httpx_mock):
    httpx_mock.add_response(
      method="POST", url=QUERY_URL, status_code=202, json=QUERY_QUEUED
    )
    httpx_mock.add_response(
      url=_stream_url(),
      content=_sse(("operation_completed", {"result": QUERY_ROWS})),
    )

    clients = AuthenticatedClients("rfs_test", base_url=BASE)

    assert clients.execute_cypher_query(GRAPH, "RETURN 1")["data"] == [{"n": 1}]


# ── Async facade ─────────────────────────────────────────────────────


@pytest.mark.unit
class TestAsyncClients:
  @pytest.mark.asyncio
  async def test_async_query_200(self, httpx_mock):
    httpx_mock.add_response(
      method="POST", url=QUERY_URL, json={"success": True, **QUERY_ROWS}
    )

    clients = AsyncRoboSystemsClients(
      RoboSystemsClientConfig(base_url=BASE, headers={"X-API-Key": "rfs_test"})
    )
    result = await clients.execute_query(GRAPH, "RETURN 1")

    assert result.data == [{"n": 1}]
    assert httpx_mock.get_requests()[0].headers["X-API-Key"] == "rfs_test"

  @pytest.mark.asyncio
  async def test_async_query_202_is_followed(self, httpx_mock):
    httpx_mock.add_response(
      method="POST", url=QUERY_URL, status_code=202, json=QUERY_QUEUED
    )
    httpx_mock.add_response(
      url=_stream_url(),
      content=_sse(("operation_completed", {"result": QUERY_ROWS})),
    )

    client = AsyncQueryClient({**CONFIG})
    result = await client.query(GRAPH, "RETURN 1")

    assert result.data == [{"n": 1}]

  @pytest.mark.asyncio
  async def test_async_stream_query_yields_rows(self, httpx_mock):
    httpx_mock.add_response(
      method="POST", url=QUERY_URL, json={"success": True, **QUERY_ROWS}
    )

    clients = AsyncRoboSystemsClients(
      RoboSystemsClientConfig(base_url=BASE, headers={"X-API-Key": "rfs_test"})
    )
    rows = [row async for row in clients.stream_query(GRAPH, "RETURN 1")]

    assert rows == [{"n": 1}]

  @pytest.mark.asyncio
  async def test_async_operation_status_and_cancel(self, httpx_mock):
    httpx_mock.add_response(
      url=f"{BASE}/v1/operations/{OP}/status",
      json={"operation_id": OP, "operation_type": "operator", "status": "running"},
    )
    httpx_mock.add_response(
      method="DELETE",
      url=f"{BASE}/v1/operations/{OP}",
      json={
        "operation_id": OP,
        "status": "cancelled",
        "message": "Operation has been cancelled",
      },
    )

    client = AsyncOperationClient({**CONFIG})

    status = await client.get_operation_status(OP)
    assert status["status"] == "running"
    assert await client.cancel_operation(OP) is True


# ── Operations monitoring ────────────────────────────────────────────


@pytest.mark.unit
class TestOperationMonitoring:
  def test_cancelled_event_settles_the_monitor(self, httpx_mock):
    httpx_mock.add_response(
      url=_stream_url(),
      content=_sse(("operation_cancelled", {"reason": "Cancelled by user request"})),
    )

    result = OperationClient(CONFIG).monitor_operation(OP)

    assert result.status == OperationStatus.CANCELLED

  def test_stream_ending_without_a_verdict_raises(self, httpx_mock):
    httpx_mock.add_response(
      url=_stream_url(),
      content=_sse(
        ("operation_progress", {"message": "Working", "progress_percent": 5})
      ),
    )

    with pytest.raises(Exception, match="ended before a terminal event"):
      OperationClient(CONFIG).monitor_operation(OP)

  def test_progress_reads_progress_percent(self, httpx_mock):
    httpx_mock.add_response(
      url=_stream_url(),
      content=_sse(
        ("operation_progress", {"message": "Loading", "progress_percent": 55.0}),
        ("operation_completed", {"message": "done", "result": {"ok": True}}),
      ),
    )
    seen = []

    result = OperationClient(CONFIG).monitor_operation(
      OP, MonitorOptions(on_progress=seen.append)
    )

    assert result.status == OperationStatus.COMPLETED
    assert seen[0].percentage == 55.0

  def test_cancel_reads_the_status_field(self, httpx_mock):
    httpx_mock.add_response(
      method="DELETE",
      url=f"{BASE}/v1/operations/{OP}",
      json={
        "operation_id": OP,
        "status": "cancelled",
        "message": "Operation has been cancelled",
      },
    )

    assert OperationClient(CONFIG).cancel_operation(OP) is True


# ── Credential routing on writes ─────────────────────────────────────

EVENT_BLOCK_ENVELOPE = {
  "operation": "create-event-block",
  "operationId": "op_1",
  "status": "completed",
  "at": "2026-02-12T00:00:00+00:00",
  "result": {
    "id": "evt_1",
    "event_type": "asset_disposed",
    "event_category": "adjustment",
    "status": "posted",
    "occurred_at": "2026-02-12T00:00:00+00:00",
    "source": "manual",
    "currency": "USD",
    "metadata": {},
    "dimension_ids": [],
    "event_class": "economic",
    "created_at": "2026-02-12T00:00:00+00:00",
    "created_by": "u_1",
  },
}


@pytest.mark.unit
class TestWriteCredentialRouting:
  def test_jwt_from_token_provider_rides_as_bearer(self, httpx_mock):
    httpx_mock.add_response(
      method="POST",
      url=f"{BASE}/extensions/roboledger/{GRAPH}/operations/create-event-block",
      json=EVENT_BLOCK_ENVELOPE,
    )
    ledger = LedgerClient(
      {"base_url": BASE, "headers": {}, "token_provider": lambda: "eyJ.jwt.sig"}
    )

    ledger.dispose_schedule(GRAPH, "str_1", "2026-02-12")

    request = httpx_mock.get_requests()[0]
    assert request.headers["Authorization"] == "Bearer eyJ.jwt.sig"
    assert "X-API-Key" not in request.headers
    # memo / reason left out for the server's defaults
    assert json.loads(request.content)["metadata"] == {"schedule_id": "str_1"}

  def test_api_key_rides_as_x_api_key(self, httpx_mock):
    httpx_mock.add_response(
      method="POST",
      url=f"{BASE}/extensions/roboledger/{GRAPH}/operations/create-event-block",
      json=EVENT_BLOCK_ENVELOPE,
    )

    LedgerClient(CONFIG).dispose_schedule(
      GRAPH, "str_1", "2026-02-12", "Sold the truck", "sale"
    )

    request = httpx_mock.get_requests()[0]
    assert request.headers["X-API-Key"] == "rfs_test"
    assert "Authorization" not in request.headers
    assert json.loads(request.content)["metadata"] == {
      "schedule_id": "str_1",
      "memo": "Sold the truck",
      "reason": "sale",
    }

  def test_graph_client_honours_token_provider(self, httpx_mock):
    httpx_mock.add_response(url=f"{BASE}/v1/graphs", json=_graphs_body())

    GraphClient({**CONFIG, "token_provider": lambda: "eyJ.rotated.sig"}).get_graph_info(
      GRAPH
    )

    request = httpx_mock.get_requests()[0]
    assert request.headers["Authorization"] == "Bearer eyJ.rotated.sig"


# ── Reads whose body shape the facade misread ────────────────────────


def _graphs_body() -> dict:
  # routers/user — UserGraphsResponse, camelCase on the wire.
  return {
    "graphs": [
      {
        "graphId": GRAPH,
        "graphName": "Acme",
        "role": "admin",
        "isSelected": True,
        "createdAt": "2026-01-01T00:00:00Z",
      }
    ],
    "selectedGraphId": GRAPH,
  }


@pytest.mark.unit
class TestReadShapes:
  def test_get_graph_info_finds_the_graph(self, httpx_mock):
    httpx_mock.add_response(url=f"{BASE}/v1/graphs", json=_graphs_body())

    info = GraphClient(CONFIG).get_graph_info(GRAPH)

    assert info.graph_id == GRAPH
    assert info.graph_name == "Acme"
    assert info.schema_extensions is None  # absent on the wire: None, not UNSET

  def test_get_graph_info_reports_a_failed_call(self, httpx_mock):
    httpx_mock.add_response(
      url=f"{BASE}/v1/graphs", status_code=401, json={"detail": "Invalid API key"}
    )

    with pytest.raises(RuntimeError, match="Failed to get graphs: 401"):
      GraphClient(CONFIG).get_graph_info(GRAPH)

  def test_table_list_reads_the_real_fields(self, httpx_mock):
    httpx_mock.add_response(
      url=f"{BASE}/v1/graphs/{GRAPH}/tables",
      json={
        "tables": [
          {
            "table_name": "Entity",
            "row_count": 3,
            "file_count": 1,
            "total_size_bytes": 2048,
            "s3_location": None,
          }
        ],
        "total_count": 1,
      },
    )

    tables = TableClient(CONFIG).list(GRAPH)

    assert len(tables) == 1
    assert tables[0].table_name == "Entity"
    assert tables[0].row_count == 3
    assert tables[0].table_type is None

  def test_file_list_and_get_turn_missing_fields_into_none(self, httpx_mock):
    file_row = {
      "file_id": "f_1",
      "file_name": "a.parquet",
      "file_format": "parquet",
      "size_bytes": 10,
      "upload_status": "uploaded",
      "upload_method": "presigned",
      "s3_key": "k",
    }
    httpx_mock.add_response(
      url=re.compile(rf"{BASE}/v1/graphs/{GRAPH}/files(\?.*)?$"),
      json={
        "graph_id": GRAPH,
        "files": [file_row],
        "total_files": 1,
        "total_size_bytes": 10,
      },
    )
    httpx_mock.add_response(
      url=f"{BASE}/v1/graphs/{GRAPH}/files/f_1",
      json={**file_row, "graph_id": GRAPH, "table_id": "t_1"},
    )
    client = FileClient(CONFIG)

    listed = client.list(GRAPH)[0]
    fetched = client.get(GRAPH, "f_1")

    for info in (listed, fetched):
      assert info is not None
      assert info.row_count is None
      assert info.created_at is None
      assert info.uploaded_at is None
    assert fetched is not None and fetched.layers is None


# ── Ledger parity additions ──────────────────────────────────────────


@pytest.mark.unit
class TestLedgerParity:
  def test_create_report_sends_periods_and_iso_dates(self, httpx_mock):
    httpx_mock.add_response(
      method="POST",
      url=f"{BASE}/extensions/roboledger/{GRAPH}/operations/create-report",
      status_code=500,
      json={"detail": "stop here"},
    )

    with pytest.raises(RuntimeError):
      LedgerClient(CONFIG).create_report(
        GRAPH,
        "FY25",
        "map_1",
        "2025-01-01",
        "2025-12-31",
        periods=[{"start": "2025-01-01", "end": "2025-03-31", "label": "Q1"}],
      )

    body = json.loads(httpx_mock.get_requests()[0].content)
    assert body["period_start"] == "2025-01-01"
    assert body["periods"] == [
      {"start": "2025-01-01", "end": "2025-03-31", "label": "Q1"}
    ]

  def test_create_report_sends_the_entity(self, httpx_mock):
    httpx_mock.add_response(
      method="POST",
      url=f"{BASE}/extensions/roboledger/{GRAPH}/operations/create-report",
      status_code=500,
      json={"detail": "stop here"},
    )

    with pytest.raises(RuntimeError):
      LedgerClient(CONFIG).create_report(
        GRAPH, "FY25", "map_sub", "2025-01-01", "2025-12-31", entity_id="ent_sub"
      )

    body = json.loads(httpx_mock.get_requests()[0].content)
    assert body["entity_id"] == "ent_sub"

  def test_list_information_blocks_sends_scenario_id(self, httpx_mock):
    httpx_mock.add_response(
      method="POST",
      url=f"{BASE}/extensions/{GRAPH}/graphql",
      json={"data": {"informationBlocks": []}},
    )

    blocks = LedgerClient(CONFIG).list_information_blocks(GRAPH, scenario_id="str_fc")

    assert blocks == []
    payload = json.loads(httpx_mock.get_requests()[0].content)
    assert payload["variables"] == {"scenarioId": "str_fc"}
    assert "$scenarioId: String" in payload["query"]
