from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.file_layer_status import FileLayerStatus


T = TypeVar("T", bound="EnhancedFileStatusLayers")


@_attrs_define
class EnhancedFileStatusLayers:
  """
  Attributes:
      s3 (FileLayerStatus):
      duckdb (FileLayerStatus):
      graph (FileLayerStatus):
  """

  s3: FileLayerStatus
  duckdb: FileLayerStatus
  graph: FileLayerStatus
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    s3 = self.s3.to_dict()

    duckdb = self.duckdb.to_dict()

    graph = self.graph.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "s3": s3,
        "duckdb": duckdb,
        "graph": graph,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.file_layer_status import FileLayerStatus

    d = dict(src_dict)
    s3 = FileLayerStatus.from_dict(d.pop("s3"))

    duckdb = FileLayerStatus.from_dict(d.pop("duckdb"))

    graph = FileLayerStatus.from_dict(d.pop("graph"))

    enhanced_file_status_layers = cls(
      s3=s3,
      duckdb=duckdb,
      graph=graph,
    )

    enhanced_file_status_layers.additional_properties = d
    return enhanced_file_status_layers

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
