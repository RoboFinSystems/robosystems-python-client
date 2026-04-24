from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteTaxonomyBlockRequest")


@_attrs_define
class DeleteTaxonomyBlockRequest:
  """Request body for the ``delete-taxonomy-block`` operation.

  ``cascade_facts=False`` (default) fails the delete if any Fact rows
  reference elements in this taxonomy. ``cascade_facts=True`` deletes the
  referencing facts alongside the taxonomy; the response reports
  ``facts_deleted``.

      Attributes:
          taxonomy_id (str):
          reason (str): Human-readable justification (audit log).
          cascade_facts (bool | Unset):  Default: False.
  """

  taxonomy_id: str
  reason: str
  cascade_facts: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    taxonomy_id = self.taxonomy_id

    reason = self.reason

    cascade_facts = self.cascade_facts

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "taxonomy_id": taxonomy_id,
        "reason": reason,
      }
    )
    if cascade_facts is not UNSET:
      field_dict["cascade_facts"] = cascade_facts

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    taxonomy_id = d.pop("taxonomy_id")

    reason = d.pop("reason")

    cascade_facts = d.pop("cascade_facts", UNSET)

    delete_taxonomy_block_request = cls(
      taxonomy_id=taxonomy_id,
      reason=reason,
      cascade_facts=cascade_facts,
    )

    delete_taxonomy_block_request.additional_properties = d
    return delete_taxonomy_block_request

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
