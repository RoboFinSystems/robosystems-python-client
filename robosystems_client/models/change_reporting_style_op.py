from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChangeReportingStyleOp")


@_attrs_define
class ChangeReportingStyleOp:
  """Body for the change-reporting-style operation (Phase 2 of §3.2).

  Switches the graph to a different Reporting Style. The target Style
  must be a library- or customer-authored Structure with
  ``block_type='reporting_style'`` and a complete composition
  (one Network per required statement type — BS / IS / CF / SE). Filed
  Reports are unaffected because each ``Report`` already pins its own
  ``structure_id`` per FactSet at create-time; new reports use the new
  Style. Idempotent on the same target id.

      Attributes:
          reporting_style_id (str): Structure id of the target Reporting Style (e.g.,
              `025f5d48-12ce-5d65-b9eb-4f137a10ef06` for the library-seeded Default Style). Must resolve to a Structure with
              block_type='reporting_style' that has a complete composition in the graph's tenant schema.
  """

  reporting_style_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    reporting_style_id = self.reporting_style_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "reporting_style_id": reporting_style_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    reporting_style_id = d.pop("reporting_style_id")

    change_reporting_style_op = cls(
      reporting_style_id=reporting_style_id,
    )

    change_reporting_style_op.additional_properties = d
    return change_reporting_style_op

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
