from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_legacy_arm_block_type import UpdateLegacyArmBlockType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.update_legacy_arm_payload import UpdateLegacyArmPayload


T = TypeVar("T", bound="UpdateLegacyArm")


@_attrs_define
class UpdateLegacyArm:
  """Update-information-block body for block types that don't yet have
  a typed update path at the API boundary.

  Statement-family blocks are library-seeded and immutable. Metric
  block updates are not yet implemented. Calling this endpoint with
  one of these block types returns HTTP 501.

      Attributes:
          block_type (UpdateLegacyArmBlockType): Statement-family or metric block type. Updates return 501 — statement
              Structures are library-seeded; metric updates are pending.
          payload (UpdateLegacyArmPayload | Unset): Untyped payload — typed-arm validation is skipped because the dispatch
              handler raises 501 before the payload is consumed.
  """

  block_type: UpdateLegacyArmBlockType
  payload: UpdateLegacyArmPayload | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    block_type = self.block_type.value

    payload: dict[str, Any] | Unset = UNSET
    if not isinstance(self.payload, Unset):
      payload = self.payload.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "block_type": block_type,
      }
    )
    if payload is not UNSET:
      field_dict["payload"] = payload

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.update_legacy_arm_payload import UpdateLegacyArmPayload

    d = dict(src_dict)
    block_type = UpdateLegacyArmBlockType(d.pop("block_type"))

    _payload = d.pop("payload", UNSET)
    payload: UpdateLegacyArmPayload | Unset
    if isinstance(_payload, Unset):
      payload = UNSET
    else:
      payload = UpdateLegacyArmPayload.from_dict(_payload)

    update_legacy_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    update_legacy_arm.additional_properties = d
    return update_legacy_arm

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
