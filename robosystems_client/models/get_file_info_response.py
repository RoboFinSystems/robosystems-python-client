from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.enhanced_file_status_layers import EnhancedFileStatusLayers


T = TypeVar("T", bound="GetFileInfoResponse")


@_attrs_define
class GetFileInfoResponse:
  """
  Attributes:
      file_id (str): Unique file identifier
      graph_id (str): Graph database identifier
      table_id (str): Table identifier
      file_name (str): Original file name
      file_format (str): File format (parquet, csv, etc.)
      size_bytes (int): File size in bytes
      upload_status (str): Current upload status
      upload_method (str): Upload method used
      s3_key (str): S3 object key
      table_name (None | str | Unset): Table name
      row_count (int | None | Unset): Estimated row count
      created_at (None | str | Unset): File creation timestamp
      uploaded_at (None | str | Unset): File upload completion timestamp
      layers (EnhancedFileStatusLayers | None | Unset): Multi-layer pipeline status (S3 → DuckDB → Graph). Shows
          status, timestamps, and row counts for each layer independently.
  """

  file_id: str
  graph_id: str
  table_id: str
  file_name: str
  file_format: str
  size_bytes: int
  upload_status: str
  upload_method: str
  s3_key: str
  table_name: None | str | Unset = UNSET
  row_count: int | None | Unset = UNSET
  created_at: None | str | Unset = UNSET
  uploaded_at: None | str | Unset = UNSET
  layers: EnhancedFileStatusLayers | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.enhanced_file_status_layers import EnhancedFileStatusLayers

    file_id = self.file_id

    graph_id = self.graph_id

    table_id = self.table_id

    file_name = self.file_name

    file_format = self.file_format

    size_bytes = self.size_bytes

    upload_status = self.upload_status

    upload_method = self.upload_method

    s3_key = self.s3_key

    table_name: None | str | Unset
    if isinstance(self.table_name, Unset):
      table_name = UNSET
    else:
      table_name = self.table_name

    row_count: int | None | Unset
    if isinstance(self.row_count, Unset):
      row_count = UNSET
    else:
      row_count = self.row_count

    created_at: None | str | Unset
    if isinstance(self.created_at, Unset):
      created_at = UNSET
    else:
      created_at = self.created_at

    uploaded_at: None | str | Unset
    if isinstance(self.uploaded_at, Unset):
      uploaded_at = UNSET
    else:
      uploaded_at = self.uploaded_at

    layers: dict[str, Any] | None | Unset
    if isinstance(self.layers, Unset):
      layers = UNSET
    elif isinstance(self.layers, EnhancedFileStatusLayers):
      layers = self.layers.to_dict()
    else:
      layers = self.layers

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "file_id": file_id,
        "graph_id": graph_id,
        "table_id": table_id,
        "file_name": file_name,
        "file_format": file_format,
        "size_bytes": size_bytes,
        "upload_status": upload_status,
        "upload_method": upload_method,
        "s3_key": s3_key,
      }
    )
    if table_name is not UNSET:
      field_dict["table_name"] = table_name
    if row_count is not UNSET:
      field_dict["row_count"] = row_count
    if created_at is not UNSET:
      field_dict["created_at"] = created_at
    if uploaded_at is not UNSET:
      field_dict["uploaded_at"] = uploaded_at
    if layers is not UNSET:
      field_dict["layers"] = layers

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.enhanced_file_status_layers import EnhancedFileStatusLayers

    d = dict(src_dict)
    file_id = d.pop("file_id")

    graph_id = d.pop("graph_id")

    table_id = d.pop("table_id")

    file_name = d.pop("file_name")

    file_format = d.pop("file_format")

    size_bytes = d.pop("size_bytes")

    upload_status = d.pop("upload_status")

    upload_method = d.pop("upload_method")

    s3_key = d.pop("s3_key")

    def _parse_table_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    table_name = _parse_table_name(d.pop("table_name", UNSET))

    def _parse_row_count(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    row_count = _parse_row_count(d.pop("row_count", UNSET))

    def _parse_created_at(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    created_at = _parse_created_at(d.pop("created_at", UNSET))

    def _parse_uploaded_at(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    uploaded_at = _parse_uploaded_at(d.pop("uploaded_at", UNSET))

    def _parse_layers(data: object) -> EnhancedFileStatusLayers | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        layers_type_0 = EnhancedFileStatusLayers.from_dict(data)

        return layers_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(EnhancedFileStatusLayers | None | Unset, data)

    layers = _parse_layers(d.pop("layers", UNSET))

    get_file_info_response = cls(
      file_id=file_id,
      graph_id=graph_id,
      table_id=table_id,
      file_name=file_name,
      file_format=file_format,
      size_bytes=size_bytes,
      upload_status=upload_status,
      upload_method=upload_method,
      s3_key=s3_key,
      table_name=table_name,
      row_count=row_count,
      created_at=created_at,
      uploaded_at=uploaded_at,
      layers=layers,
    )

    get_file_info_response.additional_properties = d
    return get_file_info_response

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
