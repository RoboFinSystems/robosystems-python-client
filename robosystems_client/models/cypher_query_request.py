from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.cypher_query_request_parameters_type_0 import (
    CypherQueryRequestParametersType0,
  )


T = TypeVar("T", bound="CypherQueryRequest")


@_attrs_define
class CypherQueryRequest:
  """Request model for Cypher query execution.

  Attributes:
      query (str): The Cypher query to execute. Use parameters ($param_name) for all dynamic values to prevent
          injection attacks.
      parameters (CypherQueryRequestParametersType0 | None | Unset): Query parameters for safe value substitution.
          ALWAYS use parameters instead of string interpolation.
      timeout (int | None | Unset): Query timeout in seconds (1-300) Default: 60.
  """

  query: str
  parameters: CypherQueryRequestParametersType0 | None | Unset = UNSET
  timeout: int | None | Unset = 60

  def to_dict(self) -> dict[str, Any]:
    from ..models.cypher_query_request_parameters_type_0 import (
      CypherQueryRequestParametersType0,
    )

    query = self.query

    parameters: dict[str, Any] | None | Unset
    if isinstance(self.parameters, Unset):
      parameters = UNSET
    elif isinstance(self.parameters, CypherQueryRequestParametersType0):
      parameters = self.parameters.to_dict()
    else:
      parameters = self.parameters

    timeout: int | None | Unset
    if isinstance(self.timeout, Unset):
      timeout = UNSET
    else:
      timeout = self.timeout

    field_dict: dict[str, Any] = {}

    field_dict.update(
      {
        "query": query,
      }
    )
    if parameters is not UNSET:
      field_dict["parameters"] = parameters
    if timeout is not UNSET:
      field_dict["timeout"] = timeout

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.cypher_query_request_parameters_type_0 import (
      CypherQueryRequestParametersType0,
    )

    d = dict(src_dict)
    query = d.pop("query")

    def _parse_parameters(
      data: object,
    ) -> CypherQueryRequestParametersType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        parameters_type_0 = CypherQueryRequestParametersType0.from_dict(data)

        return parameters_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(CypherQueryRequestParametersType0 | None | Unset, data)

    parameters = _parse_parameters(d.pop("parameters", UNSET))

    def _parse_timeout(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    timeout = _parse_timeout(d.pop("timeout", UNSET))

    cypher_query_request = cls(
      query=query,
      parameters=parameters,
      timeout=timeout,
    )

    return cypher_query_request
