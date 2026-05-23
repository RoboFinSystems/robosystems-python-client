from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InitialEntityData")


@_attrs_define
class InitialEntityData:
  """Initial entity data for entity-focused graph creation.

  When creating an entity graph with an initial entity node, this model defines
  the entity's identifying information and metadata.

      Attributes:
          name (str): Entity name
          uri (str): Entity website or URI
          ticker (None | str | Unset): Entity symbol/ticker (e.g., 'HARB', 'NVDA'). Auto-generated from name if not
              provided.
          cik (None | str | Unset): CIK number for SEC filings
          sic (None | str | Unset): SIC code
          sic_description (None | str | Unset): SIC description
          category (None | str | Unset): Business category
          state_of_incorporation (None | str | Unset): State of incorporation
          fiscal_year_end (None | str | Unset): Fiscal year end (MMDD)
          ein (None | str | Unset): Employer Identification Number
          entity_type (None | str | Unset): Entity legal form (e.g. 'corporation', 'llc' / 'limited_liability_company',
              'partnership', 'sole_proprietorship', 'non_profit'). Drives the graph's default Reporting Style at creation —
              partnership and llc get dedicated equity-form Styles; everything else defaults to corporate. Blank falls back to
              corporate.
          reporting_style_id (None | str | Unset): Optional explicit Reporting Style Structure id to pin on the graph,
              overriding the entity_type-derived default. Leave blank to derive from entity_type. Change later via the change-
              reporting-style operation.
  """

  name: str
  uri: str
  ticker: None | str | Unset = UNSET
  cik: None | str | Unset = UNSET
  sic: None | str | Unset = UNSET
  sic_description: None | str | Unset = UNSET
  category: None | str | Unset = UNSET
  state_of_incorporation: None | str | Unset = UNSET
  fiscal_year_end: None | str | Unset = UNSET
  ein: None | str | Unset = UNSET
  entity_type: None | str | Unset = UNSET
  reporting_style_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    uri = self.uri

    ticker: None | str | Unset
    if isinstance(self.ticker, Unset):
      ticker = UNSET
    else:
      ticker = self.ticker

    cik: None | str | Unset
    if isinstance(self.cik, Unset):
      cik = UNSET
    else:
      cik = self.cik

    sic: None | str | Unset
    if isinstance(self.sic, Unset):
      sic = UNSET
    else:
      sic = self.sic

    sic_description: None | str | Unset
    if isinstance(self.sic_description, Unset):
      sic_description = UNSET
    else:
      sic_description = self.sic_description

    category: None | str | Unset
    if isinstance(self.category, Unset):
      category = UNSET
    else:
      category = self.category

    state_of_incorporation: None | str | Unset
    if isinstance(self.state_of_incorporation, Unset):
      state_of_incorporation = UNSET
    else:
      state_of_incorporation = self.state_of_incorporation

    fiscal_year_end: None | str | Unset
    if isinstance(self.fiscal_year_end, Unset):
      fiscal_year_end = UNSET
    else:
      fiscal_year_end = self.fiscal_year_end

    ein: None | str | Unset
    if isinstance(self.ein, Unset):
      ein = UNSET
    else:
      ein = self.ein

    entity_type: None | str | Unset
    if isinstance(self.entity_type, Unset):
      entity_type = UNSET
    else:
      entity_type = self.entity_type

    reporting_style_id: None | str | Unset
    if isinstance(self.reporting_style_id, Unset):
      reporting_style_id = UNSET
    else:
      reporting_style_id = self.reporting_style_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "uri": uri,
      }
    )
    if ticker is not UNSET:
      field_dict["ticker"] = ticker
    if cik is not UNSET:
      field_dict["cik"] = cik
    if sic is not UNSET:
      field_dict["sic"] = sic
    if sic_description is not UNSET:
      field_dict["sic_description"] = sic_description
    if category is not UNSET:
      field_dict["category"] = category
    if state_of_incorporation is not UNSET:
      field_dict["state_of_incorporation"] = state_of_incorporation
    if fiscal_year_end is not UNSET:
      field_dict["fiscal_year_end"] = fiscal_year_end
    if ein is not UNSET:
      field_dict["ein"] = ein
    if entity_type is not UNSET:
      field_dict["entity_type"] = entity_type
    if reporting_style_id is not UNSET:
      field_dict["reporting_style_id"] = reporting_style_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    uri = d.pop("uri")

    def _parse_ticker(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    ticker = _parse_ticker(d.pop("ticker", UNSET))

    def _parse_cik(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    cik = _parse_cik(d.pop("cik", UNSET))

    def _parse_sic(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    sic = _parse_sic(d.pop("sic", UNSET))

    def _parse_sic_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    sic_description = _parse_sic_description(d.pop("sic_description", UNSET))

    def _parse_category(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    category = _parse_category(d.pop("category", UNSET))

    def _parse_state_of_incorporation(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    state_of_incorporation = _parse_state_of_incorporation(
      d.pop("state_of_incorporation", UNSET)
    )

    def _parse_fiscal_year_end(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    fiscal_year_end = _parse_fiscal_year_end(d.pop("fiscal_year_end", UNSET))

    def _parse_ein(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    ein = _parse_ein(d.pop("ein", UNSET))

    def _parse_entity_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_type = _parse_entity_type(d.pop("entity_type", UNSET))

    def _parse_reporting_style_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reporting_style_id = _parse_reporting_style_id(d.pop("reporting_style_id", UNSET))

    initial_entity_data = cls(
      name=name,
      uri=uri,
      ticker=ticker,
      cik=cik,
      sic=sic,
      sic_description=sic_description,
      category=category,
      state_of_incorporation=state_of_incorporation,
      fiscal_year_end=fiscal_year_end,
      ein=ein,
      entity_type=entity_type,
      reporting_style_id=reporting_style_id,
    )

    initial_entity_data.additional_properties = d
    return initial_entity_data

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
