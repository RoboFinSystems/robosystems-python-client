from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InitialEntityData")


@_attrs_define
class InitialEntityData:
  """Initial entity data for graph creation.

  Attributes:
      name (str): Entity name
      uri (str): Entity website or URI
      cik (Union[None, Unset, str]): CIK number for SEC filings
      sic (Union[None, Unset, str]): SIC code
      sic_description (Union[None, Unset, str]): SIC description
      category (Union[None, Unset, str]): Business category
      state_of_incorporation (Union[None, Unset, str]): State of incorporation
      fiscal_year_end (Union[None, Unset, str]): Fiscal year end (MMDD)
      ein (Union[None, Unset, str]): Employer Identification Number
  """

  name: str
  uri: str
  cik: Union[None, Unset, str] = UNSET
  sic: Union[None, Unset, str] = UNSET
  sic_description: Union[None, Unset, str] = UNSET
  category: Union[None, Unset, str] = UNSET
  state_of_incorporation: Union[None, Unset, str] = UNSET
  fiscal_year_end: Union[None, Unset, str] = UNSET
  ein: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    uri = self.uri

    cik: Union[None, Unset, str]
    if isinstance(self.cik, Unset):
      cik = UNSET
    else:
      cik = self.cik

    sic: Union[None, Unset, str]
    if isinstance(self.sic, Unset):
      sic = UNSET
    else:
      sic = self.sic

    sic_description: Union[None, Unset, str]
    if isinstance(self.sic_description, Unset):
      sic_description = UNSET
    else:
      sic_description = self.sic_description

    category: Union[None, Unset, str]
    if isinstance(self.category, Unset):
      category = UNSET
    else:
      category = self.category

    state_of_incorporation: Union[None, Unset, str]
    if isinstance(self.state_of_incorporation, Unset):
      state_of_incorporation = UNSET
    else:
      state_of_incorporation = self.state_of_incorporation

    fiscal_year_end: Union[None, Unset, str]
    if isinstance(self.fiscal_year_end, Unset):
      fiscal_year_end = UNSET
    else:
      fiscal_year_end = self.fiscal_year_end

    ein: Union[None, Unset, str]
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

    def _parse_cik(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    cik = _parse_cik(d.pop("cik", UNSET))

    def _parse_sic(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    sic = _parse_sic(d.pop("sic", UNSET))

    def _parse_sic_description(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    sic_description = _parse_sic_description(d.pop("sic_description", UNSET))

    def _parse_category(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    category = _parse_category(d.pop("category", UNSET))

    def _parse_state_of_incorporation(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    state_of_incorporation = _parse_state_of_incorporation(
      d.pop("state_of_incorporation", UNSET)
    )

    def _parse_fiscal_year_end(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    fiscal_year_end = _parse_fiscal_year_end(d.pop("fiscal_year_end", UNSET))

    def _parse_ein(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

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
