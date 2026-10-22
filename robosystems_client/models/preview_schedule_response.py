from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.information_block_envelope import InformationBlockEnvelope
  from ..models.schedule_replacement_summary import ScheduleReplacementSummary
  from ..models.schedule_roll_forward_row import ScheduleRollForwardRow


T = TypeVar("T", bound="PreviewScheduleResponse")


@_attrs_define
class PreviewScheduleResponse:
  """A generated schedule nobody kept: its envelope as create would leave
  it, period by period.

      Attributes:
          envelope (InformationBlockEnvelope): The Information Block exchange format.

              One envelope per block instance. Carries the block's identity + type,
              Information-Model attributes, the Artifact branch (mechanics +
              topic/template), and bundled atoms (elements, connections, facts).
              Rules / dimensions / FactSet / verification_results are present-but-
              empty for blocks where the upstream content (rule engine, FactSet
              expand, dimension catalog) has not yet been implemented.
          roll_forward (list[ScheduleRollForwardRow] | Unset):
          warnings (list[str] | Unset): Things create would go ahead with that deserve a look: an active schedule already
              posting to the same accounts over the same months.
          replaces (None | ScheduleReplacementSummary | Unset): With `replaces_structure_id`: the schedule being replaced.
  """

  envelope: InformationBlockEnvelope
  roll_forward: list[ScheduleRollForwardRow] | Unset = UNSET
  warnings: list[str] | Unset = UNSET
  replaces: None | ScheduleReplacementSummary | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.schedule_replacement_summary import ScheduleReplacementSummary

    envelope = self.envelope.to_dict()

    roll_forward: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.roll_forward, Unset):
      roll_forward = []
      for roll_forward_item_data in self.roll_forward:
        roll_forward_item = roll_forward_item_data.to_dict()
        roll_forward.append(roll_forward_item)

    warnings: list[str] | Unset = UNSET
    if not isinstance(self.warnings, Unset):
      warnings = self.warnings

    replaces: dict[str, Any] | None | Unset
    if isinstance(self.replaces, Unset):
      replaces = UNSET
    elif isinstance(self.replaces, ScheduleReplacementSummary):
      replaces = self.replaces.to_dict()
    else:
      replaces = self.replaces

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "envelope": envelope,
      }
    )
    if roll_forward is not UNSET:
      field_dict["roll_forward"] = roll_forward
    if warnings is not UNSET:
      field_dict["warnings"] = warnings
    if replaces is not UNSET:
      field_dict["replaces"] = replaces

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.information_block_envelope import InformationBlockEnvelope
    from ..models.schedule_replacement_summary import ScheduleReplacementSummary
    from ..models.schedule_roll_forward_row import ScheduleRollForwardRow

    d = dict(src_dict)
    envelope = InformationBlockEnvelope.from_dict(d.pop("envelope"))

    _roll_forward = d.pop("roll_forward", UNSET)
    roll_forward: list[ScheduleRollForwardRow] | Unset = UNSET
    if _roll_forward is not UNSET:
      roll_forward = []
      for roll_forward_item_data in _roll_forward:
        roll_forward_item = ScheduleRollForwardRow.from_dict(roll_forward_item_data)

        roll_forward.append(roll_forward_item)

    warnings = cast(list[str], d.pop("warnings", UNSET))

    def _parse_replaces(data: object) -> None | ScheduleReplacementSummary | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        replaces_type_0 = ScheduleReplacementSummary.from_dict(data)

        return replaces_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ScheduleReplacementSummary | Unset, data)

    replaces = _parse_replaces(d.pop("replaces", UNSET))

    preview_schedule_response = cls(
      envelope=envelope,
      roll_forward=roll_forward,
      warnings=warnings,
      replaces=replaces,
    )

    preview_schedule_response.additional_properties = d
    return preview_schedule_response

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
