from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileStatusUpdate")


@_attrs_define
class FileStatusUpdate:
  """
  Attributes:
      status (str): File status: 'uploaded' (ready for ingest), 'disabled' (exclude from ingest), 'archived' (soft
          deleted)
      ingest_to_graph (bool | Unset): Auto-ingest to graph after DuckDB staging. Default=false (batch mode). Set to
          true for real-time incremental updates. Default: False.
  """

  status: str
  ingest_to_graph: bool | Unset = False

  def to_dict(self) -> dict[str, Any]:
    status = self.status

    ingest_to_graph = self.ingest_to_graph

    field_dict: dict[str, Any] = {}

    field_dict.update(
      {
        "status": status,
      }
    )
    if ingest_to_graph is not UNSET:
      field_dict["ingest_to_graph"] = ingest_to_graph

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    status = d.pop("status")

    ingest_to_graph = d.pop("ingest_to_graph", UNSET)

    file_status_update = cls(
      status=status,
      ingest_to_graph=ingest_to_graph,
    )

    return file_status_update
