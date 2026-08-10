from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.sql_statement_request_parameters_type_1 import (
    SqlStatementRequestParametersType1,
  )


T = TypeVar("T", bound="SqlStatementRequest")


@_attrs_define
class SqlStatementRequest:
  """
  Attributes:
      sql (str): SQL query over the graph's columnar tables (DuckDB) — a relational lens on the same graph-centric
          data, often ahead of the materialized graph. Use ? placeholders or $param_name for dynamic values to prevent SQL
          injection.
      parameters (list[Any] | None | SqlStatementRequestParametersType1 | Unset): Query parameters for safe value
          substitution. ALWAYS use parameters instead of string concatenation. Pass a list for positional placeholders
          (`?` or `$1`) and an object for named ones (`$param_name`) — the two forms cannot be mixed in one statement.
  """

  sql: str
  parameters: list[Any] | None | SqlStatementRequestParametersType1 | Unset = UNSET

  def to_dict(self) -> dict[str, Any]:
    from ..models.sql_statement_request_parameters_type_1 import (
      SqlStatementRequestParametersType1,
    )

    sql = self.sql

    parameters: dict[str, Any] | list[Any] | None | Unset
    if isinstance(self.parameters, Unset):
      parameters = UNSET
    elif isinstance(self.parameters, list):
      parameters = self.parameters

    elif isinstance(self.parameters, SqlStatementRequestParametersType1):
      parameters = self.parameters.to_dict()
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
    from ..models.sql_statement_request_parameters_type_1 import (
      SqlStatementRequestParametersType1,
    )

    d = dict(src_dict)
    sql = d.pop("sql")

    def _parse_parameters(
      data: object,
    ) -> list[Any] | None | SqlStatementRequestParametersType1 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        parameters_type_0 = cast(list[Any], data)

        return parameters_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      try:
        if not isinstance(data, dict):
          raise TypeError()
        parameters_type_1 = SqlStatementRequestParametersType1.from_dict(data)

        return parameters_type_1
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[Any] | None | SqlStatementRequestParametersType1 | Unset, data)

    parameters = _parse_parameters(d.pop("parameters", UNSET))

    sql_statement_request = cls(
      sql=sql,
      parameters=parameters,
    )

    return sql_statement_request
