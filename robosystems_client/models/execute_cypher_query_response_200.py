from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.execute_cypher_query_response_200_data_item import (
    ExecuteCypherQueryResponse200DataItem,
  )


T = TypeVar("T", bound="ExecuteCypherQueryResponse200")


@_attrs_define
class ExecuteCypherQueryResponse200:
  """
  Attributes:
      success (Union[Unset, bool]):
      data (Union[Unset, list['ExecuteCypherQueryResponse200DataItem']]):
      columns (Union[Unset, list[str]]):
      row_count (Union[Unset, int]):
      execution_time_ms (Union[Unset, float]):
      graph_id (Union[Unset, str]):
      timestamp (Union[Unset, str]):
  """

  success: Union[Unset, bool] = UNSET
  data: Union[Unset, list["ExecuteCypherQueryResponse200DataItem"]] = UNSET
  columns: Union[Unset, list[str]] = UNSET
  row_count: Union[Unset, int] = UNSET
  execution_time_ms: Union[Unset, float] = UNSET
  graph_id: Union[Unset, str] = UNSET
  timestamp: Union[Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    success = self.success

    data: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(self.data, Unset):
      data = []
      for data_item_data in self.data:
        data_item = data_item_data.to_dict()
        data.append(data_item)

    columns: Union[Unset, list[str]] = UNSET
    if not isinstance(self.columns, Unset):
      columns = self.columns

    row_count = self.row_count

    execution_time_ms = self.execution_time_ms

    graph_id = self.graph_id

    timestamp = self.timestamp

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if success is not UNSET:
      field_dict["success"] = success
    if data is not UNSET:
      field_dict["data"] = data
    if columns is not UNSET:
      field_dict["columns"] = columns
    if row_count is not UNSET:
      field_dict["row_count"] = row_count
    if execution_time_ms is not UNSET:
      field_dict["execution_time_ms"] = execution_time_ms
    if graph_id is not UNSET:
      field_dict["graph_id"] = graph_id
    if timestamp is not UNSET:
      field_dict["timestamp"] = timestamp

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.execute_cypher_query_response_200_data_item import (
      ExecuteCypherQueryResponse200DataItem,
    )

    d = dict(src_dict)
    success = d.pop("success", UNSET)

    data = []
    _data = d.pop("data", UNSET)
    for data_item_data in _data or []:
      data_item = ExecuteCypherQueryResponse200DataItem.from_dict(data_item_data)

      data.append(data_item)

    columns = cast(list[str], d.pop("columns", UNSET))

    row_count = d.pop("row_count", UNSET)

    execution_time_ms = d.pop("execution_time_ms", UNSET)

    graph_id = d.pop("graph_id", UNSET)

    timestamp = d.pop("timestamp", UNSET)

    execute_cypher_query_response_200 = cls(
      success=success,
      data=data,
      columns=columns,
      row_count=row_count,
      execution_time_ms=execution_time_ms,
      graph_id=graph_id,
      timestamp=timestamp,
    )

    execute_cypher_query_response_200.additional_properties = d
    return execute_cypher_query_response_200

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
