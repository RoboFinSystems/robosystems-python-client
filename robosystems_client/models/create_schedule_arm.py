from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.create_schedule_request import CreateScheduleRequest


T = TypeVar("T", bound="CreateScheduleArm")


@_attrs_define
class CreateScheduleArm:
  """Create-information-block body for `block_type="schedule"`.

  Carries a typed schedule payload — full schedule shape is exposed
  inline in the OpenAPI schema so SDK callers see every required field.

      Attributes:
          block_type (Literal['schedule']): Discriminator value selecting this arm.
          payload (CreateScheduleRequest):
  """

  block_type: Literal["schedule"]
  payload: CreateScheduleRequest
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    block_type = self.block_type

    payload = self.payload.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "block_type": block_type,
        "payload": payload,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.create_schedule_request import CreateScheduleRequest

    d = dict(src_dict)
    block_type = cast(Literal["schedule"], d.pop("block_type"))
    if block_type != "schedule":
      raise ValueError(f"block_type must match const 'schedule', got '{block_type}'")

    payload = CreateScheduleRequest.from_dict(d.pop("payload"))

    create_schedule_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    create_schedule_arm.additional_properties = d
    return create_schedule_arm

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
