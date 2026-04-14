"""Ledger Client for RoboSystems API.

High-level facade for everything the RoboLedger domain exposes: entity,
chart of accounts, transactions, taxonomy + mappings, fiscal calendar,
schedules, and period close.

**Transport split:**
- **Reads** go through GraphQL at `/extensions/{graph_id}/graphql`
  (via the local `GraphQLClient` wrapping httpx). The graph is in the
  URL, not in the query.
- **Writes** go through named command operations at
  `/extensions/roboledger/{graph_id}/operations/{operation_name}`
  (via the OpenAPI-generated `op_*` functions in
  `robosystems_client/api/extensions_robo_ledger/`). Each command
  returns an `OperationEnvelope`; the facade unwraps
  `envelope.result` and returns either a dict or, for async dispatches
  (e.g. auto-map, create-report), a small ack dict.

Reports + publish lists + statements live on `ReportClient` — they
belong to the same backend surface but deserve their own facade.
"""

from __future__ import annotations

import datetime
from http import HTTPStatus
from typing import Any

from ..api.extensions_robo_ledger.op_auto_map_elements import (
  sync_detailed as op_auto_map_elements,
)
from ..api.extensions_robo_ledger.op_build_fact_grid import (
  sync_detailed as op_build_fact_grid,
)
from ..api.extensions_robo_ledger.op_close_period import (
  sync_detailed as op_close_period,
)
from ..api.extensions_robo_ledger.op_create_closing_entry import (
  sync_detailed as op_create_closing_entry,
)
from ..api.extensions_robo_ledger.op_create_manual_closing_entry import (
  sync_detailed as op_create_manual_closing_entry,
)
from ..api.extensions_robo_ledger.op_create_mapping_association import (
  sync_detailed as op_create_mapping_association,
)
from ..api.extensions_robo_ledger.op_create_schedule import (
  sync_detailed as op_create_schedule,
)
from ..api.extensions_robo_ledger.op_create_structure import (
  sync_detailed as op_create_structure,
)
from ..api.extensions_robo_ledger.op_create_taxonomy import (
  sync_detailed as op_create_taxonomy,
)
from ..api.extensions_robo_ledger.op_delete_mapping_association import (
  sync_detailed as op_delete_mapping_association,
)
from ..api.extensions_robo_ledger.op_initialize_ledger import (
  sync_detailed as op_initialize_ledger,
)
from ..api.extensions_robo_ledger.op_reopen_period import (
  sync_detailed as op_reopen_period,
)
from ..api.extensions_robo_ledger.op_set_close_target import (
  sync_detailed as op_set_close_target,
)
from ..api.extensions_robo_ledger.op_truncate_schedule import (
  sync_detailed as op_truncate_schedule,
)
from ..api.extensions_robo_ledger.op_update_entity import (
  sync_detailed as op_update_entity,
)
from ..client import AuthenticatedClient
from ..graphql.client import GraphQLClient, strip_none_vars
from ..graphql.queries.ledger import (
  GET_ACCOUNT_ROLLUPS_QUERY,
  GET_ACCOUNT_TREE_QUERY,
  GET_CLOSING_BOOK_STRUCTURES_QUERY,
  GET_ENTITY_QUERY,
  GET_FISCAL_CALENDAR_QUERY,
  GET_MAPPED_TRIAL_BALANCE_QUERY,
  GET_MAPPING_COVERAGE_QUERY,
  GET_MAPPING_QUERY,
  GET_PERIOD_CLOSE_STATUS_QUERY,
  GET_PERIOD_DRAFTS_QUERY,
  GET_REPORTING_TAXONOMY_QUERY,
  GET_SCHEDULE_FACTS_QUERY,
  GET_SUMMARY_QUERY,
  GET_TRANSACTION_QUERY,
  GET_TRIAL_BALANCE_QUERY,
  LIST_ACCOUNTS_QUERY,
  LIST_ELEMENTS_QUERY,
  LIST_ENTITIES_QUERY,
  LIST_MAPPINGS_QUERY,
  LIST_SCHEDULES_QUERY,
  LIST_STRUCTURES_QUERY,
  LIST_TAXONOMIES_QUERY,
  LIST_TRANSACTIONS_QUERY,
  LIST_UNMAPPED_ELEMENTS_QUERY,
  parse_account_rollups,
  parse_account_tree,
  parse_accounts,
  parse_closing_book_structures,
  parse_elements,
  parse_entities,
  parse_entity,
  parse_fiscal_calendar,
  parse_mapped_trial_balance,
  parse_mapping,
  parse_mapping_coverage,
  parse_mappings,
  parse_period_close_status,
  parse_period_drafts,
  parse_reporting_taxonomy,
  parse_schedule_facts,
  parse_schedules,
  parse_structures,
  parse_summary,
  parse_taxonomies,
  parse_transaction,
  parse_transactions,
  parse_trial_balance,
  parse_unmapped_elements,
)
from ..models.auto_map_elements_operation import AutoMapElementsOperation
from ..models.close_period_operation import ClosePeriodOperation
from ..models.create_closing_entry_operation import CreateClosingEntryOperation
from ..models.create_view_request import CreateViewRequest
from ..models.create_manual_closing_entry_request import CreateManualClosingEntryRequest
from ..models.create_manual_closing_entry_request_entry_type import (
  CreateManualClosingEntryRequestEntryType,
)
from ..models.create_mapping_association_operation import (
  CreateMappingAssociationOperation,
)
from ..models.create_schedule_request import CreateScheduleRequest
from ..models.create_structure_request import CreateStructureRequest
from ..models.create_structure_request_structure_type import (
  CreateStructureRequestStructureType,
)
from ..models.create_taxonomy_request import CreateTaxonomyRequest
from ..models.delete_mapping_association_operation import (
  DeleteMappingAssociationOperation,
)
from ..models.initialize_ledger_request import InitializeLedgerRequest
from ..models.manual_line_item_request import ManualLineItemRequest
from ..models.operation_envelope import OperationEnvelope
from ..models.reopen_period_operation import ReopenPeriodOperation
from ..models.set_close_target_operation import SetCloseTargetOperation
from ..models.truncate_schedule_operation import TruncateScheduleOperation
from ..models.update_entity_request import UpdateEntityRequest
from ..types import UNSET


class LedgerClient:
  """High-level facade for the RoboLedger domain.

  Reads go through GraphQL at `/extensions/{graph_id}/graphql`;
  writes go through REST operation endpoints at
  `/extensions/roboledger/{graph_id}/operations/{operation_name}`.

  Every method takes `graph_id` as the first argument — the facade
  builds the per-graph GraphQL URL on each read, and passes it to the
  generated REST SDK on each write.
  """

  def __init__(self, config: dict[str, Any]):
    self.config = config
    self.base_url = config["base_url"]
    self.headers = config.get("headers", {})
    self.token = config.get("token")
    self.timeout = config.get("timeout", 60)

  def _get_client(self) -> AuthenticatedClient:
    if not self.token:
      raise RuntimeError("No API key provided. Set X-API-Key in headers.")
    return AuthenticatedClient(
      base_url=self.base_url,
      token=self.token,
      prefix="",
      auth_header_name="X-API-Key",
      headers=self.headers,
    )

  def _get_graphql_client(self) -> GraphQLClient:
    """Construct a fresh GraphQL client per call.

    Same shape as `_get_client()` — no long-lived connections; auth
    comes from the same config fields the REST path uses. `graph_id`
    is passed to `execute()`, not the constructor, because it shapes
    the URL.
    """
    if not self.token:
      raise RuntimeError("No API key provided. Set X-API-Key in headers.")
    return GraphQLClient(
      base_url=self.base_url,
      token=self.token,
      headers=self.headers,
      timeout=self.timeout,
    )

  # ── Helpers ─────────────────────────────────────────────────────────

  def _query(
    self,
    graph_id: str,
    query: str,
    variables: dict[str, Any] | None = None,
  ) -> dict[str, Any]:
    """Execute a read against the per-graph GraphQL endpoint.

    ``None`` values in ``variables`` are stripped before sending — the
    facade takes ``None`` to mean "not provided", and some Strawberry
    resolvers treat an explicit ``null`` differently from an unset arg.
    See ``strip_none_vars`` in ``graphql/client.py``.
    """
    cleaned = strip_none_vars(variables) if variables else None
    return self._get_graphql_client().execute(graph_id, query, cleaned)

  def _unwrap(self, label: str, envelope: OperationEnvelope | Any) -> Any:
    """Unwrap an operation envelope and return `result` (None on failure)."""
    if not isinstance(envelope, OperationEnvelope):
      raise RuntimeError(f"{label} failed: {envelope!r}")
    # envelope.result is untyped dict / list / None in the generated model
    return envelope.result

  def _call_op(self, label: str, response: Any) -> OperationEnvelope:
    """Common error handling for every generated op_* REST call."""
    if response.status_code not in (HTTPStatus.OK, HTTPStatus.ACCEPTED):
      raise RuntimeError(
        f"{label} failed: {response.status_code}: {response.content!r}"
      )
    envelope = response.parsed
    if not isinstance(envelope, OperationEnvelope):
      raise RuntimeError(f"{label} failed: unexpected response shape: {envelope!r}")
    return envelope

  # ── Entity ──────────────────────────────────────────────────────────

  def get_entity(self, graph_id: str) -> dict[str, Any] | None:
    """Get the entity (company/organization) for this graph.

    Returns None when the ledger has no entity yet.
    """
    data = self._query(graph_id, GET_ENTITY_QUERY)
    return parse_entity(data)

  def list_entities(
    self, graph_id: str, source: str | None = None
  ) -> list[dict[str, Any]]:
    """List all entities for this graph, optionally filtered by source system."""
    data = self._query(graph_id, LIST_ENTITIES_QUERY, {"source": source})
    return parse_entities(data)

  def update_entity(self, graph_id: str, updates: dict[str, Any]) -> dict[str, Any]:
    """Update the entity for this graph. Only provided fields are applied."""
    body = UpdateEntityRequest.from_dict(updates)
    response = op_update_entity(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Update entity", response)
    return envelope.result or {}

  # ── Summary ────────────────────────────────────────────────────────

  def get_summary(self, graph_id: str) -> dict[str, Any] | None:
    """Ledger rollup counts + QB sync metadata."""
    data = self._query(graph_id, GET_SUMMARY_QUERY)
    return parse_summary(data)

  # ── Accounts ────────────────────────────────────────────────────────

  def list_accounts(
    self,
    graph_id: str,
    classification: str | None = None,
    is_active: bool | None = None,
    limit: int = 100,
    offset: int = 0,
  ) -> dict[str, Any] | None:
    """List CoA accounts with optional filters and pagination."""
    data = self._query(
      graph_id,
      LIST_ACCOUNTS_QUERY,
      {
        "classification": classification,
        "isActive": is_active,
        "limit": limit,
        "offset": offset,
      },
    )
    return parse_accounts(data)

  def get_account_tree(self, graph_id: str) -> dict[str, Any] | None:
    """Hierarchical Chart of Accounts (up to 4 levels deep)."""
    data = self._query(graph_id, GET_ACCOUNT_TREE_QUERY)
    return parse_account_tree(data)

  def get_account_rollups(
    self,
    graph_id: str,
    mapping_id: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
  ) -> dict[str, Any] | None:
    """Accounts rolled up to reporting concepts via a mapping structure."""
    data = self._query(
      graph_id,
      GET_ACCOUNT_ROLLUPS_QUERY,
      {"mappingId": mapping_id, "startDate": start_date, "endDate": end_date},
    )
    return parse_account_rollups(data)

  # ── Transactions ────────────────────────────────────────────────────

  def list_transactions(
    self,
    graph_id: str,
    type: str | None = None,  # noqa: A002 — matches backend arg name
    start_date: str | None = None,
    end_date: str | None = None,
    limit: int = 100,
    offset: int = 0,
  ) -> dict[str, Any] | None:
    """List transactions with optional type + date filters and pagination."""
    data = self._query(
      graph_id,
      LIST_TRANSACTIONS_QUERY,
      {
        "type": type,
        "startDate": start_date,
        "endDate": end_date,
        "limit": limit,
        "offset": offset,
      },
    )
    return parse_transactions(data)

  def get_transaction(
    self, graph_id: str, transaction_id: str
  ) -> dict[str, Any] | None:
    """Get transaction detail with entries + line items."""
    data = self._query(
      graph_id, GET_TRANSACTION_QUERY, {"transactionId": transaction_id}
    )
    return parse_transaction(data)

  # ── Trial balance ──────────────────────────────────────────────────

  def get_trial_balance(
    self,
    graph_id: str,
    start_date: str | None = None,
    end_date: str | None = None,
  ) -> dict[str, Any] | None:
    """Trial balance by raw CoA account."""
    data = self._query(
      graph_id,
      GET_TRIAL_BALANCE_QUERY,
      {"startDate": start_date, "endDate": end_date},
    )
    return parse_trial_balance(data)

  def get_mapped_trial_balance(
    self,
    graph_id: str,
    mapping_id: str,
    start_date: str | None = None,
    end_date: str | None = None,
  ) -> dict[str, Any] | None:
    """Trial balance rolled up to GAAP reporting concepts via a mapping."""
    data = self._query(
      graph_id,
      GET_MAPPED_TRIAL_BALANCE_QUERY,
      {"mappingId": mapping_id, "startDate": start_date, "endDate": end_date},
    )
    return parse_mapped_trial_balance(data)

  # ── Taxonomy ────────────────────────────────────────────────────────

  def get_reporting_taxonomy(self, graph_id: str) -> dict[str, Any] | None:
    """The locked US GAAP reporting taxonomy for this graph."""
    data = self._query(graph_id, GET_REPORTING_TAXONOMY_QUERY)
    return parse_reporting_taxonomy(data)

  def list_taxonomies(
    self, graph_id: str, taxonomy_type: str | None = None
  ) -> list[dict[str, Any]]:
    """List active taxonomies with optional type filter."""
    data = self._query(graph_id, LIST_TAXONOMIES_QUERY, {"taxonomyType": taxonomy_type})
    return parse_taxonomies(data)

  def create_taxonomy(self, graph_id: str, body: dict[str, Any]) -> dict[str, Any]:
    """Create a new taxonomy (used for CoA + mapping taxonomies)."""
    request = CreateTaxonomyRequest.from_dict(body)
    response = op_create_taxonomy(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Create taxonomy", response)
    return envelope.result or {}

  def list_elements(
    self,
    graph_id: str,
    taxonomy_id: str | None = None,
    source: str | None = None,
    classification: str | None = None,
    is_abstract: bool | None = None,
    limit: int = 100,
    offset: int = 0,
  ) -> dict[str, Any] | None:
    """List elements (CoA accounts, GAAP concepts, etc.) with filters."""
    data = self._query(
      graph_id,
      LIST_ELEMENTS_QUERY,
      {
        "taxonomyId": taxonomy_id,
        "source": source,
        "classification": classification,
        "isAbstract": is_abstract,
        "limit": limit,
        "offset": offset,
      },
    )
    return parse_elements(data)

  def list_unmapped_elements(
    self, graph_id: str, mapping_id: str | None = None
  ) -> list[dict[str, Any]]:
    """CoA elements not yet mapped to a reporting concept."""
    data = self._query(
      graph_id, LIST_UNMAPPED_ELEMENTS_QUERY, {"mappingId": mapping_id}
    )
    return parse_unmapped_elements(data)

  # ── Structures / mappings ──────────────────────────────────────────

  def list_structures(
    self,
    graph_id: str,
    taxonomy_id: str | None = None,
    structure_type: str | None = None,
  ) -> list[dict[str, Any]]:
    """List reporting structures (IS, BS, CF, schedules) with optional filters."""
    data = self._query(
      graph_id,
      LIST_STRUCTURES_QUERY,
      {"taxonomyId": taxonomy_id, "structureType": structure_type},
    )
    return parse_structures(data)

  def create_structure(self, graph_id: str, body: dict[str, Any]) -> dict[str, Any]:
    """Create a new structure (mapping, statement, schedule)."""
    request = CreateStructureRequest.from_dict(body)
    response = op_create_structure(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Create structure", response)
    return envelope.result or {}

  def create_mapping_structure(
    self,
    graph_id: str,
    name: str = "CoA to Reporting",
    description: str | None = "Map Chart of Accounts to US GAAP reporting concepts",
    taxonomy_id: str = "tax_usgaap_reporting",
  ) -> dict[str, Any]:
    """Convenience wrapper — create a CoA→GAAP mapping structure."""
    body = CreateStructureRequest(
      name=name,
      structure_type=CreateStructureRequestStructureType.COA_MAPPING,
      taxonomy_id=taxonomy_id,
      description=description if description is not None else UNSET,
    )
    response = op_create_structure(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Create mapping structure", response)
    return envelope.result or {}

  def list_mappings(self, graph_id: str) -> list[dict[str, Any]]:
    """List active CoA→reporting mapping structures."""
    data = self._query(graph_id, LIST_MAPPINGS_QUERY)
    return parse_mappings(data)

  def get_mapping(self, graph_id: str, mapping_id: str) -> dict[str, Any] | None:
    """Get a mapping structure with all its associations."""
    data = self._query(graph_id, GET_MAPPING_QUERY, {"mappingId": mapping_id})
    return parse_mapping(data)

  def get_mapping_coverage(
    self, graph_id: str, mapping_id: str
  ) -> dict[str, Any] | None:
    """Mapping coverage stats — how many CoA elements are mapped."""
    data = self._query(graph_id, GET_MAPPING_COVERAGE_QUERY, {"mappingId": mapping_id})
    return parse_mapping_coverage(data)

  def create_mapping_association(
    self,
    graph_id: str,
    mapping_id: str,
    from_element_id: str,
    to_element_id: str,
    confidence: float = 1.0,
  ) -> dict[str, Any]:
    """Create a manual mapping association between two elements."""
    body = CreateMappingAssociationOperation(
      mapping_id=mapping_id,
      from_element_id=from_element_id,
      to_element_id=to_element_id,
      confidence=confidence,
    )
    response = op_create_mapping_association(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Create mapping association", response)
    return envelope.result or {}

  def delete_mapping_association(
    self, graph_id: str, mapping_id: str, association_id: str
  ) -> dict[str, Any]:
    """Delete a mapping association."""
    body = DeleteMappingAssociationOperation(
      mapping_id=mapping_id, association_id=association_id
    )
    response = op_delete_mapping_association(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Delete mapping association", response)
    return envelope.result if envelope.result is not None else {"deleted": True}

  def auto_map_elements(self, graph_id: str, mapping_id: str) -> dict[str, Any]:
    """Trigger the AI MappingAgent (async). Returns an operation ack."""
    body = AutoMapElementsOperation(mapping_id=mapping_id)
    response = op_auto_map_elements(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Auto-map elements", response)
    return {"operation_id": envelope.operation_id, "status": envelope.status}

  # ── Schedules ──────────────────────────────────────────────────────

  def list_schedules(self, graph_id: str) -> list[dict[str, Any]]:
    """List all schedule structures with metadata."""
    data = self._query(graph_id, LIST_SCHEDULES_QUERY)
    return parse_schedules(data)

  def get_schedule_facts(
    self,
    graph_id: str,
    structure_id: str,
    period_start: str | None = None,
    period_end: str | None = None,
  ) -> list[dict[str, Any]]:
    """Schedule facts optionally filtered by period window."""
    data = self._query(
      graph_id,
      GET_SCHEDULE_FACTS_QUERY,
      {
        "structureId": structure_id,
        "periodStart": period_start,
        "periodEnd": period_end,
      },
    )
    parsed = parse_schedule_facts(data)
    if parsed is None:
      return []
    return parsed.get("facts", [])

  def create_schedule(
    self,
    graph_id: str,
    *,
    name: str,
    element_ids: list[str],
    period_start: str,
    period_end: str,
    monthly_amount: int,
    debit_element_id: str,
    credit_element_id: str,
    entry_type: str = "closing",
    memo_template: str = "",
    taxonomy_id: str | None = None,
    method: str | None = None,
    original_amount: int | None = None,
    residual_value: int | None = None,
    useful_life_months: int | None = None,
    asset_element_id: str | None = None,
    auto_reverse: bool = False,
  ) -> dict[str, Any]:
    """Create a new schedule with pre-generated monthly facts."""
    body_dict: dict[str, Any] = {
      "name": name,
      "element_ids": element_ids,
      "period_start": period_start,
      "period_end": period_end,
      "monthly_amount": monthly_amount,
      "entry_template": {
        "debit_element_id": debit_element_id,
        "credit_element_id": credit_element_id,
        "entry_type": entry_type,
        "memo_template": memo_template,
        "auto_reverse": auto_reverse,
      },
    }
    if taxonomy_id:
      body_dict["taxonomy_id"] = taxonomy_id
    schedule_metadata: dict[str, Any] = {}
    if method:
      schedule_metadata["method"] = method
    if original_amount is not None:
      schedule_metadata["original_amount"] = original_amount
    if residual_value is not None:
      schedule_metadata["residual_value"] = residual_value
    if useful_life_months is not None:
      schedule_metadata["useful_life_months"] = useful_life_months
    if asset_element_id:
      schedule_metadata["asset_element_id"] = asset_element_id
    if schedule_metadata:
      body_dict["schedule_metadata"] = schedule_metadata

    body = CreateScheduleRequest.from_dict(body_dict)
    response = op_create_schedule(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Create schedule", response)
    return envelope.result or {}

  def truncate_schedule(
    self,
    graph_id: str,
    structure_id: str,
    new_end_date: str,
    reason: str,
  ) -> dict[str, Any]:
    """Truncate a schedule — end it early at `new_end_date`."""
    body = TruncateScheduleOperation(
      structure_id=structure_id,
      new_end_date=datetime.date.fromisoformat(new_end_date),
      reason=reason,
    )
    response = op_truncate_schedule(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Truncate schedule", response)
    return envelope.result or {}

  # ── Period close ────────────────────────────────────────────────────

  def get_period_close_status(
    self,
    graph_id: str,
    period_start: str,
    period_end: str,
  ) -> dict[str, Any] | None:
    """Close status for all schedules in a fiscal period."""
    data = self._query(
      graph_id,
      GET_PERIOD_CLOSE_STATUS_QUERY,
      {"periodStart": period_start, "periodEnd": period_end},
    )
    return parse_period_close_status(data)

  def list_period_drafts(self, graph_id: str, period: str) -> dict[str, Any] | None:
    """All draft entries in a period, fully expanded for review pre-close."""
    data = self._query(graph_id, GET_PERIOD_DRAFTS_QUERY, {"period": period})
    return parse_period_drafts(data)

  def create_closing_entry(
    self,
    graph_id: str,
    structure_id: str,
    posting_date: str,
    period_start: str,
    period_end: str,
    memo: str | None = None,
  ) -> dict[str, Any]:
    """Idempotently create (or refresh) a draft closing entry from a schedule."""
    body = CreateClosingEntryOperation(
      structure_id=structure_id,
      posting_date=datetime.date.fromisoformat(posting_date),
      period_start=datetime.date.fromisoformat(period_start),
      period_end=datetime.date.fromisoformat(period_end),
      memo=memo if memo is not None else UNSET,
    )
    response = op_create_closing_entry(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Create closing entry", response)
    return envelope.result or {}

  def create_manual_closing_entry(
    self,
    graph_id: str,
    *,
    posting_date: str,
    memo: str,
    line_items: list[dict[str, Any]],
    entry_type: str | None = None,
  ) -> dict[str, Any]:
    """Create a manual balanced closing entry (not tied to a schedule)."""
    items = [
      ManualLineItemRequest(
        element_id=li["element_id"],
        debit_amount=li.get("debit_amount", 0),
        credit_amount=li.get("credit_amount", 0),
        description=(
          li.get("description") if li.get("description") is not None else UNSET
        ),
      )
      for li in line_items
    ]
    body = CreateManualClosingEntryRequest(
      posting_date=datetime.date.fromisoformat(posting_date),
      memo=memo,
      line_items=items,
      entry_type=(
        CreateManualClosingEntryRequestEntryType(entry_type)
        if entry_type is not None
        else UNSET
      ),
    )
    response = op_create_manual_closing_entry(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Create manual closing entry", response)
    return envelope.result or {}

  # ── Fact grid (graph-backed analytical query) ─────────────────────

  def build_fact_grid(self, graph_id: str, request: dict[str, Any]) -> dict[str, Any]:
    """Build a multi-dimensional fact grid against the graph schema.

    This is a graph-database *read* dispatched through the operation
    surface — it runs against LadybugDB (not the extensions OLTP
    database) and returns a deduplicated pivot table of XBRL facts.
    The same operation works for roboledger tenant graphs (after
    materialization) and for the SEC shared repository, which uses the
    same hypercube schema.

    ``request`` accepts any fields of
    ``robosystems_client.models.create_view_request.CreateViewRequest``:
    ``elements`` (qnames), ``canonical_concepts``, ``periods``,
    ``entities``, ``form``, ``fiscal_year``, ``fiscal_period``,
    ``period_type``, ``include_summary``, ``view_config``. The legacy
    model name ``CreateViewRequest`` is a holdover from when fact grids
    were exposed under a ``/views`` route; the shape is unchanged.
    """
    body = CreateViewRequest.from_dict(request)
    response = op_build_fact_grid(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Build fact grid", response)
    return envelope.result or {}

  # ── Closing book ───────────────────────────────────────────────────

  def get_closing_book_structures(self, graph_id: str) -> dict[str, Any] | None:
    """Grouped closing book structures for the close-screen sidebar."""
    data = self._query(graph_id, GET_CLOSING_BOOK_STRUCTURES_QUERY)
    return parse_closing_book_structures(data)

  # ── Fiscal Calendar ────────────────────────────────────────────────

  def get_fiscal_calendar(self, graph_id: str) -> dict[str, Any] | None:
    """Current fiscal calendar state — pointers, gap, closeable status."""
    data = self._query(graph_id, GET_FISCAL_CALENDAR_QUERY)
    return parse_fiscal_calendar(data)

  def initialize_ledger(
    self,
    graph_id: str,
    *,
    closed_through: str | None = None,
    fiscal_year_start_month: int | None = None,
    earliest_data_period: str | None = None,
    auto_seed_schedules: bool | None = None,
    note: str | None = None,
  ) -> dict[str, Any]:
    """One-time ledger initialization — seed fiscal calendar + periods."""
    body = InitializeLedgerRequest(
      closed_through=closed_through if closed_through is not None else UNSET,
      fiscal_year_start_month=(
        fiscal_year_start_month if fiscal_year_start_month is not None else UNSET
      ),
      earliest_data_period=(
        earliest_data_period if earliest_data_period is not None else UNSET
      ),
      auto_seed_schedules=(
        auto_seed_schedules if auto_seed_schedules is not None else UNSET
      ),
      note=note if note is not None else UNSET,
    )
    response = op_initialize_ledger(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Initialize ledger", response)
    return envelope.result or {}

  def set_close_target(
    self,
    graph_id: str,
    period: str,
    note: str | None = None,
  ) -> dict[str, Any]:
    """Set the user-controlled close target (YYYY-MM)."""
    body = SetCloseTargetOperation(
      period=period,
      note=note if note is not None else UNSET,
    )
    response = op_set_close_target(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Set close target", response)
    return envelope.result or {}

  def close_period(
    self,
    graph_id: str,
    period: str,
    note: str | None = None,
    allow_stale_sync: bool | None = None,
  ) -> dict[str, Any]:
    """Close a fiscal period — the final commit action."""
    body = ClosePeriodOperation(
      period=period,
      note=note if note is not None else UNSET,
      allow_stale_sync=(allow_stale_sync if allow_stale_sync is not None else UNSET),
    )
    response = op_close_period(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Close period", response)
    return envelope.result or {}

  def reopen_period(
    self,
    graph_id: str,
    period: str,
    reason: str,
    note: str | None = None,
  ) -> dict[str, Any]:
    """Reopen a closed fiscal period. Requires a reason for the audit log."""
    body = ReopenPeriodOperation(
      period=period,
      reason=reason,
      note=note if note is not None else UNSET,
    )
    response = op_reopen_period(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Reopen period", response)
    return envelope.result or {}
