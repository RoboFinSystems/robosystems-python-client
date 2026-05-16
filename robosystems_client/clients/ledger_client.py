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

Reports, statements, and publish lists are included on this client —
same backend surface as the ledger operations.
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
from ..api.extensions_robo_ledger.op_create_agent import (
  sync_detailed as op_create_agent,
)
from ..api.extensions_robo_ledger.op_create_event_block import (
  sync_detailed as op_create_event_block,
)
from ..api.extensions_robo_ledger.op_create_event_handler import (
  sync_detailed as op_create_event_handler,
)
from ..api.extensions_robo_ledger.op_financial_statement_analysis import (
  sync_detailed as op_financial_statement_analysis,
)
from ..api.extensions_robo_ledger.op_live_financial_statement import (
  sync_detailed as op_live_financial_statement,
)
from ..api.extensions_robo_ledger.op_preview_event_block import (
  sync_detailed as op_preview_event_block,
)
from ..api.extensions_robo_ledger.op_update_agent import (
  sync_detailed as op_update_agent,
)
from ..api.extensions_robo_ledger.op_update_event_block import (
  sync_detailed as op_update_event_block,
)
from ..api.extensions_robo_ledger.op_update_event_handler import (
  sync_detailed as op_update_event_handler,
)
from ..api.extensions_robo_ledger.op_create_mapping_association import (
  sync_detailed as op_create_mapping_association,
)
from ..api.extensions_robo_ledger.op_create_information_block import (
  sync_detailed as op_create_information_block,
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
from ..api.extensions_robo_ledger.op_create_taxonomy_block import (
  sync_detailed as op_create_taxonomy_block,
)
from ..api.extensions_robo_ledger.op_update_taxonomy_block import (
  sync_detailed as op_update_taxonomy_block,
)
from ..api.extensions_robo_ledger.op_delete_taxonomy_block import (
  sync_detailed as op_delete_taxonomy_block,
)
from ..api.extensions_robo_ledger.op_evaluate_rules import (
  sync_detailed as op_evaluate_rules,
)
from ..api.extensions_robo_ledger.op_update_entity import (
  sync_detailed as op_update_entity,
)
from ..api.extensions_robo_ledger.op_update_information_block import (
  sync_detailed as op_update_information_block,
)
from ..api.extensions_robo_ledger.op_add_publish_list_members import (
  sync_detailed as op_add_publish_list_members,
)
from ..api.extensions_robo_ledger.op_create_publish_list import (
  sync_detailed as op_create_publish_list,
)
from ..api.extensions_robo_ledger.op_create_report import (
  sync_detailed as op_create_report,
)
from ..api.extensions_robo_ledger.op_delete_publish_list import (
  sync_detailed as op_delete_publish_list,
)
from ..api.extensions_robo_ledger.op_delete_report import (
  sync_detailed as op_delete_report,
)
from ..api.extensions_robo_ledger.op_file_report import (
  sync_detailed as op_file_report,
)
from ..api.extensions_robo_ledger.op_regenerate_report import (
  sync_detailed as op_regenerate_report,
)
from ..api.extensions_robo_ledger.op_remove_publish_list_member import (
  sync_detailed as op_remove_publish_list_member,
)
from ..api.extensions_robo_ledger.op_share_report import (
  sync_detailed as op_share_report,
)
from ..api.extensions_robo_ledger.op_transition_filing_status import (
  sync_detailed as op_transition_filing_status,
)
from ..api.extensions_robo_ledger.op_update_publish_list import (
  sync_detailed as op_update_publish_list,
)
from ..api.extensions_robo_ledger.op_link_entity_taxonomy import (
  sync_detailed as op_link_entity_taxonomy,
)
from ..api.extensions_robo_ledger.op_delete_journal_entry import (
  sync_detailed as op_delete_journal_entry,
)
from ..api.extensions_robo_ledger.op_delete_information_block import (
  sync_detailed as op_delete_information_block,
)
from ..api.extensions_robo_ledger.op_update_journal_entry import (
  sync_detailed as op_update_journal_entry,
)
from ..client import AuthenticatedClient
from ..graphql.client import GraphQLClient, strip_none_vars
from ..graphql.queries.ledger import (
  GET_ACCOUNT_ROLLUPS_QUERY,
  GET_ACCOUNT_TREE_QUERY,
  GET_AGENT_QUERY,
  GET_CLOSING_BOOK_STRUCTURES_QUERY,
  GET_ENTITY_QUERY,
  GET_EVENT_BLOCK_QUERY,
  GET_FISCAL_CALENDAR_QUERY,
  GET_MAPPED_TRIAL_BALANCE_QUERY,
  GET_MAPPING_COVERAGE_QUERY,
  GET_MAPPING_QUERY,
  GET_PERIOD_CLOSE_STATUS_QUERY,
  GET_PERIOD_DRAFTS_QUERY,
  GET_INFORMATION_BLOCK_QUERY,
  GET_REPORTING_TAXONOMY_QUERY,
  GET_SUMMARY_QUERY,
  GET_TRANSACTION_QUERY,
  GET_TRIAL_BALANCE_QUERY,
  LIST_ACCOUNTS_QUERY,
  LIST_AGENTS_QUERY,
  LIST_ELEMENTS_QUERY,
  LIST_ENTITIES_QUERY,
  LIST_EVENT_BLOCKS_QUERY,
  LIST_INFORMATION_BLOCKS_QUERY,
  LIST_MAPPINGS_QUERY,
  LIST_STRUCTURES_QUERY,
  LIST_TAXONOMIES_QUERY,
  LIST_TRANSACTIONS_QUERY,
  LIST_UNMAPPED_ELEMENTS_QUERY,
  parse_account_rollups,
  parse_account_tree,
  parse_accounts,
  parse_agent,
  parse_agents,
  parse_closing_book_structures,
  parse_elements,
  parse_entities,
  parse_entity,
  parse_event_block,
  parse_event_blocks,
  parse_fiscal_calendar,
  parse_information_block,
  parse_information_blocks,
  parse_mapped_trial_balance,
  parse_mapping,
  parse_mapping_coverage,
  parse_mappings,
  parse_period_close_status,
  parse_period_drafts,
  parse_reporting_taxonomy,
  parse_structures,
  parse_summary,
  parse_taxonomies,
  parse_transaction,
  parse_transactions,
  parse_trial_balance,
  parse_unmapped_elements,
)
from ..graphql.queries.ledger import (
  GET_PUBLISH_LIST_QUERY,
  GET_REPORT_PACKAGE_QUERY,
  GET_REPORT_QUERY,
  GET_STATEMENT_QUERY,
  LIST_PUBLISH_LISTS_QUERY,
  LIST_REPORTS_QUERY,
  parse_publish_list,
  parse_publish_lists,
  parse_report,
  parse_report_package,
  parse_reports,
  parse_statement,
)
from ..models.add_publish_list_members_operation import AddPublishListMembersOperation
from ..models.auto_map_elements_operation import AutoMapElementsOperation
from ..models.create_agent_request import CreateAgentRequest
from ..models.create_event_block_request import CreateEventBlockRequest
from ..models.create_event_block_request_event_category import (
  CreateEventBlockRequestEventCategory,
)
from ..models.create_event_block_request_event_class import (
  CreateEventBlockRequestEventClass,
)
from ..models.create_event_block_request_metadata import (
  CreateEventBlockRequestMetadata,
)
from ..models.create_event_handler_request import CreateEventHandlerRequest
from ..models.financial_statement_analysis_request import (
  FinancialStatementAnalysisRequest,
)
from ..models.live_financial_statement_request import LiveFinancialStatementRequest
from ..models.update_agent_request import UpdateAgentRequest
from ..models.update_event_block_request import UpdateEventBlockRequest
from ..models.update_event_handler_request import UpdateEventHandlerRequest
from ..models.delete_journal_entry_request import DeleteJournalEntryRequest
from ..models.delete_schedule_arm import DeleteScheduleArm
from ..models.delete_schedule_request import DeleteScheduleRequest
from ..models.link_entity_taxonomy_request import LinkEntityTaxonomyRequest
from ..models.update_journal_entry_request import UpdateJournalEntryRequest
from ..models.update_schedule_arm import UpdateScheduleArm
from ..models.update_schedule_request import UpdateScheduleRequest
from ..models.close_period_operation import ClosePeriodOperation
from ..models.create_view_request import CreateViewRequest
from ..models.create_mapping_association_operation import (
  CreateMappingAssociationOperation,
)
from ..models.create_schedule_arm import CreateScheduleArm
from ..models.create_schedule_request import CreateScheduleRequest
from ..models.delete_mapping_association_operation import (
  DeleteMappingAssociationOperation,
)
from ..models.initialize_ledger_request import InitializeLedgerRequest
from ..models.create_publish_list_request import CreatePublishListRequest
from ..models.create_report_request import CreateReportRequest
from ..models.delete_publish_list_operation import DeletePublishListOperation
from ..models.delete_report_operation import DeleteReportOperation
from ..models.file_report_request import FileReportRequest
from ..models.regenerate_report_operation import RegenerateReportOperation
from ..models.transition_filing_status_request import TransitionFilingStatusRequest
from ..models.remove_publish_list_member_operation import (
  RemovePublishListMemberOperation,
)
from ..models.share_report_operation import ShareReportOperation
from ..models.update_publish_list_operation import UpdatePublishListOperation
from ..models.reopen_period_operation import ReopenPeriodOperation
from ..models.set_close_target_operation import SetCloseTargetOperation
from ..models.create_taxonomy_block_request import CreateTaxonomyBlockRequest
from ..models.update_taxonomy_block_request import UpdateTaxonomyBlockRequest
from ..models.delete_taxonomy_block_request import DeleteTaxonomyBlockRequest
from ..models.evaluate_rules_request import EvaluateRulesRequest
from ..models.update_entity_request import UpdateEntityRequest

# Typed result models — used as facade method return types.
from ..models.association_response import AssociationResponse
from ..models.close_period_response import ClosePeriodResponse
from ..models.delete_information_block_response import DeleteInformationBlockResponse
from ..models.delete_result import DeleteResult
from ..models.delete_taxonomy_block_response import DeleteTaxonomyBlockResponse
from ..models.entity_taxonomy_response import EntityTaxonomyResponse
from ..models.evaluate_rules_response import EvaluateRulesResponse
from ..models.event_block_envelope import EventBlockEnvelope
from ..models.event_handler_response import EventHandlerResponse
from ..models.fiscal_calendar_response import FiscalCalendarResponse
from ..models.information_block_envelope import InformationBlockEnvelope
from ..models.initialize_ledger_response import InitializeLedgerResponse
from ..models.journal_entry_response import JournalEntryResponse
from ..models.ledger_agent_response import LedgerAgentResponse
from ..models.ledger_entity_response import LedgerEntityResponse
from ..models.preview_event_block_response import PreviewEventBlockResponse
from ..models.publish_list_member_response import PublishListMemberResponse
from ..models.publish_list_response import PublishListResponse
from ..models.report_response import ReportResponse
from ..models.share_report_response import ShareReportResponse
from ..models.taxonomy_block_envelope import TaxonomyBlockEnvelope

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

  # The backend's `OperationEnvelope` is generic on the result type
  # (`OperationEnvelope[T]`). Each typed op generates a separate
  # `OperationEnvelope<ResultType>` attrs class in the SDK, with no
  # shared base — so an `isinstance(envelope, OperationEnvelope)` check
  # would reject typed ops like `create-event-block`. We duck-type on
  # the four envelope fields instead, which keeps the helper working
  # for every current and future typed op without import bookkeeping.
  _ENVELOPE_FIELDS = ("operation", "operation_id", "status", "result")

  def _is_envelope(self, value: Any) -> bool:
    return all(hasattr(value, f) for f in self._ENVELOPE_FIELDS)

  def _unwrap(self, label: str, envelope: Any) -> Any:
    """Unwrap an operation envelope and return `result` (None on failure)."""
    if not self._is_envelope(envelope):
      raise RuntimeError(f"{label} failed: {envelope!r}")
    return envelope.result

  def _typed_result(self, label: str, envelope: Any, expected: type[Any]) -> Any:
    """Return ``envelope.result`` for typed-envelope facade methods.

    The calling facade method's return-type annotation advertises the
    expected typed class (e.g. ``LedgerAgentResponse``); the runtime
    return is whatever the SDK gave us:

    - In production the SDK has parsed the typed envelope into the
      generated attrs class — callers get autocomplete + ``.field``
      access.
    - In tests using dict mocks (or untyped envelopes), the result is
      a plain ``dict`` — callers can use either ``result["field"]`` or
      promote with ``ExpectedClass.from_dict(result)``.

    A ``None`` result is normalized to ``{"deleted": True}`` for
    delete-style returns to preserve the legacy sentinel behavior.

    Raises :class:`RuntimeError` only when the envelope itself is
    malformed (label included for debuggability).
    """
    result = envelope.result
    if result is None or (
      hasattr(result, "__class__") and "Unset" in result.__class__.__name__
    ):
      # Delete-style ops historically returned {"deleted": True} when the
      # server omitted the result body. Preserve that sentinel for back-compat.
      return {"deleted": True}
    return result

  def _call_op(self, label: str, response: Any) -> Any:
    """Common error handling for every generated op_* REST call.

    Returns the parsed envelope unchanged. Typed-envelope ops surface
    ``envelope.result`` as the SDK's typed attrs class (e.g.
    ``ReportResponse``); untyped ops surface it as a plain dict via
    ``OperationEnvelopeResultType0``. Facade methods are responsible
    for asserting / casting the result to the type they advertise.
    """
    if response.status_code not in (HTTPStatus.OK, HTTPStatus.ACCEPTED):
      raise RuntimeError(
        f"{label} failed: {response.status_code}: {response.content!r}"
      )
    envelope = response.parsed
    if not self._is_envelope(envelope):
      raise RuntimeError(f"{label} failed: unexpected response shape: {envelope!r}")
    return envelope

  def _build_event_block_request(
    self,
    *,
    event_type: str,
    event_category: str,
    occurred_at: str,
    metadata: dict[str, Any],
    source: str = "manual",
    event_class: str = "economic",
    obligated_by_event_id: str | None = None,
    discharges_event_id: str | None = None,
  ) -> CreateEventBlockRequest:
    """Build a ``CreateEventBlockRequest`` for one of the registered handlers.

    ``occurred_at`` accepts either a date string (``YYYY-MM-DD``) — which
    is normalized to midnight UTC — or a full ISO-8601 timestamp.

    ``source`` describes who fired the event — must match the server's
    CHECK constraint set: ``manual`` (user-initiated, the default),
    ``schedule`` (recurring schedule fired), ``system`` (internal
    automation), or one of the adapter-driven values
    (``quickbooks`` / ``xero`` / ``plaid``) for sync ingestion.
    """
    if "T" not in occurred_at:
      occurred_dt = datetime.datetime.fromisoformat(f"{occurred_at}T00:00:00+00:00")
    else:
      occurred_dt = datetime.datetime.fromisoformat(occurred_at.replace("Z", "+00:00"))
    return CreateEventBlockRequest(
      event_type=event_type,
      event_category=CreateEventBlockRequestEventCategory(event_category),
      source=source,
      occurred_at=occurred_dt,
      apply_handlers=True,
      metadata=CreateEventBlockRequestMetadata.from_dict(metadata),
      event_class=CreateEventBlockRequestEventClass(event_class),
      obligated_by_event_id=obligated_by_event_id
      if obligated_by_event_id is not None
      else UNSET,
      discharges_event_id=discharges_event_id
      if discharges_event_id is not None
      else UNSET,
    )

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

  def update_entity(
    self, graph_id: str, updates: dict[str, Any]
  ) -> LedgerEntityResponse:
    """Update the entity for this graph. Only provided fields are applied."""
    body = UpdateEntityRequest.from_dict(updates)
    response = op_update_entity(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Update entity", response)
    return self._typed_result("Update entity", envelope, LedgerEntityResponse)

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

  # ── Event blocks (inbox surface) ───────────────────────────────────

  def list_event_blocks(
    self,
    graph_id: str,
    event_type: str | None = None,
    event_category: str | None = None,
    status: str | None = None,
    agent_id: str | None = None,
    source: str | None = None,
    limit: int = 50,
    offset: int = 0,
  ) -> list[dict[str, Any]]:
    """List captured event blocks (inbox surface)."""
    data = self._query(
      graph_id,
      LIST_EVENT_BLOCKS_QUERY,
      {
        "eventType": event_type,
        "eventCategory": event_category,
        "status": status,
        "agentId": agent_id,
        "source": source,
        "limit": limit,
        "offset": offset,
      },
    )
    return parse_event_blocks(data)

  def get_event_block(self, graph_id: str, event_id: str) -> dict[str, Any] | None:
    """Get event block detail by id."""
    data = self._query(graph_id, GET_EVENT_BLOCK_QUERY, {"id": event_id})
    return parse_event_block(data)

  # ── Agents (REA counterparties) ────────────────────────────────────

  def list_agents(
    self,
    graph_id: str,
    agent_type: str | None = None,
    source: str | None = None,
    is_active: bool | None = True,
    limit: int = 50,
    offset: int = 0,
  ) -> list[dict[str, Any]]:
    """List agents (customers, vendors, employees)."""
    data = self._query(
      graph_id,
      LIST_AGENTS_QUERY,
      {
        "agentType": agent_type,
        "source": source,
        "isActive": is_active,
        "limit": limit,
        "offset": offset,
      },
    )
    return parse_agents(data)

  def get_agent(self, graph_id: str, agent_id: str) -> dict[str, Any] | None:
    """Get agent detail by id."""
    data = self._query(graph_id, GET_AGENT_QUERY, {"id": agent_id})
    return parse_agent(data)

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

  def create_taxonomy_block(
    self, graph_id: str, body: dict[str, Any], idempotency_key: str | None = None
  ) -> TaxonomyBlockEnvelope:
    """Create a taxonomy block atomically (taxonomy + structures +
    elements + associations + rules in one envelope).
    """
    request = CreateTaxonomyBlockRequest.from_dict(body)
    response = op_create_taxonomy_block(
      graph_id=graph_id,
      body=request,
      client=self._get_client(),
      idempotency_key=idempotency_key if idempotency_key is not None else UNSET,
    )
    envelope = self._call_op("Create taxonomy block", response)
    return self._typed_result("Create taxonomy block", envelope, TaxonomyBlockEnvelope)

  def update_taxonomy_block(
    self, graph_id: str, body: dict[str, Any]
  ) -> TaxonomyBlockEnvelope:
    """Update a taxonomy block — add/update/remove elements, structures, associations, or rules."""
    request = UpdateTaxonomyBlockRequest.from_dict(body)
    response = op_update_taxonomy_block(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Update taxonomy block", response)
    return self._typed_result("Update taxonomy block", envelope, TaxonomyBlockEnvelope)

  def delete_taxonomy_block(
    self, graph_id: str, taxonomy_id: str, reason: str, cascade_facts: bool = False
  ) -> DeleteTaxonomyBlockResponse:
    """Delete a taxonomy block. Cascades through elements, structures, and associations."""
    request = DeleteTaxonomyBlockRequest.from_dict(
      {"taxonomy_id": taxonomy_id, "reason": reason, "cascade_facts": cascade_facts}
    )
    response = op_delete_taxonomy_block(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Delete taxonomy block", response)
    return self._typed_result(
      "Delete taxonomy block", envelope, DeleteTaxonomyBlockResponse
    )

  def link_entity_taxonomy(
    self,
    graph_id: str,
    taxonomy_id: str,
    basis: str = "chart_of_accounts",
    is_primary: bool = True,
    adoption_context: str | None = "voluntary",
  ) -> EntityTaxonomyResponse:
    """Link the graph's entity to a taxonomy (ENTITY_HAS_TAXONOMY edge).

    Idempotent — returns existing linkage if already present.
    """
    body = LinkEntityTaxonomyRequest.from_dict(
      {
        "taxonomy_id": taxonomy_id,
        "basis": basis,
        "is_primary": is_primary,
        "adoption_context": adoption_context,
      }
    )
    response = op_link_entity_taxonomy(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Link entity taxonomy", response)
    return self._typed_result("Link entity taxonomy", envelope, EntityTaxonomyResponse)

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
    block_type: str | None = None,
  ) -> list[dict[str, Any]]:
    """List reporting structures (IS, BS, CF, schedules) with optional filters."""
    data = self._query(
      graph_id,
      LIST_STRUCTURES_QUERY,
      {"taxonomyId": taxonomy_id, "blockType": block_type},
    )
    return parse_structures(data)

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
  ) -> AssociationResponse:
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
    return self._typed_result(
      "Create mapping association", envelope, AssociationResponse
    )

  def delete_mapping_association(
    self, graph_id: str, mapping_id: str, association_id: str
  ) -> DeleteResult:
    """Delete a mapping association."""
    body = DeleteMappingAssociationOperation(
      mapping_id=mapping_id, association_id=association_id
    )
    response = op_delete_mapping_association(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Delete mapping association", response)
    return self._typed_result("Delete mapping association", envelope, DeleteResult)

  def auto_map_elements(self, graph_id: str, mapping_id: str) -> dict[str, Any]:
    """Trigger the AI MappingAgent (async). Returns an operation ack."""
    body = AutoMapElementsOperation(mapping_id=mapping_id)
    response = op_auto_map_elements(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Auto-map elements", response)
    return {"operation_id": envelope.operation_id, "status": envelope.status}

  # ── Information Blocks ─────────────────────────────────────────────

  def get_information_block(
    self,
    graph_id: str,
    block_id: str,
  ) -> dict[str, Any] | None:
    """Fetch an Information Block envelope by id — the cross-block-type read.

    Returns ``None`` when the block doesn't exist or its type isn't
    registered. See ``information-block.md`` for the envelope contract.
    """
    data = self._query(
      graph_id,
      GET_INFORMATION_BLOCK_QUERY,
      {"id": block_id},
    )
    return parse_information_block(data)

  def list_information_blocks(
    self,
    graph_id: str,
    *,
    block_type: str | None = None,
    category: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
  ) -> list[dict[str, Any]]:
    """List Information Block envelopes, optionally filtered.

    Replaces the old ``list_schedules`` method — use
    ``block_type='schedule'`` for the same set of blocks.
    """
    data = self._query(
      graph_id,
      LIST_INFORMATION_BLOCKS_QUERY,
      {
        "blockType": block_type,
        "category": category,
        "limit": limit,
        "offset": offset,
      },
    )
    return parse_information_blocks(data)

  # ── Schedules ──────────────────────────────────────────────────────

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
  ) -> InformationBlockEnvelope:
    """Create a new schedule with pre-generated monthly facts."""
    payload_dict: dict[str, Any] = {
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
      payload_dict["taxonomy_id"] = taxonomy_id
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
      payload_dict["schedule_metadata"] = schedule_metadata

    payload = CreateScheduleRequest.from_dict(payload_dict)
    body = CreateScheduleArm(block_type="schedule", payload=payload)
    response = op_create_information_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Create schedule", response)
    return self._typed_result("Create schedule", envelope, InformationBlockEnvelope)

  def dispose_schedule(
    self,
    graph_id: str,
    structure_id: str,
    disposal_date: str,
    memo: str,
    reason: str,
    sale_proceeds: int | None = None,
    proceeds_element_id: str | None = None,
    gain_loss_element_id: str | None = None,
    source: str = "manual",
  ) -> EventBlockEnvelope:
    """Dispose of a schedule asset — atomically truncates forward facts,
    drops the SumEquals rule, and posts a balanced disposal entry.

    Routes through ``create-event-block`` with
    ``event_type='asset_disposed'``. ``source`` defaults to ``"manual"``
    (user-initiated disposal); sync adapters override.
    """
    metadata: dict[str, Any] = {
      "schedule_id": structure_id,
      "memo": memo,
      "reason": reason,
    }
    if sale_proceeds is not None:
      metadata["proceeds"] = sale_proceeds
    if proceeds_element_id is not None:
      metadata["proceeds_element_id"] = proceeds_element_id
    if gain_loss_element_id is not None:
      metadata["gain_loss_element_id"] = gain_loss_element_id
    body = self._build_event_block_request(
      event_type="asset_disposed",
      event_category="adjustment",
      occurred_at=disposal_date,
      metadata=metadata,
      source=source,
    )
    response = op_create_event_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Dispose schedule", response)
    return self._typed_result("Dispose schedule", envelope, EventBlockEnvelope)

  def evaluate_rules(
    self,
    graph_id: str,
    structure_id: str,
    fact_set_id: str | None = None,
    period_start: str | None = None,
    period_end: str | None = None,
  ) -> EvaluateRulesResponse:
    """Evaluate taxonomy rules against facts in a structure."""
    body_dict: dict[str, Any] = {"structure_id": structure_id}
    if fact_set_id is not None:
      body_dict["fact_set_id"] = fact_set_id
    if period_start is not None:
      body_dict["period_start"] = period_start
    if period_end is not None:
      body_dict["period_end"] = period_end
    request = EvaluateRulesRequest.from_dict(body_dict)
    response = op_evaluate_rules(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Evaluate rules", response)
    return self._typed_result("Evaluate rules", envelope, EvaluateRulesResponse)

  def update_schedule(
    self, graph_id: str, structure_id: str, body: dict[str, Any]
  ) -> InformationBlockEnvelope:
    """Update mutable fields on a schedule (name, entry_template, metadata)."""
    payload = UpdateScheduleRequest.from_dict({"structure_id": structure_id, **body})
    request = UpdateScheduleArm(block_type="schedule", payload=payload)
    response = op_update_information_block(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Update schedule", response)
    return self._typed_result("Update schedule", envelope, InformationBlockEnvelope)

  def delete_schedule(
    self, graph_id: str, structure_id: str
  ) -> DeleteInformationBlockResponse:
    """Permanently delete a schedule (cascades through facts + associations)."""
    payload = DeleteScheduleRequest.from_dict({"structure_id": structure_id})
    body = DeleteScheduleArm(block_type="schedule", payload=payload)
    response = op_delete_information_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Delete schedule", response)
    return self._typed_result(
      "Delete schedule", envelope, DeleteInformationBlockResponse
    )

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
  ) -> EventBlockEnvelope:
    """Idempotently create (or refresh) a draft closing entry from a schedule.

    Routes through ``create-event-block`` with
    ``event_type='schedule_entry_due'`` — the underlying handler dispatches
    one of created / unchanged / regenerated / removed / skipped internally.
    Always emits ``source='schedule'`` since the event is schedule-driven
    by definition. Returns the EventBlockEnvelope.
    """
    metadata: dict[str, Any] = {
      "schedule_id": structure_id,
      "posting_date": posting_date,
      "period_start": period_start,
      "period_end": period_end,
    }
    if memo is not None:
      metadata["memo"] = memo
    body = self._build_event_block_request(
      event_type="schedule_entry_due",
      event_category="recognition",
      occurred_at=posting_date,
      source="schedule",
      metadata=metadata,
    )
    response = op_create_event_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Create closing entry", response)
    return self._typed_result("Create closing entry", envelope, EventBlockEnvelope)

  # ── Journal entries (native accounting writes) ──────────────────────

  def create_journal_entry(
    self,
    graph_id: str,
    *,
    posting_date: str,
    memo: str,
    line_items: list[dict[str, Any]],
    type: str = "standard",  # noqa: A002
    status: str = "draft",
    transaction_id: str | None = None,
    source: str = "manual",
    idempotency_key: str | None = None,
  ) -> EventBlockEnvelope:
    """Create a journal entry with balanced line items (DR=CR enforced).

    Routes through ``create-event-block`` with
    ``event_type='journal_entry_recorded'`` — the Python handler forwards
    to the internal journal-entry command.

    Defaults to ``status='draft'`` for ongoing writes. Pass
    ``status='posted'`` for historical data import where entries
    represent already-happened business events.

    ``source`` defaults to ``"manual"`` (user-initiated). Sync adapters
    (QuickBooks, Plaid, etc.) pass their adapter name so the underlying
    Event row records the correct origin.

    Supply ``idempotency_key`` to make the call safe to retry — replays
    within 24 hours return the same envelope. Reusing the key with a
    different body returns HTTP 409.

    Returns the EventBlockEnvelope (event row fields).
    """
    metadata: dict[str, Any] = {
      "posting_date": posting_date,
      "memo": memo,
      "line_items": line_items,
      "type": type,
      "status": status,
    }
    if transaction_id is not None:
      metadata["transaction_id"] = transaction_id
    body = self._build_event_block_request(
      event_type="journal_entry_recorded",
      event_category="adjustment",
      occurred_at=posting_date,
      metadata=metadata,
      source=source,
    )
    response = op_create_event_block(
      graph_id=graph_id,
      body=body,
      client=self._get_client(),
      idempotency_key=idempotency_key if idempotency_key is not None else UNSET,
    )
    envelope = self._call_op("Create journal entry", response)
    return self._typed_result("Create journal entry", envelope, EventBlockEnvelope)

  def update_journal_entry(
    self, graph_id: str, body: dict[str, Any]
  ) -> JournalEntryResponse:
    """Update a draft journal entry. Posted entries are immutable."""
    request = UpdateJournalEntryRequest.from_dict(body)
    response = op_update_journal_entry(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Update journal entry", response)
    return self._typed_result("Update journal entry", envelope, JournalEntryResponse)

  def delete_journal_entry(self, graph_id: str, entry_id: str) -> DeleteResult:
    """Hard-delete a draft journal entry. Posted entries must be reversed."""
    body = DeleteJournalEntryRequest(entry_id=entry_id)
    response = op_delete_journal_entry(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Delete journal entry", response)
    return self._typed_result("Delete journal entry", envelope, DeleteResult)

  def reverse_journal_entry(
    self,
    graph_id: str,
    entry_id: str,
    posting_date: str | None = None,
    memo: str | None = None,
    reason: str | None = None,
    source: str = "manual",
  ) -> EventBlockEnvelope:
    """Reverse a posted journal entry (creates offsetting entry, marks original as reversed).

    Routes through ``create-event-block`` with
    ``event_type='journal_entry_reversed'``. Returns the EventBlockEnvelope.
    ``source`` defaults to ``"manual"`` — sync adapters override.
    """
    metadata: dict[str, Any] = {"entry_id": entry_id}
    if posting_date is not None:
      metadata["posting_date"] = posting_date
    if memo is not None:
      metadata["memo"] = memo
    if reason is not None:
      metadata["reason"] = reason
    occurred_at = posting_date or datetime.date.today().isoformat()
    body = self._build_event_block_request(
      event_type="journal_entry_reversed",
      event_category="adjustment",
      occurred_at=occurred_at,
      metadata=metadata,
      source=source,
    )
    response = op_create_event_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Reverse journal entry", response)
    return self._typed_result("Reverse journal entry", envelope, EventBlockEnvelope)

  # ── Event blocks (generic preview + status transitions) ──────────────

  def create_event_block(
    self,
    graph_id: str,
    body: dict[str, Any],
    idempotency_key: str | None = None,
  ) -> EventBlockEnvelope:
    """Create an event block directly from a dict.

    Use for support-class events (``event_class='support'``) with categories
    ``approval``, ``control``, ``reconciliation``, or ``inquiry``, which
    are not covered by the specialized helpers. Economic events should
    generally go through ``create_journal_entry``, ``create_closing_entry``,
    etc., but this method works for those too.
    """
    request = CreateEventBlockRequest.from_dict(body)
    response = op_create_event_block(
      graph_id=graph_id,
      body=request,
      client=self._get_client(),
      idempotency_key=idempotency_key if idempotency_key is not None else UNSET,
    )
    envelope = self._call_op("Create event block", response)
    return self._typed_result("Create event block", envelope, EventBlockEnvelope)

  def preview_event_block(
    self,
    graph_id: str,
    body: dict[str, Any],
  ) -> PreviewEventBlockResponse:
    """Dry-run an event block — resolve handler, evaluate metadata, return
    the planned GL rows without writing anything.

    Companion to ``create_journal_entry`` / ``reverse_journal_entry`` /
    ``create_closing_entry`` / ``dispose_schedule``: pass the same body
    those methods would build (a ``CreateEventBlockRequest`` shape) and
    inspect what the handler would do.
    """
    request = CreateEventBlockRequest.from_dict(body)
    response = op_preview_event_block(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Preview event block", response)
    return self._typed_result(
      "Preview event block", envelope, PreviewEventBlockResponse
    )

  def update_event_block(
    self,
    graph_id: str,
    body: dict[str, Any],
  ) -> EventBlockEnvelope:
    """Apply a status transition and/or field corrections to an event block.

    Use for posting drafts (``classified`` → ``committed`` → ``fulfilled``),
    voiding, superseding (correction chains), or patching ``description``,
    ``effective_at``, ``metadata``, ``obligated_by_event_id``, or
    ``discharges_event_id``.
    """
    request = UpdateEventBlockRequest.from_dict(body)
    response = op_update_event_block(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Update event block", response)
    return self._typed_result("Update event block", envelope, EventBlockEnvelope)

  # ── Agents (REA counterparties) ───────────────────────────────────────

  def create_agent(
    self,
    graph_id: str,
    body: dict[str, Any],
    idempotency_key: str | None = None,
  ) -> LedgerAgentResponse:
    """Create an agent — REA counterparty (customer, vendor, employee, etc.)
    referenced by event blocks via ``agent_id``.

    ``(source, external_id)`` is unique when ``external_id`` is provided,
    so external-source ingestion is idempotent at the DB level.
    """
    request = CreateAgentRequest.from_dict(body)
    response = op_create_agent(
      graph_id=graph_id,
      body=request,
      client=self._get_client(),
      idempotency_key=idempotency_key if idempotency_key is not None else UNSET,
    )
    envelope = self._call_op("Create agent", response)
    return self._typed_result("Create agent", envelope, LedgerAgentResponse)

  def update_agent(
    self,
    graph_id: str,
    body: dict[str, Any],
  ) -> LedgerAgentResponse:
    """Update an agent. ``metadata_patch`` is a partial merge into existing
    metadata; all other fields replace.
    """
    request = UpdateAgentRequest.from_dict(body)
    response = op_update_agent(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Update agent", response)
    return self._typed_result("Update agent", envelope, LedgerAgentResponse)

  # ── Event handlers (DSL handler registry) ────────────────────────────

  def create_event_handler(
    self,
    graph_id: str,
    body: dict[str, Any],
  ) -> EventHandlerResponse:
    """Register a tenant-configurable event handler — DSL row in the
    ``event_handlers`` table that drives ``create-event-block`` for event
    types not covered by a Python handler.
    """
    request = CreateEventHandlerRequest.from_dict(body)
    response = op_create_event_handler(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Create event handler", response)
    return self._typed_result("Create event handler", envelope, EventHandlerResponse)

  def update_event_handler(
    self,
    graph_id: str,
    body: dict[str, Any],
  ) -> EventHandlerResponse:
    """Update a registered event handler. Pass ``approve=True`` in the body
    to flip an AI-suggested handler from unapproved to active.
    """
    request = UpdateEventHandlerRequest.from_dict(body)
    response = op_update_event_handler(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Update event handler", response)
    return self._typed_result("Update event handler", envelope, EventHandlerResponse)

  # ── Financial statements (graph-backed) ──────────────────────────────

  def live_financial_statement(
    self,
    graph_id: str,
    body: dict[str, Any],
  ) -> dict[str, Any]:
    """Live financial statement — pulls facts directly from the graph for
    an explicit period window (or fiscal year) and returns the statement
    shape without a persisted Report row. Useful for ad-hoc previews and
    dashboards.
    """
    request = LiveFinancialStatementRequest.from_dict(body)
    response = op_live_financial_statement(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Live financial statement", response)
    return envelope.result or {}

  def financial_statement_analysis(
    self,
    graph_id: str,
    body: dict[str, Any],
  ) -> dict[str, Any]:
    """Run a financial statement analysis against an existing report.

    On shared-repo graphs (e.g. SEC), ``ticker`` is required; on tenant
    graphs it's ignored. Either pass an explicit ``report_id`` or let the
    server auto-resolve via ``fiscal_year`` + ``period_type``.
    """
    request = FinancialStatementAnalysisRequest.from_dict(body)
    response = op_financial_statement_analysis(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Financial statement analysis", response)
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
  ) -> InitializeLedgerResponse:
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
    return self._typed_result("Initialize ledger", envelope, InitializeLedgerResponse)

  def set_close_target(
    self,
    graph_id: str,
    period: str,
    note: str | None = None,
  ) -> FiscalCalendarResponse:
    """Set the user-controlled close target (YYYY-MM)."""
    body = SetCloseTargetOperation(
      period=period,
      note=note if note is not None else UNSET,
    )
    response = op_set_close_target(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Set close target", response)
    return self._typed_result("Set close target", envelope, FiscalCalendarResponse)

  def close_period(
    self,
    graph_id: str,
    period: str,
    note: str | None = None,
    allow_stale_sync: bool | None = None,
  ) -> ClosePeriodResponse:
    """Close a fiscal period — the final commit action."""
    body = ClosePeriodOperation(
      period=period,
      note=note if note is not None else UNSET,
      allow_stale_sync=(allow_stale_sync if allow_stale_sync is not None else UNSET),
    )
    response = op_close_period(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Close period", response)
    return self._typed_result("Close period", envelope, ClosePeriodResponse)

  def reopen_period(
    self,
    graph_id: str,
    period: str,
    reason: str,
    note: str | None = None,
  ) -> FiscalCalendarResponse:
    """Reopen a closed fiscal period. Requires a reason for the audit log."""
    body = ReopenPeriodOperation(
      period=period,
      reason=reason,
      note=note if note is not None else UNSET,
    )
    response = op_reopen_period(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Reopen period", response)
    return self._typed_result("Reopen period", envelope, FiscalCalendarResponse)

  # ── Reports ─────────────────────────────────────────────────────────

  def create_report(
    self,
    graph_id: str,
    name: str,
    mapping_id: str,
    period_start: str,
    period_end: str,
    taxonomy_id: str = "tax_usgaap_reporting",
    period_type: str = "quarterly",
    comparative: bool = True,
  ) -> ReportResponse:
    """Generate report facts from the ledger and publish a Report
    definition. Synchronous — returns the published report header.
    """
    body = CreateReportRequest(
      name=name,
      mapping_id=mapping_id,
      period_start=period_start,
      period_end=period_end,
      taxonomy_id=taxonomy_id,
      period_type=period_type,
      comparative=comparative,
    )
    response = op_create_report(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Create report", response)
    return self._typed_result("Create report", envelope, ReportResponse)

  def list_reports(self, graph_id: str) -> list[dict[str, Any]]:
    """List all reports for a graph (includes received shared reports)."""
    data = self._query(graph_id, LIST_REPORTS_QUERY)
    return parse_reports(data)

  def get_report(self, graph_id: str, report_id: str) -> dict[str, Any] | None:
    """Get a single report with its period list + available structures."""
    data = self._query(graph_id, GET_REPORT_QUERY, {"reportId": report_id})
    return parse_report(data)

  def get_report_package(self, graph_id: str, report_id: str) -> dict[str, Any] | None:
    """Rehydrate a Report as a package — Report metadata + N rendered
    `InformationBlock` envelopes (one per attached FactSet).

    Single round trip: returns everything needed to render BS + IS (and any
    other statements the Report generated) without per-section fetches.
    Each item's ``block`` is a fully-rehydrated ``InformationBlock`` envelope
    pinned to its specific FactSet snapshot.
    """
    data = self._query(graph_id, GET_REPORT_PACKAGE_QUERY, {"reportId": report_id})
    return parse_report_package(data)

  def get_statement(
    self, graph_id: str, report_id: str, block_type: str
  ) -> dict[str, Any] | None:
    """Render a financial statement — facts viewed through a structure.

    `block_type`: income_statement, balance_sheet, cash_flow_statement, ...
    """
    data = self._query(
      graph_id,
      GET_STATEMENT_QUERY,
      {"reportId": report_id, "blockType": block_type},
    )
    return parse_statement(data)

  def regenerate_report(
    self,
    graph_id: str,
    report_id: str,
    period_start: str | None = None,
    period_end: str | None = None,
  ) -> ReportResponse:
    """Re-run fact generation for an existing Report against the latest
    ledger state. Synchronous — returns the regenerated report header.
    """
    body = RegenerateReportOperation(
      report_id=report_id,
      period_start=period_start if period_start is not None else UNSET,
      period_end=period_end if period_end is not None else UNSET,
    )
    response = op_regenerate_report(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Regenerate report", response)
    return self._typed_result("Regenerate report", envelope, ReportResponse)

  def delete_report(self, graph_id: str, report_id: str) -> DeleteResult:
    """Delete a report and its generated facts."""
    body = DeleteReportOperation(report_id=report_id)
    response = op_delete_report(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Delete report", response)
    return self._typed_result("Delete report", envelope, DeleteResult)

  def share_report(
    self, graph_id: str, report_id: str, publish_list_id: str
  ) -> ShareReportResponse:
    """Share a published report to every member of a publish list. Each
    target receives an independent copy; per-recipient outcomes appear
    in the response's ``results`` list.
    """
    body = ShareReportOperation(report_id=report_id, publish_list_id=publish_list_id)
    response = op_share_report(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Share report", response)
    return self._typed_result("Share report", envelope, ShareReportResponse)

  def file_report(self, graph_id: str, report_id: str) -> ReportResponse:
    """Transition a Report's filing_status to 'filed' — locks the package.

    Allowed from 'draft' or 'under_review'. Stamps filed_at + filed_by from
    the auth context + server clock.
    """
    body = FileReportRequest(report_id=report_id)
    response = op_file_report(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("File report", response)
    return self._typed_result("File report", envelope, ReportResponse)

  def transition_filing_status(
    self, graph_id: str, report_id: str, target_status: str
  ) -> ReportResponse:
    """Move a Report along the non-file legs of the filing lifecycle.

    Use ``file_report()`` to reach 'filed' so audit fields land cleanly.
    Other transitions (draft ↔ under_review, filed → archived) go through
    here so the legal-transition graph stays in one place.
    """
    body = TransitionFilingStatusRequest(
      report_id=report_id, target_status=target_status
    )
    response = op_transition_filing_status(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Transition filing status", response)
    return self._typed_result("Transition filing status", envelope, ReportResponse)

  def is_shared_report(self, report: dict[str, Any] | Any) -> bool:
    """Check if a report was received via sharing (vs locally created)."""
    if isinstance(report, dict):
      return report.get("source_graph_id") is not None
    return getattr(report, "source_graph_id", None) is not None

  # ── Publish Lists ────────────────────────────────────────────────────

  def list_publish_lists(
    self, graph_id: str, limit: int = 100, offset: int = 0
  ) -> dict[str, Any] | None:
    """List publish lists with pagination."""
    data = self._query(
      graph_id, LIST_PUBLISH_LISTS_QUERY, {"limit": limit, "offset": offset}
    )
    return parse_publish_lists(data)

  def get_publish_list(self, graph_id: str, list_id: str) -> dict[str, Any] | None:
    """Get a single publish list with its full member list."""
    data = self._query(graph_id, GET_PUBLISH_LIST_QUERY, {"listId": list_id})
    return parse_publish_list(data)

  def create_publish_list(
    self, graph_id: str, name: str, description: str | None = None
  ) -> PublishListResponse:
    """Create a new publish list."""
    body = CreatePublishListRequest(
      name=name,
      description=description if description is not None else UNSET,
    )
    response = op_create_publish_list(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Create publish list", response)
    return self._typed_result("Create publish list", envelope, PublishListResponse)

  def update_publish_list(
    self,
    graph_id: str,
    list_id: str,
    name: str | None = None,
    description: str | None = None,
  ) -> PublishListResponse:
    """Update a publish list's name or description."""
    body = UpdatePublishListOperation(
      list_id=list_id,
      name=name if name is not None else UNSET,
      description=description if description is not None else UNSET,
    )
    response = op_update_publish_list(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Update publish list", response)
    return self._typed_result("Update publish list", envelope, PublishListResponse)

  def delete_publish_list(self, graph_id: str, list_id: str) -> DeleteResult:
    """Delete a publish list."""
    body = DeletePublishListOperation(list_id=list_id)
    response = op_delete_publish_list(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Delete publish list", response)
    return self._typed_result("Delete publish list", envelope, DeleteResult)

  def add_publish_list_members(
    self, graph_id: str, list_id: str, target_graph_ids: list[str]
  ) -> list[PublishListMemberResponse]:
    """Add target graphs as members of a publish list. Returns the
    membership rows that were just created."""
    body = AddPublishListMembersOperation(
      list_id=list_id, target_graph_ids=target_graph_ids
    )
    response = op_add_publish_list_members(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Add publish list members", response)
    result = envelope.result
    if not isinstance(result, list):
      raise RuntimeError(
        f"Add publish list members: expected list result, got "
        f"{type(result).__name__}: {envelope!r}"
      )
    return result

  def remove_publish_list_member(
    self, graph_id: str, list_id: str, member_id: str
  ) -> DeleteResult:
    """Remove a single member from a publish list."""
    body = RemovePublishListMemberOperation(list_id=list_id, member_id=member_id)
    response = op_remove_publish_list_member(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Remove publish list member", response)
    return self._typed_result("Remove publish list member", envelope, DeleteResult)
