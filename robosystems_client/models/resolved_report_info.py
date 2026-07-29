from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResolvedReportInfo")


@_attrs_define
class ResolvedReportInfo:
  """Information about the auto-resolved report.

  Attributes:
      report_id (str):
      form (None | str | Unset):
      filing_date (None | str | Unset):
      fiscal_year (int | None | Unset):
      fiscal_period (None | str | Unset):
  """

  report_id: str
  form: None | str | Unset = UNSET
  filing_date: None | str | Unset = UNSET
  fiscal_year: int | None | Unset = UNSET
  fiscal_period: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    report_id = self.report_id

    form: None | str | Unset
    if isinstance(self.form, Unset):
      form = UNSET
    else:
      form = self.form

    filing_date: None | str | Unset
    if isinstance(self.filing_date, Unset):
      filing_date = UNSET
    else:
      filing_date = self.filing_date

    fiscal_year: int | None | Unset
    if isinstance(self.fiscal_year, Unset):
      fiscal_year = UNSET
    else:
      fiscal_year = self.fiscal_year

    fiscal_period: None | str | Unset
    if isinstance(self.fiscal_period, Unset):
      fiscal_period = UNSET
    else:
      fiscal_period = self.fiscal_period

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "report_id": report_id,
      }
    )
    if form is not UNSET:
      field_dict["form"] = form
    if filing_date is not UNSET:
      field_dict["filing_date"] = filing_date
    if fiscal_year is not UNSET:
      field_dict["fiscal_year"] = fiscal_year
    if fiscal_period is not UNSET:
      field_dict["fiscal_period"] = fiscal_period

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    report_id = d.pop("report_id")

    def _parse_form(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    form = _parse_form(d.pop("form", UNSET))

    def _parse_filing_date(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    filing_date = _parse_filing_date(d.pop("filing_date", UNSET))

    def _parse_fiscal_year(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    fiscal_year = _parse_fiscal_year(d.pop("fiscal_year", UNSET))

    def _parse_fiscal_period(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    fiscal_period = _parse_fiscal_period(d.pop("fiscal_period", UNSET))

    resolved_report_info = cls(
      report_id=report_id,
      form=form,
      filing_date=filing_date,
      fiscal_year=fiscal_year,
      fiscal_period=fiscal_period,
    )

    resolved_report_info.additional_properties = d
    return resolved_report_info

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
