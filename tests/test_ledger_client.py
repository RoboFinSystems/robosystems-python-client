"""Unit tests for LedgerClient.

LedgerClient speaks two wire protocols:

1. Reads → GraphQL at POST /extensions/{graph_id}/graphql
2. Writes → POST /extensions/roboledger/{graph_id}/operations/{name}

These tests mock at the function-import boundary: GraphQL reads patch
`GraphQLClient.execute`, and REST writes patch the `op_*` callables that
`ledger_client` imported at module level.
"""

from __future__ import annotations

from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest

from robosystems_client.extensions.ledger_client import LedgerClient
from robosystems_client.models.operation_envelope import OperationEnvelope
from robosystems_client.models.operation_envelope_status import OperationEnvelopeStatus


# ── Helpers ────────────────────────────────────────────────────────────


def _envelope(
  operation: str,
  result: dict | list | None,
  status: OperationEnvelopeStatus = OperationEnvelopeStatus.COMPLETED,
) -> OperationEnvelope:
  return OperationEnvelope(
    operation=operation,
    operation_id=f"op_{operation.upper()}_01",
    status=status,
    result=result,
    at="2026-04-14T12:00:00Z",
  )


def _mock_response(
  envelope: OperationEnvelope, status_code: int = HTTPStatus.OK
) -> Mock:
  resp = Mock()
  resp.status_code = status_code
  resp.parsed = envelope
  resp.content = b""
  return resp


# ── Init ───────────────────────────────────────────────────────────────


@pytest.mark.unit
class TestLedgerClientInit:
  def test_client_initialization(self, mock_config):
    client = LedgerClient(mock_config)
    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"
    assert client.headers == {"X-API-Key": "test-api-key"}
    assert client.timeout == 60

  def test_get_client_no_token(self, mock_config):
    mock_config["token"] = None
    client = LedgerClient(mock_config)
    with pytest.raises(RuntimeError, match="No API key"):
      client._get_client()

  def test_get_graphql_client_no_token(self, mock_config):
    mock_config["token"] = None
    client = LedgerClient(mock_config)
    with pytest.raises(RuntimeError, match="No API key"):
      client._get_graphql_client()


# ── Reads (GraphQL) ────────────────────────────────────────────────────


@pytest.mark.unit
class TestLedgerReads:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_entity_returns_dict(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "entity": {
        "id": "ent_1",
        "name": "ACME Corp",
        "legalName": "ACME Corporation Inc.",
        "entityType": "corporation",
        "status": "active",
      }
    }
    client = LedgerClient(mock_config)
    entity = client.get_entity(graph_id)
    assert entity is not None
    assert entity["id"] == "ent_1"
    assert entity["legal_name"] == "ACME Corporation Inc."
    assert entity["entity_type"] == "corporation"
    # graph_id passed through as first positional arg
    assert mock_execute.call_args[0][0] == graph_id

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_entity_returns_none_when_missing(
    self, mock_execute, mock_config, graph_id
  ):
    mock_execute.return_value = {"entity": None}
    client = LedgerClient(mock_config)
    assert client.get_entity(graph_id) is None

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_entities(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "entities": [
        {
          "id": "ent_1",
          "name": "ACME",
          "legalName": None,
          "ticker": None,
          "cik": None,
          "industry": None,
          "entityType": None,
          "status": "active",
          "isParent": True,
          "parentEntityId": None,
          "source": "qb",
          "sourceGraphId": None,
          "connectionId": None,
          "createdAt": None,
          "updatedAt": None,
        }
      ]
    }
    client = LedgerClient(mock_config)
    entities = client.list_entities(graph_id)
    assert len(entities) == 1
    assert entities[0]["id"] == "ent_1"
    assert entities[0]["is_parent"] is True

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_accounts_with_pagination(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "accounts": {
        "accounts": [
          {
            "id": "acc_1",
            "code": "1000",
            "name": "Cash",
            "description": None,
            "classification": "asset",
            "subClassification": None,
            "balanceType": "debit",
            "parentId": None,
            "depth": 0,
            "currency": "USD",
            "isActive": True,
            "isPlaceholder": False,
            "accountType": None,
            "externalId": None,
            "externalSource": None,
          }
        ],
        "pagination": {"total": 1, "limit": 100, "offset": 0, "hasMore": False},
      }
    }
    client = LedgerClient(mock_config)
    result = client.list_accounts(graph_id, classification="asset", limit=50)
    assert result is not None
    assert len(result["accounts"]) == 1
    assert result["accounts"][0]["sub_classification"] is None
    assert result["pagination"]["has_more"] is False
    # Variables forwarded (positional call from ledger_client._query)
    variables = mock_execute.call_args[0][2]
    assert variables["classification"] == "asset"
    assert variables["limit"] == 50

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_trial_balance(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "trialBalance": {
        "totalDebits": 1000,
        "totalCredits": 1000,
        "rows": [],
      }
    }
    client = LedgerClient(mock_config)
    tb = client.get_trial_balance(
      graph_id, start_date="2026-01-01", end_date="2026-03-31"
    )
    assert tb["total_debits"] == 1000
    variables = mock_execute.call_args[0][2]
    assert variables["startDate"] == "2026-01-01"
    assert variables["endDate"] == "2026-03-31"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_mappings_unwraps_structures(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "mappings": {
        "structures": [
          {
            "id": "map_1",
            "name": "CoA → GAAP",
            "description": None,
            "structureType": "coa_mapping",
            "taxonomyId": "tax_usgaap",
            "isActive": True,
          }
        ]
      }
    }
    client = LedgerClient(mock_config)
    mappings = client.list_mappings(graph_id)
    assert len(mappings) == 1
    assert mappings[0]["structure_type"] == "coa_mapping"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_fiscal_calendar(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "fiscalCalendar": {
        "graphId": graph_id,
        "fiscalYearStartMonth": 1,
        "closedThrough": "2026-02",
        "closeTarget": "2026-03",
        "gapPeriods": 0,
        "catchUpSequence": [],
        "closeableNow": True,
        "blockers": [],
        "lastCloseAt": None,
        "initializedAt": "2026-01-01T00:00:00Z",
        "lastSyncAt": None,
        "periods": [],
      }
    }
    client = LedgerClient(mock_config)
    cal = client.get_fiscal_calendar(graph_id)
    assert cal["closed_through"] == "2026-02"
    assert cal["closeable_now"] is True
    assert cal["fiscal_year_start_month"] == 1


# ── Writes (Operation envelope) ────────────────────────────────────────


@pytest.mark.unit
class TestLedgerWrites:
  @patch("robosystems_client.extensions.ledger_client.op_update_entity")
  def test_update_entity_unwraps_envelope(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "update-entity",
      {"id": "ent_1", "name": "New Name", "status": "active"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.update_entity(graph_id, {"name": "New Name"})
    assert result["name"] == "New Name"
    assert mock_op.called
    assert mock_op.call_args.kwargs["graph_id"] == graph_id

  @patch("robosystems_client.extensions.ledger_client.op_update_entity")
  def test_update_entity_raises_on_4xx(self, mock_op, mock_config, graph_id):
    resp = Mock()
    resp.status_code = 400
    resp.parsed = None
    resp.content = b'{"detail":"No fields"}'
    mock_op.return_value = resp
    client = LedgerClient(mock_config)
    with pytest.raises(RuntimeError, match="Update entity failed"):
      client.update_entity(graph_id, {})

  @patch("robosystems_client.extensions.ledger_client.op_initialize_ledger")
  def test_initialize_ledger(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "initialize",
      {
        "periods_created": 12,
        "warnings": [],
        "fiscal_calendar": {
          "graph_id": graph_id,
          "fiscal_year_start_month": 1,
          "closed_through": None,
          "close_target": None,
        },
      },
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.initialize_ledger(graph_id, fiscal_year_start_month=1)
    assert result["periods_created"] == 12

  @patch("robosystems_client.extensions.ledger_client.op_close_period")
  def test_close_period(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "close-period",
      {
        "period": "2026-03",
        "entries_posted": 5,
        "target_auto_advanced": True,
        "fiscal_calendar": {},
      },
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.close_period(graph_id, "2026-03", allow_stale_sync=True)
    assert result["entries_posted"] == 5
    body = mock_op.call_args.kwargs["body"]
    assert body.period == "2026-03"
    assert body.allow_stale_sync is True

  @patch("robosystems_client.extensions.ledger_client.op_create_schedule")
  def test_create_schedule(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-schedule",
      {
        "structure_id": "str_1",
        "name": "Depreciation",
        "taxonomy_id": "tax_dep",
        "total_periods": 36,
        "total_facts": 36,
      },
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.create_schedule(
      graph_id,
      name="Depreciation",
      element_ids=["elem_1"],
      period_start="2026-01-01",
      period_end="2028-12-31",
      monthly_amount=100000,
      debit_element_id="elem_depr_exp",
      credit_element_id="elem_accum_depr",
    )
    assert result["total_periods"] == 36

  @patch("robosystems_client.extensions.ledger_client.op_auto_map_elements")
  def test_auto_map_elements_returns_ack(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "auto-map-elements", None, status=OperationEnvelopeStatus.PENDING
    )
    mock_op.return_value = _mock_response(envelope, status_code=HTTPStatus.ACCEPTED)
    client = LedgerClient(mock_config)
    ack = client.auto_map_elements(graph_id, "map_1")
    assert ack["operation_id"].startswith("op_")
    assert ack["status"] == OperationEnvelopeStatus.PENDING

  @patch("robosystems_client.extensions.ledger_client.op_create_closing_entry")
  def test_create_closing_entry(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-closing-entry",
      {
        "outcome": "created",
        "entry_id": "entry_1",
        "status": "draft",
        "amount": 100000,
      },
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.create_closing_entry(
      graph_id, "str_1", "2026-03-31", "2026-03-01", "2026-03-31", memo="Depr"
    )
    assert result["outcome"] == "created"
    body = mock_op.call_args.kwargs["body"]
    assert body.memo == "Depr"

  @patch("robosystems_client.extensions.ledger_client.op_truncate_schedule")
  def test_truncate_schedule(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "truncate-schedule",
      {
        "structure_id": "str_1",
        "new_end_date": "2026-06-30",
        "facts_deleted": 6,
        "reason": "asset disposed",
      },
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.truncate_schedule(
      graph_id, "str_1", new_end_date="2026-06-30", reason="asset disposed"
    )
    assert result["facts_deleted"] == 6

  @patch("robosystems_client.extensions.ledger_client.op_build_fact_grid")
  def test_build_fact_grid_dispatches_via_operations(
    self, mock_op, mock_config, graph_id
  ):
    envelope = _envelope(
      "build-fact-grid",
      {
        "rows": [
          {"element": "us-gaap:Revenues", "period": "2026-03-31", "value": 1000000},
        ],
        "row_count": 1,
      },
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.build_fact_grid(
      graph_id,
      {
        "elements": ["us-gaap:Revenues"],
        "periods": ["2026-03-31"],
        "include_summary": False,
      },
    )
    assert result["row_count"] == 1
    assert result["rows"][0]["value"] == 1000000
    # Body serialized into the generated CreateViewRequest attrs model
    call_kwargs = mock_op.call_args.kwargs
    assert call_kwargs["graph_id"] == graph_id
    body = call_kwargs["body"]
    assert body.elements == ["us-gaap:Revenues"]
    assert body.periods == ["2026-03-31"]
    assert body.include_summary is False


# ── Journal entries ────────────────────────────────────────────────────


@pytest.mark.unit
class TestJournalEntries:
  _LINE_ITEMS = [
    {"element_id": "elem_cash", "debit_amount": 50000, "credit_amount": 0},
    {"element_id": "elem_revenue", "debit_amount": 0, "credit_amount": 50000},
  ]

  @patch("robosystems_client.extensions.ledger_client.op_create_journal_entry")
  def test_create_journal_entry_basic(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-journal-entry",
      {"entry_id": "je_1", "status": "draft", "memo": "Q1 revenue"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.create_journal_entry(
      graph_id,
      posting_date="2026-03-31",
      memo="Q1 revenue",
      line_items=self._LINE_ITEMS,
    )
    assert result["entry_id"] == "je_1"
    assert result["status"] == "draft"
    call_kwargs = mock_op.call_args.kwargs
    assert call_kwargs["graph_id"] == graph_id
    assert call_kwargs["idempotency_key"] is None
    body = call_kwargs["body"]
    assert body.memo == "Q1 revenue"
    assert len(body.line_items) == 2

  @patch("robosystems_client.extensions.ledger_client.op_create_journal_entry")
  def test_create_journal_entry_idempotency_key_forwarded(
    self, mock_op, mock_config, graph_id
  ):
    envelope = _envelope(
      "create-journal-entry",
      {"entry_id": "je_2", "status": "draft", "memo": "retry-safe write"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    client.create_journal_entry(
      graph_id,
      posting_date="2026-03-31",
      memo="retry-safe write",
      line_items=self._LINE_ITEMS,
      idempotency_key="idem-key-abc123",
    )
    assert mock_op.call_args.kwargs["idempotency_key"] == "idem-key-abc123"

  @patch("robosystems_client.extensions.ledger_client.op_create_journal_entry")
  def test_create_journal_entry_posted_status(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-journal-entry",
      {"entry_id": "je_3", "status": "posted"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    client.create_journal_entry(
      graph_id,
      posting_date="2025-12-31",
      memo="Historical import",
      line_items=self._LINE_ITEMS,
      status="posted",
    )
    body = mock_op.call_args.kwargs["body"]
    assert body.status.value == "posted"

  @patch("robosystems_client.extensions.ledger_client.op_update_journal_entry")
  def test_update_journal_entry(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "update-journal-entry",
      {"entry_id": "je_1", "memo": "Updated memo", "status": "draft"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.update_journal_entry(
      graph_id, {"entry_id": "je_1", "memo": "Updated memo"}
    )
    assert result["memo"] == "Updated memo"
    assert mock_op.call_args.kwargs["graph_id"] == graph_id

  @patch("robosystems_client.extensions.ledger_client.op_delete_journal_entry")
  def test_delete_journal_entry_returns_deleted_sentinel(
    self, mock_op, mock_config, graph_id
  ):
    envelope = _envelope("delete-journal-entry", None)
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.delete_journal_entry(graph_id, "je_1")
    assert result == {"deleted": True}
    body = mock_op.call_args.kwargs["body"]
    assert body.entry_id == "je_1"

  @patch("robosystems_client.extensions.ledger_client.op_delete_journal_entry")
  def test_delete_journal_entry_returns_result_when_present(
    self, mock_op, mock_config, graph_id
  ):
    envelope = _envelope("delete-journal-entry", {"entry_id": "je_1"})
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.delete_journal_entry(graph_id, "je_1")
    assert result["entry_id"] == "je_1"

  @patch("robosystems_client.extensions.ledger_client.op_reverse_journal_entry")
  def test_reverse_journal_entry(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "reverse-journal-entry",
      {
        "original_entry_id": "je_1",
        "reversal_entry_id": "je_2",
        "posting_date": "2026-04-01",
      },
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.reverse_journal_entry(
      graph_id, "je_1", posting_date="2026-04-01", memo="Reversal of Q1 entry"
    )
    assert result["reversal_entry_id"] == "je_2"
    body = mock_op.call_args.kwargs["body"]
    assert body.entry_id == "je_1"
    assert body.memo == "Reversal of Q1 entry"


# ── Taxonomy / entity linking ───────────────────────────────────────────


@pytest.mark.unit
class TestLinkEntityTaxonomy:
  @patch("robosystems_client.extensions.ledger_client.op_link_entity_taxonomy")
  def test_link_entity_taxonomy_uses_sdk_op(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "link-entity-taxonomy",
      {"taxonomy_id": "tax_coa_1", "basis": "chart_of_accounts", "is_primary": True},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.link_entity_taxonomy(graph_id, taxonomy_id="tax_coa_1")
    assert result["taxonomy_id"] == "tax_coa_1"
    assert mock_op.called
    call_kwargs = mock_op.call_args.kwargs
    assert call_kwargs["graph_id"] == graph_id

  @patch("robosystems_client.extensions.ledger_client.op_link_entity_taxonomy")
  def test_link_entity_taxonomy_forwards_all_params(
    self, mock_op, mock_config, graph_id
  ):
    envelope = _envelope("link-entity-taxonomy", {"taxonomy_id": "tax_rep_1"})
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    client.link_entity_taxonomy(
      graph_id,
      taxonomy_id="tax_rep_1",
      basis="reporting",
      is_primary=False,
      adoption_context="required",
    )
    body = mock_op.call_args.kwargs["body"]
    assert body.taxonomy_id == "tax_rep_1"
    assert body.basis.value == "reporting"
    assert body.is_primary is False
    assert body.adoption_context == "required"

  @patch("robosystems_client.extensions.ledger_client.op_link_entity_taxonomy")
  def test_link_entity_taxonomy_raises_on_error(self, mock_op, mock_config, graph_id):
    resp = Mock()
    resp.status_code = 404
    resp.parsed = None
    resp.content = b'{"detail":"entity not found"}'
    mock_op.return_value = resp
    client = LedgerClient(mock_config)
    with pytest.raises(RuntimeError, match="Link entity taxonomy failed"):
      client.link_entity_taxonomy(graph_id, taxonomy_id="tax_missing")


# ── Additional reads (GraphQL) ─────────────────────────────────────────


@pytest.mark.unit
class TestLedgerReadsAdditional:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_summary(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "summary": {
        "graphId": graph_id,
        "accountCount": 120,
        "transactionCount": 500,
        "entryCount": 300,
        "lineItemCount": 900,
        "earliestTransactionDate": "2025-01-01",
        "latestTransactionDate": "2026-03-31",
        "connectionCount": 2,
        "lastSyncAt": None,
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_summary(graph_id)
    assert result is not None
    assert result["account_count"] == 120
    assert result["transaction_count"] == 500

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_summary_returns_none_when_missing(
    self, mock_execute, mock_config, graph_id
  ):
    mock_execute.return_value = {"summary": None}
    client = LedgerClient(mock_config)
    assert client.get_summary(graph_id) is None

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_account_tree(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "accountTree": {
        "totalAccounts": 3,
        "roots": [
          {
            "id": "acc_1",
            "code": "1000",
            "name": "Assets",
            "classification": "asset",
            "accountType": None,
            "balanceType": "debit",
            "depth": 0,
            "isActive": True,
            "children": [],
          }
        ],
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_account_tree(graph_id)
    assert result is not None
    assert result["total_accounts"] == 3
    assert result["roots"][0]["code"] == "1000"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_account_rollups(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "accountRollups": {
        "mappingId": "map_1",
        "mappingName": "CoA → GAAP",
        "totalMapped": 80,
        "totalUnmapped": 5,
        "groups": [],
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_account_rollups(
      graph_id, mapping_id="map_1", start_date="2026-01-01", end_date="2026-03-31"
    )
    assert result is not None
    assert result["total_mapped"] == 80
    variables = mock_execute.call_args[0][2]
    assert variables["mappingId"] == "map_1"
    assert variables["startDate"] == "2026-01-01"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_transactions(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "transactions": {
        "transactions": [
          {
            "id": "tx_1",
            "number": "INV-001",
            "type": "invoice",
            "category": None,
            "amount": 100000,
            "currency": "USD",
            "date": "2026-03-15",
            "dueDate": None,
            "merchantName": None,
            "referenceNumber": None,
            "description": "Q1 invoice",
            "source": "qb",
            "status": "open",
          }
        ],
        "pagination": {"total": 1, "limit": 100, "offset": 0, "hasMore": False},
      }
    }
    client = LedgerClient(mock_config)
    result = client.list_transactions(
      graph_id, type="invoice", start_date="2026-01-01", end_date="2026-03-31"
    )
    assert result is not None
    assert len(result["transactions"]) == 1
    assert result["transactions"][0]["id"] == "tx_1"
    variables = mock_execute.call_args[0][2]
    assert variables["type"] == "invoice"
    assert variables["startDate"] == "2026-01-01"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_transaction(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "transaction": {
        "id": "tx_1",
        "number": "INV-001",
        "type": "invoice",
        "category": None,
        "amount": 100000,
        "currency": "USD",
        "date": "2026-03-15",
        "dueDate": None,
        "merchantName": None,
        "referenceNumber": None,
        "description": None,
        "source": "qb",
        "sourceId": None,
        "status": "open",
        "postedAt": None,
        "entries": [],
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_transaction(graph_id, "tx_1")
    assert result is not None
    assert result["id"] == "tx_1"
    variables = mock_execute.call_args[0][2]
    assert variables["transactionId"] == "tx_1"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_mapped_trial_balance(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "mappedTrialBalance": {
        "mappingId": "map_1",
        "rows": [
          {
            "reportingElementId": "elem_rev",
            "qname": "us-gaap:Revenues",
            "reportingName": "Revenues",
            "classification": "income",
            "balanceType": "credit",
            "totalDebits": 0,
            "totalCredits": 500000,
            "netBalance": 500000,
          }
        ],
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_mapped_trial_balance(
      graph_id, "map_1", start_date="2026-01-01", end_date="2026-03-31"
    )
    assert result is not None
    assert result["mapping_id"] == "map_1"
    assert len(result["rows"]) == 1
    variables = mock_execute.call_args[0][2]
    assert variables["mappingId"] == "map_1"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_reporting_taxonomy(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "reportingTaxonomy": {
        "id": "tax_usgaap",
        "name": "US GAAP",
        "description": None,
        "taxonomyType": "reporting",
        "version": "2024",
        "standard": "us-gaap",
        "namespaceUri": "http://fasb.org/us-gaap/2024",
        "isShared": True,
        "isActive": True,
        "isLocked": True,
        "sourceTaxonomyId": None,
        "targetTaxonomyId": None,
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_reporting_taxonomy(graph_id)
    assert result is not None
    assert result["standard"] == "us-gaap"
    assert result["is_locked"] is True

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_taxonomies(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "taxonomies": {
        "taxonomies": [
          {
            "id": "tax_coa_1",
            "name": "My CoA",
            "description": None,
            "taxonomyType": "chart_of_accounts",
            "version": None,
            "standard": None,
            "namespaceUri": None,
            "isShared": False,
            "isActive": True,
            "isLocked": False,
            "sourceTaxonomyId": None,
            "targetTaxonomyId": None,
          }
        ]
      }
    }
    client = LedgerClient(mock_config)
    result = client.list_taxonomies(graph_id, taxonomy_type="chart_of_accounts")
    assert len(result) == 1
    assert result[0]["taxonomy_type"] == "chart_of_accounts"
    variables = mock_execute.call_args[0][2]
    assert variables["taxonomyType"] == "chart_of_accounts"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_elements(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "elements": {
        "elements": [
          {
            "id": "elem_1",
            "code": "1000",
            "name": "Cash",
            "description": None,
            "qname": None,
            "namespace": None,
            "classification": "asset",
            "subClassification": None,
            "balanceType": "debit",
            "periodType": None,
            "isAbstract": False,
            "elementType": "account",
            "source": "native",
            "taxonomyId": "tax_coa_1",
            "parentId": None,
            "depth": 0,
            "isActive": True,
            "externalId": None,
            "externalSource": None,
          }
        ],
        "pagination": {"total": 1, "limit": 100, "offset": 0, "hasMore": False},
      }
    }
    client = LedgerClient(mock_config)
    result = client.list_elements(
      graph_id, taxonomy_id="tax_coa_1", classification="asset"
    )
    assert result is not None
    assert len(result["elements"]) == 1
    assert result["elements"][0]["balance_type"] == "debit"
    variables = mock_execute.call_args[0][2]
    assert variables["taxonomyId"] == "tax_coa_1"
    assert variables["classification"] == "asset"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_unmapped_elements(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "unmappedElements": [
        {
          "id": "elem_2",
          "code": "4500",
          "name": "Other Revenue",
          "classification": "income",
          "balanceType": "credit",
          "externalSource": "qb",
          "suggestedTargets": [
            {
              "elementId": "elem_rev",
              "qname": "us-gaap:Revenues",
              "name": "Revenues",
              "confidence": 0.9,
            }
          ],
        }
      ]
    }
    client = LedgerClient(mock_config)
    result = client.list_unmapped_elements(graph_id, mapping_id="map_1")
    assert len(result) == 1
    assert result[0]["code"] == "4500"
    assert result[0]["suggested_targets"][0]["confidence"] == 0.9
    variables = mock_execute.call_args[0][2]
    assert variables["mappingId"] == "map_1"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_structures(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "structures": {
        "structures": [
          {
            "id": "str_1",
            "name": "Income Statement",
            "description": None,
            "structureType": "income_statement",
            "taxonomyId": "tax_usgaap",
            "isActive": True,
          }
        ]
      }
    }
    client = LedgerClient(mock_config)
    result = client.list_structures(graph_id, structure_type="income_statement")
    assert len(result) == 1
    assert result[0]["structure_type"] == "income_statement"
    variables = mock_execute.call_args[0][2]
    assert variables["structureType"] == "income_statement"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_mapping(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "mapping": {
        "id": "map_1",
        "name": "CoA → GAAP",
        "structureType": "coa_mapping",
        "taxonomyId": "tax_usgaap",
        "totalAssociations": 2,
        "associations": [
          {
            "id": "assoc_1",
            "structureId": "map_1",
            "fromElementId": "elem_cash",
            "fromElementName": "Cash",
            "fromElementQname": None,
            "toElementId": "elem_rev",
            "toElementName": "Revenues",
            "toElementQname": "us-gaap:Revenues",
            "associationType": "mapping",
            "orderValue": 0,
            "weight": 1.0,
            "confidence": 1.0,
            "suggestedBy": None,
            "approvedBy": None,
          }
        ],
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_mapping(graph_id, "map_1")
    assert result is not None
    assert result["total_associations"] == 2
    assert len(result["associations"]) == 1
    variables = mock_execute.call_args[0][2]
    assert variables["mappingId"] == "map_1"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_mapping_coverage(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "mappingCoverage": {
        "mappingId": "map_1",
        "totalCoaElements": 100,
        "mappedCount": 80,
        "unmappedCount": 20,
        "coveragePercent": 80.0,
        "highConfidence": 70,
        "mediumConfidence": 10,
        "lowConfidence": 0,
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_mapping_coverage(graph_id, "map_1")
    assert result is not None
    assert result["coverage_percent"] == 80.0
    assert result["unmapped_count"] == 20
    variables = mock_execute.call_args[0][2]
    assert variables["mappingId"] == "map_1"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_schedules(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "schedules": {
        "schedules": [
          {
            "structureId": "str_sched_1",
            "name": "Depreciation",
            "taxonomyName": "My CoA",
            "entryTemplate": {},
            "scheduleMetadata": {},
            "totalPeriods": 36,
            "periodsWithEntries": 3,
          }
        ]
      }
    }
    client = LedgerClient(mock_config)
    result = client.list_schedules(graph_id)
    assert len(result) == 1
    assert result[0]["structure_id"] == "str_sched_1"
    assert result[0]["total_periods"] == 36

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_schedule_facts(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "scheduleFacts": {
        "structureId": "str_sched_1",
        "facts": [
          {
            "elementId": "elem_depr",
            "elementName": "Depreciation Expense",
            "value": 100000,
            "periodStart": "2026-01-01",
            "periodEnd": "2026-01-31",
          }
        ],
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_schedule_facts(
      graph_id, "str_sched_1", period_start="2026-01-01", period_end="2026-03-31"
    )
    assert len(result) == 1
    assert result[0]["value"] == 100000
    variables = mock_execute.call_args[0][2]
    assert variables["structureId"] == "str_sched_1"
    assert variables["periodStart"] == "2026-01-01"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_schedule_facts_returns_empty_list_when_none(
    self, mock_execute, mock_config, graph_id
  ):
    mock_execute.return_value = {"scheduleFacts": None}
    client = LedgerClient(mock_config)
    assert client.get_schedule_facts(graph_id, "str_1") == []

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_period_close_status(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "periodCloseStatus": {
        "fiscalPeriodStart": "2026-03-01",
        "fiscalPeriodEnd": "2026-03-31",
        "periodStatus": "open",
        "totalDraft": 2,
        "totalPosted": 0,
        "schedules": [],
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_period_close_status(graph_id, "2026-03-01", "2026-03-31")
    assert result is not None
    assert result["period_status"] == "open"
    assert result["total_draft"] == 2
    variables = mock_execute.call_args[0][2]
    assert variables["periodStart"] == "2026-03-01"
    assert variables["periodEnd"] == "2026-03-31"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_period_drafts(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "periodDrafts": {
        "period": "2026-03",
        "periodStart": "2026-03-01",
        "periodEnd": "2026-03-31",
        "draftCount": 1,
        "totalDebit": 100000,
        "totalCredit": 100000,
        "allBalanced": True,
        "drafts": [],
      }
    }
    client = LedgerClient(mock_config)
    result = client.list_period_drafts(graph_id, "2026-03")
    assert result is not None
    assert result["all_balanced"] is True
    assert result["draft_count"] == 1
    variables = mock_execute.call_args[0][2]
    assert variables["period"] == "2026-03"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_closing_book_structures(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "closingBookStructures": {
        "hasData": True,
        "categories": [
          {
            "label": "Schedules",
            "items": [
              {
                "id": "str_1",
                "name": "Depreciation",
                "itemType": "schedule",
                "structureType": "schedule",
                "reportId": None,
                "status": None,
              }
            ],
          }
        ],
      }
    }
    client = LedgerClient(mock_config)
    result = client.get_closing_book_structures(graph_id)
    assert result is not None
    assert result["has_data"] is True
    assert len(result["categories"]) == 1
    assert result["categories"][0]["label"] == "Schedules"


# ── Taxonomy ops ────────────────────────────────────────────────────────


@pytest.mark.unit
class TestTaxonomyOps:
  @patch("robosystems_client.extensions.ledger_client.op_create_taxonomy")
  def test_create_taxonomy(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-taxonomy",
      {
        "taxonomy_id": "tax_coa_1",
        "name": "My CoA",
        "taxonomy_type": "chart_of_accounts",
      },
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.create_taxonomy(
      graph_id, {"name": "My CoA", "taxonomy_type": "chart_of_accounts"}
    )
    assert result["taxonomy_id"] == "tax_coa_1"
    assert mock_op.call_args.kwargs["graph_id"] == graph_id

  @patch("robosystems_client.extensions.ledger_client.op_update_taxonomy")
  def test_update_taxonomy(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "update-taxonomy",
      {"taxonomy_id": "tax_coa_1", "name": "Updated CoA"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.update_taxonomy(
      graph_id, {"taxonomy_id": "tax_coa_1", "name": "Updated CoA"}
    )
    assert result["name"] == "Updated CoA"

  @patch("robosystems_client.extensions.ledger_client.op_delete_taxonomy")
  def test_delete_taxonomy(self, mock_op, mock_config, graph_id):
    envelope = _envelope("delete-taxonomy", {"taxonomy_id": "tax_coa_1"})
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.delete_taxonomy(graph_id, "tax_coa_1")
    assert result["taxonomy_id"] == "tax_coa_1"
    body = mock_op.call_args.kwargs["body"]
    assert body.taxonomy_id == "tax_coa_1"


# ── Element ops ─────────────────────────────────────────────────────────


@pytest.mark.unit
class TestElementOps:
  @patch("robosystems_client.extensions.ledger_client.op_create_element")
  def test_create_element(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-element",
      {"element_id": "elem_1", "name": "Cash", "classification": "asset"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.create_element(
      graph_id,
      {
        "name": "Cash",
        "taxonomy_id": "tax_coa_1",
        "classification": "asset",
        "balance_type": "debit",
      },
    )
    assert result["element_id"] == "elem_1"
    assert mock_op.call_args.kwargs["graph_id"] == graph_id

  @patch("robosystems_client.extensions.ledger_client.op_update_element")
  def test_update_element(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "update-element",
      {"element_id": "elem_1", "name": "Cash and Cash Equivalents"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.update_element(
      graph_id, {"element_id": "elem_1", "name": "Cash and Cash Equivalents"}
    )
    assert result["name"] == "Cash and Cash Equivalents"

  @patch("robosystems_client.extensions.ledger_client.op_delete_element")
  def test_delete_element(self, mock_op, mock_config, graph_id):
    envelope = _envelope("delete-element", {"element_id": "elem_1"})
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.delete_element(graph_id, "elem_1")
    assert result["element_id"] == "elem_1"
    body = mock_op.call_args.kwargs["body"]
    assert body.element_id == "elem_1"


# ── Structure ops ───────────────────────────────────────────────────────


@pytest.mark.unit
class TestStructureOps:
  @patch("robosystems_client.extensions.ledger_client.op_create_structure")
  def test_create_structure(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-structure",
      {"structure_id": "str_1", "name": "CoA Mapping", "structure_type": "coa_mapping"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.create_structure(
      graph_id,
      {
        "name": "CoA Mapping",
        "structure_type": "coa_mapping",
        "taxonomy_id": "tax_usgaap",
      },
    )
    assert result["structure_id"] == "str_1"
    assert mock_op.call_args.kwargs["graph_id"] == graph_id

  @patch("robosystems_client.extensions.ledger_client.op_update_structure")
  def test_update_structure(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "update-structure",
      {"structure_id": "str_1", "name": "Updated Mapping"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.update_structure(
      graph_id, {"structure_id": "str_1", "name": "Updated Mapping"}
    )
    assert result["name"] == "Updated Mapping"

  @patch("robosystems_client.extensions.ledger_client.op_delete_structure")
  def test_delete_structure(self, mock_op, mock_config, graph_id):
    envelope = _envelope("delete-structure", {"structure_id": "str_1"})
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.delete_structure(graph_id, "str_1")
    assert result["structure_id"] == "str_1"
    body = mock_op.call_args.kwargs["body"]
    assert body.structure_id == "str_1"

  @patch("robosystems_client.extensions.ledger_client.op_create_structure")
  def test_create_mapping_structure_convenience(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-structure",
      {"structure_id": "str_map_1", "structure_type": "coa_mapping"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.create_mapping_structure(graph_id)
    assert result["structure_type"] == "coa_mapping"
    body = mock_op.call_args.kwargs["body"]
    assert body.structure_type.value == "coa_mapping"
    assert body.taxonomy_id == "tax_usgaap_reporting"


# ── Association ops ─────────────────────────────────────────────────────


@pytest.mark.unit
class TestAssociationOps:
  @patch("robosystems_client.extensions.ledger_client.op_create_mapping_association")
  def test_create_mapping_association(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-mapping-association",
      {"association_id": "assoc_1", "confidence": 1.0},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.create_mapping_association(
      graph_id,
      mapping_id="map_1",
      from_element_id="elem_cash",
      to_element_id="elem_rev",
      confidence=0.95,
    )
    assert result["association_id"] == "assoc_1"
    body = mock_op.call_args.kwargs["body"]
    assert body.mapping_id == "map_1"
    assert body.from_element_id == "elem_cash"
    assert body.confidence == 0.95

  @patch("robosystems_client.extensions.ledger_client.op_delete_mapping_association")
  def test_delete_mapping_association_returns_sentinel(
    self, mock_op, mock_config, graph_id
  ):
    envelope = _envelope("delete-mapping-association", None)
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.delete_mapping_association(graph_id, "map_1", "assoc_1")
    assert result == {"deleted": True}
    body = mock_op.call_args.kwargs["body"]
    assert body.mapping_id == "map_1"
    assert body.association_id == "assoc_1"

  @patch("robosystems_client.extensions.ledger_client.op_create_associations")
  def test_create_associations_bulk(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-associations",
      {"created": 2, "structure_id": "str_1"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.create_associations(
      graph_id,
      structure_id="str_1",
      associations=[
        {
          "from_element_id": "elem_a",
          "to_element_id": "elem_x",
          "association_type": "presentation",
        },
        {
          "from_element_id": "elem_b",
          "to_element_id": "elem_y",
          "association_type": "presentation",
        },
      ],
    )
    assert result["created"] == 2
    body = mock_op.call_args.kwargs["body"]
    assert body.structure_id == "str_1"
    assert len(body.associations) == 2

  @patch("robosystems_client.extensions.ledger_client.op_update_association")
  def test_update_association(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "update-association",
      {"association_id": "assoc_1", "confidence": 0.75},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.update_association(
      graph_id, {"association_id": "assoc_1", "confidence": 0.75}
    )
    assert result["confidence"] == 0.75

  @patch("robosystems_client.extensions.ledger_client.op_delete_association")
  def test_delete_association_returns_sentinel(self, mock_op, mock_config, graph_id):
    envelope = _envelope("delete-association", None)
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.delete_association(graph_id, "assoc_1")
    assert result == {"deleted": True}
    body = mock_op.call_args.kwargs["body"]
    assert body.association_id == "assoc_1"

  @patch("robosystems_client.extensions.ledger_client.op_delete_association")
  def test_delete_association_returns_result_when_present(
    self, mock_op, mock_config, graph_id
  ):
    envelope = _envelope("delete-association", {"association_id": "assoc_1"})
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.delete_association(graph_id, "assoc_1")
    assert result["association_id"] == "assoc_1"


# ── Schedule additional ops ─────────────────────────────────────────────


@pytest.mark.unit
class TestScheduleAdditionalOps:
  @patch("robosystems_client.extensions.ledger_client.op_update_schedule")
  def test_update_schedule(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "update-schedule",
      {"structure_id": "str_sched_1", "name": "Renamed Schedule"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.update_schedule(
      graph_id, {"structure_id": "str_sched_1", "name": "Renamed Schedule"}
    )
    assert result["name"] == "Renamed Schedule"
    assert mock_op.call_args.kwargs["graph_id"] == graph_id

  @patch("robosystems_client.extensions.ledger_client.op_delete_schedule")
  def test_delete_schedule_returns_sentinel(self, mock_op, mock_config, graph_id):
    envelope = _envelope("delete-schedule", None)
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.delete_schedule(graph_id, "str_sched_1")
    assert result == {"deleted": True}
    body = mock_op.call_args.kwargs["body"]
    assert body.structure_id == "str_sched_1"

  @patch("robosystems_client.extensions.ledger_client.op_delete_schedule")
  def test_delete_schedule_returns_result_when_present(
    self, mock_op, mock_config, graph_id
  ):
    envelope = _envelope("delete-schedule", {"structure_id": "str_sched_1"})
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.delete_schedule(graph_id, "str_sched_1")
    assert result["structure_id"] == "str_sched_1"


# ── Period close additional ops ─────────────────────────────────────────


@pytest.mark.unit
class TestPeriodCloseAdditionalOps:
  @patch("robosystems_client.extensions.ledger_client.op_set_close_target")
  def test_set_close_target(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "set-close-target",
      {"period": "2026-03", "close_target": "2026-03"},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.set_close_target(graph_id, "2026-03", note="End of Q1")
    assert result["period"] == "2026-03"
    body = mock_op.call_args.kwargs["body"]
    assert body.period == "2026-03"
    assert body.note == "End of Q1"

  @patch("robosystems_client.extensions.ledger_client.op_reopen_period")
  def test_reopen_period(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "reopen-period",
      {"period": "2026-02", "status": "open", "entries_unposted": 3},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.reopen_period(
      graph_id, "2026-02", reason="Correction required", note="Found error in entry"
    )
    assert result["entries_unposted"] == 3
    body = mock_op.call_args.kwargs["body"]
    assert body.period == "2026-02"
    assert body.reason == "Correction required"
    assert body.note == "Found error in entry"

  @patch("robosystems_client.extensions.ledger_client.op_create_manual_closing_entry")
  def test_create_manual_closing_entry(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-manual-closing-entry",
      {"entry_id": "je_manual_1", "status": "draft", "total_amount": 25000},
    )
    mock_op.return_value = _mock_response(envelope)
    client = LedgerClient(mock_config)
    result = client.create_manual_closing_entry(
      graph_id,
      posting_date="2026-03-31",
      memo="Manual accrual",
      line_items=[
        {"element_id": "elem_exp", "debit_amount": 25000, "credit_amount": 0},
        {"element_id": "elem_accrued", "debit_amount": 0, "credit_amount": 25000},
      ],
      entry_type="adjusting",
    )
    assert result["entry_id"] == "je_manual_1"
    body = mock_op.call_args.kwargs["body"]
    assert body.memo == "Manual accrual"
    assert len(body.line_items) == 2
    assert body.line_items[0].element_id == "elem_exp"
    assert body.line_items[0].debit_amount == 25000
    assert body.entry_type.value == "adjusting"


# ── Variable-stripping behaviour in _query ────────────────────────────


@pytest.mark.unit
class TestLedgerQueryNoneStripping:
  """``_query`` drops ``None`` variables before sending to GraphQL.

  Rationale lives in ``strip_none_vars`` — some Strawberry resolvers
  treat ``isActive: null`` as "filter for inactive" rather than "not
  provided". The facade takes ``None`` to mean "not provided".
  """

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_accounts_strips_none_filters(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {"accounts": {"accounts": [], "pagination": {}}}
    client = LedgerClient(mock_config)
    client.list_accounts(graph_id, classification=None, is_active=None, limit=25)
    # Only the non-None variables are forwarded
    variables = mock_execute.call_args[0][2]
    assert variables == {"limit": 25, "offset": 0}
    assert "classification" not in variables
    assert "isActive" not in variables

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_accounts_keeps_explicitly_set_filters(
    self, mock_execute, mock_config, graph_id
  ):
    mock_execute.return_value = {"accounts": {"accounts": [], "pagination": {}}}
    client = LedgerClient(mock_config)
    client.list_accounts(graph_id, classification="asset", is_active=True)
    variables = mock_execute.call_args[0][2]
    assert variables["classification"] == "asset"
    assert variables["isActive"] is True
    # And False (falsy but not None) is also kept
    client.list_accounts(graph_id, is_active=False)
    variables = mock_execute.call_args[0][2]
    assert variables["isActive"] is False
