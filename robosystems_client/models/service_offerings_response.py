from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.graph_subscriptions import GraphSubscriptions
  from ..models.operation_costs import OperationCosts
  from ..models.repository_subscriptions import RepositorySubscriptions
  from ..models.service_offering_summary import ServiceOfferingSummary


T = TypeVar("T", bound="ServiceOfferingsResponse")


@_attrs_define
class ServiceOfferingsResponse:
  """Complete service offerings response.

  Attributes:
      graph_subscriptions (GraphSubscriptions): Graph subscription offerings.
      repository_subscriptions (RepositorySubscriptions): Repository subscription offerings.
      operation_costs (OperationCosts): Operation cost information.
      summary (ServiceOfferingSummary): Summary of service offerings.
  """

  graph_subscriptions: "GraphSubscriptions"
  repository_subscriptions: "RepositorySubscriptions"
  operation_costs: "OperationCosts"
  summary: "ServiceOfferingSummary"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_subscriptions = self.graph_subscriptions.to_dict()

    repository_subscriptions = self.repository_subscriptions.to_dict()

    operation_costs = self.operation_costs.to_dict()

    summary = self.summary.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_subscriptions": graph_subscriptions,
        "repository_subscriptions": repository_subscriptions,
        "operation_costs": operation_costs,
        "summary": summary,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.graph_subscriptions import GraphSubscriptions
    from ..models.operation_costs import OperationCosts
    from ..models.repository_subscriptions import RepositorySubscriptions
    from ..models.service_offering_summary import ServiceOfferingSummary

    d = dict(src_dict)
    graph_subscriptions = GraphSubscriptions.from_dict(d.pop("graph_subscriptions"))

    repository_subscriptions = RepositorySubscriptions.from_dict(
      d.pop("repository_subscriptions")
    )

    operation_costs = OperationCosts.from_dict(d.pop("operation_costs"))

    summary = ServiceOfferingSummary.from_dict(d.pop("summary"))

    service_offerings_response = cls(
      graph_subscriptions=graph_subscriptions,
      repository_subscriptions=repository_subscriptions,
      operation_costs=operation_costs,
      summary=summary,
    )

    service_offerings_response.additional_properties = d
    return service_offerings_response

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
