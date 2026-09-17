from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthInitResponse")


@_attrs_define
class OAuthInitResponse:
  """Where the user authorizes: a redirect URL, or a token for an embedded widget.

  Attributes:
      state (str): OAuth state for security
      expires_at (datetime.datetime): When this OAuth request expires
      auth_url (None | str | Unset): URL to redirect the user to for authorization. Null for providers that authorize
          in an embedded widget (Plaid: see link_token).
      link_token (None | str | Unset): Plaid only: the token that opens Plaid Link. Link's public_token completes the
          flow through the callback, as code.
  """

  state: str
  expires_at: datetime.datetime
  auth_url: None | str | Unset = UNSET
  link_token: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    state = self.state

    expires_at = self.expires_at.isoformat()

    auth_url: None | str | Unset
    if isinstance(self.auth_url, Unset):
      auth_url = UNSET
    else:
      auth_url = self.auth_url

    link_token: None | str | Unset
    if isinstance(self.link_token, Unset):
      link_token = UNSET
    else:
      link_token = self.link_token

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "state": state,
        "expires_at": expires_at,
      }
    )
    if auth_url is not UNSET:
      field_dict["auth_url"] = auth_url
    if link_token is not UNSET:
      field_dict["link_token"] = link_token

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    state = d.pop("state")

    expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

    def _parse_auth_url(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    auth_url = _parse_auth_url(d.pop("auth_url", UNSET))

    def _parse_link_token(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    link_token = _parse_link_token(d.pop("link_token", UNSET))

    o_auth_init_response = cls(
      state=state,
      expires_at=expires_at,
      auth_url=auth_url,
      link_token=link_token,
    )

    o_auth_init_response.additional_properties = d
    return o_auth_init_response

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
