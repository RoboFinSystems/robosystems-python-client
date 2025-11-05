from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.offering_repository_plan_rate_limits_type_0 import (
    OfferingRepositoryPlanRateLimitsType0,
  )


T = TypeVar("T", bound="OfferingRepositoryPlan")


@_attrs_define
class OfferingRepositoryPlan:
  """Information about a repository plan.

  Attributes:
      plan (str): Plan identifier
      name (str): Plan name
      monthly_price (float): Monthly price in USD
      monthly_credits (int): Monthly credit allocation
      access_level (str): Access level
      features (list[str]): List of features
      rate_limits (Union['OfferingRepositoryPlanRateLimitsType0', None, Unset]): Rate limits for this plan
  """

  plan: str
  name: str
  monthly_price: float
  monthly_credits: int
  access_level: str
  features: list[str]
  rate_limits: Union["OfferingRepositoryPlanRateLimitsType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.offering_repository_plan_rate_limits_type_0 import (
      OfferingRepositoryPlanRateLimitsType0,
    )

    plan = self.plan

    name = self.name

    monthly_price = self.monthly_price

    monthly_credits = self.monthly_credits

    access_level = self.access_level

    features = self.features

    rate_limits: Union[None, Unset, dict[str, Any]]
    if isinstance(self.rate_limits, Unset):
      rate_limits = UNSET
    elif isinstance(self.rate_limits, OfferingRepositoryPlanRateLimitsType0):
      rate_limits = self.rate_limits.to_dict()
    else:
      rate_limits = self.rate_limits

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "plan": plan,
        "name": name,
        "monthly_price": monthly_price,
        "monthly_credits": monthly_credits,
        "access_level": access_level,
        "features": features,
      }
    )
    if rate_limits is not UNSET:
      field_dict["rate_limits"] = rate_limits

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.offering_repository_plan_rate_limits_type_0 import (
      OfferingRepositoryPlanRateLimitsType0,
    )

    d = dict(src_dict)
    plan = d.pop("plan")

    name = d.pop("name")

    monthly_price = d.pop("monthly_price")

    monthly_credits = d.pop("monthly_credits")

    access_level = d.pop("access_level")

    features = cast(list[str], d.pop("features"))

    def _parse_rate_limits(
      data: object,
    ) -> Union["OfferingRepositoryPlanRateLimitsType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        rate_limits_type_0 = OfferingRepositoryPlanRateLimitsType0.from_dict(data)

        return rate_limits_type_0
      except:  # noqa: E722
        pass
      return cast(Union["OfferingRepositoryPlanRateLimitsType0", None, Unset], data)

    rate_limits = _parse_rate_limits(d.pop("rate_limits", UNSET))

    offering_repository_plan = cls(
      plan=plan,
      name=name,
      monthly_price=monthly_price,
      monthly_credits=monthly_credits,
      access_level=access_level,
      features=features,
      rate_limits=rate_limits,
    )

    offering_repository_plan.additional_properties = d
    return offering_repository_plan

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
