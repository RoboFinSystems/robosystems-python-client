from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeReportingStyleResponse")


@_attrs_define
class ChangeReportingStyleResponse:
  """Result of a change-reporting-style operation.

  Attributes:
      entity_id (str): Entity whose Style was targeted.
      reporting_style_id (str): Active Style id after the call.
      changed (bool): False when the target equals the current Style (no-op).
      previous_reporting_style_id (None | str | Unset): Style id before the change (null for legacy/unset).
      reporting_style_code (None | str | Unset): 4-segment Style code (e.g. BSC-CORP-IS02-CF1), when stamped.
  """

  entity_id: str
  reporting_style_id: str
  changed: bool
  previous_reporting_style_id: None | str | Unset = UNSET
  reporting_style_code: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    reporting_style_id = self.reporting_style_id

    changed = self.changed

    previous_reporting_style_id: None | str | Unset
    if isinstance(self.previous_reporting_style_id, Unset):
      previous_reporting_style_id = UNSET
    else:
      previous_reporting_style_id = self.previous_reporting_style_id

    reporting_style_code: None | str | Unset
    if isinstance(self.reporting_style_code, Unset):
      reporting_style_code = UNSET
    else:
      reporting_style_code = self.reporting_style_code

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "reporting_style_id": reporting_style_id,
        "changed": changed,
      }
    )
    if previous_reporting_style_id is not UNSET:
      field_dict["previous_reporting_style_id"] = previous_reporting_style_id
    if reporting_style_code is not UNSET:
      field_dict["reporting_style_code"] = reporting_style_code

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    reporting_style_id = d.pop("reporting_style_id")

    changed = d.pop("changed")

    def _parse_previous_reporting_style_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    previous_reporting_style_id = _parse_previous_reporting_style_id(
      d.pop("previous_reporting_style_id", UNSET)
    )

    def _parse_reporting_style_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reporting_style_code = _parse_reporting_style_code(
      d.pop("reporting_style_code", UNSET)
    )

    change_reporting_style_response = cls(
      entity_id=entity_id,
      reporting_style_id=reporting_style_id,
      changed=changed,
      previous_reporting_style_id=previous_reporting_style_id,
      reporting_style_code=reporting_style_code,
    )

    change_reporting_style_response.additional_properties = d
    return change_reporting_style_response

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
