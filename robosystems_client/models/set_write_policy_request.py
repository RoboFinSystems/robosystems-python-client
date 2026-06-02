from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_write_policy_request_write_policy import (
  SetWritePolicyRequestWritePolicy,
)

T = TypeVar("T", bound="SetWritePolicyRequest")


@_attrs_define
class SetWritePolicyRequest:
  """Request to set a connection's source-of-truth write policy.

  The explicit operator opt-in for outbound write-back. `hybrid` is omitted
  until its code path ships.

      Attributes:
          write_policy (SetWritePolicyRequestWritePolicy): 'native' = RoboSystems authoritative, no write-back;
              'qb_authoritative' = QuickBooks authoritative, entries publish to QB.
  """

  write_policy: SetWritePolicyRequestWritePolicy
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    write_policy = self.write_policy.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "write_policy": write_policy,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    write_policy = SetWritePolicyRequestWritePolicy(d.pop("write_policy"))

    set_write_policy_request = cls(
      write_policy=write_policy,
    )

    set_write_policy_request.additional_properties = d
    return set_write_policy_request

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
