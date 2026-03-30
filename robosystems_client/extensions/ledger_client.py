"""Ledger Client for RoboSystems API

High-level client for all ledger concerns: chart of accounts, transactions,
trial balance, taxonomy, mappings, and AI auto-mapping.
"""

from __future__ import annotations

from http import HTTPStatus
from typing import Any

from ..api.ledger.auto_map_elements import sync_detailed as auto_map_elements
from ..api.ledger.create_mapping_association import (
  sync_detailed as create_mapping_association,
)
from ..api.ledger.create_structure import sync_detailed as create_structure
from ..api.ledger.delete_mapping_association import (
  sync_detailed as delete_mapping_association,
)
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
from ..api.ledger.get_reporting_taxonomy import (
  sync_detailed as get_reporting_taxonomy,
)
from ..api.ledger.list_elements import sync_detailed as list_elements
from ..api.ledger.list_ledger_accounts import (
  sync_detailed as list_ledger_accounts,
)
from ..api.ledger.list_ledger_transactions import (
  sync_detailed as list_ledger_transactions,
)
from ..api.ledger.list_mappings import sync_detailed as list_mappings
from ..api.ledger.list_structures import sync_detailed as list_structures
from ..client import AuthenticatedClient


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
    from ..models.create_mapping_association_request import (
      CreateMappingAssociationRequest,
    )

    body = CreateMappingAssociationRequest(
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
