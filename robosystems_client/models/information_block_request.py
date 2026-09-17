from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InformationBlockRequest")


@_attrs_define
class InformationBlockRequest:
  """Request for the information-block view op — one section read whole.

  Attributes:
      block (str): The block id from disclosures (a role name or its last segment also resolves)
      ticker (None | str | Unset): Company ticker. On shared-repository graphs (SEC) it resolves the latest matching
          filing when report_id is not given; ignored on tenant graphs.
      report_id (None | str | Unset): Specific report identifier. Required on tenant graphs; on SEC, optional when
          ticker is given.
      fiscal_year (int | None | Unset): Narrow auto-resolution to this fiscal year focus
      period_type (None | str | Unset): Which forms auto-resolution considers: annual (10-K / 20-F / 40-F, the
          default) or quarterly (10-Q as well)
      periods (list[str] | None | Unset): Period keys to keep, from a previous call's columns. Default keeps the
          budgeted set, year and balance columns first on an annual form.
      member (None | str | Unset): Keep only breakdowns whose member key contains this text (a segment name)
      max_rows (int | None | Unset): Cap on presentation rows (default 400)
      max_members (int | None | Unset): An explicit cap on member breakdowns, instead of the response budget
      offset (int | None | Unset): Rows to skip: the next_offset a truncated response returned
  """

  block: str
  ticker: None | str | Unset = UNSET
  report_id: None | str | Unset = UNSET
  fiscal_year: int | None | Unset = UNSET
  period_type: None | str | Unset = UNSET
  periods: list[str] | None | Unset = UNSET
  member: None | str | Unset = UNSET
  max_rows: int | None | Unset = UNSET
  max_members: int | None | Unset = UNSET
  offset: int | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    block = self.block

    ticker: None | str | Unset
    if isinstance(self.ticker, Unset):
      ticker = UNSET
    else:
      ticker = self.ticker

    report_id: None | str | Unset
    if isinstance(self.report_id, Unset):
      report_id = UNSET
    else:
      report_id = self.report_id

    fiscal_year: int | None | Unset
    if isinstance(self.fiscal_year, Unset):
      fiscal_year = UNSET
    else:
      fiscal_year = self.fiscal_year

    period_type: None | str | Unset
    if isinstance(self.period_type, Unset):
      period_type = UNSET
    else:
      period_type = self.period_type

    periods: list[str] | None | Unset
    if isinstance(self.periods, Unset):
      periods = UNSET
    elif isinstance(self.periods, list):
      periods = self.periods

    else:
      periods = self.periods

    member: None | str | Unset
    if isinstance(self.member, Unset):
      member = UNSET
    else:
      member = self.member

    max_rows: int | None | Unset
    if isinstance(self.max_rows, Unset):
      max_rows = UNSET
    else:
      max_rows = self.max_rows

    max_members: int | None | Unset
    if isinstance(self.max_members, Unset):
      max_members = UNSET
    else:
      max_members = self.max_members

    offset: int | None | Unset
    if isinstance(self.offset, Unset):
      offset = UNSET
    else:
      offset = self.offset

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "block": block,
      }
    )
    if ticker is not UNSET:
      field_dict["ticker"] = ticker
    if report_id is not UNSET:
      field_dict["report_id"] = report_id
    if fiscal_year is not UNSET:
      field_dict["fiscal_year"] = fiscal_year
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if periods is not UNSET:
      field_dict["periods"] = periods
    if member is not UNSET:
      field_dict["member"] = member
    if max_rows is not UNSET:
      field_dict["max_rows"] = max_rows
    if max_members is not UNSET:
      field_dict["max_members"] = max_members
    if offset is not UNSET:
      field_dict["offset"] = offset

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    block = d.pop("block")

    def _parse_ticker(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    ticker = _parse_ticker(d.pop("ticker", UNSET))

    def _parse_report_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    report_id = _parse_report_id(d.pop("report_id", UNSET))

    def _parse_fiscal_year(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    fiscal_year = _parse_fiscal_year(d.pop("fiscal_year", UNSET))

    def _parse_period_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_type = _parse_period_type(d.pop("period_type", UNSET))

    def _parse_periods(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        periods_type_0 = cast(list[str], data)

        return periods_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    periods = _parse_periods(d.pop("periods", UNSET))

    def _parse_member(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    member = _parse_member(d.pop("member", UNSET))

    def _parse_max_rows(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    max_rows = _parse_max_rows(d.pop("max_rows", UNSET))

    def _parse_max_members(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    max_members = _parse_max_members(d.pop("max_members", UNSET))

    def _parse_offset(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    offset = _parse_offset(d.pop("offset", UNSET))

    information_block_request = cls(
      block=block,
      ticker=ticker,
      report_id=report_id,
      fiscal_year=fiscal_year,
      period_type=period_type,
      periods=periods,
      member=member,
      max_rows=max_rows,
      max_members=max_members,
      offset=offset,
    )

    information_block_request.additional_properties = d
    return information_block_request

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
