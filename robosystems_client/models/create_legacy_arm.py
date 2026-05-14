from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_legacy_arm_block_type import CreateLegacyArmBlockType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.create_legacy_arm_payload import CreateLegacyArmPayload


T = TypeVar("T", bound="CreateLegacyArm")


@_attrs_define
class CreateLegacyArm:
  """Create-information-block body for block types that don't yet have
  a typed construction path at the API boundary.

  Statement-family blocks (balance_sheet, income_statement,
  cash_flow_statement, equity_statement, comprehensive_income) are
  constructed via `create-report`, not this endpoint. Metric blocks
  are recognized but their evaluator has not shipped. Calling this
  endpoint with one of these block types returns HTTP 501 with a hint
  pointing to the correct construction path.

      Attributes:
          block_type (CreateLegacyArmBlockType): Statement-family or metric block type. The endpoint returns 501 for these
              values — statements are constructed via `create-report`; metric construction is pending.
          payload (CreateLegacyArmPayload | Unset): Untyped payload — typed-arm validation is skipped because the dispatch
              handler raises 501 before the payload is consumed.
  """

  block_type: CreateLegacyArmBlockType
  payload: CreateLegacyArmPayload | Unset = UNSET
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
    from ..models.create_legacy_arm_payload import CreateLegacyArmPayload

    d = dict(src_dict)
    block_type = CreateLegacyArmBlockType(d.pop("block_type"))

    _payload = d.pop("payload", UNSET)
    payload: CreateLegacyArmPayload | Unset
    if isinstance(_payload, Unset):
      payload = UNSET
    else:
      payload = CreateLegacyArmPayload.from_dict(_payload)

    create_legacy_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    create_legacy_arm.additional_properties = d
    return create_legacy_arm

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
