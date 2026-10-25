from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSOExchangeRequest")


@_attrs_define
class SSOExchangeRequest:
  """SSO token exchange request model.

  Attributes:
      token (str): Temporary SSO token
      target_app (str): Target application identifier
      return_url (None | str | Unset): Optional return URL after authentication
      browser_nonce_hash (None | str | Unset): SHA-256 (hex) of a nonce the target app minted in the browser that is
          signing in. Completion must present the nonce, so the handoff cannot be redeemed by any other browser; a session
          exchanged without one cannot be completed.
  """

  token: str
  target_app: str
  return_url: None | str | Unset = UNSET
  browser_nonce_hash: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    token = self.token

    target_app = self.target_app

    return_url: None | str | Unset
    if isinstance(self.return_url, Unset):
      return_url = UNSET
    else:
      return_url = self.return_url

    browser_nonce_hash: None | str | Unset
    if isinstance(self.browser_nonce_hash, Unset):
      browser_nonce_hash = UNSET
    else:
      browser_nonce_hash = self.browser_nonce_hash

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "token": token,
        "target_app": target_app,
      }
    )
    if return_url is not UNSET:
      field_dict["return_url"] = return_url
    if browser_nonce_hash is not UNSET:
      field_dict["browser_nonce_hash"] = browser_nonce_hash

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    token = d.pop("token")

    target_app = d.pop("target_app")

    def _parse_return_url(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    return_url = _parse_return_url(d.pop("return_url", UNSET))

    def _parse_browser_nonce_hash(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    browser_nonce_hash = _parse_browser_nonce_hash(d.pop("browser_nonce_hash", UNSET))

    sso_exchange_request = cls(
      token=token,
      target_app=target_app,
      return_url=return_url,
      browser_nonce_hash=browser_nonce_hash,
    )

    sso_exchange_request.additional_properties = d
    return sso_exchange_request

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
