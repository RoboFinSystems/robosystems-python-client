from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseInfoResponse")


@_attrs_define
class DatabaseInfoResponse:
  """Response model for database information and statistics.

  Attributes:
      graph_id (str): Graph database identifier
      database_name (str): Database name
      database_size_bytes (int): Database size in bytes
      database_size_mb (float): Database size in MB
      node_count (int): Total number of nodes
      relationship_count (int): Total number of relationships
      node_labels (list[str]): List of node labels
      relationship_types (list[str]): List of relationship types
      created_at (str): Database creation timestamp
      last_modified (str): Last modification timestamp
      read_only (bool): Whether database is read-only
      backup_count (int): Number of available backups
      schema_version (Union[None, Unset, str]): Schema version
      last_backup_date (Union[None, Unset, str]): Date of last backup
  """

  graph_id: str
  database_name: str
  database_size_bytes: int
  database_size_mb: float
  node_count: int
  relationship_count: int
  node_labels: list[str]
  relationship_types: list[str]
  created_at: str
  last_modified: str
  read_only: bool
  backup_count: int
  schema_version: Union[None, Unset, str] = UNSET
  last_backup_date: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    database_name = self.database_name

    database_size_bytes = self.database_size_bytes

    database_size_mb = self.database_size_mb

    node_count = self.node_count

    relationship_count = self.relationship_count

    node_labels = self.node_labels

    relationship_types = self.relationship_types

    created_at = self.created_at

    last_modified = self.last_modified

    read_only = self.read_only

    backup_count = self.backup_count

    schema_version: Union[None, Unset, str]
    if isinstance(self.schema_version, Unset):
      schema_version = UNSET
    else:
      schema_version = self.schema_version

    last_backup_date: Union[None, Unset, str]
    if isinstance(self.last_backup_date, Unset):
      last_backup_date = UNSET
    else:
      last_backup_date = self.last_backup_date

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "database_name": database_name,
        "database_size_bytes": database_size_bytes,
        "database_size_mb": database_size_mb,
        "node_count": node_count,
        "relationship_count": relationship_count,
        "node_labels": node_labels,
        "relationship_types": relationship_types,
        "created_at": created_at,
        "last_modified": last_modified,
        "read_only": read_only,
        "backup_count": backup_count,
      }
    )
    if schema_version is not UNSET:
      field_dict["schema_version"] = schema_version
    if last_backup_date is not UNSET:
      field_dict["last_backup_date"] = last_backup_date

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    database_name = d.pop("database_name")

    database_size_bytes = d.pop("database_size_bytes")

    database_size_mb = d.pop("database_size_mb")

    node_count = d.pop("node_count")

    relationship_count = d.pop("relationship_count")

    node_labels = cast(list[str], d.pop("node_labels"))

    relationship_types = cast(list[str], d.pop("relationship_types"))

    created_at = d.pop("created_at")

    last_modified = d.pop("last_modified")

    read_only = d.pop("read_only")

    backup_count = d.pop("backup_count")

    def _parse_schema_version(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    schema_version = _parse_schema_version(d.pop("schema_version", UNSET))

    def _parse_last_backup_date(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    last_backup_date = _parse_last_backup_date(d.pop("last_backup_date", UNSET))

    database_info_response = cls(
      graph_id=graph_id,
      database_name=database_name,
      database_size_bytes=database_size_bytes,
      database_size_mb=database_size_mb,
      node_count=node_count,
      relationship_count=relationship_count,
      node_labels=node_labels,
      relationship_types=relationship_types,
      created_at=created_at,
      last_modified=last_modified,
      read_only=read_only,
      backup_count=backup_count,
      schema_version=schema_version,
      last_backup_date=last_backup_date,
    )

    database_info_response.additional_properties = d
    return database_info_response

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
