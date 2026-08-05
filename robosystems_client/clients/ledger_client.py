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
import re
from dataclasses import dataclass
from http import HTTPStatus
from pathlib import Path
from typing import Any

import httpx

from ..api.extensions_robo_ledger.auto_map_elements import (
  sync_detailed as op_auto_map_elements,
)
from ..api.extensions_robo_ledger.build_fact_grid import (
  sync_detailed as op_build_fact_grid,
)
from ..api.extensions_robo_ledger.close_period import (
  sync_detailed as op_close_period,
)
from ..api.extensions_robo_ledger.create_agent import (
  sync_detailed as op_create_agent,
)
from ..api.extensions_robo_ledger.create_event_block import (
  sync_detailed as op_create_event_block,
)
from ..api.extensions_robo_ledger.create_event_handler import (
  sync_detailed as op_create_event_handler,
)
from ..api.extensions_robo_ledger.financial_statement_analysis import (
  sync_detailed as op_financial_statement_analysis,
)
from ..api.extensions_robo_ledger.live_financial_statement import (
  sync_detailed as op_live_financial_statement,
)
from ..api.extensions_robo_ledger.preview_event_block import (
  sync_detailed as op_preview_event_block,
)
from ..api.extensions_robo_ledger.update_agent import (
  sync_detailed as op_update_agent,
)
from ..api.extensions_robo_ledger.update_event_block import (
  sync_detailed as op_update_event_block,
)
from ..api.extensions_robo_ledger.update_event_handler import (
  sync_detailed as op_update_event_handler,
)
from ..api.extensions_robo_ledger.create_mapping_association import (
  sync_detailed as op_create_mapping_association,
)
from ..api.extensions_robo_ledger.create_information_block import (
  sync_detailed as op_create_information_block,
)
from ..api.extensions_robo_ledger.delete_mapping_association import (
  sync_detailed as op_delete_mapping_association,
)
from ..api.extensions_robo_ledger.initialize_ledger import (
  sync_detailed as op_initialize_ledger,
)
from ..api.extensions_robo_ledger.reopen_period import (
  sync_detailed as op_reopen_period,
)
from ..api.extensions_robo_ledger.set_close_target import (
  sync_detailed as op_set_close_target,
)
from ..api.extensions_robo_ledger.create_taxonomy_block import (
  sync_detailed as op_create_taxonomy_block,
)
from ..api.extensions_robo_ledger.update_taxonomy_block import (
  sync_detailed as op_update_taxonomy_block,
)
from ..api.extensions_robo_ledger.delete_taxonomy_block import (
  sync_detailed as op_delete_taxonomy_block,
)
from ..api.extensions_robo_ledger.bind_text_block import (
  sync_detailed as op_bind_text_block,
)
from ..api.extensions_robo_ledger.evaluate_rules import (
  sync_detailed as op_evaluate_rules,
)
from ..api.extensions_robo_ledger.update_entity import (
  sync_detailed as op_update_entity,
)
from ..api.extensions_robo_ledger.update_information_block import (
  sync_detailed as op_update_information_block,
)
from ..api.extensions_robo_ledger.rebuild_schedule import (
  sync_detailed as op_rebuild_schedule,
)
from ..api.extensions_robo_ledger.add_publish_list_members import (
  sync_detailed as op_add_publish_list_members,
)
from ..api.extensions_robo_ledger.create_publish_list import (
  sync_detailed as op_create_publish_list,
)
from ..api.extensions_robo_ledger.create_report import (
  sync_detailed as op_create_report,
)
from ..api.extensions_robo_ledger.delete_publish_list import (
  sync_detailed as op_delete_publish_list,
)
from ..api.extensions_robo_ledger.delete_report import (
  sync_detailed as op_delete_report,
)
from ..api.extensions_robo_ledger.file_report import (
  sync_detailed as op_file_report,
)
from ..api.extensions_robo_ledger.regenerate_report import (
  sync_detailed as op_regenerate_report,
)
from ..api.extensions_robo_ledger.remove_publish_list_member import (
  sync_detailed as op_remove_publish_list_member,
)
from ..api.extensions_robo_ledger.share_report import (
  sync_detailed as op_share_report,
)
from ..api.extensions_robo_ledger.transition_filing_status import (
  sync_detailed as op_transition_filing_status,
)
from ..api.extensions_robo_ledger.update_publish_list import (
  sync_detailed as op_update_publish_list,
)
from ..api.extensions_robo_ledger.link_entity_taxonomy import (
  sync_detailed as op_link_entity_taxonomy,
)
from ..api.extensions_robo_ledger.delete_journal_entry import (
  sync_detailed as op_delete_journal_entry,
)
from ..api.extensions_robo_ledger.delete_information_block import (
  sync_detailed as op_delete_information_block,
)
from ..api.extensions_robo_ledger.update_journal_entry import (
  sync_detailed as op_update_journal_entry,
)
from ..client import AuthenticatedClient
from ..graphql.client import GraphQLClient, strip_none_vars
from ..graphql.generated.get_information_block import (
  GetInformationBlock,
)
from ..graphql.generated.get_information_block import (
  GetInformationBlockInformationBlock as InformationBlock,
)
from ..graphql.generated.get_ledger_account_rollups import (
  GetLedgerAccountRollups,
)
from ..graphql.generated.get_ledger_account_rollups import (
  GetLedgerAccountRollupsAccountRollups as LedgerAccountRollups,
)
from ..graphql.generated.get_ledger_account_tree import (
  GetLedgerAccountTree,
)
from ..graphql.generated.get_ledger_account_tree import (
  GetLedgerAccountTreeAccountTree as LedgerAccountTree,
)
from ..graphql.generated.get_ledger_agent import (
  GetLedgerAgent,
)
from ..graphql.generated.get_ledger_agent import (
  GetLedgerAgentAgent as LedgerAgent,
)
from ..graphql.generated.get_ledger_closing_book_structures import (
  GetLedgerClosingBookStructures,
)
from ..graphql.generated.get_ledger_closing_book_structures import (
  GetLedgerClosingBookStructuresClosingBookStructures as ClosingBookStructures,
)
from ..graphql.generated.get_ledger_entity import (
  GetLedgerEntity,
)
from ..graphql.generated.get_ledger_entity import (
  GetLedgerEntityEntity as LedgerEntity,
)
from ..graphql.generated.get_ledger_event_block import (
  GetLedgerEventBlock,
)
from ..graphql.generated.get_ledger_event_block import (
  GetLedgerEventBlockEventBlock as LedgerEventBlock,
)
from ..graphql.generated.get_ledger_fiscal_calendar import (
  GetLedgerFiscalCalendar,
)
from ..graphql.generated.get_ledger_fiscal_calendar import (
  GetLedgerFiscalCalendarFiscalCalendar as FiscalCalendar,
)
from ..graphql.generated.get_ledger_mapped_trial_balance import (
  GetLedgerMappedTrialBalance,
)
from ..graphql.generated.get_ledger_mapped_trial_balance import (
  GetLedgerMappedTrialBalanceMappedTrialBalance as MappedTrialBalance,
)
from ..graphql.generated.get_ledger_mapping import (
  GetLedgerMapping,
)
from ..graphql.generated.get_ledger_mapping import (
  GetLedgerMappingMapping as LedgerMapping,
)
from ..graphql.generated.get_ledger_mapping_coverage import (
  GetLedgerMappingCoverage,
)
from ..graphql.generated.get_ledger_mapping_coverage import (
  GetLedgerMappingCoverageMappingCoverage as MappingCoverage,
)
from ..graphql.generated.get_ledger_period_close_status import (
  GetLedgerPeriodCloseStatus,
)
from ..graphql.generated.get_ledger_period_close_status import (
  GetLedgerPeriodCloseStatusPeriodCloseStatus as PeriodCloseStatus,
)
from ..graphql.generated.get_ledger_period_drafts import (
  GetLedgerPeriodDrafts,
)
from ..graphql.generated.get_ledger_period_drafts import (
  GetLedgerPeriodDraftsPeriodDrafts as PeriodDrafts,
)
from ..graphql.generated.get_ledger_publish_list import (
  GetLedgerPublishList,
)
from ..graphql.generated.get_ledger_publish_list import (
  GetLedgerPublishListPublishList as PublishList,
)
from ..graphql.generated.get_ledger_report import (
  GetLedgerReport,
)
from ..graphql.generated.get_ledger_report import (
  GetLedgerReportReport as LedgerReport,
)
from ..graphql.generated.get_ledger_report_download_url import (
  GetLedgerReportDownloadUrl,
)
from ..graphql.generated.get_ledger_report_package import (
  GetLedgerReportPackage,
)
from ..graphql.generated.get_ledger_report_package import (
  GetLedgerReportPackageReportPackage as ReportPackage,
)
from ..graphql.generated.get_ledger_reporting_taxonomy import (
  GetLedgerReportingTaxonomy,
)
from ..graphql.generated.get_ledger_reporting_taxonomy import (
  GetLedgerReportingTaxonomyReportingTaxonomy as ReportingTaxonomy,
)
from ..graphql.generated.get_ledger_statement import (
  GetLedgerStatement,
)
from ..graphql.generated.get_ledger_statement import (
  GetLedgerStatementStatement as LedgerStatement,
)
from ..graphql.generated.get_ledger_summary import (
  GetLedgerSummary,
)
from ..graphql.generated.get_ledger_summary import (
  GetLedgerSummarySummary as LedgerSummary,
)
from ..graphql.generated.get_ledger_transaction import (
  GetLedgerTransaction,
)
from ..graphql.generated.get_ledger_transaction import (
  GetLedgerTransactionTransaction as LedgerTransaction,
)
from ..graphql.generated.get_ledger_trial_balance import (
  GetLedgerTrialBalance,
)
from ..graphql.generated.get_ledger_trial_balance import (
  GetLedgerTrialBalanceTrialBalance as TrialBalance,
)
from ..graphql.generated.list_information_blocks import (
  ListInformationBlocks,
  ListInformationBlocksInformationBlocks,
)
from ..graphql.generated.list_ledger_accounts import (
  ListLedgerAccounts,
)
from ..graphql.generated.list_ledger_accounts import (
  ListLedgerAccountsAccounts as LedgerAccountsPage,
)
from ..graphql.generated.list_ledger_agents import (
  ListLedgerAgents,
  ListLedgerAgentsAgents,
)
from ..graphql.generated.list_ledger_elements import (
  ListLedgerElements,
)
from ..graphql.generated.list_ledger_elements import (
  ListLedgerElementsElements as LedgerElementsPage,
)
from ..graphql.generated.list_ledger_entities import (
  ListLedgerEntities,
  ListLedgerEntitiesEntities,
)
from ..graphql.generated.list_ledger_event_blocks import (
  ListLedgerEventBlocks,
  ListLedgerEventBlocksEventBlocks,
)
from ..graphql.generated.list_ledger_mappings import (
  ListLedgerMappings,
  ListLedgerMappingsMappingsStructures,
)
from ..graphql.generated.list_ledger_publish_lists import (
  ListLedgerPublishLists,
)
from ..graphql.generated.list_ledger_publish_lists import (
  ListLedgerPublishListsPublishLists as PublishListsPage,
)
from ..graphql.generated.list_ledger_reports import (
  ListLedgerReports,
  ListLedgerReportsReportsReports,
)
from ..graphql.generated.list_ledger_structures import (
  ListLedgerStructures,
  ListLedgerStructuresStructuresStructures,
)
from ..graphql.generated.list_ledger_taxonomies import (
  ListLedgerTaxonomies,
  ListLedgerTaxonomiesTaxonomiesTaxonomies,
)
from ..graphql.generated.list_ledger_transactions import (
  ListLedgerTransactions,
)
from ..graphql.generated.list_ledger_transactions import (
  ListLedgerTransactionsTransactions as LedgerTransactionsPage,
)
from ..graphql.generated.list_ledger_unmapped_elements import (
  ListLedgerUnmappedElements,
  ListLedgerUnmappedElementsUnmappedElements,
)
from ..graphql.generated.operations import (
  GET_INFORMATION_BLOCK_GQL,
  GET_LEDGER_ACCOUNT_ROLLUPS_GQL,
  GET_LEDGER_ACCOUNT_TREE_GQL,
  GET_LEDGER_AGENT_GQL,
  GET_LEDGER_CLOSING_BOOK_STRUCTURES_GQL,
  GET_LEDGER_ENTITY_GQL,
  GET_LEDGER_EVENT_BLOCK_GQL,
  GET_LEDGER_FISCAL_CALENDAR_GQL,
  GET_LEDGER_MAPPED_TRIAL_BALANCE_GQL,
  GET_LEDGER_MAPPING_COVERAGE_GQL,
  GET_LEDGER_MAPPING_GQL,
  GET_LEDGER_PERIOD_CLOSE_STATUS_GQL,
  GET_LEDGER_PERIOD_DRAFTS_GQL,
  GET_LEDGER_PUBLISH_LIST_GQL,
  GET_LEDGER_REPORT_DOWNLOAD_URL_GQL,
  GET_LEDGER_REPORT_GQL,
  GET_LEDGER_REPORT_PACKAGE_GQL,
  GET_LEDGER_REPORTING_TAXONOMY_GQL,
  GET_LEDGER_STATEMENT_GQL,
  GET_LEDGER_SUMMARY_GQL,
  GET_LEDGER_TRANSACTION_GQL,
  GET_LEDGER_TRIAL_BALANCE_GQL,
  LIST_INFORMATION_BLOCKS_GQL,
  LIST_LEDGER_ACCOUNTS_GQL,
  LIST_LEDGER_AGENTS_GQL,
  LIST_LEDGER_ELEMENTS_GQL,
  LIST_LEDGER_ENTITIES_GQL,
  LIST_LEDGER_EVENT_BLOCKS_GQL,
  LIST_LEDGER_MAPPINGS_GQL,
  LIST_LEDGER_PUBLISH_LISTS_GQL,
  LIST_LEDGER_REPORTS_GQL,
  LIST_LEDGER_STRUCTURES_GQL,
  LIST_LEDGER_TAXONOMIES_GQL,
  LIST_LEDGER_TRANSACTIONS_GQL,
  LIST_LEDGER_UNMAPPED_ELEMENTS_GQL,
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
from ..models.financial_statement_analysis_response import (
  FinancialStatementAnalysisResponse,
)
from ..models.live_financial_statement_response import LiveFinancialStatementResponse
from ..models.view_response import ViewResponse
from ..models.update_agent_request import UpdateAgentRequest
from ..models.update_event_block_request import UpdateEventBlockRequest
from ..models.update_event_handler_request import UpdateEventHandlerRequest
from ..models.delete_journal_entry_request import DeleteJournalEntryRequest
from ..models.create_legacy_arm import CreateLegacyArm
from ..models.create_rollforward_arm import CreateRollforwardArm
from ..models.delete_legacy_arm import DeleteLegacyArm
from ..models.delete_rollforward_arm import DeleteRollforwardArm
from ..models.delete_schedule_arm import DeleteScheduleArm
from ..models.delete_schedule_request import DeleteScheduleRequest
from ..models.rebuild_schedule_request import RebuildScheduleRequest
from ..models.update_legacy_arm import UpdateLegacyArm
from ..models.update_rollforward_arm import UpdateRollforwardArm
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
from ..models.bind_text_block_request import BindTextBlockRequest
from ..models.bind_text_block_response import BindTextBlockResponse
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
from ..models.schedule_created_response import ScheduleCreatedResponse
from ..models.share_report_response import ShareReportResponse
from ..models.taxonomy_block_envelope import TaxonomyBlockEnvelope

from ..types import UNSET


# Captures the ``filename`` value from a Content-Disposition header, with
# or without quotes. Used by ``download_report_bundle`` to recover the
# server-suggested filename when writing the bundle to disk.
_FILENAME_PATTERN = re.compile(r'filename="?([^";]+)"?', re.IGNORECASE)

# Map the wire flavor strings the facade accepts to the GraphQL
# ``ReportDownloadFormat`` enum names used as query variables.
_DOWNLOAD_FORMAT_ALIASES = {
  "jsonld": "JSONLD",
  "holon-jsonld": "HOLON_JSONLD",
  "xbrl-2.1": "XBRL_2_1",
}


def _parse_filename(content_disposition: str) -> str | None:
  """Extract the ``filename`` value from a Content-Disposition header.

  Returns ``None`` when the header is empty or doesn't carry a
  filename — the caller falls back to a synthesized name in that case.
  """
  if not content_disposition:
    return None
  match = _FILENAME_PATTERN.search(content_disposition)
  return match.group(1) if match else None


@dataclass
class ReportBundleDownload:
  """Result of downloading a Report's serialization bundle.

  ``content`` is the raw artifact bytes. ``filename`` is the
  server-suggested name (``{report_id}-g{generation}.{ext}``).
  ``path`` is populated when the caller passed a ``to=`` argument to
  :meth:`LedgerClient.download_report_bundle` — points at the file
  the SDK wrote to disk.
  """

  content: bytes
  filename: str
  format: str
  content_type: str
  generation_count: int | None
  path: Path | None = None


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

  def _typed_result(
    self,
    label: str,
    envelope: Any,
    expected: type[Any],
    *,
    sentinel_on_empty: bool = False,
  ) -> Any:
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
      if sentinel_on_empty:
        # Delete-style ops historically returned {"deleted": True} when the
        # server omitted the result body. Preserve that sentinel for back-compat.
        return {"deleted": True}
      # Everything else advertises a real payload type. Returning the delete
      # sentinel here handed callers a success-shaped dict that satisfies no
      # field of the declared model — close_period reported {"deleted": True}
      # while declaring ClosePeriodResponse. Raise instead, matching the
      # TypeScript client's requireResult.
      raise RuntimeError(f"{label}: operation envelope had no result")
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

  def get_entity(self, graph_id: str) -> LedgerEntity | None:
    """Get the entity (company/organization) for this graph.

    Returns None when the ledger has no entity yet.
    """
    data = self._query(graph_id, GET_LEDGER_ENTITY_GQL)
    return GetLedgerEntity.model_validate(data).entity

  def list_entities(
    self, graph_id: str, source: str | None = None
  ) -> list[ListLedgerEntitiesEntities]:
    """List all entities for this graph, optionally filtered by source system."""
    data = self._query(graph_id, LIST_LEDGER_ENTITIES_GQL, {"source": source})
    return ListLedgerEntities.model_validate(data).entities

  def update_entity(
    self, graph_id: str, updates: dict[str, Any]
  ) -> LedgerEntityResponse:
    """Update the entity for this graph. Only provided fields are applied."""
    body = UpdateEntityRequest.from_dict(updates)
    response = op_update_entity(graph_id=graph_id, body=body, client=self._get_client())
    envelope = self._call_op("Update entity", response)
    return self._typed_result("Update entity", envelope, LedgerEntityResponse)

  # ── Summary ────────────────────────────────────────────────────────

  def get_summary(self, graph_id: str) -> LedgerSummary | None:
    """Ledger rollup counts + QB sync metadata.

    Returns the codegen-typed ``LedgerSummary`` model (attribute access,
    snake_case) rather than a dict.
    """
    data = self._query(graph_id, GET_LEDGER_SUMMARY_GQL)
    return GetLedgerSummary.model_validate(data).summary

  # ── Accounts ────────────────────────────────────────────────────────

  def list_accounts(
    self,
    graph_id: str,
    classification: str | None = None,
    is_active: bool | None = None,
    limit: int = 100,
    offset: int = 0,
  ) -> LedgerAccountsPage | None:
    """List CoA accounts with optional filters and pagination."""
    data = self._query(
      graph_id,
      LIST_LEDGER_ACCOUNTS_GQL,
      {
        "classification": classification,
        "isActive": is_active,
        "limit": limit,
        "offset": offset,
      },
    )
    return ListLedgerAccounts.model_validate(data).accounts

  def get_account_tree(self, graph_id: str) -> LedgerAccountTree | None:
    """Hierarchical Chart of Accounts (up to 4 levels deep)."""
    data = self._query(graph_id, GET_LEDGER_ACCOUNT_TREE_GQL)
    return GetLedgerAccountTree.model_validate(data).account_tree

  def get_account_rollups(
    self,
    graph_id: str,
    mapping_id: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
  ) -> LedgerAccountRollups | None:
    """Accounts rolled up to reporting concepts via a mapping structure."""
    data = self._query(
      graph_id,
      GET_LEDGER_ACCOUNT_ROLLUPS_GQL,
      {"mappingId": mapping_id, "startDate": start_date, "endDate": end_date},
    )
    return GetLedgerAccountRollups.model_validate(data).account_rollups

  # ── Transactions ────────────────────────────────────────────────────

  def list_transactions(
    self,
    graph_id: str,
    type: str | None = None,  # noqa: A002 — matches backend arg name
    start_date: str | None = None,
    end_date: str | None = None,
    limit: int = 100,
    offset: int = 0,
  ) -> LedgerTransactionsPage | None:
    """List transactions with optional type + date filters and pagination."""
    data = self._query(
      graph_id,
      LIST_LEDGER_TRANSACTIONS_GQL,
      {
        "type": type,
        "startDate": start_date,
        "endDate": end_date,
        "limit": limit,
        "offset": offset,
      },
    )
    return ListLedgerTransactions.model_validate(data).transactions

  def get_transaction(
    self, graph_id: str, transaction_id: str
  ) -> LedgerTransaction | None:
    """Get transaction detail with entries + line items."""
    data = self._query(
      graph_id, GET_LEDGER_TRANSACTION_GQL, {"transactionId": transaction_id}
    )
    return GetLedgerTransaction.model_validate(data).transaction

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
  ) -> list[ListLedgerEventBlocksEventBlocks]:
    """List captured event blocks (inbox surface)."""
    data = self._query(
      graph_id,
      LIST_LEDGER_EVENT_BLOCKS_GQL,
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
    return ListLedgerEventBlocks.model_validate(data).event_blocks

  def get_event_block(self, graph_id: str, event_id: str) -> LedgerEventBlock | None:
    """Get event block detail by id."""
    data = self._query(graph_id, GET_LEDGER_EVENT_BLOCK_GQL, {"id": event_id})
    return GetLedgerEventBlock.model_validate(data).event_block

  # ── Agents (REA counterparties) ────────────────────────────────────

  def list_agents(
    self,
    graph_id: str,
    agent_type: str | None = None,
    source: str | None = None,
    is_active: bool | None = True,
    limit: int = 50,
    offset: int = 0,
  ) -> list[ListLedgerAgentsAgents]:
    """List agents (customers, vendors, employees)."""
    data = self._query(
      graph_id,
      LIST_LEDGER_AGENTS_GQL,
      {
        "agentType": agent_type,
        "source": source,
        "isActive": is_active,
        "limit": limit,
        "offset": offset,
      },
    )
    return ListLedgerAgents.model_validate(data).agents

  def get_agent(self, graph_id: str, agent_id: str) -> LedgerAgent | None:
    """Get agent detail by id."""
    data = self._query(graph_id, GET_LEDGER_AGENT_GQL, {"id": agent_id})
    return GetLedgerAgent.model_validate(data).agent

  # ── Trial balance ──────────────────────────────────────────────────

  def get_trial_balance(
    self,
    graph_id: str,
    start_date: str | None = None,
    end_date: str | None = None,
  ) -> TrialBalance | None:
    """Trial balance by raw CoA account."""
    data = self._query(
      graph_id,
      GET_LEDGER_TRIAL_BALANCE_GQL,
      {"startDate": start_date, "endDate": end_date},
    )
    return GetLedgerTrialBalance.model_validate(data).trial_balance

  def get_mapped_trial_balance(
    self,
    graph_id: str,
    mapping_id: str,
    start_date: str | None = None,
    end_date: str | None = None,
  ) -> MappedTrialBalance | None:
    """Trial balance rolled up to GAAP reporting concepts via a mapping."""
    data = self._query(
      graph_id,
      GET_LEDGER_MAPPED_TRIAL_BALANCE_GQL,
      {"mappingId": mapping_id, "startDate": start_date, "endDate": end_date},
    )
    return GetLedgerMappedTrialBalance.model_validate(data).mapped_trial_balance

  # ── Taxonomy ────────────────────────────────────────────────────────

  def get_reporting_taxonomy(self, graph_id: str) -> ReportingTaxonomy | None:
    """The locked US GAAP reporting taxonomy for this graph."""
    data = self._query(graph_id, GET_LEDGER_REPORTING_TAXONOMY_GQL)
    return GetLedgerReportingTaxonomy.model_validate(data).reporting_taxonomy

  def list_taxonomies(
    self, graph_id: str, taxonomy_type: str | None = None
  ) -> list[ListLedgerTaxonomiesTaxonomiesTaxonomies]:
    """List active taxonomies with optional type filter."""
    data = self._query(
      graph_id, LIST_LEDGER_TAXONOMIES_GQL, {"taxonomyType": taxonomy_type}
    )
    page = ListLedgerTaxonomies.model_validate(data).taxonomies
    return page.taxonomies if page else []

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
      "Delete taxonomy block",
      envelope,
      DeleteTaxonomyBlockResponse,
      sentinel_on_empty=True,
    )

  def bind_text_block(
    self, graph_id: str, body: dict[str, Any], idempotency_key: str | None = None
  ) -> BindTextBlockResponse:
    """Bind a platform Document (or one section) to a disclosure element
    as a Nonnumeric text-block fact in a standing 'disclosure' FactSet.

    ``body`` mirrors BindTextBlockRequest: document_id, structure_id,
    exactly one of element_id / element_qname, period_start, period_end,
    plus optional section_id / entity_id. Re-binding the same element
    and period replaces the fact (``replaced=True`` in the response).
    """
    request = BindTextBlockRequest.from_dict(body)
    response = op_bind_text_block(
      graph_id=graph_id,
      body=request,
      client=self._get_client(),
      idempotency_key=idempotency_key if idempotency_key is not None else UNSET,
    )
    envelope = self._call_op("Bind text block", response)
    return self._typed_result("Bind text block", envelope, BindTextBlockResponse)

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
  ) -> LedgerElementsPage | None:
    """List elements (CoA accounts, GAAP concepts, etc.) with filters."""
    data = self._query(
      graph_id,
      LIST_LEDGER_ELEMENTS_GQL,
      {
        "taxonomyId": taxonomy_id,
        "source": source,
        "classification": classification,
        "isAbstract": is_abstract,
        "limit": limit,
        "offset": offset,
      },
    )
    return ListLedgerElements.model_validate(data).elements

  def list_unmapped_elements(
    self, graph_id: str, mapping_id: str | None = None
  ) -> list[ListLedgerUnmappedElementsUnmappedElements]:
    """CoA elements not yet mapped to a reporting concept."""
    data = self._query(
      graph_id, LIST_LEDGER_UNMAPPED_ELEMENTS_GQL, {"mappingId": mapping_id}
    )
    return ListLedgerUnmappedElements.model_validate(data).unmapped_elements

  # ── Structures / mappings ──────────────────────────────────────────

  def list_structures(
    self,
    graph_id: str,
    taxonomy_id: str | None = None,
    block_type: str | None = None,
  ) -> list[ListLedgerStructuresStructuresStructures]:
    """List reporting structures (IS, BS, CF, schedules) with optional filters."""
    data = self._query(
      graph_id,
      LIST_LEDGER_STRUCTURES_GQL,
      {"taxonomyId": taxonomy_id, "blockType": block_type},
    )
    page = ListLedgerStructures.model_validate(data).structures
    return page.structures if page else []

  def list_mappings(self, graph_id: str) -> list[ListLedgerMappingsMappingsStructures]:
    """List active CoA→reporting mapping structures."""
    data = self._query(graph_id, LIST_LEDGER_MAPPINGS_GQL)
    page = ListLedgerMappings.model_validate(data).mappings
    return page.structures if page else []

  def get_mapping(self, graph_id: str, mapping_id: str) -> LedgerMapping | None:
    """Get a mapping structure with all its associations."""
    data = self._query(graph_id, GET_LEDGER_MAPPING_GQL, {"mappingId": mapping_id})
    return GetLedgerMapping.model_validate(data).mapping

  def get_mapping_coverage(
    self, graph_id: str, mapping_id: str
  ) -> MappingCoverage | None:
    """Mapping coverage stats — how many CoA elements are mapped."""
    data = self._query(
      graph_id, GET_LEDGER_MAPPING_COVERAGE_GQL, {"mappingId": mapping_id}
    )
    return GetLedgerMappingCoverage.model_validate(data).mapping_coverage

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
    return self._typed_result(
      "Delete mapping association", envelope, DeleteResult, sentinel_on_empty=True
    )

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
  ) -> InformationBlock | None:
    """Fetch an Information Block envelope by id — the cross-block-type read.

    Returns ``None`` when the block doesn't exist or its type isn't
    registered. See ``information-block.md`` for the envelope contract.
    """
    data = self._query(
      graph_id,
      GET_INFORMATION_BLOCK_GQL,
      {"id": block_id},
    )
    return GetInformationBlock.model_validate(data).information_block

  def list_information_blocks(
    self,
    graph_id: str,
    *,
    block_type: str | None = None,
    category: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
  ) -> list[ListInformationBlocksInformationBlocks]:
    """List Information Block envelopes, optionally filtered.

    Replaces the old ``list_schedules`` method — use
    ``block_type='schedule'`` for the same set of blocks.
    """
    data = self._query(
      graph_id,
      LIST_INFORMATION_BLOCKS_GQL,
      {
        "blockType": block_type,
        "category": category,
        "limit": limit,
        "offset": offset,
      },
    )
    return ListInformationBlocks.model_validate(data).information_blocks

  def create_information_block(
    self,
    graph_id: str,
    body: CreateLegacyArm | CreateRollforwardArm | CreateScheduleArm,
    *,
    idempotency_key: str | None = None,
  ) -> InformationBlockEnvelope:
    """Create an Information Block of any registered block_type.

    Generic wrapper over ``create-information-block``. Pass a typed
    arm body (``CreateScheduleArm``, ``CreateRollforwardArm``, or
    ``CreateLegacyArm``) — the discriminator routes server-side to
    the correct dispatch handler.

    Convenience methods exist for specific block types — e.g.
    ``create_schedule()`` builds + posts a ``CreateScheduleArm``.
    For block types without a convenience method (currently
    ``rollforward``), use this generic entry.
    """
    response = op_create_information_block(
      graph_id=graph_id,
      body=body,
      client=self._get_client(),
      idempotency_key=idempotency_key if idempotency_key is not None else UNSET,
    )
    envelope = self._call_op("Create information block", response)
    return self._typed_result(
      "Create information block", envelope, InformationBlockEnvelope
    )

  def update_information_block(
    self,
    graph_id: str,
    body: UpdateLegacyArm | UpdateRollforwardArm | UpdateScheduleArm,
  ) -> InformationBlockEnvelope:
    """Update an Information Block. Generic wrapper over
    ``update-information-block``."""
    response = op_update_information_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Update information block", response)
    return self._typed_result(
      "Update information block", envelope, InformationBlockEnvelope
    )

  def delete_information_block(
    self,
    graph_id: str,
    body: DeleteLegacyArm | DeleteRollforwardArm | DeleteScheduleArm,
  ) -> DeleteInformationBlockResponse:
    """Delete an Information Block. Generic wrapper over
    ``delete-information-block``."""
    response = op_delete_information_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Delete information block", response)
    return self._typed_result(
      "Delete information block",
      envelope,
      DeleteInformationBlockResponse,
      sentinel_on_empty=True,
    )

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
      "Delete schedule",
      envelope,
      DeleteInformationBlockResponse,
      sentinel_on_empty=True,
    )

  def rebuild_schedule(
    self,
    graph_id: str,
    structure_id: str,
    *,
    idempotency_key: str | None = None,
  ) -> ScheduleCreatedResponse:
    """Rebuild a schedule in place — re-run the generator on an existing schedule.

    Atomic alternative to delete-then-recreate (which orphans pending
    obligations): preserves the structure id, element associations, and
    taxonomy; voids the old pending obligation chain; deletes the old
    facts + SumEquals rules; and regenerates fresh forward facts + a
    fresh obligation chain from the schedule's stored definition
    (``entry_template`` / ``schedule_metadata`` / ``monthly_amount`` /
    period bounds). The historical-vs-in-scope split is re-derived from
    the current fiscal calendar ``closed_through``, so a rebuild re-scopes
    the schedule to today's close state. Use this to pick up a fixed
    generator without orphaning obligations.

    Supply ``idempotency_key`` to make the call safe to retry — replays
    within 24 hours return the same envelope. Reusing the key with a
    different body returns HTTP 409.
    """
    body = RebuildScheduleRequest(structure_id=structure_id)
    response = op_rebuild_schedule(
      graph_id=graph_id,
      body=body,
      client=self._get_client(),
      idempotency_key=idempotency_key if idempotency_key is not None else UNSET,
    )
    envelope = self._call_op("Rebuild schedule", response)
    return self._typed_result("Rebuild schedule", envelope, ScheduleCreatedResponse)

  # ── Period close ────────────────────────────────────────────────────

  def get_period_close_status(
    self,
    graph_id: str,
    period_start: str,
    period_end: str,
  ) -> PeriodCloseStatus | None:
    """Close status for all schedules in a fiscal period."""
    data = self._query(
      graph_id,
      GET_LEDGER_PERIOD_CLOSE_STATUS_GQL,
      {"periodStart": period_start, "periodEnd": period_end},
    )
    return GetLedgerPeriodCloseStatus.model_validate(data).period_close_status

  def list_period_drafts(self, graph_id: str, period: str) -> PeriodDrafts | None:
    """All draft entries in a period, fully expanded for review pre-close."""
    data = self._query(graph_id, GET_LEDGER_PERIOD_DRAFTS_GQL, {"period": period})
    return GetLedgerPeriodDrafts.model_validate(data).period_drafts

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
    return self._typed_result(
      "Delete journal entry", envelope, DeleteResult, sentinel_on_empty=True
    )

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
  ) -> LiveFinancialStatementResponse:
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
    return self._typed_result(
      "Live financial statement", envelope, LiveFinancialStatementResponse
    )

  def financial_statement_analysis(
    self,
    graph_id: str,
    body: dict[str, Any],
  ) -> FinancialStatementAnalysisResponse:
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
    return self._typed_result(
      "Financial statement analysis", envelope, FinancialStatementAnalysisResponse
    )

  # ── Fact grid (graph-backed analytical query) ─────────────────────

  def build_fact_grid(self, graph_id: str, request: dict[str, Any]) -> ViewResponse:
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
    return self._typed_result("Build fact grid", envelope, ViewResponse)

  # ── Closing book ───────────────────────────────────────────────────

  def get_closing_book_structures(self, graph_id: str) -> ClosingBookStructures | None:
    """Grouped closing book structures for the close-screen sidebar."""
    data = self._query(graph_id, GET_LEDGER_CLOSING_BOOK_STRUCTURES_GQL)
    return GetLedgerClosingBookStructures.model_validate(data).closing_book_structures

  # ── Fiscal Calendar ────────────────────────────────────────────────

  def get_fiscal_calendar(self, graph_id: str) -> FiscalCalendar | None:
    """Current fiscal calendar state — pointers, gap, closeable status."""
    data = self._query(graph_id, GET_LEDGER_FISCAL_CALENDAR_GQL)
    return GetLedgerFiscalCalendar.model_validate(data).fiscal_calendar

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

  def list_reports(self, graph_id: str) -> list[ListLedgerReportsReportsReports]:
    """List all reports for a graph (includes received shared reports)."""
    data = self._query(graph_id, LIST_LEDGER_REPORTS_GQL)
    page = ListLedgerReports.model_validate(data).reports
    return page.reports if page else []

  def get_report(self, graph_id: str, report_id: str) -> LedgerReport | None:
    """Get a single report with its period list + available structures."""
    data = self._query(graph_id, GET_LEDGER_REPORT_GQL, {"reportId": report_id})
    return GetLedgerReport.model_validate(data).report

  def get_report_package(self, graph_id: str, report_id: str) -> ReportPackage | None:
    """Rehydrate a Report as a package — Report metadata + N rendered
    `InformationBlock` envelopes (one per attached FactSet).

    Single round trip: returns everything needed to render BS + IS (and any
    other statements the Report generated) without per-section fetches.
    Each item's ``block`` is a fully-rehydrated ``InformationBlock`` envelope
    pinned to its specific FactSet snapshot.
    """
    data = self._query(graph_id, GET_LEDGER_REPORT_PACKAGE_GQL, {"reportId": report_id})
    return GetLedgerReportPackage.model_validate(data).report_package

  def get_statement(
    self, graph_id: str, report_id: str, block_type: str
  ) -> LedgerStatement | None:
    """Render a financial statement — facts viewed through a structure.

    `block_type`: income_statement, balance_sheet, cash_flow_statement, ...
    """
    data = self._query(
      graph_id,
      GET_LEDGER_STATEMENT_GQL,
      {"reportId": report_id, "blockType": block_type},
    )
    return GetLedgerStatement.model_validate(data).statement

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
    return self._typed_result(
      "Delete report", envelope, DeleteResult, sentinel_on_empty=True
    )

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

  def download_report_bundle(
    self,
    graph_id: str,
    report_id: str,
    *,
    format: str = "jsonld",
    to: str | Path | None = None,
    expires_in: int = 300,
  ) -> ReportBundleDownload:
    """Download a published Report's serialization bundle (JSON-LD or XBRL 2.1).

    A download is a read, so the presigned URL is resolved through the
    GraphQL ``reportDownloadUrl`` field (the REST download route was
    retired). Every flavor resolves to a short-lived presigned S3 URL —
    JSON-LD is stamped at publish time; XBRL is materialized + cached on
    first request. The client follows the URL and pulls the bytes.

    Args:
        graph_id: Graph identifier owning the Report.
        report_id: Report identifier (``rpt_``-prefixed ULID).
        format: Serialization flavor — ``"jsonld"`` (default, the flat
            canonical bundle), ``"holon-jsonld"`` (the dataset-form
            scene/boundary/projection holon), or ``"xbrl-2.1"``. The enum
            names ``"JSONLD"`` / ``"HOLON_JSONLD"`` / ``"XBRL_2_1"`` are
            also accepted.
        to: Optional file path to write the bytes to. When set, the
            returned ``ReportBundleDownload.path`` points at the
            written file.
        expires_in: Presigned URL lifetime in seconds (60–3600).

    Returns:
        :class:`ReportBundleDownload` with the artifact bytes,
        server-suggested filename, content type, generation count,
        and (when ``to`` is set) the path written.

    Raises:
        RuntimeError: the report doesn't exist, or the presigned URL
            could not be followed.
        GraphQLError: the report exists but has no published bundle
            (``REPORT_BUNDLE_NOT_AVAILABLE``), or another GraphQL error.
        httpx.TimeoutException: following the presigned URL exceeded
            ``self.timeout`` (passed through unwrapped so callers with
            their own retry / backoff can distinguish it from a generic
            failure).
        httpx.RequestError: any other transport-level failure (DNS,
            connection refused, TLS); not wrapped so the original
            networking context surfaces in tracebacks.
    """
    gql_format = _DOWNLOAD_FORMAT_ALIASES.get(format.lower(), format)
    data = self._query(
      graph_id,
      GET_LEDGER_REPORT_DOWNLOAD_URL_GQL,
      {"reportId": report_id, "format": gql_format, "expiresIn": expires_in},
    )
    info = GetLedgerReportDownloadUrl.model_validate(data).report_download_url
    if info is None:
      raise RuntimeError(f"Report '{report_id}' not found.")

    download_url = info.download_url
    with httpx.Client(timeout=self.timeout) as client:
      # Presigned URL is pre-authorized — no auth headers attached.
      artifact = client.get(download_url)
    if artifact.status_code != 200:
      raise RuntimeError(
        f"Failed to follow presigned URL ({artifact.status_code}): {artifact.text}"
      )

    generation_count = info.generation_count
    default_ext = {"XBRL_2_1": "zip", "HOLON_JSONLD": "holon.jsonld"}.get(
      gql_format, "jsonld"
    )
    filename = (
      _parse_filename(artifact.headers.get("content-disposition", ""))
      or f"{report_id}-g{generation_count or 1}.{default_ext}"
    )
    result = ReportBundleDownload(
      content=artifact.content,
      filename=filename,
      format=info.format,
      content_type=info.content_type,
      generation_count=generation_count,
    )
    if to is not None:
      path = Path(to)
      path.parent.mkdir(parents=True, exist_ok=True)
      path.write_bytes(result.content)
      result.path = path
    return result

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
  ) -> PublishListsPage | None:
    """List publish lists with pagination."""
    data = self._query(
      graph_id, LIST_LEDGER_PUBLISH_LISTS_GQL, {"limit": limit, "offset": offset}
    )
    return ListLedgerPublishLists.model_validate(data).publish_lists

  def get_publish_list(self, graph_id: str, list_id: str) -> PublishList | None:
    """Get a single publish list with its full member list."""
    data = self._query(graph_id, GET_LEDGER_PUBLISH_LIST_GQL, {"listId": list_id})
    return GetLedgerPublishList.model_validate(data).publish_list

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
    return self._typed_result(
      "Delete publish list", envelope, DeleteResult, sentinel_on_empty=True
    )

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
    return self._typed_result(
      "Remove publish list member", envelope, DeleteResult, sentinel_on_empty=True
    )
