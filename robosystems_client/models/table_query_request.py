from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TableQueryRequest")


@_attrs_define
class TableQueryRequest:
  """
  Attributes:
      sql (str): SQL query to execute on staging tables. Use ? placeholders or $param_name for dynamic values to
          prevent SQL injection.
      parameters (Union[None, Unset, list[Any]]): Query parameters for safe value substitution. ALWAYS use parameters
          instead of string concatenation.
  """

  sql: str
  parameters: Union[None, Unset, list[Any]] = UNSET

  def to_dict(self) -> dict[str, Any]:
    sql = self.sql

    parameters: Union[None, Unset, list[Any]]
    if isinstance(self.parameters, Unset):
      parameters = UNSET
    elif isinstance(self.parameters, list):
      parameters = self.parameters

    else:
      parameters = self.parameters

    field_dict: dict[str, Any] = {}

    field_dict.update(
      {
        "sql": sql,
      }
    )
    if parameters is not UNSET:
      field_dict["parameters"] = parameters

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    sql = d.pop("sql")

    def _parse_parameters(data: object) -> Union[None, Unset, list[Any]]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        parameters_type_0 = cast(list[Any], data)

        return parameters_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, list[Any]], data)

    parameters = _parse_parameters(d.pop("parameters", UNSET))

    table_query_request = cls(
      sql=sql,
      parameters=parameters,
    )

    return table_query_request
