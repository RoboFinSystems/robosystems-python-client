from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.agent_response import AgentResponse


T = TypeVar("T", bound="BatchAgentResponse")


@_attrs_define
class BatchAgentResponse:
  """Response for batch processing.

  Attributes:
      results (list['AgentResponse']): List of agent responses
      total_execution_time (float): Total execution time
      parallel_processed (bool): Whether queries were processed in parallel
  """

  results: list["AgentResponse"]
  total_execution_time: float
  parallel_processed: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    results = []
    for results_item_data in self.results:
      results_item = results_item_data.to_dict()
      results.append(results_item)

    total_execution_time = self.total_execution_time

    parallel_processed = self.parallel_processed

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "results": results,
        "total_execution_time": total_execution_time,
        "parallel_processed": parallel_processed,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.agent_response import AgentResponse

    d = dict(src_dict)
    results = []
    _results = d.pop("results")
    for results_item_data in _results:
      results_item = AgentResponse.from_dict(results_item_data)

      results.append(results_item)

    total_execution_time = d.pop("total_execution_time")

    parallel_processed = d.pop("parallel_processed")

    batch_agent_response = cls(
      results=results,
      total_execution_time=total_execution_time,
      parallel_processed=parallel_processed,
    )

    batch_agent_response.additional_properties = d
    return batch_agent_response

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
