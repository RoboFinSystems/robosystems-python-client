from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SECConnectionConfig")


@_attrs_define
class SECConnectionConfig:
  """SEC-specific connection configuration.

  Attributes:
      cik (str): 10-digit CIK number
      company_name (Union[None, Unset, str]): Company name from SEC
  """

  cik: str
  company_name: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    cik = self.cik

    company_name: Union[None, Unset, str]
    if isinstance(self.company_name, Unset):
      company_name = UNSET
    else:
      company_name = self.company_name

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "cik": cik,
      }
    )
    if company_name is not UNSET:
      field_dict["company_name"] = company_name

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    cik = d.pop("cik")

    def _parse_company_name(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    company_name = _parse_company_name(d.pop("company_name", UNSET))

    sec_connection_config = cls(
      cik=cik,
      company_name=company_name,
    )

    sec_connection_config.additional_properties = d
    return sec_connection_config

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
