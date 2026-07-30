from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaterializeOp")


@_attrs_define
class MaterializeOp:
  """Body for the materialize operation.

  Attributes:
      force (bool | Unset): Force materialization even if already up to date Default: False.
      rebuild (bool | Unset): Rebuild the graph from scratch, dropping existing data. Required (staged source) when
          materializing new uploads into a graph that already contains materialized data — staging replays all uploaded
          files, so a non-rebuild pass would re-copy ingested rows (409). Default: False.
      dry_run (bool | Unset): Validate tables without writing to the graph Default: False.
      source (None | str | Unset): Materialization source: 'extensions' for OLTP, omit for DuckDB staging tables
      materialize_embeddings (bool | Unset): Generate vector embeddings during materialization Default: False.
  """

  force: bool | Unset = False
  rebuild: bool | Unset = False
  dry_run: bool | Unset = False
  source: None | str | Unset = UNSET
  materialize_embeddings: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    force = self.force

    rebuild = self.rebuild

    dry_run = self.dry_run

    source: None | str | Unset
    if isinstance(self.source, Unset):
      source = UNSET
    else:
      source = self.source

    materialize_embeddings = self.materialize_embeddings

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if force is not UNSET:
      field_dict["force"] = force
    if rebuild is not UNSET:
      field_dict["rebuild"] = rebuild
    if dry_run is not UNSET:
      field_dict["dry_run"] = dry_run
    if source is not UNSET:
      field_dict["source"] = source
    if materialize_embeddings is not UNSET:
      field_dict["materialize_embeddings"] = materialize_embeddings

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    force = d.pop("force", UNSET)

    rebuild = d.pop("rebuild", UNSET)

    dry_run = d.pop("dry_run", UNSET)

    def _parse_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source = _parse_source(d.pop("source", UNSET))

    materialize_embeddings = d.pop("materialize_embeddings", UNSET)

    materialize_op = cls(
      force=force,
      rebuild=rebuild,
      dry_run=dry_run,
      source=source,
      materialize_embeddings=materialize_embeddings,
    )

    materialize_op.additional_properties = d
    return materialize_op

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
