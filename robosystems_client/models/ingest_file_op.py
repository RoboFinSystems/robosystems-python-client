from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestFileOp")


@_attrs_define
class IngestFileOp:
  """Body for ingest-file (raw→staging content flow).

  Marks an uploaded file ready and triggers DuckDB staging. Set
  ``ingest_to_graph`` to auto-chain graph materialization after staging.

      Attributes:
          file_id (str): Uploaded file id to ingest
          ingest_to_graph (bool | Unset): Auto-materialize into the graph after DuckDB staging Default: False.
  """

  file_id: str
  ingest_to_graph: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    file_id = self.file_id

    ingest_to_graph = self.ingest_to_graph

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "file_id": file_id,
      }
    )
    if ingest_to_graph is not UNSET:
      field_dict["ingest_to_graph"] = ingest_to_graph

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    file_id = d.pop("file_id")

    ingest_to_graph = d.pop("ingest_to_graph", UNSET)

    ingest_file_op = cls(
      file_id=file_id,
      ingest_to_graph=ingest_to_graph,
    )

    ingest_file_op.additional_properties = d
    return ingest_file_op

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
