"""Ledger Client for RoboSystems API

High-level client for all ledger concerns: chart of accounts, transactions,
trial balance, taxonomy, mappings, and AI auto-mapping.
"""

from __future__ import annotations

import datetime
from http import HTTPStatus
from typing import Any

from ..api.ledger.auto_map_elements import sync_detailed as auto_map_elements
from ..api.ledger.close_fiscal_period import sync_detailed as close_fiscal_period
from ..api.ledger.create_closing_entry import sync_detailed as create_closing_entry
from ..api.ledger.create_manual_closing_entry import (
  sync_detailed as create_manual_closing_entry,
)
from ..api.ledger.create_mapping_association import (
  sync_detailed as create_mapping_association,
)
from ..api.ledger.create_schedule import sync_detailed as create_schedule
from ..api.ledger.create_structure import sync_detailed as create_structure
from ..api.ledger.delete_mapping_association import (
  sync_detailed as delete_mapping_association,
)
from ..api.ledger.get_account_rollups import sync_detailed as get_account_rollups
from ..api.ledger.get_closing_book_structures import (
  sync_detailed as get_closing_book_structures,
)
from ..api.ledger.get_fiscal_calendar import sync_detailed as get_fiscal_calendar
from ..api.ledger.get_ledger_account_tree import (
  sync_detailed as get_ledger_account_tree,
)
from ..api.ledger.get_ledger_entity import sync_detailed as get_ledger_entity
from ..api.ledger.get_ledger_summary import sync_detailed as get_ledger_summary
from ..api.ledger.get_ledger_transaction import (
  sync_detailed as get_ledger_transaction,
)
from ..api.ledger.get_ledger_trial_balance import (
  sync_detailed as get_ledger_trial_balance,
)
from ..api.ledger.get_mapped_trial_balance import (
  sync_detailed as get_mapped_trial_balance,
)
from ..api.ledger.get_mapping_coverage import (
  sync_detailed as get_mapping_coverage,
)
from ..api.ledger.get_mapping_detail import sync_detailed as get_mapping_detail
from ..api.ledger.get_period_close_status import (
  sync_detailed as get_period_close_status,
)
from ..api.ledger.get_reporting_taxonomy import (
  sync_detailed as get_reporting_taxonomy,
)
from ..api.ledger.get_schedule_facts import sync_detailed as get_schedule_facts
from ..api.ledger.initialize_ledger import sync_detailed as initialize_ledger
from ..api.ledger.list_elements import sync_detailed as list_elements
from ..api.ledger.list_ledger_accounts import (
  sync_detailed as list_ledger_accounts,
)
from ..api.ledger.list_ledger_transactions import (
  sync_detailed as list_ledger_transactions,
)
from ..api.ledger.list_mappings import sync_detailed as list_mappings
from ..api.ledger.list_period_drafts import sync_detailed as list_period_drafts
from ..api.ledger.list_schedules import sync_detailed as list_schedules
from ..api.ledger.list_structures import sync_detailed as list_structures
from ..api.ledger.reopen_fiscal_period import sync_detailed as reopen_fiscal_period
from ..api.ledger.set_close_target import sync_detailed as set_close_target
from ..api.ledger.truncate_schedule import sync_detailed as truncate_schedule
from ..client import AuthenticatedClient
from ..types import UNSET


class LedgerClient:
  """Client for ledger operations: accounts, transactions, trial balance, mappings."""

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

  # ── Entity ──────────────────────────────────────────────────────────

  def get_entity(self, graph_id: str) -> Any:
    """Get the entity (company/organization) for this graph."""
    response = get_ledger_entity(graph_id=graph_id, client=self._get_client())
    if response.status_code == HTTPStatus.NOT_FOUND:
      return None
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get entity failed: {response.status_code}")
    return response.parsed

  # ── Accounts ────────────────────────────────────────────────────────

  def list_accounts(self, graph_id: str) -> Any:
    """List accounts (flat)."""
    response = list_ledger_accounts(graph_id=graph_id, client=self._get_client())
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"List accounts failed: {response.status_code}")
    return response.parsed

  def get_account_tree(self, graph_id: str) -> Any:
    """Get the account tree (hierarchical)."""
    response = get_ledger_account_tree(graph_id=graph_id, client=self._get_client())
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get account tree failed: {response.status_code}")
    return response.parsed

  # ── Transactions ────────────────────────────────────────────────────

  def list_transactions(
    self,
    graph_id: str,
    start_date: str | None = None,
    end_date: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
  ) -> Any:
    """List transactions with optional date filters."""
    response = list_ledger_transactions(
      graph_id=graph_id,
      start_date=start_date,
      end_date=end_date,
      limit=limit,
      offset=offset,
      client=self._get_client(),
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"List transactions failed: {response.status_code}")
    return response.parsed

  def get_transaction(self, graph_id: str, transaction_id: str) -> Any:
    """Get transaction detail with entries and line items."""
    response = get_ledger_transaction(
      graph_id=graph_id, transaction_id=transaction_id, client=self._get_client()
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get transaction failed: {response.status_code}")
    return response.parsed

  # ── Trial Balance ──────────────────────────────────────────────────

  def get_trial_balance(
    self,
    graph_id: str,
    start_date: str | None = None,
    end_date: str | None = None,
  ) -> Any:
    """Get trial balance (CoA-level debits/credits)."""
    response = get_ledger_trial_balance(
      graph_id=graph_id,
      start_date=start_date,
      end_date=end_date,
      client=self._get_client(),
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get trial balance failed: {response.status_code}")
    return response.parsed

  def get_mapped_trial_balance(
    self,
    graph_id: str,
    mapping_id: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
  ) -> Any:
    """Get mapped trial balance (CoA rolled up to GAAP concepts)."""
    response = get_mapped_trial_balance(
      graph_id=graph_id,
      mapping_id=mapping_id,
      start_date=start_date,
      end_date=end_date,
      client=self._get_client(),
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get mapped trial balance failed: {response.status_code}")
    return response.parsed

  # ── Summary ────────────────────────────────────────────────────────

  def get_summary(self, graph_id: str) -> Any:
    """Get ledger summary."""
    response = get_ledger_summary(graph_id=graph_id, client=self._get_client())
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get summary failed: {response.status_code}")
    return response.parsed

  # ── Taxonomy ────────────────────────────────────────────────────────

  def get_reporting_taxonomy(self, graph_id: str) -> Any:
    """Get the reporting taxonomy (US GAAP seed)."""
    response = get_reporting_taxonomy(graph_id=graph_id, client=self._get_client())
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get reporting taxonomy failed: {response.status_code}")
    return response.parsed

  def list_structures(self, graph_id: str, taxonomy_id: str | None = None) -> Any:
    """List reporting structures (IS, BS, CF)."""
    response = list_structures(
      graph_id=graph_id, taxonomy_id=taxonomy_id, client=self._get_client()
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"List structures failed: {response.status_code}")
    return response.parsed

  def list_elements(
    self,
    graph_id: str,
    taxonomy_id: str | None = None,
    source: str | None = None,
    classification: str | None = None,
    is_abstract: bool | None = None,
    limit: int | None = None,
    offset: int | None = None,
  ) -> Any:
    """List elements (CoA accounts, GAAP concepts, etc.)."""
    response = list_elements(
      graph_id=graph_id,
      taxonomy_id=taxonomy_id,
      source=source,
      classification=classification,
      is_abstract=is_abstract,
      limit=limit,
      offset=offset,
      client=self._get_client(),
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"List elements failed: {response.status_code}")
    return response.parsed

  # ── Mappings ────────────────────────────────────────────────────────

  def create_mapping_structure(
    self,
    graph_id: str,
    name: str = "CoA to Reporting",
    description: str | None = "Map Chart of Accounts to US GAAP reporting concepts",
    taxonomy_id: str = "tax_usgaap_reporting",
  ) -> Any:
    """Create a new CoA→GAAP mapping structure."""
    from ..models.create_structure_request import CreateStructureRequest
    from ..models.create_structure_request_structure_type import (
      CreateStructureRequestStructureType,
    )

    body = CreateStructureRequest(
      name=name,
      structure_type=CreateStructureRequestStructureType.COA_MAPPING,
      taxonomy_id=taxonomy_id,
      description=description,
    )
    response = create_structure(graph_id=graph_id, body=body, client=self._get_client())
    if response.status_code != HTTPStatus.CREATED:
      raise RuntimeError(f"Create mapping structure failed: {response.status_code}")
    return response.parsed

  def list_mappings(self, graph_id: str) -> Any:
    """List available CoA→GAAP mapping structures."""
    response = list_mappings(graph_id=graph_id, client=self._get_client())
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"List mappings failed: {response.status_code}")
    return response.parsed

  def get_mapping_detail(self, graph_id: str, mapping_id: str) -> Any:
    """Get mapping detail — all associations with element names."""
    response = get_mapping_detail(
      graph_id=graph_id, mapping_id=mapping_id, client=self._get_client()
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get mapping detail failed: {response.status_code}")
    return response.parsed

  def get_mapping_coverage(self, graph_id: str, mapping_id: str) -> Any:
    """Get mapping coverage — how many CoA elements are mapped."""
    response = get_mapping_coverage(
      graph_id=graph_id, mapping_id=mapping_id, client=self._get_client()
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get mapping coverage failed: {response.status_code}")
    return response.parsed

  def create_mapping(
    self,
    graph_id: str,
    mapping_id: str,
    from_element_id: str,
    to_element_id: str,
    confidence: float = 1.0,
  ) -> None:
    """Create a manual mapping association (CoA element → GAAP element)."""
    from ..models.create_association_request import CreateAssociationRequest

    body = CreateAssociationRequest(
      from_element_id=from_element_id,
      to_element_id=to_element_id,
      confidence=confidence,
    )
    response = create_mapping_association(
      graph_id=graph_id, mapping_id=mapping_id, body=body, client=self._get_client()
    )
    if response.status_code not in (HTTPStatus.OK, HTTPStatus.CREATED):
      raise RuntimeError(f"Create mapping failed: {response.status_code}")

  def delete_mapping(self, graph_id: str, mapping_id: str, association_id: str) -> None:
    """Delete a mapping association."""
    response = delete_mapping_association(
      graph_id=graph_id,
      mapping_id=mapping_id,
      association_id=association_id,
      client=self._get_client(),
    )
    if response.status_code not in (HTTPStatus.OK, HTTPStatus.NO_CONTENT):
      raise RuntimeError(f"Delete mapping failed: {response.status_code}")

  def auto_map(self, graph_id: str, mapping_id: str) -> dict[str, Any]:
    """Trigger AI auto-mapping (MappingAgent). Returns immediately."""
    response = auto_map_elements(
      graph_id=graph_id, mapping_id=mapping_id, client=self._get_client()
    )
    if response.status_code != HTTPStatus.ACCEPTED:
      raise RuntimeError(f"Auto-map failed: {response.status_code}")
    return response.parsed or {}

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
  ) -> Any:
    """Create a schedule with pre-generated monthly facts."""
    body: dict[str, Any] = {
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
      body["taxonomy_id"] = taxonomy_id
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
      body["schedule_metadata"] = schedule_metadata

    response = create_schedule(graph_id=graph_id, body=body, client=self._get_client())
    if response.status_code != HTTPStatus.CREATED:
      raise RuntimeError(f"Create schedule failed: {response.status_code}")
    return response.parsed

  def list_schedules(self, graph_id: str) -> Any:
    """List all active schedule structures."""
    response = list_schedules(graph_id=graph_id, client=self._get_client())
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"List schedules failed: {response.status_code}")
    return response.parsed

  def get_schedule_facts(
    self,
    graph_id: str,
    structure_id: str,
    period_start: str | None = None,
    period_end: str | None = None,
  ) -> Any:
    """Get fact values for a schedule, optionally filtered by period."""
    response = get_schedule_facts(
      graph_id=graph_id,
      structure_id=structure_id,
      period_start=period_start,
      period_end=period_end,
      client=self._get_client(),
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get schedule facts failed: {response.status_code}")
    return response.parsed

  def get_period_close_status(
    self,
    graph_id: str,
    period_start: str,
    period_end: str,
  ) -> Any:
    """Get close status for all schedules in a fiscal period."""
    response = get_period_close_status(
      graph_id=graph_id,
      period_start=period_start,
      period_end=period_end,
      client=self._get_client(),
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get period close status failed: {response.status_code}")
    return response.parsed

  def create_closing_entry(
    self,
    graph_id: str,
    structure_id: str,
    posting_date: str,
    period_start: str,
    period_end: str,
    memo: str | None = None,
  ) -> Any:
    """Create a draft closing entry from a schedule's facts for a period."""
    body: dict[str, Any] = {
      "posting_date": posting_date,
      "period_start": period_start,
      "period_end": period_end,
    }
    if memo:
      body["memo"] = memo

    response = create_closing_entry(
      graph_id=graph_id,
      structure_id=structure_id,
      body=body,
      client=self._get_client(),
    )
    if response.status_code != HTTPStatus.CREATED:
      raise RuntimeError(f"Create closing entry failed: {response.status_code}")
    return response.parsed

  # ── Closing Book ─────────────────────────────────────────────────────

  def get_closing_book_structures(self, graph_id: str) -> Any:
    """Get all closing book structure categories for the sidebar."""
    response = get_closing_book_structures(graph_id=graph_id, client=self._get_client())
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get closing book structures failed: {response.status_code}")
    return response.parsed

  def get_account_rollups(
    self,
    graph_id: str,
    mapping_id: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
  ) -> Any:
    """Get account rollups — CoA accounts grouped by reporting element with balances.

    Shows how company-specific accounts roll up to standardized reporting lines.
    Auto-discovers the mapping structure if mapping_id is not provided.
    """
    response = get_account_rollups(
      graph_id=graph_id,
      mapping_id=mapping_id,
      start_date=start_date,
      end_date=end_date,
      client=self._get_client(),
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get account rollups failed: {response.status_code}")
    return response.parsed

  # ── Fiscal Calendar ─────────────────────────────────────────────────

  def initialize_ledger(
    self,
    graph_id: str,
    *,
    closed_through: str | None = None,
    fiscal_year_start_month: int | None = None,
    earliest_data_period: str | None = None,
    auto_seed_schedules: bool | None = None,
    note: str | None = None,
  ) -> Any:
    """Initialize the fiscal calendar for a graph.

    Creates FiscalPeriod rows for the data window, sets `closed_through` /
    `close_target`, and emits an `initialized` audit event. Fails with 409
    if already initialized.
    """
    from ..models.initialize_ledger_request import InitializeLedgerRequest

    body = InitializeLedgerRequest(
      closed_through=closed_through if closed_through is not None else UNSET,
      fiscal_year_start_month=fiscal_year_start_month
      if fiscal_year_start_month is not None
      else UNSET,
      earliest_data_period=earliest_data_period
      if earliest_data_period is not None
      else UNSET,
      auto_seed_schedules=auto_seed_schedules
      if auto_seed_schedules is not None
      else UNSET,
      note=note if note is not None else UNSET,
    )
    response = initialize_ledger(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    if response.status_code != HTTPStatus.CREATED:
      raise RuntimeError(f"Initialize ledger failed: {response.status_code}")
    return response.parsed

  def get_fiscal_calendar(self, graph_id: str) -> Any:
    """Get the current fiscal calendar state — pointers, gap, closeable status."""
    response = get_fiscal_calendar(graph_id=graph_id, client=self._get_client())
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Get fiscal calendar failed: {response.status_code}")
    return response.parsed

  def set_close_target(
    self,
    graph_id: str,
    period: str,
    note: str | None = None,
  ) -> Any:
    """Set the close target for a graph.

    Validates that the target is not in the future and not before
    `closed_through`.
    """
    from ..models.set_close_target_request import SetCloseTargetRequest

    body = SetCloseTargetRequest(
      period=period,
      note=note if note is not None else UNSET,
    )
    response = set_close_target(graph_id=graph_id, body=body, client=self._get_client())
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Set close target failed: {response.status_code}")
    return response.parsed

  def close_period(
    self,
    graph_id: str,
    period: str,
    note: str | None = None,
    allow_stale_sync: bool | None = None,
  ) -> Any:
    """Close a fiscal period — the final commit action.

    Validates closeable gates, transitions all draft entries in the period
    to `posted`, marks the FiscalPeriod closed, and advances `closed_through`
    (auto-advancing `close_target` when reached).
    """
    from ..models.close_period_request import ClosePeriodRequest

    body = ClosePeriodRequest(
      note=note if note is not None else UNSET,
      allow_stale_sync=allow_stale_sync if allow_stale_sync is not None else UNSET,
    )
    response = close_fiscal_period(
      graph_id=graph_id, period=period, body=body, client=self._get_client()
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Close period failed: {response.status_code}")
    return response.parsed

  def reopen_period(
    self,
    graph_id: str,
    period: str,
    reason: str,
    note: str | None = None,
  ) -> Any:
    """Reopen a closed fiscal period.

    Requires a non-empty `reason` for the audit log. Posted entries stay
    posted; the period transitions to `closing` so the user can post
    adjustments and re-close.
    """
    from ..models.reopen_period_request import ReopenPeriodRequest

    body = ReopenPeriodRequest(
      reason=reason,
      note=note if note is not None else UNSET,
    )
    response = reopen_fiscal_period(
      graph_id=graph_id, period=period, body=body, client=self._get_client()
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Reopen period failed: {response.status_code}")
    return response.parsed

  def list_period_drafts(self, graph_id: str, period: str) -> Any:
    """List all draft entries in a fiscal period for review before close.

    Fully expanded with line items, element metadata, and per-entry balance.
    Pure read — call repeatedly without side effects.
    """
    response = list_period_drafts(
      graph_id=graph_id, period=period, client=self._get_client()
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"List period drafts failed: {response.status_code}")
    return response.parsed

  # ── Schedule mutations ──────────────────────────────────────────────

  def truncate_schedule(
    self,
    graph_id: str,
    structure_id: str,
    new_end_date: str,
    reason: str,
  ) -> Any:
    """Truncate a schedule — end it early.

    Deletes facts with `period_start > new_end_date` along with any stale
    draft entries they produced. Historical posted facts are preserved.
    `new_end_date` must be a month-end date (service enforces this).
    """
    from ..models.truncate_schedule_request import TruncateScheduleRequest

    body = TruncateScheduleRequest(
      new_end_date=datetime.date.fromisoformat(new_end_date),
      reason=reason,
    )
    response = truncate_schedule(
      graph_id=graph_id,
      structure_id=structure_id,
      body=body,
      client=self._get_client(),
    )
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Truncate schedule failed: {response.status_code}")
    return response.parsed

  def create_manual_closing_entry(
    self,
    graph_id: str,
    *,
    posting_date: str,
    memo: str,
    line_items: list[dict[str, Any]],
    entry_type: str | None = None,
  ) -> Any:
    """Create a manual draft closing entry with arbitrary balanced line items.

    Not tied to a schedule — used for disposals, adjustments, and other
    one-off closing events. Line items must sum to balanced debits/credits.
    Rejects entries targeting an already-closed period.

    Each line item dict should have:
      element_id (str), debit_amount (int, cents), credit_amount (int, cents),
      description (str | None, optional).
    """
    from ..models.create_manual_closing_entry_request import (
      CreateManualClosingEntryRequest,
    )
    from ..models.create_manual_closing_entry_request_entry_type import (
      CreateManualClosingEntryRequestEntryType,
    )
    from ..models.manual_line_item_request import ManualLineItemRequest

    items = [
      ManualLineItemRequest(
        element_id=li["element_id"],
        debit_amount=li.get("debit_amount", 0),
        credit_amount=li.get("credit_amount", 0),
        description=li.get("description")
        if li.get("description") is not None
        else UNSET,
      )
      for li in line_items
    ]
    body = CreateManualClosingEntryRequest(
      posting_date=datetime.date.fromisoformat(posting_date),
      memo=memo,
      line_items=items,
      entry_type=CreateManualClosingEntryRequestEntryType(entry_type)
      if entry_type is not None
      else UNSET,
    )
    response = create_manual_closing_entry(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    if response.status_code != HTTPStatus.CREATED:
      raise RuntimeError(f"Create manual closing entry failed: {response.status_code}")
    return response.parsed
