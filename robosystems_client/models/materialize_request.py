from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaterializeRequest")


@_attrs_define
class MaterializeRequest:
  """
  Attributes:
      force (bool | Unset): Force materialization even if graph is not stale Default: False.
      rebuild (bool | Unset): Delete and recreate graph database before materialization Default: False.
      ignore_errors (bool | Unset): Continue ingestion on row errors Default: True.
      dry_run (bool | Unset): Validate limits without executing materialization. Returns usage, limits, and warnings.
          Default: False.
      source (None | str | Unset): Data source for materialization. Auto-detected from graph type if not specified.
          'staged' materializes from uploaded files (generic graphs). 'extensions' materializes from the extensions OLTP
          database (entity graphs).
      materialize_embeddings (bool | Unset): Include embedding columns in materialization and build HNSW vector
          indexes in the graph database. When false (default), embedding columns are NULLed out to save space. Set to true
          for graphs that need vector search. Default: False.
  """

  force: bool | Unset = False
  rebuild: bool | Unset = False
  ignore_errors: bool | Unset = True
  dry_run: bool | Unset = False
  source: None | str | Unset = UNSET
  materialize_embeddings: bool | Unset = False

  def to_dict(self) -> dict[str, Any]:
    force = self.force

    rebuild = self.rebuild

    ignore_errors = self.ignore_errors

    dry_run = self.dry_run

    source: None | str | Unset
    if isinstance(self.source, Unset):
      source = UNSET
    else:
      source = self.source

    materialize_embeddings = self.materialize_embeddings

    field_dict: dict[str, Any] = {}

    field_dict.update({})
    if force is not UNSET:
      field_dict["force"] = force
    if rebuild is not UNSET:
      field_dict["rebuild"] = rebuild
    if ignore_errors is not UNSET:
      field_dict["ignore_errors"] = ignore_errors
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

    ignore_errors = d.pop("ignore_errors", UNSET)

    dry_run = d.pop("dry_run", UNSET)

    def _parse_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source = _parse_source(d.pop("source", UNSET))

    materialize_embeddings = d.pop("materialize_embeddings", UNSET)

    materialize_request = cls(
      force=force,
      rebuild=rebuild,
      ignore_errors=ignore_errors,
      dry_run=dry_run,
      source=source,
      materialize_embeddings=materialize_embeddings,
    )

    return materialize_request
