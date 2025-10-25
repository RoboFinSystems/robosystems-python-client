from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.table_ingest_result import TableIngestResult


T = TypeVar("T", bound="BulkIngestResponse")


@_attrs_define
class BulkIngestResponse:
  """
  Attributes:
      status (str): Overall ingestion status
      graph_id (str): Graph database identifier
      total_tables (int): Total number of tables processed
      successful_tables (int): Number of successfully ingested tables
      failed_tables (int): Number of failed table ingestions
      skipped_tables (int): Number of skipped tables (no files)
      total_rows_ingested (int): Total rows ingested across all tables
      total_execution_time_ms (float): Total execution time in milliseconds
      results (list['TableIngestResult']): Per-table ingestion results
  """

  status: str
  graph_id: str
  total_tables: int
  successful_tables: int
  failed_tables: int
  skipped_tables: int
  total_rows_ingested: int
  total_execution_time_ms: float
  results: list["TableIngestResult"]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    status = self.status

    graph_id = self.graph_id

    total_tables = self.total_tables

    successful_tables = self.successful_tables

    failed_tables = self.failed_tables

    skipped_tables = self.skipped_tables

    total_rows_ingested = self.total_rows_ingested

    total_execution_time_ms = self.total_execution_time_ms

    results = []
    for results_item_data in self.results:
      results_item = results_item_data.to_dict()
      results.append(results_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "status": status,
        "graph_id": graph_id,
        "total_tables": total_tables,
        "successful_tables": successful_tables,
        "failed_tables": failed_tables,
        "skipped_tables": skipped_tables,
        "total_rows_ingested": total_rows_ingested,
        "total_execution_time_ms": total_execution_time_ms,
        "results": results,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.table_ingest_result import TableIngestResult

    d = dict(src_dict)
    status = d.pop("status")

    graph_id = d.pop("graph_id")

    total_tables = d.pop("total_tables")

    successful_tables = d.pop("successful_tables")

    failed_tables = d.pop("failed_tables")

    skipped_tables = d.pop("skipped_tables")

    total_rows_ingested = d.pop("total_rows_ingested")

    total_execution_time_ms = d.pop("total_execution_time_ms")

    results = []
    _results = d.pop("results")
    for results_item_data in _results:
      results_item = TableIngestResult.from_dict(results_item_data)

      results.append(results_item)

    bulk_ingest_response = cls(
      status=status,
      graph_id=graph_id,
      total_tables=total_tables,
      successful_tables=successful_tables,
      failed_tables=failed_tables,
      skipped_tables=skipped_tables,
      total_rows_ingested=total_rows_ingested,
      total_execution_time_ms=total_execution_time_ms,
      results=results,
    )

    bulk_ingest_response.additional_properties = d
    return bulk_ingest_response

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
