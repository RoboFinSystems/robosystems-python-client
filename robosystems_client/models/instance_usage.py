from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.database_storage_entry import DatabaseStorageEntry
  from ..models.storage_item import StorageItem


T = TypeVar("T", bound="InstanceUsage")


@_attrs_define
class InstanceUsage:
  """Aggregate storage usage across the dedicated instance.

  Covers the parent graph, all subgraphs, DuckDB staging, and
  future LanceDB vector indexes.

      Attributes:
          limit_gb (float): Soft storage limit for this tier in GB
          status (str): Instance status: 'healthy' (<80%), 'approaching' (80-100%), 'over_limit' (>100%)
          node_count (int | None | Unset): Current node count (informational, no limit enforced)
          total_storage_gb (float | None | Unset): Total storage used across all databases in GB
          usage_percentage (float | None | Unset): Storage usage as percentage of limit (e.g. 105.2). Derived from the
              enforced figure — durable bytes only, excluding `transient` build artifacts — so it can read lower than
              total_storage_gb/limit_gb while a blue-green rebuild is in flight.
          databases (list[DatabaseStorageEntry] | Unset): Per-database storage breakdown
          items (list[StorageItem] | Unset): Itemized storage by type — graph, memory, subgraph, vectors, staging,
              transient, orphan. Sums to total_storage_gb. Only `subgraph` items correspond to live subgraphs, so this is the
              type to sum when reconciling against the subgraph list.
  """

  limit_gb: float
  status: str
  node_count: int | None | Unset = UNSET
  total_storage_gb: float | None | Unset = UNSET
  usage_percentage: float | None | Unset = UNSET
  databases: list[DatabaseStorageEntry] | Unset = UNSET
  items: list[StorageItem] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    limit_gb = self.limit_gb

    status = self.status

    node_count: int | None | Unset
    if isinstance(self.node_count, Unset):
      node_count = UNSET
    else:
      node_count = self.node_count

    total_storage_gb: float | None | Unset
    if isinstance(self.total_storage_gb, Unset):
      total_storage_gb = UNSET
    else:
      total_storage_gb = self.total_storage_gb

    usage_percentage: float | None | Unset
    if isinstance(self.usage_percentage, Unset):
      usage_percentage = UNSET
    else:
      usage_percentage = self.usage_percentage

    databases: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.databases, Unset):
      databases = []
      for databases_item_data in self.databases:
        databases_item = databases_item_data.to_dict()
        databases.append(databases_item)

    items: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.items, Unset):
      items = []
      for items_item_data in self.items:
        items_item = items_item_data.to_dict()
        items.append(items_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "limit_gb": limit_gb,
        "status": status,
      }
    )
    if node_count is not UNSET:
      field_dict["node_count"] = node_count
    if total_storage_gb is not UNSET:
      field_dict["total_storage_gb"] = total_storage_gb
    if usage_percentage is not UNSET:
      field_dict["usage_percentage"] = usage_percentage
    if databases is not UNSET:
      field_dict["databases"] = databases
    if items is not UNSET:
      field_dict["items"] = items

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.database_storage_entry import DatabaseStorageEntry
    from ..models.storage_item import StorageItem

    d = dict(src_dict)
    limit_gb = d.pop("limit_gb")

    status = d.pop("status")

    def _parse_node_count(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    node_count = _parse_node_count(d.pop("node_count", UNSET))

    def _parse_total_storage_gb(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    total_storage_gb = _parse_total_storage_gb(d.pop("total_storage_gb", UNSET))

    def _parse_usage_percentage(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    usage_percentage = _parse_usage_percentage(d.pop("usage_percentage", UNSET))

    _databases = d.pop("databases", UNSET)
    databases: list[DatabaseStorageEntry] | Unset = UNSET
    if _databases is not UNSET:
      databases = []
      for databases_item_data in _databases:
        databases_item = DatabaseStorageEntry.from_dict(databases_item_data)

        databases.append(databases_item)

    _items = d.pop("items", UNSET)
    items: list[StorageItem] | Unset = UNSET
    if _items is not UNSET:
      items = []
      for items_item_data in _items:
        items_item = StorageItem.from_dict(items_item_data)

        items.append(items_item)

    instance_usage = cls(
      limit_gb=limit_gb,
      status=status,
      node_count=node_count,
      total_storage_gb=total_storage_gb,
      usage_percentage=usage_percentage,
      databases=databases,
      items=items,
    )

    instance_usage.additional_properties = d
    return instance_usage

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
