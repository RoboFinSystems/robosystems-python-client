"""Unit tests for InvestorClient.

Mirrors the LedgerClient test pattern: GraphQL reads patched at
`GraphQLClient.execute`, REST writes patched at the `op_*` imports on
`investor_client`.
"""

from __future__ import annotations

from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest

from robosystems_client.clients.investor_client import InvestorClient
from robosystems_client.models.operation_envelope import OperationEnvelope
from robosystems_client.models.operation_envelope_status import OperationEnvelopeStatus


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


_SAMPLE_BLOCK_RESULT = {
  "id": "port_new",
  "name": "New Fund",
  "description": None,
  "strategy": "growth",
  "inception_date": "2026-01-01",
  "base_currency": "USD",
  "owner": {"id": "ent_owner", "name": "Family Office", "source_graph_id": None},
  "positions": [
    {
      "id": "pos_new",
      "quantity": 100,
      "quantity_type": "shares",
      "cost_basis_dollars": 1000,
      "current_value_dollars": None,
      "valuation_date": None,
      "valuation_source": None,
      "acquisition_date": "2026-01-01",
      "status": "active",
      "notes": None,
      "security": {
        "id": "sec_1",
        "name": "Series A Preferred",
        "security_type": "common_stock",
        "security_subtype": None,
        "is_active": True,
        "issuer": {"id": "ent_issuer", "name": "ACME", "source_graph_id": "kg_acme"},
        "source_graph_id": "kg_acme",
      },
    }
  ],
  "total_cost_basis_dollars": 1000,
  "total_current_value_dollars": None,
  "active_position_count": 1,
  "created_at": "2026-04-14T00:00:00Z",
  "updated_at": "2026-04-14T00:00:00Z",
}


@pytest.mark.unit
class TestInvestorClientInit:
  def test_initialization(self, mock_config):
    client = InvestorClient(mock_config)
    assert client.base_url == "http://localhost:8000"
    assert client.token == "test-api-key"

  def test_no_token_raises(self, mock_config):
    mock_config["token"] = None
    client = InvestorClient(mock_config)
    with pytest.raises(RuntimeError, match="No API key"):
      client._get_client()


# ── Portfolio reads ────────────────────────────────────────────────────


@pytest.mark.unit
class TestPortfolioReads:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_portfolios(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "portfolios": {
        "portfolios": [
          {
            "id": "port_1",
            "name": "Seed Fund I",
            "description": None,
            "strategy": "early-stage",
            "inceptionDate": "2024-01-01",
            "baseCurrency": "USD",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z",
          }
        ],
        "pagination": {"total": 1, "limit": 100, "offset": 0, "hasMore": False},
      }
    }
    client = InvestorClient(mock_config)
    result = client.list_portfolios(graph_id)
    assert result is not None
    assert len(result["portfolios"]) == 1
    assert result["portfolios"][0]["name"] == "Seed Fund I"
    assert result["portfolios"][0]["base_currency"] == "USD"

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_portfolio_block_missing(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {"portfolioBlock": None}
    client = InvestorClient(mock_config)
    assert client.get_portfolio_block(graph_id, "port_x") is None

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_portfolio_block_found(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "portfolioBlock": {
        "id": "port_1",
        "name": "Seed Fund I",
        "description": None,
        "strategy": "early-stage",
        "inceptionDate": "2024-01-01",
        "baseCurrency": "USD",
        "owner": {"id": "ent_owner", "name": "FO", "sourceGraphId": None},
        "positions": [],
        "totalCostBasisDollars": 0,
        "totalCurrentValueDollars": None,
        "activePositionCount": 0,
        "createdAt": "2024-01-01T00:00:00Z",
        "updatedAt": "2024-01-01T00:00:00Z",
      }
    }
    client = InvestorClient(mock_config)
    result = client.get_portfolio_block(graph_id, "port_1")
    assert result is not None
    assert result["id"] == "port_1"
    assert result["owner"]["name"] == "FO"
    assert result["positions"] == []


# ── Portfolio block writes ─────────────────────────────────────────────


@pytest.mark.unit
class TestPortfolioBlockWrites:
  @patch("robosystems_client.clients.investor_client.op_create_portfolio_block")
  def test_create_portfolio_block(self, mock_op, mock_config, graph_id):
    envelope = _envelope("create-portfolio-block", _SAMPLE_BLOCK_RESULT)
    mock_op.return_value = _mock_response(envelope)
    client = InvestorClient(mock_config)
    result = client.create_portfolio_block(
      graph_id,
      {
        "portfolio": {"name": "New Fund", "strategy": "growth"},
        "positions": [{"security_id": "sec_1", "quantity": 100, "cost_basis": 100000}],
      },
    )
    assert result["id"] == "port_new"
    assert result["owner"]["name"] == "Family Office"
    assert len(result["positions"]) == 1

  @patch("robosystems_client.clients.investor_client.op_update_portfolio_block")
  def test_update_portfolio_block_merges_id(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "update-portfolio-block", {**_SAMPLE_BLOCK_RESULT, "name": "Renamed Fund"}
    )
    mock_op.return_value = _mock_response(envelope)
    client = InvestorClient(mock_config)
    result = client.update_portfolio_block(
      graph_id,
      "port_1",
      {
        "portfolio": {"name": "Renamed Fund"},
        "positions": {"dispose": [{"id": "pos_old"}]},
      },
    )
    assert result["name"] == "Renamed Fund"
    body = mock_op.call_args.kwargs["body"]
    assert body.portfolio_id == "port_1"

  @patch("robosystems_client.clients.investor_client.op_delete_portfolio_block")
  def test_delete_portfolio_block_default_no_confirm(
    self, mock_op, mock_config, graph_id
  ):
    envelope = _envelope("delete-portfolio-block", {"deleted": True})
    mock_op.return_value = _mock_response(envelope)
    client = InvestorClient(mock_config)
    result = client.delete_portfolio_block(graph_id, "port_1")
    assert result["deleted"] is True
    body = mock_op.call_args.kwargs["body"]
    assert body.confirm_active_positions is False

  @patch("robosystems_client.clients.investor_client.op_delete_portfolio_block")
  def test_delete_portfolio_block_confirm_flag(self, mock_op, mock_config, graph_id):
    envelope = _envelope("delete-portfolio-block", {"deleted": True})
    mock_op.return_value = _mock_response(envelope)
    client = InvestorClient(mock_config)
    client.delete_portfolio_block(graph_id, "port_1", confirm_active_positions=True)
    body = mock_op.call_args.kwargs["body"]
    assert body.confirm_active_positions is True

  @patch("robosystems_client.clients.investor_client.op_delete_portfolio_block")
  def test_delete_portfolio_block_stubs_when_result_is_none(
    self, mock_op, mock_config, graph_id
  ):
    envelope = _envelope("delete-portfolio-block", None)
    mock_op.return_value = _mock_response(envelope)
    client = InvestorClient(mock_config)
    result = client.delete_portfolio_block(graph_id, "port_1")
    assert result == {"deleted": True}


# ── Securities ─────────────────────────────────────────────────────────


@pytest.mark.unit
class TestSecurities:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_securities_forwards_entity_filter(
    self, mock_execute, mock_config, graph_id
  ):
    mock_execute.return_value = {
      "securities": {
        "securities": [],
        "pagination": {"total": 0, "limit": 100, "offset": 0, "hasMore": False},
      }
    }
    client = InvestorClient(mock_config)
    client.list_securities(graph_id, entity_id="ent_1")
    variables = mock_execute.call_args[0][2]
    assert variables["entityId"] == "ent_1"
    # None filters are stripped so Strawberry sees them as "not provided"
    assert "securityType" not in variables
    assert "isActive" not in variables

  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_securities_all_none_filters_stripped(
    self, mock_execute, mock_config, graph_id
  ):
    mock_execute.return_value = {
      "securities": {
        "securities": [],
        "pagination": {"total": 0, "limit": 100, "offset": 0, "hasMore": False},
      }
    }
    client = InvestorClient(mock_config)
    client.list_securities(graph_id)
    variables = mock_execute.call_args[0][2]
    # Pagination defaults stay; every optional filter is gone.
    assert variables == {"limit": 100, "offset": 0}

  @patch("robosystems_client.clients.investor_client.op_create_security")
  def test_create_security(self, mock_op, mock_config, graph_id):
    envelope = _envelope(
      "create-security",
      {
        "id": "sec_new",
        "name": "Series A Preferred",
        "security_type": "equity",
        "entity_id": "ent_1",
      },
    )
    mock_op.return_value = _mock_response(envelope)
    client = InvestorClient(mock_config)
    result = client.create_security(
      graph_id,
      {
        "name": "Series A Preferred",
        "security_type": "equity",
        "entity_id": "ent_1",
      },
    )
    assert result["id"] == "sec_new"


# ── Positions (read-only) ──────────────────────────────────────────────


@pytest.mark.unit
class TestPositions:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_list_positions(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "positions": {
        "positions": [
          {
            "id": "pos_1",
            "portfolioId": "port_1",
            "securityId": "sec_1",
            "securityName": "Series A Preferred",
            "entityName": "ACME",
            "quantity": 100,
            "quantityType": "shares",
            "costBasis": 100000,
            "costBasisDollars": 1000,
            "currency": "USD",
            "currentValue": None,
            "currentValueDollars": None,
            "valuationDate": None,
            "valuationSource": None,
            "acquisitionDate": "2026-01-01",
            "dispositionDate": None,
            "status": "active",
            "notes": None,
            "createdAt": "2026-01-01T00:00:00Z",
            "updatedAt": "2026-01-01T00:00:00Z",
          }
        ],
        "pagination": {"total": 1, "limit": 100, "offset": 0, "hasMore": False},
      }
    }
    client = InvestorClient(mock_config)
    result = client.list_positions(graph_id)
    assert result is not None
    assert len(result["positions"]) == 1
    assert result["positions"][0]["cost_basis_dollars"] == 1000


# ── Holdings ───────────────────────────────────────────────────────────


@pytest.mark.unit
class TestHoldings:
  @patch("robosystems_client.graphql.client.GraphQLClient.execute")
  def test_get_holdings(self, mock_execute, mock_config, graph_id):
    mock_execute.return_value = {
      "holdings": {
        "totalEntities": 1,
        "totalPositions": 2,
        "holdings": [
          {
            "entityId": "ent_1",
            "entityName": "ACME",
            "sourceGraphId": None,
            "totalCostBasisDollars": 2000,
            "totalCurrentValueDollars": 2500,
            "positionCount": 2,
            "securities": [
              {
                "securityId": "sec_1",
                "securityName": "Series A Preferred",
                "securityType": "equity",
                "quantity": 100,
                "quantityType": "shares",
                "costBasisDollars": 1000,
                "currentValueDollars": 1250,
              }
            ],
          }
        ],
      }
    }
    client = InvestorClient(mock_config)
    holdings = client.get_holdings(graph_id, "port_1")
    assert holdings is not None
    assert holdings["total_entities"] == 1
    assert holdings["holdings"][0]["securities"][0]["security_id"] == "sec_1"
