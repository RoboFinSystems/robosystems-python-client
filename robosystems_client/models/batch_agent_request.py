from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.agent_request import AgentRequest


T = TypeVar("T", bound="BatchAgentRequest")


@_attrs_define
class BatchAgentRequest:
  """Request for batch processing multiple queries.

  Attributes:
      queries (list['AgentRequest']): List of queries to process
      parallel (Union[Unset, bool]): Process queries in parallel Default: False.
  """

  queries: list["AgentRequest"]
  parallel: Union[Unset, bool] = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    queries = []
    for queries_item_data in self.queries:
      queries_item = queries_item_data.to_dict()
      queries.append(queries_item)

    parallel = self.parallel

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "queries": queries,
      }
    )
    if parallel is not UNSET:
      field_dict["parallel"] = parallel

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.agent_request import AgentRequest

    d = dict(src_dict)
    queries = []
    _queries = d.pop("queries")
    for queries_item_data in _queries:
      queries_item = AgentRequest.from_dict(queries_item_data)

      queries.append(queries_item)

    parallel = d.pop("parallel", UNSET)

    batch_agent_request = cls(
      queries=queries,
      parallel=parallel,
    )

    batch_agent_request.additional_properties = d
    return batch_agent_request

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
