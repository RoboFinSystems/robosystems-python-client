from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecordDeconsolidationRequest")


@_attrs_define
class RecordDeconsolidationRequest:
  """A member has left the group (`left_on` set): what the parent received
  for its shares, and the basis. The entry derecognizes what the
  consolidation entity still holds for the member and takes the gain or
  loss on its leaving; the parent's own sale entry stays on its books.

      Attributes:
          entity_id (str): The member that left: its `left_on` is set.
          consideration (int): Cents the parent received for its shares; 0 for a dissolution or an abandonment. Recorded
              with the entry for the record: the parent's own books hold the sale, cash against its investment and its own
              gain or loss, which this entry adjusts to the group's.
          basis (str): The sale agreement, the dissolution, or what sets the price.
  """

  entity_id: str
  consideration: int
  basis: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    consideration = self.consideration

    basis = self.basis

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "consideration": consideration,
        "basis": basis,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    consideration = d.pop("consideration")

    basis = d.pop("basis")

    record_deconsolidation_request = cls(
      entity_id=entity_id,
      consideration=consideration,
      basis=basis,
    )

    record_deconsolidation_request.additional_properties = d
    return record_deconsolidation_request

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
