import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteSubgraphResponse")


@_attrs_define
class DeleteSubgraphResponse:
  """Response model for subgraph deletion.

  Attributes:
      graph_id (str): Deleted subgraph identifier
      status (str): Deletion status
      deleted_at (datetime.datetime): When deletion occurred
      backup_location (Union[None, Unset, str]): Location of backup if created
      message (Union[None, Unset, str]): Additional information about the deletion
  """

  graph_id: str
  status: str
  deleted_at: datetime.datetime
  backup_location: Union[None, Unset, str] = UNSET
  message: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    status = self.status

    deleted_at = self.deleted_at.isoformat()

    backup_location: Union[None, Unset, str]
    if isinstance(self.backup_location, Unset):
      backup_location = UNSET
    else:
      backup_location = self.backup_location

    message: Union[None, Unset, str]
    if isinstance(self.message, Unset):
      message = UNSET
    else:
      message = self.message

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "status": status,
        "deleted_at": deleted_at,
      }
    )
    if backup_location is not UNSET:
      field_dict["backup_location"] = backup_location
    if message is not UNSET:
      field_dict["message"] = message

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    status = d.pop("status")

    deleted_at = isoparse(d.pop("deleted_at"))

    def _parse_backup_location(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    backup_location = _parse_backup_location(d.pop("backup_location", UNSET))

    def _parse_message(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    message = _parse_message(d.pop("message", UNSET))

    delete_subgraph_response = cls(
      graph_id=graph_id,
      status=status,
      deleted_at=deleted_at,
      backup_location=backup_location,
      message=message,
    )

    delete_subgraph_response.additional_properties = d
    return delete_subgraph_response

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
