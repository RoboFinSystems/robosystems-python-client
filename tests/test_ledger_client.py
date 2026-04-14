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
