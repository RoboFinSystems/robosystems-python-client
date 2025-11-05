from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.offering_repository_plan import OfferingRepositoryPlan


T = TypeVar("T", bound="RepositoryInfo")


@_attrs_define
class RepositoryInfo:
  """Information about a shared repository.

  Attributes:
      type_ (str): Repository type identifier
      name (str): Repository name
      description (str): Repository description
      enabled (bool): Whether repository is enabled
      coming_soon (bool): Whether repository is coming soon
      plans (list['OfferingRepositoryPlan']): Available plans
  """

  type_: str
  name: str
  description: str
  enabled: bool
  coming_soon: bool
  plans: list["OfferingRepositoryPlan"]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    type_ = self.type_

    name = self.name

    description = self.description

    enabled = self.enabled

    coming_soon = self.coming_soon

    plans = []
    for plans_item_data in self.plans:
      plans_item = plans_item_data.to_dict()
      plans.append(plans_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "type": type_,
        "name": name,
        "description": description,
        "enabled": enabled,
        "coming_soon": coming_soon,
        "plans": plans,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.offering_repository_plan import OfferingRepositoryPlan

    d = dict(src_dict)
    type_ = d.pop("type")

    name = d.pop("name")

    description = d.pop("description")

    enabled = d.pop("enabled")

    coming_soon = d.pop("coming_soon")

    plans = []
    _plans = d.pop("plans")
    for plans_item_data in _plans:
      plans_item = OfferingRepositoryPlan.from_dict(plans_item_data)

      plans.append(plans_item)

    repository_info = cls(
      type_=type_,
      name=name,
      description=description,
      enabled=enabled,
      coming_soon=coming_soon,
      plans=plans,
    )

    repository_info.additional_properties = d
    return repository_info

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
