from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteFileOp")


@_attrs_define
class DeleteFileOp:
  """Body for delete-file (raw content-op).

  Attributes:
      file_id (str): File id to delete
      cascade (bool | Unset): Also delete the file's rows from DuckDB tables and mark the graph stale Default: False.
  """

  file_id: str
  cascade: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    file_id = self.file_id

    cascade = self.cascade

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "file_id": file_id,
      }
    )
    if cascade is not UNSET:
      field_dict["cascade"] = cascade

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    file_id = d.pop("file_id")

    cascade = d.pop("cascade", UNSET)

    delete_file_op = cls(
      file_id=file_id,
      cascade=cascade,
    )

    delete_file_op.additional_properties = d
    return delete_file_op

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
