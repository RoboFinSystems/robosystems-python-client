from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.auth_response_user import AuthResponseUser


T = TypeVar("T", bound="AuthResponse")


@_attrs_define
class AuthResponse:
  """Authentication response model.

  Attributes:
      user (AuthResponseUser): User information
      message (str): Success message
      token (Union[None, Unset, str]): JWT authentication token (optional for cookie-based auth)
  """

  user: "AuthResponseUser"
  message: str
  token: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    user = self.user.to_dict()

    message = self.message

    token: Union[None, Unset, str]
    if isinstance(self.token, Unset):
      token = UNSET
    else:
      token = self.token

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "user": user,
        "message": message,
      }
    )
    if token is not UNSET:
      field_dict["token"] = token

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.auth_response_user import AuthResponseUser

    d = dict(src_dict)
    user = AuthResponseUser.from_dict(d.pop("user"))

    message = d.pop("message")

    def _parse_token(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    token = _parse_token(d.pop("token", UNSET))

    auth_response = cls(
      user=user,
      message=message,
      token=token,
    )

    auth_response.additional_properties = d
    return auth_response

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
