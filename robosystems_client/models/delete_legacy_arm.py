from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_legacy_arm_block_type import DeleteLegacyArmBlockType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.delete_legacy_arm_payload import DeleteLegacyArmPayload


T = TypeVar("T", bound="DeleteLegacyArm")


@_attrs_define
class DeleteLegacyArm:
  """Delete-information-block body for block types that don't yet have
  a typed delete path at the API boundary.

  Statement-family blocks cannot be deleted per tenant (the underlying
  Report should be archived via the report APIs instead). Metric
  deletion is not yet implemented. Calls return HTTP 501.

      Attributes:
          block_type (DeleteLegacyArmBlockType): Statement-family or metric block type. Deletion returns 501 — statements
              are library-seeded (archive the underlying Report instead); metric deletion is pending.
          payload (DeleteLegacyArmPayload | Unset): Untyped payload — typed-arm validation is skipped because the dispatch
              handler raises 501 before the payload is consumed.
  """

  block_type: DeleteLegacyArmBlockType
  payload: DeleteLegacyArmPayload | Unset = UNSET
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
    from ..models.delete_legacy_arm_payload import DeleteLegacyArmPayload

    d = dict(src_dict)
    block_type = DeleteLegacyArmBlockType(d.pop("block_type"))

    _payload = d.pop("payload", UNSET)
    payload: DeleteLegacyArmPayload | Unset
    if isinstance(_payload, Unset):
      payload = UNSET
    else:
      payload = DeleteLegacyArmPayload.from_dict(_payload)

    delete_legacy_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    delete_legacy_arm.additional_properties = d
    return delete_legacy_arm

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
