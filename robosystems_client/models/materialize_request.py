from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

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
  """

  force: bool | Unset = False
  rebuild: bool | Unset = False
  ignore_errors: bool | Unset = True

  def to_dict(self) -> dict[str, Any]:
    force = self.force

    rebuild = self.rebuild

    ignore_errors = self.ignore_errors

    field_dict: dict[str, Any] = {}

    field_dict.update({})
    if force is not UNSET:
      field_dict["force"] = force
    if rebuild is not UNSET:
      field_dict["rebuild"] = rebuild
    if ignore_errors is not UNSET:
      field_dict["ignore_errors"] = ignore_errors

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    force = d.pop("force", UNSET)

    rebuild = d.pop("rebuild", UNSET)

    ignore_errors = d.pop("ignore_errors", UNSET)

    materialize_request = cls(
      force=force,
      rebuild=rebuild,
      ignore_errors=ignore_errors,
    )

    return materialize_request
