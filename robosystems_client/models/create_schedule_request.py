from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.entry_template_request import EntryTemplateRequest
  from ..models.schedule_metadata_request import ScheduleMetadataRequest


T = TypeVar("T", bound="CreateScheduleRequest")


@_attrs_define
class CreateScheduleRequest:
  """
  Attributes:
      name (str): Schedule name
      element_ids (list[str]): Element IDs to include
      period_start (datetime.date): First period start
      period_end (datetime.date): Last period end
      monthly_amount (int): Monthly amount in cents
      entry_template (EntryTemplateRequest):
      taxonomy_id (None | str | Unset): Taxonomy ID (auto-creates if omitted)
      schedule_metadata (None | ScheduleMetadataRequest | Unset):
  """

  name: str
  element_ids: list[str]
  period_start: datetime.date
  period_end: datetime.date
  monthly_amount: int
  entry_template: EntryTemplateRequest
  taxonomy_id: None | str | Unset = UNSET
  schedule_metadata: None | ScheduleMetadataRequest | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.schedule_metadata_request import ScheduleMetadataRequest

    name = self.name

    element_ids = self.element_ids

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    monthly_amount = self.monthly_amount

    entry_template = self.entry_template.to_dict()

    taxonomy_id: None | str | Unset
    if isinstance(self.taxonomy_id, Unset):
      taxonomy_id = UNSET
    else:
      taxonomy_id = self.taxonomy_id

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
        "name": name,
        "element_ids": element_ids,
        "period_start": period_start,
        "period_end": period_end,
        "monthly_amount": monthly_amount,
        "entry_template": entry_template,
      }
    )
    if taxonomy_id is not UNSET:
      field_dict["taxonomy_id"] = taxonomy_id
    if schedule_metadata is not UNSET:
      field_dict["schedule_metadata"] = schedule_metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.entry_template_request import EntryTemplateRequest
    from ..models.schedule_metadata_request import ScheduleMetadataRequest

    d = dict(src_dict)
    name = d.pop("name")

    element_ids = cast(list[str], d.pop("element_ids"))

    period_start = isoparse(d.pop("period_start")).date()

    period_end = isoparse(d.pop("period_end")).date()

    monthly_amount = d.pop("monthly_amount")

    entry_template = EntryTemplateRequest.from_dict(d.pop("entry_template"))

    def _parse_taxonomy_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    taxonomy_id = _parse_taxonomy_id(d.pop("taxonomy_id", UNSET))

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

    create_schedule_request = cls(
      name=name,
      element_ids=element_ids,
      period_start=period_start,
      period_end=period_end,
      monthly_amount=monthly_amount,
      entry_template=entry_template,
      taxonomy_id=taxonomy_id,
      schedule_metadata=schedule_metadata,
    )

    create_schedule_request.additional_properties = d
    return create_schedule_request

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
