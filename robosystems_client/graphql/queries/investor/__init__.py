"""Investor-domain GraphQL queries and parsers.

All investor reads from the `/extensions/{graph_id}/graphql` endpoint
live here. Same pattern as the ledger queries: one constant + one
`parse_*` helper per query, returning camelCase → snake_case dicts.

Portfolio reads go through the `portfolioBlock` molecule envelope —
the singular `portfolio(id)` field has been retired in favor of the
block. List portfolios remains for collection scans.
"""

from __future__ import annotations

from typing import Any

from ...client import keys_to_snake


# ── Portfolios ─────────────────────────────────────────────────────────

LIST_PORTFOLIOS_QUERY = """
query ListInvestorPortfolios($limit: Int! = 100, $offset: Int! = 0) {
  portfolios(limit: $limit, offset: $offset) {
    portfolios {
      id name description strategy
      inceptionDate baseCurrency
      createdAt updatedAt
    }
    pagination { total limit offset hasMore }
  }
}
""".strip()


def parse_portfolios(data: dict[str, Any]) -> dict[str, Any] | None:
  p = data.get("portfolios")
  return keys_to_snake(p) if p is not None else None


# ── Portfolio Block (molecule envelope) ────────────────────────────────

GET_PORTFOLIO_BLOCK_QUERY = """
query GetInvestorPortfolioBlock($portfolioId: String!) {
  portfolioBlock(portfolioId: $portfolioId) {
    id name description strategy
    inceptionDate baseCurrency
    owner { id name sourceGraphId }
    positions {
      id quantity quantityType
      costBasisDollars currentValueDollars
      valuationDate valuationSource
      acquisitionDate
      status notes
      security {
        id name securityType securitySubtype
        isActive sourceGraphId
        issuer { id name sourceGraphId }
      }
    }
    totalCostBasisDollars totalCurrentValueDollars
    activePositionCount
    createdAt updatedAt
  }
}
""".strip()


def parse_portfolio_block(data: dict[str, Any]) -> dict[str, Any] | None:
  block = data.get("portfolioBlock")
  return keys_to_snake(block) if block is not None else None


# ── Securities ─────────────────────────────────────────────────────────

LIST_SECURITIES_QUERY = """
query ListInvestorSecurities(
  $entityId: String
  $securityType: String
  $isActive: Boolean
  $limit: Int! = 100
  $offset: Int! = 0
) {
  securities(
    entityId: $entityId
    securityType: $securityType
    isActive: $isActive
    limit: $limit
    offset: $offset
  ) {
    securities {
      id entityId entityName sourceGraphId
      name securityType securitySubtype
      terms isActive authorizedShares outstandingShares
      createdAt updatedAt
    }
    pagination { total limit offset hasMore }
  }
}
""".strip()


def parse_securities(data: dict[str, Any]) -> dict[str, Any] | None:
  s = data.get("securities")
  return keys_to_snake(s) if s is not None else None


GET_SECURITY_QUERY = """
query GetInvestorSecurity($securityId: String!) {
  security(securityId: $securityId) {
    id entityId entityName sourceGraphId
    name securityType securitySubtype
    terms isActive authorizedShares outstandingShares
    createdAt updatedAt
  }
}
""".strip()


def parse_security(data: dict[str, Any]) -> dict[str, Any] | None:
  s = data.get("security")
  return keys_to_snake(s) if s is not None else None


# ── Positions ──────────────────────────────────────────────────────────

LIST_POSITIONS_QUERY = """
query ListInvestorPositions(
  $portfolioId: String
  $securityId: String
  $status: String
  $limit: Int! = 100
  $offset: Int! = 0
) {
  positions(
    portfolioId: $portfolioId
    securityId: $securityId
    status: $status
    limit: $limit
    offset: $offset
  ) {
    positions {
      id portfolioId securityId securityName entityName
      quantity quantityType
      costBasis costBasisDollars currency
      currentValue currentValueDollars
      valuationDate valuationSource
      acquisitionDate dispositionDate
      status notes
      createdAt updatedAt
    }
    pagination { total limit offset hasMore }
  }
}
""".strip()


def parse_positions(data: dict[str, Any]) -> dict[str, Any] | None:
  p = data.get("positions")
  return keys_to_snake(p) if p is not None else None


GET_POSITION_QUERY = """
query GetInvestorPosition($positionId: String!) {
  position(positionId: $positionId) {
    id portfolioId securityId securityName entityName
    quantity quantityType
    costBasis costBasisDollars currency
    currentValue currentValueDollars
    valuationDate valuationSource
    acquisitionDate dispositionDate
    status notes
    createdAt updatedAt
  }
}
""".strip()


def parse_position(data: dict[str, Any]) -> dict[str, Any] | None:
  p = data.get("position")
  return keys_to_snake(p) if p is not None else None


# ── Holdings (aggregation) ─────────────────────────────────────────────

GET_HOLDINGS_QUERY = """
query GetInvestorHoldings($portfolioId: String!) {
  holdings(portfolioId: $portfolioId) {
    totalEntities
    totalPositions
    holdings {
      entityId
      entityName
      sourceGraphId
      totalCostBasisDollars
      totalCurrentValueDollars
      positionCount
      securities {
        securityId
        securityName
        securityType
        quantity
        quantityType
        costBasisDollars
        currentValueDollars
      }
    }
  }
}
""".strip()


def parse_holdings(data: dict[str, Any]) -> dict[str, Any] | None:
  h = data.get("holdings")
  return keys_to_snake(h) if h is not None else None
