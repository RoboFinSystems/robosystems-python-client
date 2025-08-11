from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
      query (str): The Cypher query to execute
      parameters (Union['CypherQueryRequestParametersType0', None, Unset]): Optional parameters for the Cypher query
      timeout (Union[None, Unset, int]): Query timeout in seconds (1-300) Default: 60.
  """

  query: str
  parameters: Union["CypherQueryRequestParametersType0", None, Unset] = UNSET
  timeout: Union[None, Unset, int] = 60
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.cypher_query_request_parameters_type_0 import (
      CypherQueryRequestParametersType0,
    )

    query = self.query

    parameters: Union[None, Unset, dict[str, Any]]
    if isinstance(self.parameters, Unset):
      parameters = UNSET
    elif isinstance(self.parameters, CypherQueryRequestParametersType0):
      parameters = self.parameters.to_dict()
    else:
      parameters = self.parameters

    timeout: Union[None, Unset, int]
    if isinstance(self.timeout, Unset):
      timeout = UNSET
    else:
      timeout = self.timeout

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
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
    ) -> Union["CypherQueryRequestParametersType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        parameters_type_0 = CypherQueryRequestParametersType0.from_dict(data)

        return parameters_type_0
      except:  # noqa: E722
        pass
      return cast(Union["CypherQueryRequestParametersType0", None, Unset], data)

    parameters = _parse_parameters(d.pop("parameters", UNSET))

    def _parse_timeout(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    timeout = _parse_timeout(d.pop("timeout", UNSET))

    cypher_query_request = cls(
      query=query,
      parameters=parameters,
      timeout=timeout,
    )

    cypher_query_request.additional_properties = d
    return cypher_query_request

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
