from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.auth_response_org_type_0 import AuthResponseOrgType0
  from ..models.auth_response_user import AuthResponseUser


T = TypeVar("T", bound="AuthResponse")


@_attrs_define
class AuthResponse:
  """Authentication response model.

  Attributes:
      user (AuthResponseUser): User information
      message (str): Success message
      org (Union['AuthResponseOrgType0', None, Unset]): Organization information (personal org created automatically
          on registration)
      token (Union[None, Unset, str]): JWT authentication token (optional for cookie-based auth)
      expires_in (Union[None, Unset, int]): Token expiry time in seconds from now
      refresh_threshold (Union[None, Unset, int]): Recommended refresh threshold in seconds before expiry
  """

  user: "AuthResponseUser"
  message: str
  org: Union["AuthResponseOrgType0", None, Unset] = UNSET
  token: Union[None, Unset, str] = UNSET
  expires_in: Union[None, Unset, int] = UNSET
  refresh_threshold: Union[None, Unset, int] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.auth_response_org_type_0 import AuthResponseOrgType0

    user = self.user.to_dict()

    message = self.message

    org: Union[None, Unset, dict[str, Any]]
    if isinstance(self.org, Unset):
      org = UNSET
    elif isinstance(self.org, AuthResponseOrgType0):
      org = self.org.to_dict()
    else:
      org = self.org

    token: Union[None, Unset, str]
    if isinstance(self.token, Unset):
      token = UNSET
    else:
      token = self.token

    expires_in: Union[None, Unset, int]
    if isinstance(self.expires_in, Unset):
      expires_in = UNSET
    else:
      expires_in = self.expires_in

    refresh_threshold: Union[None, Unset, int]
    if isinstance(self.refresh_threshold, Unset):
      refresh_threshold = UNSET
    else:
      refresh_threshold = self.refresh_threshold

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "user": user,
        "message": message,
      }
    )
    if org is not UNSET:
      field_dict["org"] = org
    if token is not UNSET:
      field_dict["token"] = token
    if expires_in is not UNSET:
      field_dict["expires_in"] = expires_in
    if refresh_threshold is not UNSET:
      field_dict["refresh_threshold"] = refresh_threshold

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.auth_response_org_type_0 import AuthResponseOrgType0
    from ..models.auth_response_user import AuthResponseUser

    d = dict(src_dict)
    user = AuthResponseUser.from_dict(d.pop("user"))

    message = d.pop("message")

    def _parse_org(data: object) -> Union["AuthResponseOrgType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        org_type_0 = AuthResponseOrgType0.from_dict(data)

        return org_type_0
      except:  # noqa: E722
        pass
      return cast(Union["AuthResponseOrgType0", None, Unset], data)

    org = _parse_org(d.pop("org", UNSET))

    def _parse_token(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    token = _parse_token(d.pop("token", UNSET))

    def _parse_expires_in(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    expires_in = _parse_expires_in(d.pop("expires_in", UNSET))

    def _parse_refresh_threshold(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    refresh_threshold = _parse_refresh_threshold(d.pop("refresh_threshold", UNSET))

    auth_response = cls(
      user=user,
      message=message,
      org=org,
      token=token,
      expires_in=expires_in,
      refresh_threshold=refresh_threshold,
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
