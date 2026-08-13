from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasskeyInfo")


@_attrs_define
class PasskeyInfo:
  """One enrolled passkey, as listed in account settings.

  Attributes:
      id (str): Passkey identifier
      name (str): User-facing label
      created_at (str): Enrollment time (ISO 8601)
      backup_eligible (bool): Whether the credential is synced (multi-device) capable
      backup_state (bool): Whether the credential is currently backed up
      last_used_at (None | str | Unset): Last successful assertion time (ISO 8601)
  """

  id: str
  name: str
  created_at: str
  backup_eligible: bool
  backup_state: bool
  last_used_at: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    created_at = self.created_at

    backup_eligible = self.backup_eligible

    backup_state = self.backup_state

    last_used_at: None | str | Unset
    if isinstance(self.last_used_at, Unset):
      last_used_at = UNSET
    else:
      last_used_at = self.last_used_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "created_at": created_at,
        "backup_eligible": backup_eligible,
        "backup_state": backup_state,
      }
    )
    if last_used_at is not UNSET:
      field_dict["last_used_at"] = last_used_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    created_at = d.pop("created_at")

    backup_eligible = d.pop("backup_eligible")

    backup_state = d.pop("backup_state")

    def _parse_last_used_at(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

    passkey_info = cls(
      id=id,
      name=name,
      created_at=created_at,
      backup_eligible=backup_eligible,
      backup_state=backup_state,
      last_used_at=last_used_at,
    )

    passkey_info.additional_properties = d
    return passkey_info

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
