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
          cik (None | str | Unset): CIK number for SEC filings
          sic (None | str | Unset): SIC code
          sic_description (None | str | Unset): SIC description
          category (None | str | Unset): Business category
          state_of_incorporation (None | str | Unset): State of incorporation
          fiscal_year_end (None | str | Unset): Fiscal year end (MMDD)
          ein (None | str | Unset): Employer Identification Number
  """

  name: str
  uri: str
  cik: None | str | Unset = UNSET
  sic: None | str | Unset = UNSET
  sic_description: None | str | Unset = UNSET
  category: None | str | Unset = UNSET
  state_of_incorporation: None | str | Unset = UNSET
  fiscal_year_end: None | str | Unset = UNSET
  ein: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    uri = self.uri

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

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "uri": uri,
      }
    )
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

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    uri = d.pop("uri")

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

    initial_entity_data = cls(
      name=name,
      uri=uri,
      cik=cik,
      sic=sic,
      sic_description=sic_description,
      category=category,
      state_of_incorporation=state_of_incorporation,
      fiscal_year_end=fiscal_year_end,
      ein=ein,
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
