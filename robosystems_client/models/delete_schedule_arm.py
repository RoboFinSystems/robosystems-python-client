from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.delete_schedule_request import DeleteScheduleRequest


T = TypeVar("T", bound="DeleteScheduleArm")


@_attrs_define
class DeleteScheduleArm:
  """Delete-information-block body for `block_type="schedule"`.

  Carries a typed schedule delete payload — just the `structure_id`.

      Attributes:
          block_type (Literal['schedule']): Discriminator value selecting this arm.
          payload (DeleteScheduleRequest): Delete a schedule — cascades through facts and associations.

              Hard deletes the Structure, all Facts tied to it, and all
              Associations tied to it. This is a permanent, irreversible
              operation. For ending a schedule early without removing history,
              fire `create-event-block(event_type='asset_disposed')` instead — the
              handler truncates the schedule + posts the disposal entry atomically.
  """

  block_type: Literal["schedule"]
  payload: DeleteScheduleRequest
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
    from ..models.delete_schedule_request import DeleteScheduleRequest

    d = dict(src_dict)
    block_type = cast(Literal["schedule"], d.pop("block_type"))
    if block_type != "schedule":
      raise ValueError(f"block_type must match const 'schedule', got '{block_type}'")

    payload = DeleteScheduleRequest.from_dict(d.pop("payload"))

    delete_schedule_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    delete_schedule_arm.additional_properties = d
    return delete_schedule_arm

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
