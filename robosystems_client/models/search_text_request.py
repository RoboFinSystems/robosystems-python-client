from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchTextRequest")


@_attrs_define
class SearchTextRequest:
  """Request for the search-text view op — words inside one filing.

  Attributes:
      query (str): Words matched in order across any spacing, case-insensitive; `|` between alternative phrases, a
          trailing `*` for a stem. Not a regular expression.
      ticker (None | str | Unset): Company ticker. On shared-repository graphs (SEC) it resolves the latest matching
          filing when report_id is not given; ignored on tenant graphs.
      report_id (None | str | Unset): Specific report identifier. Required on tenant graphs; on SEC, optional when
          ticker is given.
      fiscal_year (int | None | Unset): Narrow auto-resolution to this fiscal year focus
      period_type (None | str | Unset): Which forms auto-resolution considers: annual (10-K / 20-F / 40-F, the
          default) or quarterly (10-Q as well)
      accession (None | str | Unset): SEC only, with ticker: one filing by accession number — a report, or an 8-K from
          resolved_report.recent_releases
      form (None | str | Unset): SEC only, with ticker: '8-K' reads the latest earnings release, or with fiscal_year
          the latest filed in that calendar year
      window (int | None | Unset): Characters of context around each match (default 300)
      max_hits (int | None | Unset): Matches to return (default 10)
  """

  query: str
  ticker: None | str | Unset = UNSET
  report_id: None | str | Unset = UNSET
  fiscal_year: int | None | Unset = UNSET
  period_type: None | str | Unset = UNSET
  accession: None | str | Unset = UNSET
  form: None | str | Unset = UNSET
  window: int | None | Unset = UNSET
  max_hits: int | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    query = self.query

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

    accession: None | str | Unset
    if isinstance(self.accession, Unset):
      accession = UNSET
    else:
      accession = self.accession

    form: None | str | Unset
    if isinstance(self.form, Unset):
      form = UNSET
    else:
      form = self.form

    window: int | None | Unset
    if isinstance(self.window, Unset):
      window = UNSET
    else:
      window = self.window

    max_hits: int | None | Unset
    if isinstance(self.max_hits, Unset):
      max_hits = UNSET
    else:
      max_hits = self.max_hits

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "query": query,
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
    if accession is not UNSET:
      field_dict["accession"] = accession
    if form is not UNSET:
      field_dict["form"] = form
    if window is not UNSET:
      field_dict["window"] = window
    if max_hits is not UNSET:
      field_dict["max_hits"] = max_hits

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    query = d.pop("query")

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

    def _parse_accession(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    accession = _parse_accession(d.pop("accession", UNSET))

    def _parse_form(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    form = _parse_form(d.pop("form", UNSET))

    def _parse_window(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    window = _parse_window(d.pop("window", UNSET))

    def _parse_max_hits(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    max_hits = _parse_max_hits(d.pop("max_hits", UNSET))

    search_text_request = cls(
      query=query,
      ticker=ticker,
      report_id=report_id,
      fiscal_year=fiscal_year,
      period_type=period_type,
      accession=accession,
      form=form,
      window=window,
      max_hits=max_hits,
    )

    search_text_request.additional_properties = d
    return search_text_request

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
