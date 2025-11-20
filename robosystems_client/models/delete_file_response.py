from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteFileResponse")


@_attrs_define
class DeleteFileResponse:
  """
  Attributes:
      status (str): Deletion status
      file_id (str): Deleted file ID
      file_name (str): Deleted file name
      message (str): Operation message
      cascade_deleted (bool | Unset): Whether cascade deletion was performed Default: False.
      tables_affected (list[str] | None | Unset): Tables from which file data was deleted (if cascade=true)
      graph_marked_stale (bool | Unset): Whether graph was marked as stale Default: False.
  """

  status: str
  file_id: str
  file_name: str
  message: str
  cascade_deleted: bool | Unset = False
  tables_affected: list[str] | None | Unset = UNSET
  graph_marked_stale: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    status = self.status

    file_id = self.file_id

    file_name = self.file_name

    message = self.message

    cascade_deleted = self.cascade_deleted

    tables_affected: list[str] | None | Unset
    if isinstance(self.tables_affected, Unset):
      tables_affected = UNSET
    elif isinstance(self.tables_affected, list):
      tables_affected = self.tables_affected

    else:
      tables_affected = self.tables_affected

    graph_marked_stale = self.graph_marked_stale

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "status": status,
        "file_id": file_id,
        "file_name": file_name,
        "message": message,
      }
    )
    if cascade_deleted is not UNSET:
      field_dict["cascade_deleted"] = cascade_deleted
    if tables_affected is not UNSET:
      field_dict["tables_affected"] = tables_affected
    if graph_marked_stale is not UNSET:
      field_dict["graph_marked_stale"] = graph_marked_stale

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    status = d.pop("status")

    file_id = d.pop("file_id")

    file_name = d.pop("file_name")

    message = d.pop("message")

    cascade_deleted = d.pop("cascade_deleted", UNSET)

    def _parse_tables_affected(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        tables_affected_type_0 = cast(list[str], data)

        return tables_affected_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    tables_affected = _parse_tables_affected(d.pop("tables_affected", UNSET))

    graph_marked_stale = d.pop("graph_marked_stale", UNSET)

    delete_file_response = cls(
      status=status,
      file_id=file_id,
      file_name=file_name,
      message=message,
      cascade_deleted=cascade_deleted,
      tables_affected=tables_affected,
      graph_marked_stale=graph_marked_stale,
    )

    delete_file_response.additional_properties = d
    return delete_file_response

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
