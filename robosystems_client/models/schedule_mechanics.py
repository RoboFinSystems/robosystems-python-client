from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.entry_template_request import EntryTemplateRequest
  from ..models.schedule_metadata_request import ScheduleMetadataRequest


T = TypeVar("T", bound="ScheduleMechanics")


@_attrs_define
class ScheduleMechanics:
  """Closing-entry generator mechanics for ``block_type='schedule'``.

  Reads directly from the typed ``structures.artifact_mechanics`` JSONB
  column. ``entry_template`` and ``schedule_metadata`` are typed
  sub-models (reusing the wire-level request shapes so OpenAPI emits one
  canonical type per concept); the envelope builder falls back to
  ``structures.metadata_`` for legacy Schedule rows that the tenant
  backfill hasn't yet migrated to the typed column.

      Attributes:
          entry_template (EntryTemplateRequest):
          kind (Literal['closing_entry_generator'] | Unset):  Default: 'closing_entry_generator'.
          schedule_metadata (None | ScheduleMetadataRequest | Unset): Method (straight_line / declining_balance /
              units_of_production), original_amount, residual_value, useful_life_months, optional asset_element_id for net-
              book-value cross-reference.
          periods_with_entries (int | Unset): Number of in-scope periods that have at least one closing entry posted.
              Runtime state derived at envelope-build time from the Entry table. Default: 0.
  """

  entry_template: EntryTemplateRequest
  kind: Literal["closing_entry_generator"] | Unset = "closing_entry_generator"
  schedule_metadata: None | ScheduleMetadataRequest | Unset = UNSET
  periods_with_entries: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.schedule_metadata_request import ScheduleMetadataRequest

    entry_template = self.entry_template.to_dict()

    kind = self.kind

    schedule_metadata: dict[str, Any] | None | Unset
    if isinstance(self.schedule_metadata, Unset):
      schedule_metadata = UNSET
    elif isinstance(self.schedule_metadata, ScheduleMetadataRequest):
      schedule_metadata = self.schedule_metadata.to_dict()
    else:
      schedule_metadata = self.schedule_metadata

    periods_with_entries = self.periods_with_entries

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entry_template": entry_template,
      }
    )
    if kind is not UNSET:
      field_dict["kind"] = kind
    if schedule_metadata is not UNSET:
      field_dict["schedule_metadata"] = schedule_metadata
    if periods_with_entries is not UNSET:
      field_dict["periods_with_entries"] = periods_with_entries

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.entry_template_request import EntryTemplateRequest
    from ..models.schedule_metadata_request import ScheduleMetadataRequest

    d = dict(src_dict)
    entry_template = EntryTemplateRequest.from_dict(d.pop("entry_template"))

    kind = cast(Literal["closing_entry_generator"] | Unset, d.pop("kind", UNSET))
    if kind != "closing_entry_generator" and not isinstance(kind, Unset):
      raise ValueError(f"kind must match const 'closing_entry_generator', got '{kind}'")

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

    periods_with_entries = d.pop("periods_with_entries", UNSET)

    schedule_mechanics = cls(
      entry_template=entry_template,
      kind=kind,
      schedule_metadata=schedule_metadata,
      periods_with_entries=periods_with_entries,
    )

    schedule_mechanics.additional_properties = d
    return schedule_mechanics

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
