from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeReportingStyleRequest")


@_attrs_define
class ChangeReportingStyleRequest:
  """Switch a reporting entity's Reporting Style.

  The Reporting Style governs how the entity's statements are laid out
  (equity-form, close-target concept, per-statement Networks). It's
  validated against the tenant schema — the target must be a renderable
  Style with a complete composition — before the switch is applied.

      Attributes:
          reporting_style_id (str): Structure id of the target Reporting Style. Must exist in the tenant schema with a
              complete Network composition.
          entity_id (None | str | Unset): Target entity. Omit to target the graph's primary (earliest-created) entity —
              the single-entity default.
  """

  reporting_style_id: str
  entity_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    reporting_style_id = self.reporting_style_id

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "reporting_style_id": reporting_style_id,
      }
    )
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    reporting_style_id = d.pop("reporting_style_id")

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    change_reporting_style_request = cls(
      reporting_style_id=reporting_style_id,
      entity_id=entity_id,
    )

    change_reporting_style_request.additional_properties = d
    return change_reporting_style_request

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
