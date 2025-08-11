import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SSOTokenResponse")


@_attrs_define
class SSOTokenResponse:
  """SSO token response model.

  Attributes:
      token (str): Temporary SSO token for cross-app authentication
      expires_at (datetime.datetime): Token expiration time
      apps (list[str]): Available apps for this user
  """

  token: str
  expires_at: datetime.datetime
  apps: list[str]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    token = self.token

    expires_at = self.expires_at.isoformat()

    apps = self.apps

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "token": token,
        "expires_at": expires_at,
        "apps": apps,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    token = d.pop("token")

    expires_at = isoparse(d.pop("expires_at"))

    apps = cast(list[str], d.pop("apps"))

    sso_token_response = cls(
      token=token,
      expires_at=expires_at,
      apps=apps,
    )

    sso_token_response.additional_properties = d
    return sso_token_response

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
