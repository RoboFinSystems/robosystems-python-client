from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteSubgraphRequest")


@_attrs_define
class DeleteSubgraphRequest:
  """Request model for deleting a subgraph.

  Attributes:
      force (Union[Unset, bool]): Force deletion even if subgraph contains data Default: False.
      backup_first (Union[Unset, bool]): Create a backup before deletion Default: True.
      backup_location (Union[None, Unset, str]): S3 location for backup (uses default if not specified)
  """

  force: Union[Unset, bool] = False
  backup_first: Union[Unset, bool] = True
  backup_location: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    force = self.force

    backup_first = self.backup_first

    backup_location: Union[None, Unset, str]
    if isinstance(self.backup_location, Unset):
      backup_location = UNSET
    else:
      backup_location = self.backup_location

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if force is not UNSET:
      field_dict["force"] = force
    if backup_first is not UNSET:
      field_dict["backup_first"] = backup_first
    if backup_location is not UNSET:
      field_dict["backup_location"] = backup_location

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    force = d.pop("force", UNSET)

    backup_first = d.pop("backup_first", UNSET)

    def _parse_backup_location(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    backup_location = _parse_backup_location(d.pop("backup_location", UNSET))

    delete_subgraph_request = cls(
      force=force,
      backup_first=backup_first,
      backup_location=backup_location,
    )

    delete_subgraph_request.additional_properties = d
    return delete_subgraph_request

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
