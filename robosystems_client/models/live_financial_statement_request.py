from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiveFinancialStatementRequest")


@_attrs_define
class LiveFinancialStatementRequest:
  """Request for live-financial-statement (OLTP, entity graphs only).

  Attributes:
      statement_type (str): income_statement | balance_sheet | equity_statement
      period_start (datetime.date | None | Unset): Explicit window start. Overrides period_type/fiscal_year.
      period_end (datetime.date | None | Unset): Explicit window end. Overrides period_type/fiscal_year.
      period_type (None | str | Unset): annual | quarterly | instant (ignored when dates supplied)
      fiscal_year (int | None | Unset): Fiscal year for annual window (anchored on FiscalCalendar)
      limit (int | Unset): Max fact rows returned Default: 50.
  """

  statement_type: str
  period_start: datetime.date | None | Unset = UNSET
  period_end: datetime.date | None | Unset = UNSET
  period_type: None | str | Unset = UNSET
  fiscal_year: int | None | Unset = UNSET
  limit: int | Unset = 50
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    statement_type = self.statement_type

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

    limit = self.limit

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "statement_type": statement_type,
      }
    )
    if period_start is not UNSET:
      field_dict["period_start"] = period_start
    if period_end is not UNSET:
      field_dict["period_end"] = period_end
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if fiscal_year is not UNSET:
      field_dict["fiscal_year"] = fiscal_year
    if limit is not UNSET:
      field_dict["limit"] = limit

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    statement_type = d.pop("statement_type")

    def _parse_period_start(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_start_type_0 = isoparse(data).date()

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
        period_end_type_0 = isoparse(data).date()

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

    limit = d.pop("limit", UNSET)

    live_financial_statement_request = cls(
      statement_type=statement_type,
      period_start=period_start,
      period_end=period_end,
      period_type=period_type,
      fiscal_year=fiscal_year,
      limit=limit,
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
