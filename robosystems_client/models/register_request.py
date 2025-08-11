from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterRequest")


@_attrs_define
class RegisterRequest:
  """Registration request model.

  Attributes:
      name (str): User's display name
      email (str): User's email address
      password (str): User's password (must meet security requirements)
      captcha_token (Union[None, Unset, str]): CAPTCHA verification token (required in production)
  """

  name: str
  email: str
  password: str
  captcha_token: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    email = self.email

    password = self.password

    captcha_token: Union[None, Unset, str]
    if isinstance(self.captcha_token, Unset):
      captcha_token = UNSET
    else:
      captcha_token = self.captcha_token

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
        "email": email,
        "password": password,
      }
    )
    if captcha_token is not UNSET:
      field_dict["captcha_token"] = captcha_token

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    email = d.pop("email")

    password = d.pop("password")

    def _parse_captcha_token(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    captcha_token = _parse_captcha_token(d.pop("captcha_token", UNSET))

    register_request = cls(
      name=name,
      email=email,
      password=password,
      captcha_token=captcha_token,
    )

    register_request.additional_properties = d
    return register_request

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
