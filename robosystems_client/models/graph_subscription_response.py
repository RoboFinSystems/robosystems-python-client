from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphSubscriptionResponse")


@_attrs_define
class GraphSubscriptionResponse:
  """Response for graph or repository subscription details.

  Attributes:
      id (str): Subscription ID
      resource_type (str): Resource type (graph or repository)
      resource_id (str): Resource identifier
      plan_name (str): Current plan name
      billing_interval (str): Billing interval
      status (str): Subscription status
      base_price_cents (int): Base price in cents
      created_at (str): Creation timestamp
      current_period_start (Union[None, Unset, str]): Current billing period start
      current_period_end (Union[None, Unset, str]): Current billing period end
      started_at (Union[None, Unset, str]): Subscription start date
      canceled_at (Union[None, Unset, str]): Cancellation date
      ends_at (Union[None, Unset, str]): Subscription end date (when access will be revoked, especially relevant for
          cancelled subscriptions)
  """

  id: str
  resource_type: str
  resource_id: str
  plan_name: str
  billing_interval: str
  status: str
  base_price_cents: int
  created_at: str
  current_period_start: Union[None, Unset, str] = UNSET
  current_period_end: Union[None, Unset, str] = UNSET
  started_at: Union[None, Unset, str] = UNSET
  canceled_at: Union[None, Unset, str] = UNSET
  ends_at: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    resource_type = self.resource_type

    resource_id = self.resource_id

    plan_name = self.plan_name

    billing_interval = self.billing_interval

    status = self.status

    base_price_cents = self.base_price_cents

    created_at = self.created_at

    current_period_start: Union[None, Unset, str]
    if isinstance(self.current_period_start, Unset):
      current_period_start = UNSET
    else:
      current_period_start = self.current_period_start

    current_period_end: Union[None, Unset, str]
    if isinstance(self.current_period_end, Unset):
      current_period_end = UNSET
    else:
      current_period_end = self.current_period_end

    started_at: Union[None, Unset, str]
    if isinstance(self.started_at, Unset):
      started_at = UNSET
    else:
      started_at = self.started_at

    canceled_at: Union[None, Unset, str]
    if isinstance(self.canceled_at, Unset):
      canceled_at = UNSET
    else:
      canceled_at = self.canceled_at

    ends_at: Union[None, Unset, str]
    if isinstance(self.ends_at, Unset):
      ends_at = UNSET
    else:
      ends_at = self.ends_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "resource_type": resource_type,
        "resource_id": resource_id,
        "plan_name": plan_name,
        "billing_interval": billing_interval,
        "status": status,
        "base_price_cents": base_price_cents,
        "created_at": created_at,
      }
    )
    if current_period_start is not UNSET:
      field_dict["current_period_start"] = current_period_start
    if current_period_end is not UNSET:
      field_dict["current_period_end"] = current_period_end
    if started_at is not UNSET:
      field_dict["started_at"] = started_at
    if canceled_at is not UNSET:
      field_dict["canceled_at"] = canceled_at
    if ends_at is not UNSET:
      field_dict["ends_at"] = ends_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    resource_type = d.pop("resource_type")

    resource_id = d.pop("resource_id")

    plan_name = d.pop("plan_name")

    billing_interval = d.pop("billing_interval")

    status = d.pop("status")

    base_price_cents = d.pop("base_price_cents")

    created_at = d.pop("created_at")

    def _parse_current_period_start(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    current_period_start = _parse_current_period_start(
      d.pop("current_period_start", UNSET)
    )

    def _parse_current_period_end(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    current_period_end = _parse_current_period_end(d.pop("current_period_end", UNSET))

    def _parse_started_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    started_at = _parse_started_at(d.pop("started_at", UNSET))

    def _parse_canceled_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    canceled_at = _parse_canceled_at(d.pop("canceled_at", UNSET))

    def _parse_ends_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    ends_at = _parse_ends_at(d.pop("ends_at", UNSET))

    graph_subscription_response = cls(
      id=id,
      resource_type=resource_type,
      resource_id=resource_id,
      plan_name=plan_name,
      billing_interval=billing_interval,
      status=status,
      base_price_cents=base_price_cents,
      created_at=created_at,
      current_period_start=current_period_start,
      current_period_end=current_period_end,
      started_at=started_at,
      canceled_at=canceled_at,
      ends_at=ends_at,
    )

    graph_subscription_response.additional_properties = d
    return graph_subscription_response

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
