from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.schedule_summary_response_entry_template_type_0 import (
    ScheduleSummaryResponseEntryTemplateType0,
  )
  from ..models.schedule_summary_response_schedule_metadata_type_0 import (
    ScheduleSummaryResponseScheduleMetadataType0,
  )


T = TypeVar("T", bound="ScheduleSummaryResponse")


@_attrs_define
class ScheduleSummaryResponse:
  """
  Attributes:
      structure_id (str):
      name (str):
      taxonomy_name (str):
      total_periods (int):
      periods_with_entries (int):
      entry_template (None | ScheduleSummaryResponseEntryTemplateType0 | Unset):
      schedule_metadata (None | ScheduleSummaryResponseScheduleMetadataType0 | Unset):
  """

  structure_id: str
  name: str
  taxonomy_name: str
  total_periods: int
  periods_with_entries: int
  entry_template: None | ScheduleSummaryResponseEntryTemplateType0 | Unset = UNSET
  schedule_metadata: None | ScheduleSummaryResponseScheduleMetadataType0 | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.schedule_summary_response_entry_template_type_0 import (
      ScheduleSummaryResponseEntryTemplateType0,
    )
    from ..models.schedule_summary_response_schedule_metadata_type_0 import (
      ScheduleSummaryResponseScheduleMetadataType0,
    )

    structure_id = self.structure_id

    name = self.name

    taxonomy_name = self.taxonomy_name

    total_periods = self.total_periods

    periods_with_entries = self.periods_with_entries

    entry_template: dict[str, Any] | None | Unset
    if isinstance(self.entry_template, Unset):
      entry_template = UNSET
    elif isinstance(self.entry_template, ScheduleSummaryResponseEntryTemplateType0):
      entry_template = self.entry_template.to_dict()
    else:
      entry_template = self.entry_template

    schedule_metadata: dict[str, Any] | None | Unset
    if isinstance(self.schedule_metadata, Unset):
      schedule_metadata = UNSET
    elif isinstance(
      self.schedule_metadata, ScheduleSummaryResponseScheduleMetadataType0
    ):
      schedule_metadata = self.schedule_metadata.to_dict()
    else:
      schedule_metadata = self.schedule_metadata

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "name": name,
        "taxonomy_name": taxonomy_name,
        "total_periods": total_periods,
        "periods_with_entries": periods_with_entries,
      }
    )
    if entry_template is not UNSET:
      field_dict["entry_template"] = entry_template
    if schedule_metadata is not UNSET:
      field_dict["schedule_metadata"] = schedule_metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.schedule_summary_response_entry_template_type_0 import (
      ScheduleSummaryResponseEntryTemplateType0,
    )
    from ..models.schedule_summary_response_schedule_metadata_type_0 import (
      ScheduleSummaryResponseScheduleMetadataType0,
    )

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    name = d.pop("name")

    taxonomy_name = d.pop("taxonomy_name")

    total_periods = d.pop("total_periods")

    periods_with_entries = d.pop("periods_with_entries")

    def _parse_entry_template(
      data: object,
    ) -> None | ScheduleSummaryResponseEntryTemplateType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        entry_template_type_0 = ScheduleSummaryResponseEntryTemplateType0.from_dict(
          data
        )

        return entry_template_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ScheduleSummaryResponseEntryTemplateType0 | Unset, data)

    entry_template = _parse_entry_template(d.pop("entry_template", UNSET))

    def _parse_schedule_metadata(
      data: object,
    ) -> None | ScheduleSummaryResponseScheduleMetadataType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        schedule_metadata_type_0 = (
          ScheduleSummaryResponseScheduleMetadataType0.from_dict(data)
        )

        return schedule_metadata_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ScheduleSummaryResponseScheduleMetadataType0 | Unset, data)

    schedule_metadata = _parse_schedule_metadata(d.pop("schedule_metadata", UNSET))

    schedule_summary_response = cls(
      structure_id=structure_id,
      name=name,
      taxonomy_name=taxonomy_name,
      total_periods=total_periods,
      periods_with_entries=periods_with_entries,
      entry_template=entry_template,
      schedule_metadata=schedule_metadata,
    )

    schedule_summary_response.additional_properties = d
    return schedule_summary_response

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
