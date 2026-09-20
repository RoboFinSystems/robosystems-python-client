from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.handle_http_post_extensions_graph_id_graphql_post_body_variables import (
    HandleHttpPostExtensionsGraphIdGraphqlPostBodyVariables,
  )


T = TypeVar("T", bound="HandleHttpPostExtensionsGraphIdGraphqlPostBody")


@_attrs_define
class HandleHttpPostExtensionsGraphIdGraphqlPostBody:
  """
  Attributes:
      query (str): The GraphQL document to execute.
      variables (HandleHttpPostExtensionsGraphIdGraphqlPostBodyVariables | Unset): Values for the document's
          variables.
      operation_name (str | Unset): Which operation to run, when the document declares more than one.
  """

  query: str
  variables: HandleHttpPostExtensionsGraphIdGraphqlPostBodyVariables | Unset = UNSET
  operation_name: str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    query = self.query

    variables: dict[str, Any] | Unset = UNSET
    if not isinstance(self.variables, Unset):
      variables = self.variables.to_dict()

    operation_name = self.operation_name

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "query": query,
      }
    )
    if variables is not UNSET:
      field_dict["variables"] = variables
    if operation_name is not UNSET:
      field_dict["operationName"] = operation_name

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.handle_http_post_extensions_graph_id_graphql_post_body_variables import (
      HandleHttpPostExtensionsGraphIdGraphqlPostBodyVariables,
    )

    d = dict(src_dict)
    query = d.pop("query")

    _variables = d.pop("variables", UNSET)
    variables: HandleHttpPostExtensionsGraphIdGraphqlPostBodyVariables | Unset
    if isinstance(_variables, Unset):
      variables = UNSET
    else:
      variables = HandleHttpPostExtensionsGraphIdGraphqlPostBodyVariables.from_dict(
        _variables
      )

    operation_name = d.pop("operationName", UNSET)

    handle_http_post_extensions_graph_id_graphql_post_body = cls(
      query=query,
      variables=variables,
      operation_name=operation_name,
    )

    handle_http_post_extensions_graph_id_graphql_post_body.additional_properties = d
    return handle_http_post_extensions_graph_id_graphql_post_body

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
