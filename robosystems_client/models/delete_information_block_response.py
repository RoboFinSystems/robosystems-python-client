from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteInformationBlockResponse")


@_attrs_define
class DeleteInformationBlockResponse:
  """Response for ``delete-information-block``.

  The envelope is gone once the block is deleted, so the response is a
  thin confirmation instead — structure_id + block_type + name for
  caller bookkeeping.

      Attributes:
          structure_id (str):
          block_type (str):
          name (str):
          deleted (bool | Unset):  Default: True.
  """

  structure_id: str
  block_type: str
  name: str
  deleted: bool | Unset = True
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    block_type = self.block_type

    name = self.name

    deleted = self.deleted

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "block_type": block_type,
        "name": name,
      }
    )
    if deleted is not UNSET:
      field_dict["deleted"] = deleted

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    block_type = d.pop("block_type")

    name = d.pop("name")

    deleted = d.pop("deleted", UNSET)

    delete_information_block_response = cls(
      structure_id=structure_id,
      block_type=block_type,
      name=name,
      deleted=deleted,
    )

    delete_information_block_response.additional_properties = d
    return delete_information_block_response

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
