from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkIngestRequest")


@_attrs_define
class BulkIngestRequest:
  """
  Attributes:
      ignore_errors (Union[Unset, bool]): Continue ingestion on row errors Default: True.
      rebuild (Union[Unset, bool]): Rebuild graph database from scratch before ingestion. Safe operation - staged data
          is the source of truth, graph can always be regenerated. Default: False.
  """

  ignore_errors: Union[Unset, bool] = True
  rebuild: Union[Unset, bool] = False

  def to_dict(self) -> dict[str, Any]:
    ignore_errors = self.ignore_errors

    rebuild = self.rebuild

    field_dict: dict[str, Any] = {}

    field_dict.update({})
    if ignore_errors is not UNSET:
      field_dict["ignore_errors"] = ignore_errors
    if rebuild is not UNSET:
      field_dict["rebuild"] = rebuild

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    ignore_errors = d.pop("ignore_errors", UNSET)

    rebuild = d.pop("rebuild", UNSET)

    bulk_ingest_request = cls(
      ignore_errors=ignore_errors,
      rebuild=rebuild,
    )

    return bulk_ingest_request
