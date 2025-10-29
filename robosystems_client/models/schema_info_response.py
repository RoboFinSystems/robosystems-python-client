from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.schema_info_response_schema import SchemaInfoResponseSchema


T = TypeVar("T", bound="SchemaInfoResponse")


@_attrs_define
class SchemaInfoResponse:
  """Response model for runtime schema introspection.

  This model represents the actual current state of the graph database,
  showing what node labels, relationship types, and properties exist right now.

      Attributes:
          graph_id (str): Graph database identifier
          schema (SchemaInfoResponseSchema): Runtime schema information showing actual database structure
  """

  graph_id: str
  schema: "SchemaInfoResponseSchema"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    schema = self.schema.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "schema": schema,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.schema_info_response_schema import SchemaInfoResponseSchema

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    schema = SchemaInfoResponseSchema.from_dict(d.pop("schema"))

    schema_info_response = cls(
      graph_id=graph_id,
      schema=schema,
    )

    schema_info_response.additional_properties = d
    return schema_info_response

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
