from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.schema_export_response_data_stats_type_0 import (
    SchemaExportResponseDataStatsType0,
  )
  from ..models.schema_export_response_schema_definition_type_0 import (
    SchemaExportResponseSchemaDefinitionType0,
  )


T = TypeVar("T", bound="SchemaExportResponse")


@_attrs_define
class SchemaExportResponse:
  """Response model for schema export.

  Attributes:
      graph_id (str): Graph ID
      schema_definition (Union['SchemaExportResponseSchemaDefinitionType0', str]): Exported schema definition (format
          depends on 'format' parameter)
      format_ (str): Export format used
      exported_at (str): Export timestamp
      data_stats (Union['SchemaExportResponseDataStatsType0', None, Unset]): Data statistics if requested (only when
          include_data_stats=true)
  """

  graph_id: str
  schema_definition: Union["SchemaExportResponseSchemaDefinitionType0", str]
  format_: str
  exported_at: str
  data_stats: Union["SchemaExportResponseDataStatsType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.schema_export_response_data_stats_type_0 import (
      SchemaExportResponseDataStatsType0,
    )
    from ..models.schema_export_response_schema_definition_type_0 import (
      SchemaExportResponseSchemaDefinitionType0,
    )

    graph_id = self.graph_id

    schema_definition: Union[dict[str, Any], str]
    if isinstance(self.schema_definition, SchemaExportResponseSchemaDefinitionType0):
      schema_definition = self.schema_definition.to_dict()
    else:
      schema_definition = self.schema_definition

    format_ = self.format_

    exported_at = self.exported_at

    data_stats: Union[None, Unset, dict[str, Any]]
    if isinstance(self.data_stats, Unset):
      data_stats = UNSET
    elif isinstance(self.data_stats, SchemaExportResponseDataStatsType0):
      data_stats = self.data_stats.to_dict()
    else:
      data_stats = self.data_stats

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "schema_definition": schema_definition,
        "format": format_,
        "exported_at": exported_at,
      }
    )
    if data_stats is not UNSET:
      field_dict["data_stats"] = data_stats

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.schema_export_response_data_stats_type_0 import (
      SchemaExportResponseDataStatsType0,
    )
    from ..models.schema_export_response_schema_definition_type_0 import (
      SchemaExportResponseSchemaDefinitionType0,
    )

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    def _parse_schema_definition(
      data: object,
    ) -> Union["SchemaExportResponseSchemaDefinitionType0", str]:
      try:
        if not isinstance(data, dict):
          raise TypeError()
        schema_definition_type_0 = SchemaExportResponseSchemaDefinitionType0.from_dict(
          data
        )

        return schema_definition_type_0
      except:  # noqa: E722
        pass
      return cast(Union["SchemaExportResponseSchemaDefinitionType0", str], data)

    schema_definition = _parse_schema_definition(d.pop("schema_definition"))

    format_ = d.pop("format")

    exported_at = d.pop("exported_at")

    def _parse_data_stats(
      data: object,
    ) -> Union["SchemaExportResponseDataStatsType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        data_stats_type_0 = SchemaExportResponseDataStatsType0.from_dict(data)

        return data_stats_type_0
      except:  # noqa: E722
        pass
      return cast(Union["SchemaExportResponseDataStatsType0", None, Unset], data)

    data_stats = _parse_data_stats(d.pop("data_stats", UNSET))

    schema_export_response = cls(
      graph_id=graph_id,
      schema_definition=schema_definition,
      format_=format_,
      exported_at=exported_at,
      data_stats=data_stats,
    )

    schema_export_response.additional_properties = d
    return schema_export_response

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
