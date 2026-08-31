"""Investor Client for RoboSystems API.

High-level facade for the RoboInvestor domain: portfolios, securities,
positions, and portfolio holdings aggregation. Same hybrid transport
pattern as `LedgerClient`:

- **Reads** go through GraphQL at `/extensions/{graph_id}/graphql`.
- **Writes** go through named operations at
  `/extensions/roboinvestor/{graph_id}/operations/{operation_name}`.

Every write returns an `OperationEnvelope`; the facade unwraps
`envelope.result` and returns the typed SDK class advertised on the
method's return-type annotation (e.g. ``PortfolioBlockEnvelope``,
``SecurityResponse``, ``DeleteResult``). In production the result is
the SDK's generated attrs class; in unit-test contexts using dict
mocks, the result is a plain dict — both surface fields the same way
in the JSON-serialized response.
"""

from __future__ import annotations

from http import HTTPStatus
from typing import Any

from ..api.extensions_robo_investor.create_portfolio_block import (
  sync_detailed as op_create_portfolio_block,
)
from ..api.extensions_robo_investor.create_security import (
  sync_detailed as op_create_security,
)
from ..api.extensions_robo_investor.delete_portfolio_block import (
  sync_detailed as op_delete_portfolio_block,
)
from ..api.extensions_robo_investor.delete_security import (
  sync_detailed as op_delete_security,
)
from ..api.extensions_robo_investor.update_portfolio_block import (
  sync_detailed as op_update_portfolio_block,
)
from ..api.extensions_robo_investor.update_security import (
  sync_detailed as op_update_security,
)
from ..client import AuthenticatedClient
from .retry import (
  DEFAULT_MAX_RETRIES,
  DEFAULT_RETRY_DELAY_MS,
  retrying_authenticated_client,
)
from ..graphql.client import GraphQLClient, strip_none_vars
from .token_utils import resolve_config_token
from ..graphql.generated.get_investor_holdings import (
  GetInvestorHoldings,
)
from ..graphql.generated.get_investor_holdings import (
  GetInvestorHoldingsHoldings as InvestorHoldings,
)
from ..graphql.generated.get_investor_portfolio_block import (
  GetInvestorPortfolioBlock,
)
from ..graphql.generated.get_investor_portfolio_block import (
  GetInvestorPortfolioBlockPortfolioBlock as PortfolioBlock,
)
from ..graphql.generated.get_investor_position import (
  GetInvestorPosition,
)
from ..graphql.generated.get_investor_position import (
  GetInvestorPositionPosition as InvestorPosition,
)
from ..graphql.generated.get_investor_security import (
  GetInvestorSecurity,
)
from ..graphql.generated.get_investor_security import (
  GetInvestorSecuritySecurity as InvestorSecurity,
)
from ..graphql.generated.list_investor_portfolios import (
  ListInvestorPortfolios,
)
from ..graphql.generated.list_investor_portfolios import (
  ListInvestorPortfoliosPortfolios as PortfoliosPage,
)
from ..graphql.generated.list_investor_positions import (
  ListInvestorPositions,
)
from ..graphql.generated.list_investor_positions import (
  ListInvestorPositionsPositions as PositionsPage,
)
from ..graphql.generated.list_investor_securities import (
  ListInvestorSecurities,
)
from ..graphql.generated.list_investor_securities import (
  ListInvestorSecuritiesSecurities as SecuritiesPage,
)
from ..graphql.generated.operations import (
  GET_INVESTOR_HOLDINGS_GQL,
  GET_INVESTOR_PORTFOLIO_BLOCK_GQL,
  GET_INVESTOR_POSITION_GQL,
  GET_INVESTOR_SECURITY_GQL,
  LIST_INVESTOR_PORTFOLIOS_GQL,
  LIST_INVESTOR_POSITIONS_GQL,
  LIST_INVESTOR_SECURITIES_GQL,
)
from ..models.create_portfolio_block_request import CreatePortfolioBlockRequest
from ..models.create_security_request import CreateSecurityRequest
from ..models.delete_portfolio_block_operation import DeletePortfolioBlockOperation
from ..models.delete_portfolio_block_response import DeletePortfolioBlockResponse
from ..models.delete_result import DeleteResult
from ..models.delete_security_operation import DeleteSecurityOperation
from ..models.portfolio_block_envelope import PortfolioBlockEnvelope
from ..models.security_response import SecurityResponse
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
    # Resolved per call: a configured `token_provider` wins over the
    # static token, so rotating credentials are picked up per-request.
    token = resolve_config_token(self.config)
    if not token:
      raise RuntimeError("No API key provided. Set X-API-Key in headers.")
    return retrying_authenticated_client(
      base_url=self.base_url,
      token=token,
      headers=self.headers,
      config=self.config,
    )

  def _get_graphql_client(self) -> GraphQLClient:
    token = resolve_config_token(self.config)
    if not token:
      raise RuntimeError("No API key provided. Set X-API-Key in headers.")
    return GraphQLClient(
      base_url=self.base_url,
      token=token,
      headers=self.headers,
      timeout=self.timeout,
      max_retries=self.config.get("max_retries", DEFAULT_MAX_RETRIES),
      retry_delay_ms=self.config.get("retry_delay", DEFAULT_RETRY_DELAY_MS),
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
    """Common error handling for every generated op_* REST call.

    Returns the parsed envelope unchanged. Typed-envelope ops surface
    ``envelope.result`` as the SDK's typed attrs class (e.g.
    ``PortfolioBlockEnvelope``); untyped ops surface it as a plain dict.
    Facade methods are responsible for casting the result to the type
    they advertise.
    """
    if response.status_code not in (HTTPStatus.OK, HTTPStatus.ACCEPTED):
      raise RuntimeError(
        f"{label} failed: {response.status_code}: {response.content!r}"
      )
    envelope = response.parsed
    if not self._is_envelope(envelope):
      raise RuntimeError(f"{label} failed: unexpected response shape: {envelope!r}")
    return envelope

  def _typed_result(
    self,
    label: str,
    envelope: Any,
    expected: type[Any],
    *,
    sentinel_on_empty: bool = False,
  ) -> Any:
    """Return ``envelope.result`` for typed-envelope facade methods.

    See :meth:`LedgerClient._typed_result` for the contract. Briefly: in
    production the SDK gives back the typed attrs class; in tests using
    dict mocks the result is a plain dict. ``None``/``Unset`` raises unless
    ``sentinel_on_empty`` is set, which delete-style ops pass to preserve
    their historical ``{"deleted": True}`` return.
    """
    result = envelope.result
    if result is None or (
      hasattr(result, "__class__") and "Unset" in result.__class__.__name__
    ):
      if sentinel_on_empty:
        return {"deleted": True}
      raise RuntimeError(f"{label}: operation envelope had no result")
    return result

  # ── Portfolios ──────────────────────────────────────────────────────

  def list_portfolios(
    self, graph_id: str, limit: int = 100, offset: int = 0
  ) -> PortfoliosPage | None:
    """List portfolios with pagination."""
    data = self._query(
      graph_id, LIST_INVESTOR_PORTFOLIOS_GQL, {"limit": limit, "offset": offset}
    )
    return ListInvestorPortfolios.model_validate(data).portfolios

  def get_portfolio_block(
    self, graph_id: str, portfolio_id: str
  ) -> PortfolioBlock | None:
    """Get the full portfolio block (portfolio + positions + securities). Returns None if not found."""
    data = self._query(
      graph_id, GET_INVESTOR_PORTFOLIO_BLOCK_GQL, {"portfolioId": portfolio_id}
    )
    return GetInvestorPortfolioBlock.model_validate(data).portfolio_block

  def create_portfolio_block(
    self, graph_id: str, body: dict[str, Any]
  ) -> PortfolioBlockEnvelope:
    """Create a portfolio with optional initial positions in one atomic operation."""
    request = CreatePortfolioBlockRequest.from_dict(body)
    response = op_create_portfolio_block(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Create portfolio block", response)
    return self._typed_result(
      "Create portfolio block", envelope, PortfolioBlockEnvelope
    )

  def update_portfolio_block(
    self,
    graph_id: str,
    portfolio_id: str,
    updates: dict[str, Any],
  ) -> PortfolioBlockEnvelope:
    """Update portfolio metadata and/or apply position deltas (add/update/dispose)."""
    body_dict = {**updates, "portfolio_id": portfolio_id}
    body = UpdatePortfolioBlockOperation.from_dict(body_dict)
    response = op_update_portfolio_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Update portfolio block", response)
    return self._typed_result(
      "Update portfolio block", envelope, PortfolioBlockEnvelope
    )

  def delete_portfolio_block(
    self,
    graph_id: str,
    portfolio_id: str,
    confirm_active_positions: bool = False,
  ) -> DeletePortfolioBlockResponse:
    """Delete a portfolio and all its positions. Requires `confirm_active_positions=True` when active positions exist."""
    body = DeletePortfolioBlockOperation(
      portfolio_id=portfolio_id,
      confirm_active_positions=confirm_active_positions,
    )
    response = op_delete_portfolio_block(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Delete portfolio block", response)
    return self._typed_result(
      "Delete portfolio block",
      envelope,
      DeletePortfolioBlockResponse,
      sentinel_on_empty=True,
    )

  # ── Securities ──────────────────────────────────────────────────────

  def list_securities(
    self,
    graph_id: str,
    entity_id: str | None = None,
    security_type: str | None = None,
    is_active: bool | None = None,
    limit: int = 100,
    offset: int = 0,
  ) -> SecuritiesPage | None:
    """List securities with pagination and filters."""
    data = self._query(
      graph_id,
      LIST_INVESTOR_SECURITIES_GQL,
      {
        "entityId": entity_id,
        "securityType": security_type,
        "isActive": is_active,
        "limit": limit,
        "offset": offset,
      },
    )
    return ListInvestorSecurities.model_validate(data).securities

  def get_security(self, graph_id: str, security_id: str) -> InvestorSecurity | None:
    """Get a single security by id. Returns None if it doesn't exist."""
    data = self._query(graph_id, GET_INVESTOR_SECURITY_GQL, {"securityId": security_id})
    return GetInvestorSecurity.model_validate(data).security

  def create_security(self, graph_id: str, body: dict[str, Any]) -> SecurityResponse:
    """Create a new security. Auto-links to an entity when `source_graph_id` is set."""
    request = CreateSecurityRequest.from_dict(body)
    response = op_create_security(
      graph_id=graph_id, body=request, client=self._get_client()
    )
    envelope = self._call_op("Create security", response)
    return self._typed_result("Create security", envelope, SecurityResponse)

  def update_security(
    self,
    graph_id: str,
    security_id: str,
    updates: dict[str, Any],
  ) -> SecurityResponse:
    """Update a security's metadata. Only provided fields are applied."""
    body_dict = {**updates, "security_id": security_id}
    body = UpdateSecurityOperation.from_dict(body_dict)
    response = op_update_security(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Update security", response)
    return self._typed_result("Update security", envelope, SecurityResponse)

  def delete_security(self, graph_id: str, security_id: str) -> DeleteResult:
    """Soft-delete a security (sets is_active=False)."""
    body = DeleteSecurityOperation(security_id=security_id)
    response = op_delete_security(
      graph_id=graph_id, body=body, client=self._get_client()
    )
    envelope = self._call_op("Delete security", response)
    return self._typed_result(
      "Delete security", envelope, DeleteResult, sentinel_on_empty=True
    )

  # ── Positions (read-only — writes go through portfolio block) ────────

  def list_positions(
    self,
    graph_id: str,
    portfolio_id: str | None = None,
    security_id: str | None = None,
    status: str | None = None,
    limit: int = 100,
    offset: int = 0,
  ) -> PositionsPage | None:
    """List positions with pagination and filters."""
    data = self._query(
      graph_id,
      LIST_INVESTOR_POSITIONS_GQL,
      {
        "portfolioId": portfolio_id,
        "securityId": security_id,
        "status": status,
        "limit": limit,
        "offset": offset,
      },
    )
    return ListInvestorPositions.model_validate(data).positions

  def get_position(self, graph_id: str, position_id: str) -> InvestorPosition | None:
    """Get a single position by id. Returns None if it doesn't exist."""
    data = self._query(graph_id, GET_INVESTOR_POSITION_GQL, {"positionId": position_id})
    return GetInvestorPosition.model_validate(data).position

  # ── Holdings (aggregation) ─────────────────────────────────────────

  def get_holdings(self, graph_id: str, portfolio_id: str) -> InvestorHoldings | None:
    """Get portfolio holdings grouped by entity."""
    data = self._query(
      graph_id, GET_INVESTOR_HOLDINGS_GQL, {"portfolioId": portfolio_id}
    )
    return GetInvestorHoldings.model_validate(data).holdings
