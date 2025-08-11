import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SSOExchangeResponse")


@_attrs_define
class SSOExchangeResponse:
  """SSO token exchange response model.

  Attributes:
      session_id (str): Temporary session ID for secure handoff
      redirect_url (str): URL to redirect to for authentication
      expires_at (datetime.datetime): Session expiration time
  """

  session_id: str
  redirect_url: str
  expires_at: datetime.datetime
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    session_id = self.session_id

    redirect_url = self.redirect_url

    expires_at = self.expires_at.isoformat()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "session_id": session_id,
        "redirect_url": redirect_url,
        "expires_at": expires_at,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    session_id = d.pop("session_id")

    redirect_url = d.pop("redirect_url")

    expires_at = isoparse(d.pop("expires_at"))

    sso_exchange_response = cls(
      session_id=session_id,
      redirect_url=redirect_url,
      expires_at=expires_at,
    )

    sso_exchange_response.additional_properties = d
    return sso_exchange_response

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
