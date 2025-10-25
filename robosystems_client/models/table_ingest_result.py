from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TableIngestResult")


@_attrs_define
class TableIngestResult:
  """
  Attributes:
      table_name (str): Table name
      status (str): Ingestion status (success/failed/skipped)
      rows_ingested (Union[Unset, int]): Number of rows ingested Default: 0.
      execution_time_ms (Union[Unset, float]): Ingestion time in milliseconds Default: 0.0.
      error (Union[None, Unset, str]): Error message if failed
  """

  table_name: str
  status: str
  rows_ingested: Union[Unset, int] = 0
  execution_time_ms: Union[Unset, float] = 0.0
  error: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    table_name = self.table_name

    status = self.status

    rows_ingested = self.rows_ingested

    execution_time_ms = self.execution_time_ms

    error: Union[None, Unset, str]
    if isinstance(self.error, Unset):
      error = UNSET
    else:
      error = self.error

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "table_name": table_name,
        "status": status,
      }
    )
    if rows_ingested is not UNSET:
      field_dict["rows_ingested"] = rows_ingested
    if execution_time_ms is not UNSET:
      field_dict["execution_time_ms"] = execution_time_ms
    if error is not UNSET:
      field_dict["error"] = error

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    table_name = d.pop("table_name")

    status = d.pop("status")

    rows_ingested = d.pop("rows_ingested", UNSET)

    execution_time_ms = d.pop("execution_time_ms", UNSET)

    def _parse_error(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    error = _parse_error(d.pop("error", UNSET))

    table_ingest_result = cls(
      table_name=table_name,
      status=status,
      rows_ingested=rows_ingested,
      execution_time_ms=execution_time_ms,
      error=error,
    )

    table_ingest_result.additional_properties = d
    return table_ingest_result

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
