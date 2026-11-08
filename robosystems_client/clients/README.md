# RoboSystems Python Client: Facades

`robosystems_client.clients` is the hand-written layer over the generated `api/` and `models/` packages and the GraphQL client. It sets auth headers, follows queued operations to a result, and replays rate-limited requests.

Install with `pip install robosystems-client`. It requires Python 3.12 or newer. `httpx` is a core dependency. `pandas` is optional and only the DataFrame helpers need it. Tests live in `tests/` at the repository root; run them with `just test`.

## Quick start

```python
from robosystems_client.clients import AuthenticatedClients

clients = AuthenticatedClients("rfs-your-api-key")

result = clients.execute_query(
  "sec",
  "MATCH (e:Entity) WHERE e.ticker = $ticker RETURN e.name, e.cik LIMIT 1",
  {"ticker": "NVDA"},
)
for row in result.data:
  print(row["e.name"], row["e.cik"])

clients.close()
```

Reading the shared `sec` graph needs a key with access to it. Later examples continue from a `clients` built this way and use placeholders such as `graph_id` and `operation_id`.

## What a client holds

| Attribute | Class | Covers |
| --------- | ----- | ------ |
| `query` | `QueryClient` | Cypher: `query`, `execute_query`, `stream_query`, `query_batch` |
| `operator` | `OperatorClient` | AI Operator runs: `query`, `execute_query`, `execute_operator` |
| `operations` | `OperationClient` | `monitor_operation`, `get_operation_status`, `cancel_operation` |
| `graphs` | `GraphClient` | `create_graph_and_wait`, `get_graph_info`, `materialize`, `change_tier`, `delete_graph` |
| `files` | `FileClient` | Parquet files: `upload`, `list`, `get`, `delete` |
| `tables` | `TableClient` | Staging tables: `list`, `query` (SQL) |
| `documents` | `DocumentClient` | Markdown documents: `upload`, `upload_file`, `upload_directory`, `update`, `get`, `get_section`, `search`, `list`, `delete` |
| `ledger` | `LedgerClient` | RoboLedger reads and writes (`reports` is the same object) |
| `investor` | `InvestorClient` | RoboInvestor reads and writes |
| `library` | `LibraryClient` | Taxonomy library reads |

The top level also has `execute_query`, `stream_query`, `monitor_operation`, `get_operation_status`, `cancel_operation`, `create_sse_client` and `close`.

The package root exports `RoboSystemsClients`, `RoboSystemsClientConfig`, `LedgerClient`, `InvestorClient`, `LibraryClient`, `GraphQLError` and `get_clients`. The other classes and helpers here import from `robosystems_client.clients`, except `DocumentClient` (`robosystems_client.clients.document_client`) and `MonitorOptions` (`robosystems_client.clients.operation_client`).

## Authentication

| Constructor | Credential | Default base URL |
| ----------- | ---------- | ---------------- |
| `AuthenticatedClients(api_key, config=None, base_url=None)` | API key | `https://api.robosystems.ai` |
| `TokenClients(token, config=None, base_url=None)` | JWT | `https://api.robosystems.ai` |
| `RoboSystemsClients(config=None)` | `config.headers` or `config.token_provider` | `http://localhost:8000` |

`create_production_clients(api_key)` and `create_development_clients(api_key)` build `AuthenticatedClients` for `https://api.robosystems.ai` and `http://localhost:8000`. A credential is routed by its shape: a value starting with `rfs` goes in `X-API-Key`, anything else in `Authorization: Bearer`. Only one header is sent.

For a credential that rotates, build `RoboSystemsClients(RoboSystemsClientConfig(base_url=url, token_provider=load_current_jwt))`. The zero-argument callable runs on every request and stream connect and wins over a static credential, so keep it cheap. `create_sse_client()` and `authenticated_client` do not consult it; they hold the credential set at construction.

`CookieAuthClients` and `create_clients("cookie", ...)` are not a working way to authenticate. The cookies never reach the child clients, whose calls raise "No API key provided", and the API authenticates data calls by header. `get_clients()` takes no arguments and returns a shared `RoboSystemsClients` with the defaults, localhost and no credential, so build your own client to reach the API.

The package reads no environment variables on its own. `extract_token_from_environment(env_var="ROBOSYSTEMS_TOKEN")` reads one only when you call it, and returns the value only if it is JWT-shaped.

## Configuration

| `RoboSystemsClientConfig` field | Default | Effect |
| ------------------------------- | ------- | ------ |
| `base_url` | `None` | API root; see the table above for what `None` becomes |
| `headers` | `None` | Sent on API calls; may carry a static `X-API-Key` or `Authorization: Bearer` |
| `max_retries` | `5` | Replays of a `429` response; reconnect attempts for `create_sse_client()` |
| `retry_delay` | `1000` | Base backoff in milliseconds for both of the above |
| `timeout` | `30` | Seconds, for ledger, investor and library GraphQL reads and `create_sse_client()`. Other REST calls set no client timeout |
| `s3_endpoint_url` | `None` | Where the client connects for file uploads when it reaches S3 by a different name than the API signed for (a container reaching a dev stack through `host.docker.internal`). The signed `Host` header is kept, as SigV4 requires |
| `token_provider` | `None` | Callable returning the current credential |

## Cypher queries

`clients.execute_query(graph_id, query, parameters=None)` and `clients.query.query(...)` return a `QueryResult` with `data`, `columns`, `row_count`, `execution_time_ms`, `graph_id` and `timestamp`. Each row is a dict keyed by column, so `RETURN e.name` gives `row["e.name"]` and `RETURN e.name AS name` gives `row["name"]`. A failed query raises `Exception` with the status and detail in its message.

**Queued queries.** When the API queues a query, those calls block on the operation's SSE stream until it ends. To get control back, call `QueryClient.execute_query` with `max_wait=0`, the only path that raises `QueuedQueryError`. No other `max_wait` value has an effect.

```python
from robosystems_client.clients import QueryOptions, QueryRequest, QueuedQueryError

request = QueryRequest(query="MATCH (n) RETURN count(n) AS total")
try:
  result = clients.query.execute_query(graph_id, request, QueryOptions(max_wait=0))
except QueuedQueryError as queued:
  print(queued.queue_info.operation_id, queued.queue_info.queue_position)
```

**`stream_query`** returns an iterator of rows, but it is not incremental. The facade collects the whole result, from the NDJSON response or from a queued query's SSE stream, and then yields it row by row. Memory use is the size of the full result, and `chunk_size` does not change that. Call it as `clients.stream_query(graph_id, query, parameters=None, chunk_size=1000)`.

**`clients.query.query_batch(graph_id, queries, parameters_list=None)`** runs queries one after another; its `parallel` argument has no effect. A failed query appears in the list as `{"error": ..., "query": ...}`.

**`QueryBuilder`** appends clauses in the order you call it, one per line. Each `.where()` adds its own `WHERE` line, so two calls produce invalid Cypher. Use one `.where()` with `AND`.

```python
from robosystems_client.clients import QueryBuilder

builder = QueryBuilder().match("(e:Entity)")
builder.where("e.sic = $sic AND e.ticker IS NOT NULL").with_param("sic", "3674")
builder.return_("e.name", "e.ticker").order_by("e.name").limit(10)
query, params = builder.build()
result = clients.execute_query("sec", query, params)
```

**Standalone helpers.** No facade uses these automatically; call them yourself. `CacheManager` is an in-memory TTL cache, and `ProgressTracker` and `DataBatcher` are small bookkeeping classes. `ResultProcessor` has `to_json`, `to_csv` and `to_dataframe`. `validate_cypher_query` checks bracket balance and a few patterns and is not a parser. `estimate_query_cost` counts keywords and does not contact the server. `query_result_to_dataframe` and `DataFrameQueryClient` need pandas.

## Long-running operations

`monitor_operation` follows `GET /v1/operations/{id}/stream`, replayed from the start, and returns an `OperationResult`. A failed or cancelled operation comes back as a `status`, not an exception. Without a timeout, it raises only if the stream ends with no terminal event. The optional callback receives an `OperationProgress`, with `message` and `percentage`.

```python
result = clients.monitor_operation(operation_id, on_progress)
print(result.status.value, result.result, result.error)
```

`status` is an `OperationStatus`. A dropped stream reconnects, so a brief outage doesn't change the result. `FAILED` can still mean the reconnects ran out while the operation was running, with the transport error in `error`. `get_operation_status(operation_id)` returns the server's view as a dict, and `cancel_operation(operation_id)` returns a bool. To set a limit, call `clients.operations.monitor_operation(operation_id, MonitorOptions(timeout=600))`, which raises `TimeoutError`.

For custom event handling, use `create_sse_client()`, which copies the configured headers. An `SSEConfig` you build yourself needs credentials in `headers`, because the stream endpoint returns 401 without them. `connect` reports problems through events rather than raising. A dropped stream, a clean close before the operation finishes, or a `429` or `5xx` response reconnects with backoff at the original `from_sequence`, so a running operation's events during the gap are lost and a finished one replays. The attempts reset only when a real event arrives, and `max_retries_exceeded` fires when they run out. Any other non-200 response emits `error` and returns. `stream_end` ends the connection without a reconnect.

```python
from robosystems_client.clients import EventType

sse = clients.create_sse_client()
sse.on(EventType.OPERATION_PROGRESS.value, lambda data: print(data.get("message")))
sse.on(EventType.OPERATION_COMPLETED.value, lambda data: print(data.get("result")))
sse.on("error", lambda error: print("stream error:", error))
sse.connect(operation_id)  # blocks until the stream ends
sse.close()
```

## AI Operator

`clients.operator.query(graph_id, message)` picks an operator and returns an `OperatorResult` with `content`, `operator_used`, `mode_used`, `operation_id` and `error_details`. `error_details` is set when the API reports a failed run inside a successful response. Use `execute_query` for options, or `execute_operator(graph_id, "analyst", request)` to name the operator.

```python
from robosystems_client.clients import OperatorQueryRequest, OperatorRunError

request = OperatorQueryRequest(message="What changed in revenue?", thread_id=thread_id)
try:
  result = clients.operator.execute_query(graph_id, request)
except OperatorRunError as run:
  print(run.status, run.message, run.writes)  # writes made before the run stopped
```

Reuse a `thread_id` of your choosing, such as a UUID, for follow-up questions. A queued run is followed over SSE, then over `/v1/operations/{id}/status` if the stream gives no verdict; `OperatorOptions(poll_interval=5)`, passed as the third argument, sets the seconds between polls. `OperatorOptions(max_wait=0)` raises `QueuedOperatorError` instead of waiting.

## Ledger

`LedgerClient` reads through GraphQL at `POST /extensions/{graph_id}/graphql` and writes through `POST /extensions/roboledger/{graph_id}/operations/{op}`. Its API methods take `graph_id` first. Reads return typed models, or `None` when the record is missing. Writes return the operation's result, not its envelope. Many methods take `entity_id`; omitted, they act on the group parent.

```python
ledger = clients.ledger
entity = ledger.get_entity(graph_id)
calendar = ledger.get_fiscal_calendar(graph_id)
print(entity.name, calendar.closed_through, calendar.closeable_now)
accounts = ledger.list_accounts(graph_id, classification="asset", limit=50).accounts

ledger.create_journal_entry(
  graph_id,
  posting_date="2026-03-31",
  memo="March accrual",
  line_items=[
    {"element_id": expense_element_id, "debit_amount": 50000, "credit_amount": 0},
    {"element_id": accrual_element_id, "debit_amount": 0, "credit_amount": 50000},
  ],
  idempotency_key="accrual-2026-03",
)
closed = ledger.close_period(graph_id, "2026-03", note="March close")
print(closed.period, closed.entries_posted)
```

Line amounts are in cents, and a journal entry is a draft unless you pass `status="posted"`. Only some writes take `idempotency_key`; check the signature. A selection of the rest:

| Area | Methods |
| ---- | ------- |
| Setup and chart | `initialize_ledger`, `initialize_chart_of_accounts`, `create_entity`, `update_entity`, `link_bank_account`, `get_account_tree`, `list_elements` |
| Mapping | `list_taxonomies`, `list_mappings`, `create_mapping_association`, `auto_map_elements`, `list_unmapped_elements` |
| Events and entries | `create_event_block`, `update_event_block`, `preview_event_block`, `list_event_blocks`, `accept_suggestions`, `update_journal_entry`, `reverse_journal_entry` |
| Balances and views | `get_trial_balance`, `get_account_register`, `get_aged_balances`, `get_summary`, `build_fact_grid`, `financial_statement_analysis`, `live_financial_statement` |
| Schedules and blocks | `create_schedule`, `preview_schedule`, `rebuild_schedule`, `create_information_block`, `get_information_block` |
| Close and consolidation | `get_period_close_status`, `list_period_drafts`, `reopen_period`, `set_close_target`, `list_reconciliations`, `sign_off_reconciliation`, `record_acquisition`, `consolidation_worksheet` |
| Reports | `create_report`, `get_report`, `get_statement`, `file_report`, `share_report`, `download_report_bundle` |

## Investor

`InvestorClient` follows the same pattern, with writes at `POST /extensions/roboinvestor/{graph_id}/operations/{op}`. Positions have no write methods of their own; they change through `create_portfolio_block` and `update_portfolio_block`.

```python
investor = clients.investor
body = {"name": "Example Common", "security_type": "common_stock"}
security = investor.create_security(graph_id, body)
positions = [{"security_id": security.id, "quantity": 100}]
body = {"portfolio": {"name": "Core"}, "positions": positions}
block = investor.create_portfolio_block(graph_id, body)
print(investor.list_portfolios(graph_id, limit=25).portfolios)
print(investor.get_holdings(graph_id, block.id).total_positions)
```

It also has `get_portfolio_block`, `delete_portfolio_block` (pass `confirm_active_positions=True` when positions are active), `list_securities`, `get_security`, `update_security`, `delete_security` (sets `is_active` to false), `list_positions` and `get_position`.

## Library

`LibraryClient` is read-only. `graph_id` defaults to `LIBRARY_GRAPH_ID` (`"library"`), which reads the shared library. Pass a tenant `graph_id` to read that graph's copy plus its own extensions. A credential is still required.

```python
library = clients.library
print([(t.standard, t.version) for t in library.list_library_taxonomies()])
print([e.qname for e in library.search_library_elements("revenue", limit=10)])
print(library.get_library_element(qname="rs-gaap:ProceedsFromIssuanceOfLongTermDebt"))
```

It also has `get_library_taxonomy`, `list_library_elements`, `list_library_taxonomy_arcs`, `list_library_structures`, `get_library_element_arcs`, `get_library_element_classifications` and `get_library_element_equivalents`. `LedgerClient`, `InvestorClient` and `LibraryClient` can also be built alone from a plain dict, such as `LibraryClient({"base_url": "https://api.robosystems.ai", "token": api_key})`. `base_url` is required, and `timeout` defaults to 60 this way.

## Graphs, files, tables and documents

```python
from robosystems_client.clients import GraphMetadata, InitialEntityData

metadata = GraphMetadata(graph_name="Example Holdings")
entity = InitialEntityData(name="Example Holdings LLC", uri="https://example.com")
graph_id = clients.graphs.create_graph_and_wait(metadata, entity, timeout=120)

uploaded = clients.files.upload(graph_id, "Entity", "entity.parquet")
staged = clients.tables.query(graph_id, "SELECT * FROM Entity", limit=5)
done = clients.graphs.materialize(graph_id)
print(uploaded.success, staged.rows, done.total_rows)

clients.documents.upload(graph_id, title="Close memo", content="# March\n\nNotes.")
hits = clients.documents.search(graph_id, "close memo", size=5).hits
```

`upload`, `tables.query` and `materialize` report failure through `success` and `error` on their results. `MaterializationOptions` sets `rebuild`, `force`, `on_progress` and `timeout`. `files.upload` reads the whole file into memory and sends it as Parquet. Its `row_count` is 0 when a large file stages asynchronously. `change_tier` takes `ladybug-standard`, `ladybug-large` or `ladybug-xlarge`. `delete_graph` cancels the subscription and starts deprovisioning, which `at_period_end=True` defers.

Subgraphs and backups have no facade method. `AuthenticatedClients` and `TokenClients` expose `authenticated_client` for the generated functions in `robosystems_client.api`, such as `sync_detailed(graph_id, client=clients.authenticated_client, body=body)` from `robosystems_client.api.graph_operations.create_subgraph`. Calls through it do not replay `429` responses.

## Async

`AsyncRoboSystemsClients` has only `query` and `operations`, plus `execute_query`, `stream_query`, `monitor_operation`, `get_operation_status`, `cancel_operation`, `create_sse_client` and `close`. There is no async ledger, investor, library, graph, file, table, document or operator client, and no auth subclass. Its `base_url` defaults to localhost, its REST calls do not replay `429` responses, and its `stream_query` also collects the result first.

```python
from robosystems_client.clients import AsyncRoboSystemsClients, RoboSystemsClientConfig

headers = {"X-API-Key": api_key}
config = RoboSystemsClientConfig(base_url="https://api.robosystems.ai", headers=headers)
clients = AsyncRoboSystemsClients(config)
result = await clients.execute_query("sec", "MATCH (e:Entity) RETURN count(e) AS total")
await clients.close()
```

## Errors and retries

| Call | On failure |
| ---- | ---------- |
| Ledger, investor and library reads | `GraphQLError`, with `errors` and `status_code` |
| Ledger and investor writes | `RuntimeError` |
| `query`, `operator`, `documents` | `Exception`; `documents.get` and `get_section` return `None` and `documents.delete` returns `False` for a 404 |
| `files.upload`, `tables.query`, `graphs.materialize` | A result with `success=False` and `error` set |
| `files.list`, `files.get`, `files.delete`, `tables.list` | `[]`, `None` or `False`, with the cause only in the log |
| Other `graphs` methods | Raise, usually `RuntimeError`, `ValueError` or `TimeoutError` |
| `operations.get_operation_status` | A dict with `status` of `"error"` or `"unknown"` |

The synchronous facades replay `429` responses with exponential backoff and jitter, capped by `Retry-After`. No other HTTP status is replayed. There is no shared connection pool: most calls build a new HTTP client. To check that the API is reachable, call `GET /v1/status`.
