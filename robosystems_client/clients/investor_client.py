"""Investor Client for RoboSystems API.

High-level facade for the RoboInvestor domain: portfolios, securities,
positions, and portfolio holdings aggregation. Same hybrid transport
pattern as `LedgerClient`:

- **Reads** go through GraphQL at `/extensions/{graph_id}/graphql`.
- **Writes** go through named operations at
  `/extensions/roboinvestor/{graph_id}/operations/{operation_name}`.

Every write returns an `OperationEnvelope`; the facade unwraps
`envelope.result` and returns a snake_case dict.
"""

from __future__ import annotations

from http import HTTPStatus
from typing import Any

from ..api.extensions_robo_investor.op_create_portfolio_block import (
  sync_detailed as op_create_portfolio_block,
)
from ..api.extensions_robo_investor.op_create_security import (
  sync_detailed as op_create_security,
)
from ..api.extensions_robo_investor.op_delete_portfolio_block import (
  sync_detailed as op_delete_portfolio_block,
)
from ..api.extensions_robo_investor.op_delete_security import (
  sync_detailed as op_delete_security,
)
from ..api.extensions_robo_investor.op_update_portfolio_block import (
  sync_detailed as op_update_portfolio_block,
)
from ..api.extensions_robo_investor.op_update_security import (
  sync_detailed as op_update_security,
)
from ..client import AuthenticatedClient
from ..graphql.client import GraphQLClient, strip_none_vars
from ..graphql.queries.investor import (
  GET_HOLDINGS_QUERY,
  GET_PORTFOLIO_BLOCK_QUERY,
  GET_POSITION_QUERY,
  GET_SECURITY_QUERY,
  LIST_PORTFOLIOS_QUERY,
  LIST_POSITIONS_QUERY,
  LIST_SECURITIES_QUERY,
  parse_holdings,
  parse_portfolio_block,
  parse_portfolios,
  parse_position,
  parse_positions,
  parse_securities,
  parse_security,
)
from ..models.create_portfolio_block_request import CreatePortfolioBlockRequest
from ..models.create_security_request import CreateSecurityRequest
from ..models.delete_portfolio_block_operation import DeletePortfolioBlockOperation
from ..models.delete_security_operation import DeleteSecurityOperation
from ..models.update_portfolio_block_operation import UpdatePortfolioBlockOperation
from ..models.update_security_operation import UpdateSecurityOperation


class InvestorClient:
  """High-level facade for the RoboInvestor domain."""

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
    if not self.token:
      raise RuntimeError("No API key provided. Set X-API-Key in headers.")
    return GraphQLClient(
      base_url=self.base_url,
      token=self.token,
      headers=self.headers,
      timeout=self.timeout,
    )

  def _query(
    self,
    graph_id: str,
    query: str,
    variables: dict[str, Any] | None = None,
  ) -> dict[str, Any]:
    """Execute a read against the per-graph GraphQL endpoint.

    ``None`` values in ``variables`` are stripped before sending — see
    the ``LedgerClient._query`` docstring for the rationale.
    """
    cleaned = strip_none_vars(variables) if variables else None
    return self._get_graphql_client().execute(graph_id, query, cleaned)

  # The backend's `OperationEnvelope` is generic on the result type
  # (`OperationEnvelope[T]`). Each typed op generates a separate
  # `OperationEnvelope<ResultType>` attrs class in the SDK, with no
  # shared base — so an `isinstance(envelope, OperationEnvelope)` check
  # would reject typed ops like `create-portfolio-block`. We duck-type
  # on the four envelope fields instead, which keeps the helper working
  # for every current and future typed op without import bookkeeping.
  _ENVELOPE_FIELDS = ("operation", "operation_id", "status", "result")

  def _is_envelope(self, value: Any) -> bool:
    return all(hasattr(value, f) for f in self._ENVELOPE_FIELDS)

  def _call_op(self, label: str, response: Any) -> Any:
    if response.status_code not in (HTTPStatus.OK, HTTPStatus.ACCEPTED):
      raise RuntimeError(
        f"{label} failed: {response.status_code}: {response.content!r}"
      )
    envelope = response.parsed
    if not self._is_envelope(envelope):
      raise RuntimeError(f"{label} failed: unexpected response shape: {envelope!r}")
    # Normalize result to a plain dict — typed envelopes carry the result
    # as an attrs class (e.g. `PortfolioBlockEnvelope`).
    if envelope.result is not None and hasattr(envelope.result, "to_dict"):
      envelope.result = envelope.result.to_dict()
    return envelope

  # ── Portfolios ──────────────────────────────────────────────────────

  def list_portfolios(
    self, graph_id: str, limit: int = 100, offset: int = 0
  ) -> dict[str, Any] | None:
    """List portfolios with pagination."""
    data = self._query(
      graph_id, LIST_PORTFOLIOS_QUERY, {"limit": limit, "offset": offset}
    )
    return parse_portfolios(data)

  def get_portfolio_block(
    self, graph_id: str, portfolio_id: str
  ) -> dict[str, Any] | None:
    """Get the full portfolio block (portfolio + positions + securities). Returns None if not found."""
    data = self._query(
      graph_id, GET_PORTFOLIO_BLOCK_QUERY, {"portfolioId": portfolio_id}
    )
    return parse_portfolio_block(data)

  def create_portfolio_block(
    self, graph_id: str, body: dict[str, Any]
  ) -> dict[str, Any]:
    """Create a portfolio with optional initial positions in one atomic operation."""
    request = CreatePortfolioBlockRequest.from_dict(body)
    response = op_create_portfolio_block(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Create portfolio block", response)
    return envelope.result or {}

  def update_portfolio_block(
    self,
    graph_id: str,
    portfolio_id: str,
    updates: dict[str, Any],
  ) -> dict[str, Any]:
    """Update portfolio metadata and/or apply position deltas (add/update/dispose)."""
    body_dict = {**updates, "portfolio_id": portfolio_id}
    body = UpdatePortfolioBlockOperation.from_dict(body_dict)
    response = op_update_portfolio_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Update portfolio block", response)
    return envelope.result or {}

  def delete_portfolio_block(
    self,
    graph_id: str,
    portfolio_id: str,
    confirm_active_positions: bool = False,
  ) -> dict[str, Any]:
    """Delete a portfolio and all its positions. Requires `confirm_active_positions=True` when active positions exist."""
    body = DeletePortfolioBlockOperation(
      portfolio_id=portfolio_id,
      confirm_active_positions=confirm_active_positions,
    )
    response = op_delete_portfolio_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Delete portfolio block", response)
    return envelope.result if envelope.result is not None else {"deleted": True}

  # ── Securities ──────────────────────────────────────────────────────

  def list_securities(
    self,
    graph_id: str,
    entity_id: str | None = None,
    security_type: str | None = None,
    is_active: bool | None = None,
    limit: int = 100,
    offset: int = 0,
  ) -> dict[str, Any] | None:
    """List securities with pagination and filters."""
    data = self._query(
      graph_id,
      LIST_SECURITIES_QUERY,
      {
        "entityId": entity_id,
        "securityType": security_type,
        "isActive": is_active,
        "limit": limit,
        "offset": offset,
      },
    )
    return parse_securities(data)

  def get_security(self, graph_id: str, security_id: str) -> dict[str, Any] | None:
    """Get a single security by id. Returns None if it doesn't exist."""
    data = self._query(graph_id, GET_SECURITY_QUERY, {"securityId": security_id})
    return parse_security(data)

  def create_security(self, graph_id: str, body: dict[str, Any]) -> dict[str, Any]:
    """Create a new security. Auto-links to an entity when `source_graph_id` is set."""
    request = CreateSecurityRequest.from_dict(body)
    response = op_create_security(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Create security", response)
    return envelope.result or {}

  def update_security(
    self,
    graph_id: str,
    security_id: str,
    updates: dict[str, Any],
  ) -> dict[str, Any]:
    """Update a security's metadata. Only provided fields are applied."""
    body_dict = {**updates, "security_id": security_id}
    body = UpdateSecurityOperation.from_dict(body_dict)
    response = op_update_security(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Update security", response)
    return envelope.result or {}

  def delete_security(self, graph_id: str, security_id: str) -> dict[str, Any]:
    """Soft-delete a security (sets is_active=False)."""
    body = DeleteSecurityOperation(security_id=security_id)
    response = op_delete_security(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Delete security", response)
    return envelope.result if envelope.result is not None else {"deleted": True}

  # ── Positions (read-only — writes go through portfolio block) ────────

  def list_positions(
    self,
    graph_id: str,
    portfolio_id: str | None = None,
    security_id: str | None = None,
    status: str | None = None,
    limit: int = 100,
    offset: int = 0,
  ) -> dict[str, Any] | None:
    """List positions with pagination and filters."""
    data = self._query(
      graph_id,
      LIST_POSITIONS_QUERY,
      {
        "portfolioId": portfolio_id,
        "securityId": security_id,
        "status": status,
        "limit": limit,
        "offset": offset,
      },
    )
    return parse_positions(data)

  def get_position(self, graph_id: str, position_id: str) -> dict[str, Any] | None:
    """Get a single position by id. Returns None if it doesn't exist."""
    data = self._query(graph_id, GET_POSITION_QUERY, {"positionId": position_id})
    return parse_position(data)

  # ── Holdings (aggregation) ─────────────────────────────────────────

  def get_holdings(self, graph_id: str, portfolio_id: str) -> dict[str, Any] | None:
    """Get portfolio holdings grouped by entity."""
    data = self._query(graph_id, GET_HOLDINGS_QUERY, {"portfolioId": portfolio_id})
    return parse_holdings(data)
