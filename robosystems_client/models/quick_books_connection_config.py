from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuickBooksConnectionConfig")


@_attrs_define
class QuickBooksConnectionConfig:
  """QuickBooks-specific connection configuration.

  Attributes:
      realm_id (Union[None, Unset, str]): QuickBooks Realm ID
      refresh_token (Union[None, Unset, str]): OAuth refresh token
  """

  realm_id: Union[None, Unset, str] = UNSET
  refresh_token: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    realm_id: Union[None, Unset, str]
    if isinstance(self.realm_id, Unset):
      realm_id = UNSET
    else:
      realm_id = self.realm_id

    refresh_token: Union[None, Unset, str]
    if isinstance(self.refresh_token, Unset):
      refresh_token = UNSET
    else:
      refresh_token = self.refresh_token

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if realm_id is not UNSET:
      field_dict["realm_id"] = realm_id
    if refresh_token is not UNSET:
      field_dict["refresh_token"] = refresh_token

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_realm_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    realm_id = _parse_realm_id(d.pop("realm_id", UNSET))

    def _parse_refresh_token(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    refresh_token = _parse_refresh_token(d.pop("refresh_token", UNSET))

    quick_books_connection_config = cls(
      realm_id=realm_id,
      refresh_token=refresh_token,
    )

    quick_books_connection_config.additional_properties = d
    return quick_books_connection_config

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
