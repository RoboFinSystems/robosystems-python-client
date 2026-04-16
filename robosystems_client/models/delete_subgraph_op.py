from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteSubgraphOp")


@_attrs_define
class DeleteSubgraphOp:
  """Body for the delete-subgraph operation.

  Attributes:
      subgraph_name (str): Subgraph name to delete (e.g., 'dev', 'staging')
      force (bool | Unset): Delete even if subgraph contains data Default: False.
      backup_first (bool | Unset): Create a backup before deleting Default: True.
  """

  subgraph_name: str
  force: bool | Unset = False
  backup_first: bool | Unset = True
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    subgraph_name = self.subgraph_name

    force = self.force

    backup_first = self.backup_first

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "subgraph_name": subgraph_name,
      }
    )
    if force is not UNSET:
      field_dict["force"] = force
    if backup_first is not UNSET:
      field_dict["backup_first"] = backup_first

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    subgraph_name = d.pop("subgraph_name")

    force = d.pop("force", UNSET)

    backup_first = d.pop("backup_first", UNSET)

    delete_subgraph_op = cls(
      subgraph_name=subgraph_name,
      force=force,
      backup_first=backup_first,
    )

    delete_subgraph_op.additional_properties = d
    return delete_subgraph_op

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
