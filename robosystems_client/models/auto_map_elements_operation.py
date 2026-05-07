from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AutoMapElementsOperation")


@_attrs_define
class AutoMapElementsOperation:
  """Run the MappingAgent over a mapping structure (async).

  The MappingAgent walks every unmapped CoA element and proposes
  associations to reporting concepts. Confidence thresholds: ≥0.90
  auto-approved (association created), 0.70-0.89 flagged for review
  (created with `confidence` set; surface it in your UI), <0.70 skipped.
  Returns a `pending` envelope immediately; subscribe to the SSE stream
  for progress.

      Attributes:
          mapping_id (str): The mapping structure to populate.
  """

  mapping_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    mapping_id = self.mapping_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "mapping_id": mapping_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    mapping_id = d.pop("mapping_id")

    auto_map_elements_operation = cls(
      mapping_id=mapping_id,
    )

    auto_map_elements_operation.additional_properties = d
    return auto_map_elements_operation

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
