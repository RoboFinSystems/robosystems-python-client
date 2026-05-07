from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.update_schedule_request import UpdateScheduleRequest


T = TypeVar("T", bound="UpdateScheduleArm")


@_attrs_define
class UpdateScheduleArm:
  """Update-information-block body for `block_type="schedule"`.

  Carries a typed schedule update payload — full editable shape is
  exposed inline.

      Attributes:
          block_type (Literal['schedule']): Discriminator value selecting this arm.
          payload (UpdateScheduleRequest): Update mutable fields on a schedule.

              Editable: name, entry_template, schedule_metadata (all live on the
              Structure row / its metadata_ JSONB column).

              NOT editable via this op: period_start, period_end, monthly_amount.
              Those require fact regeneration — fire an event block that terminates
              the schedule (e.g., `asset_disposed`) and create a fresh schedule via
              `create-schedule`.

              Omitted fields are left unchanged.
  """

  block_type: Literal["schedule"]
  payload: UpdateScheduleRequest
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
    from ..models.update_schedule_request import UpdateScheduleRequest

    d = dict(src_dict)
    block_type = cast(Literal["schedule"], d.pop("block_type"))
    if block_type != "schedule":
      raise ValueError(f"block_type must match const 'schedule', got '{block_type}'")

    payload = UpdateScheduleRequest.from_dict(d.pop("payload"))

    update_schedule_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    update_schedule_arm.additional_properties = d
    return update_schedule_arm

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
