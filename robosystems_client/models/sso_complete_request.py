from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSOCompleteRequest")


@_attrs_define
class SSOCompleteRequest:
  """SSO completion request model.

  Attributes:
      session_id (str): Temporary session ID from secure handoff
      browser_nonce (None | str | Unset): The nonce this browser minted when it started the bridge; its SHA-256 was
          passed through the exchange as browser_nonce_hash. Required to complete a handoff.
  """

  session_id: str
  browser_nonce: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    session_id = self.session_id

    browser_nonce: None | str | Unset
    if isinstance(self.browser_nonce, Unset):
      browser_nonce = UNSET
    else:
      browser_nonce = self.browser_nonce

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "session_id": session_id,
      }
    )
    if browser_nonce is not UNSET:
      field_dict["browser_nonce"] = browser_nonce

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    session_id = d.pop("session_id")

    def _parse_browser_nonce(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    browser_nonce = _parse_browser_nonce(d.pop("browser_nonce", UNSET))

    sso_complete_request = cls(
      session_id=session_id,
      browser_nonce=browser_nonce,
    )

    sso_complete_request.additional_properties = d
    return sso_complete_request

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
