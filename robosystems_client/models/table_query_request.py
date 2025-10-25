from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TableQueryRequest")


@_attrs_define
class TableQueryRequest:
  """
  Attributes:
      sql (str): SQL query to execute on staging tables
  """

  sql: str

  def to_dict(self) -> dict[str, Any]:
    sql = self.sql

    field_dict: dict[str, Any] = {}

    field_dict.update(
      {
        "sql": sql,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    sql = d.pop("sql")

    table_query_request = cls(
      sql=sql,
    )

    return table_query_request
