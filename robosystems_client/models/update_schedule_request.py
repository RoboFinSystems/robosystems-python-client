from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.entry_template_request import EntryTemplateRequest
  from ..models.schedule_metadata_request import ScheduleMetadataRequest


T = TypeVar("T", bound="UpdateScheduleRequest")


@_attrs_define
class UpdateScheduleRequest:
  """Update mutable fields on a schedule.

  Editable: name, entry_template, schedule_metadata (all live on the
  Structure row / its metadata_ JSONB column).

  NOT editable via this op: period_start, period_end, monthly_amount.
  Those require fact regeneration — fire an event block that terminates
  the schedule (e.g., `asset_disposed`) and create a fresh schedule via
  `create-schedule`.

  Omitted fields are left unchanged.

      Attributes:
          structure_id (str):
          name (None | str | Unset):
          entry_template (EntryTemplateRequest | None | Unset):
          schedule_metadata (None | ScheduleMetadataRequest | Unset):
  """

  structure_id: str
  name: None | str | Unset = UNSET
  entry_template: EntryTemplateRequest | None | Unset = UNSET
  schedule_metadata: None | ScheduleMetadataRequest | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.entry_template_request import EntryTemplateRequest
    from ..models.schedule_metadata_request import ScheduleMetadataRequest

    structure_id = self.structure_id

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    entry_template: dict[str, Any] | None | Unset
    if isinstance(self.entry_template, Unset):
      entry_template = UNSET
    elif isinstance(self.entry_template, EntryTemplateRequest):
      entry_template = self.entry_template.to_dict()
    else:
      entry_template = self.entry_template

    schedule_metadata: dict[str, Any] | None | Unset
    if isinstance(self.schedule_metadata, Unset):
      schedule_metadata = UNSET
    elif isinstance(self.schedule_metadata, ScheduleMetadataRequest):
      schedule_metadata = self.schedule_metadata.to_dict()
    else:
      schedule_metadata = self.schedule_metadata

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if entry_template is not UNSET:
      field_dict["entry_template"] = entry_template
    if schedule_metadata is not UNSET:
      field_dict["schedule_metadata"] = schedule_metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.entry_template_request import EntryTemplateRequest
    from ..models.schedule_metadata_request import ScheduleMetadataRequest

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_entry_template(data: object) -> EntryTemplateRequest | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        entry_template_type_0 = EntryTemplateRequest.from_dict(data)

        return entry_template_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(EntryTemplateRequest | None | Unset, data)

    entry_template = _parse_entry_template(d.pop("entry_template", UNSET))

    def _parse_schedule_metadata(
      data: object,
    ) -> None | ScheduleMetadataRequest | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        schedule_metadata_type_0 = ScheduleMetadataRequest.from_dict(data)

        return schedule_metadata_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ScheduleMetadataRequest | Unset, data)

    schedule_metadata = _parse_schedule_metadata(d.pop("schedule_metadata", UNSET))

    update_schedule_request = cls(
      structure_id=structure_id,
      name=name,
      entry_template=entry_template,
      schedule_metadata=schedule_metadata,
    )

    update_schedule_request.additional_properties = d
    return update_schedule_request

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
