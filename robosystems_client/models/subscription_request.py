from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repository_plan import RepositoryPlan
from ..models.repository_type import RepositoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionRequest")


@_attrs_define
class SubscriptionRequest:
  """Request to create a new subscription.

  Attributes:
      repository_type (RepositoryType): Types of shared repositories.
      repository_plan (Union[Unset, RepositoryPlan]): Repository access plans for shared data.
  """

  repository_type: RepositoryType
  repository_plan: Union[Unset, RepositoryPlan] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    repository_type = self.repository_type.value

    repository_plan: Union[Unset, str] = UNSET
    if not isinstance(self.repository_plan, Unset):
      repository_plan = self.repository_plan.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "repository_type": repository_type,
      }
    )
    if repository_plan is not UNSET:
      field_dict["repository_plan"] = repository_plan

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    repository_type = RepositoryType(d.pop("repository_type"))

    _repository_plan = d.pop("repository_plan", UNSET)
    repository_plan: Union[Unset, RepositoryPlan]
    if isinstance(_repository_plan, Unset):
      repository_plan = UNSET
    else:
      repository_plan = RepositoryPlan(_repository_plan)

    subscription_request = cls(
      repository_type=repository_type,
      repository_plan=repository_plan,
    )

    subscription_request.additional_properties = d
    return subscription_request

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
