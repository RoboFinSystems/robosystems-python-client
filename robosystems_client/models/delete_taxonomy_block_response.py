from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteTaxonomyBlockResponse")


@_attrs_define
class DeleteTaxonomyBlockResponse:
  """Response for ``delete-taxonomy-block``.

  Attributes:
      taxonomy_id (str):
      name (str):
      deleted (bool | Unset):  Default: True.
      facts_deleted (int | Unset):  Default: 0.
      cascade_applied (bool | Unset):  Default: False.
  """

  taxonomy_id: str
  name: str
  deleted: bool | Unset = True
  facts_deleted: int | Unset = 0
  cascade_applied: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    taxonomy_id = self.taxonomy_id

    name = self.name

    deleted = self.deleted

    facts_deleted = self.facts_deleted

    cascade_applied = self.cascade_applied

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "taxonomy_id": taxonomy_id,
        "name": name,
      }
    )
    if deleted is not UNSET:
      field_dict["deleted"] = deleted
    if facts_deleted is not UNSET:
      field_dict["facts_deleted"] = facts_deleted
    if cascade_applied is not UNSET:
      field_dict["cascade_applied"] = cascade_applied

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    taxonomy_id = d.pop("taxonomy_id")

    name = d.pop("name")

    deleted = d.pop("deleted", UNSET)

    facts_deleted = d.pop("facts_deleted", UNSET)

    cascade_applied = d.pop("cascade_applied", UNSET)

    delete_taxonomy_block_response = cls(
      taxonomy_id=taxonomy_id,
      name=name,
      deleted=deleted,
      facts_deleted=facts_deleted,
      cascade_applied=cascade_applied,
    )

    delete_taxonomy_block_response.additional_properties = d
    return delete_taxonomy_block_response

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
