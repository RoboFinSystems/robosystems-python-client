from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasswordCheckRequest")


@_attrs_define
class PasswordCheckRequest:
  """Password strength check request model.

  Attributes:
      password (str): Password to check
      email (Union[None, Unset, str]): User email for personalization checks
  """

  password: str
  email: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    password = self.password

    email: Union[None, Unset, str]
    if isinstance(self.email, Unset):
      email = UNSET
    else:
      email = self.email

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "password": password,
      }
    )
    if email is not UNSET:
      field_dict["email"] = email

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    password = d.pop("password")

    def _parse_email(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    email = _parse_email(d.pop("email", UNSET))

    password_check_request = cls(
      password=password,
      email=email,
    )

    password_check_request.additional_properties = d
    return password_check_request

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
