from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.table_info import TableInfo


T = TypeVar("T", bound="TableListResponse")


@_attrs_define
class TableListResponse:
  """
  Attributes:
      tables (list['TableInfo']): List of tables
      total_count (int): Total number of tables
  """

  tables: list["TableInfo"]
  total_count: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    tables = []
    for tables_item_data in self.tables:
      tables_item = tables_item_data.to_dict()
      tables.append(tables_item)

    total_count = self.total_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "tables": tables,
        "total_count": total_count,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.table_info import TableInfo

    d = dict(src_dict)
    tables = []
    _tables = d.pop("tables")
    for tables_item_data in _tables:
      tables_item = TableInfo.from_dict(tables_item_data)

      tables.append(tables_item)

    total_count = d.pop("total_count")

    table_list_response = cls(
      tables=tables,
      total_count=total_count,
    )

    table_list_response.additional_properties = d
    return table_list_response

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
