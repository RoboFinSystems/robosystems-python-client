from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_financial_statement_request_scope_type_0 import (
  LiveFinancialStatementRequestScopeType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.statement_dimension import StatementDimension


T = TypeVar("T", bound="LiveFinancialStatementRequest")


@_attrs_define
class LiveFinancialStatementRequest:
  """Request for live-financial-statement (OLTP, entity graphs only).

  Attributes:
      statement_type (str): income_statement | balance_sheet | cash_flow_statement | equity_statement.
          `equity_statement` is provisional — equity balances, not a rollforward — and is not offered on the MCP surface
          until it articulates.
      entity_id (None | str | Unset): The entity whose books this acts on, by id. Omit for the group parent — the
          single-entity default.
      period_start (datetime.date | None | Unset): Explicit window start. Overrides period_type/fiscal_year.
      period_end (datetime.date | None | Unset): Explicit window end. Overrides period_type/fiscal_year.
      period_type (None | str | Unset): annual | quarterly | instant (ignored when dates supplied)
      fiscal_year (int | None | Unset): Fiscal year for annual window (anchored on FiscalCalendar)
      scope (LiveFinancialStatementRequestScopeType0 | None | Unset): `entity` (the default): one entity's own books.
          `combined`: on the group parent, every member consolidated in full rendered under the parent's Reporting Style
          and summed per rs-gaap concept, each for the months it was a member — the pre-adjustment total, nothing
          eliminated. `consolidated`: the same sum plus the consolidation entity, whose eliminations and noncontrolling
          interest are the adjustments column, so a group that posts its consolidating entries there reads its
          consolidated statement. An equity-method or cost member is never summed (its `consolidation_method` says so).
          Both group scopes are read on the group parent only (422 on a subsidiary). An entity with no CoA mapping yet
          contributes nothing and is left out of `combined_entity_ids`.
      consolidated (bool | Unset): The older spelling of `scope: consolidated`, kept for callers that pass it; `scope`
          wins when both are given. Default: False.
      limit (int | Unset): Max fact rows returned. Defaults to the ceiling so a statement is never cut mid-section —
          visible rows would stop footing to visible subtotals. Lower it only for a preview. Default: 1000.
      dimension (None | StatementDimension | Unset): Slice an income statement by a management dimension (department,
          class, location, project). `{type, member_id}` reads one member's lines, current and prior; `member_id:
          unallocated` reads the lines no member of the axis tags. `{type}` alone reads the current window with one column
          per member, then Unallocated, then Total, and says in `dimension.ties_out` whether every row's members plus
          Unallocated equal its Total. Composes with `scope` and `entity_id`; a consolidation entity's lines are untagged,
          so eliminations read as Unallocated. Refused (422) on any other statement.
      include_sources (bool | Unset): Add each row's `origin` and, per column, the accounts its figure was summed from
          (`sources`), each keyed by the entity whose books hold it, so a figure opens on the account registers behind it.
          Consolidated figures list each member's accounts and the consolidation entity's. Off by default: it multiplies
          the response. Refused (422) with a `dimension` read by column. Default: False.
  """

  statement_type: str
  entity_id: None | str | Unset = UNSET
  period_start: datetime.date | None | Unset = UNSET
  period_end: datetime.date | None | Unset = UNSET
  period_type: None | str | Unset = UNSET
  fiscal_year: int | None | Unset = UNSET
  scope: LiveFinancialStatementRequestScopeType0 | None | Unset = UNSET
  consolidated: bool | Unset = False
  limit: int | Unset = 1000
  dimension: None | StatementDimension | Unset = UNSET
  include_sources: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.statement_dimension import StatementDimension

    statement_type = self.statement_type

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    period_start: None | str | Unset
    if isinstance(self.period_start, Unset):
      period_start = UNSET
    elif isinstance(self.period_start, datetime.date):
      period_start = self.period_start.isoformat()
    else:
      period_start = self.period_start

    period_end: None | str | Unset
    if isinstance(self.period_end, Unset):
      period_end = UNSET
    elif isinstance(self.period_end, datetime.date):
      period_end = self.period_end.isoformat()
    else:
      period_end = self.period_end

    period_type: None | str | Unset
    if isinstance(self.period_type, Unset):
      period_type = UNSET
    else:
      period_type = self.period_type

    fiscal_year: int | None | Unset
    if isinstance(self.fiscal_year, Unset):
      fiscal_year = UNSET
    else:
      fiscal_year = self.fiscal_year

    scope: None | str | Unset
    if isinstance(self.scope, Unset):
      scope = UNSET
    elif isinstance(self.scope, LiveFinancialStatementRequestScopeType0):
      scope = self.scope.value
    else:
      scope = self.scope

    consolidated = self.consolidated

    limit = self.limit

    dimension: dict[str, Any] | None | Unset
    if isinstance(self.dimension, Unset):
      dimension = UNSET
    elif isinstance(self.dimension, StatementDimension):
      dimension = self.dimension.to_dict()
    else:
      dimension = self.dimension

    include_sources = self.include_sources

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "statement_type": statement_type,
      }
    )
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if period_end is not UNSET:
      field_dict["period_end"] = period_end
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if fiscal_year is not UNSET:
      field_dict["fiscal_year"] = fiscal_year
    if scope is not UNSET:
      field_dict["scope"] = scope
    if consolidated is not UNSET:
      field_dict["consolidated"] = consolidated
    if limit is not UNSET:
      field_dict["limit"] = limit
    if dimension is not UNSET:
      field_dict["dimension"] = dimension
    if include_sources is not UNSET:
      field_dict["include_sources"] = include_sources

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.statement_dimension import StatementDimension

    d = dict(src_dict)
    statement_type = d.pop("statement_type")

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    def _parse_period_start(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_start_type_0 = datetime.date.fromisoformat(data)

        return period_start_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    period_start = _parse_period_start(d.pop("period_start", UNSET))

    def _parse_period_end(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_end_type_0 = datetime.date.fromisoformat(data)

        return period_end_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    period_end = _parse_period_end(d.pop("period_end", UNSET))

    def _parse_period_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_type = _parse_period_type(d.pop("period_type", UNSET))

    def _parse_fiscal_year(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    fiscal_year = _parse_fiscal_year(d.pop("fiscal_year", UNSET))

    def _parse_scope(
      data: object,
    ) -> LiveFinancialStatementRequestScopeType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        scope_type_0 = LiveFinancialStatementRequestScopeType0(data)

        return scope_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(LiveFinancialStatementRequestScopeType0 | None | Unset, data)

    scope = _parse_scope(d.pop("scope", UNSET))

    consolidated = d.pop("consolidated", UNSET)

    limit = d.pop("limit", UNSET)

    def _parse_dimension(data: object) -> None | StatementDimension | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        dimension_type_0 = StatementDimension.from_dict(data)

        return dimension_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | StatementDimension | Unset, data)

    dimension = _parse_dimension(d.pop("dimension", UNSET))

    include_sources = d.pop("include_sources", UNSET)

    live_financial_statement_request = cls(
      statement_type=statement_type,
      entity_id=entity_id,
      period_start=period_start,
      period_end=period_end,
      period_type=period_type,
      fiscal_year=fiscal_year,
      scope=scope,
      consolidated=consolidated,
      limit=limit,
      dimension=dimension,
      include_sources=include_sources,
    )

    live_financial_statement_request.additional_properties = d
    return live_financial_statement_request

  @property
  def additional_keys(self) -> list[str]:
    return list(self.additional_properties.keys())

  def __getitem__(self, key: str) -> Any:
    return self.additional_properties[key]

  def __setitem__(self, key: str, value: Any) -> None:
    self.additional_properties[key] = value

  def __delitem__(self, key: str) -> None:
    del self.additional_properties[key]

  def __contains__(self, key: str) -> bool:
    return key in self.additional_properties
