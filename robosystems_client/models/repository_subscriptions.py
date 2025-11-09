from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.repository_info import RepositoryInfo


T = TypeVar("T", bound="RepositorySubscriptions")


@_attrs_define
class RepositorySubscriptions:
  """Repository subscription offerings.

  Repository subscriptions are per-organization, not per-graph. All members
  of an organization share access to subscribed repositories.

      Attributes:
          description (str): Description of repository subscriptions
          pricing_model (str): Pricing model type (per_graph or per_organization)
          repositories (list['RepositoryInfo']): Available repositories
          notes (list[str]): Important notes
  """

  description: str
  pricing_model: str
  repositories: list["RepositoryInfo"]
  notes: list[str]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    description = self.description

    pricing_model = self.pricing_model

    repositories = []
    for repositories_item_data in self.repositories:
      repositories_item = repositories_item_data.to_dict()
      repositories.append(repositories_item)

    notes = self.notes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "description": description,
        "pricing_model": pricing_model,
        "repositories": repositories,
        "notes": notes,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.repository_info import RepositoryInfo

    d = dict(src_dict)
    description = d.pop("description")

    pricing_model = d.pop("pricing_model")

    repositories = []
    _repositories = d.pop("repositories")
    for repositories_item_data in _repositories:
      repositories_item = RepositoryInfo.from_dict(repositories_item_data)

      repositories.append(repositories_item)

    notes = cast(list[str], d.pop("notes"))

    repository_subscriptions = cls(
      description=description,
      pricing_model=pricing_model,
      repositories=repositories,
      notes=notes,
    )

    repository_subscriptions.additional_properties = d
    return repository_subscriptions

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
