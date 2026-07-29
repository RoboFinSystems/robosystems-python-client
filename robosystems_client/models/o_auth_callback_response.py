from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthCallbackResponse")


@_attrs_define
class OAuthCallbackResponse:
  """Result of completing an OAuth authorization flow.

  Attributes:
      success (bool): Whether the connection was established
      message (str): Human-readable outcome of the exchange
      connection_id (str): Connection the authorization was linked to
      auto_sync_task_id (None | str | Unset): Task id of the initial sync started after connecting, or null when no
          sync was kicked off
  """

  success: bool
  message: str
  connection_id: str
  auto_sync_task_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    success = self.success

    message = self.message

    connection_id = self.connection_id

    auto_sync_task_id: None | str | Unset
    if isinstance(self.auto_sync_task_id, Unset):
      auto_sync_task_id = UNSET
    else:
      auto_sync_task_id = self.auto_sync_task_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "success": success,
        "message": message,
        "connection_id": connection_id,
      }
    )
    if auto_sync_task_id is not UNSET:
      field_dict["auto_sync_task_id"] = auto_sync_task_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    success = d.pop("success")

    message = d.pop("message")

    connection_id = d.pop("connection_id")

    def _parse_auto_sync_task_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    auto_sync_task_id = _parse_auto_sync_task_id(d.pop("auto_sync_task_id", UNSET))

    o_auth_callback_response = cls(
      success=success,
      message=message,
      connection_id=connection_id,
      auto_sync_task_id=auto_sync_task_id,
    )

    o_auth_callback_response.additional_properties = d
    return o_auth_callback_response

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
