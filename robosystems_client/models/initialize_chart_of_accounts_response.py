from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.initialize_chart_of_accounts_response_template import (
  InitializeChartOfAccountsResponseTemplate,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InitializeChartOfAccountsResponse")


@_attrs_define
class InitializeChartOfAccountsResponse:
  """
  Attributes:
      taxonomy_id (str): The new chart's taxonomy id.
      name (str):
      template (InitializeChartOfAccountsResponseTemplate):
      entity_type (str): Legal form the equity rows were mapped for.
      elements_created (int):
      mappings_created (int):
      frameworks (list[str] | Unset): Frameworks the chart was mapped into — each template mapping set whose framework
          this graph's library carries (rs-gaap today; every framework in the graph's pin once it is plural).
      unresolved (list[str] | Unset): What could not be mapped, never fatal — the accounts exist and can be mapped by
          hand: a target qname the framework's library copy did not resolve, `<framework>: not in this graph's library`
          for a template mapping set whose framework this graph does not carry, or a template row naming an account it
          does not declare.
  """

  taxonomy_id: str
  name: str
  template: InitializeChartOfAccountsResponseTemplate
  entity_type: str
  elements_created: int
  mappings_created: int
  frameworks: list[str] | Unset = UNSET
  unresolved: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    taxonomy_id = self.taxonomy_id

    name = self.name

    template = self.template.value

    entity_type = self.entity_type

    elements_created = self.elements_created

    mappings_created = self.mappings_created

    frameworks: list[str] | Unset = UNSET
    if not isinstance(self.frameworks, Unset):
      frameworks = self.frameworks

    unresolved: list[str] | Unset = UNSET
    if not isinstance(self.unresolved, Unset):
      unresolved = self.unresolved

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "taxonomy_id": taxonomy_id,
        "name": name,
        "template": template,
        "entity_type": entity_type,
        "elements_created": elements_created,
        "mappings_created": mappings_created,
      }
    )
    if frameworks is not UNSET:
      field_dict["frameworks"] = frameworks
    if unresolved is not UNSET:
      field_dict["unresolved"] = unresolved

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    taxonomy_id = d.pop("taxonomy_id")

    name = d.pop("name")

    template = InitializeChartOfAccountsResponseTemplate(d.pop("template"))

    entity_type = d.pop("entity_type")

    elements_created = d.pop("elements_created")

    mappings_created = d.pop("mappings_created")

    frameworks = cast(list[str], d.pop("frameworks", UNSET))

    unresolved = cast(list[str], d.pop("unresolved", UNSET))

    initialize_chart_of_accounts_response = cls(
      taxonomy_id=taxonomy_id,
      name=name,
      template=template,
      entity_type=entity_type,
      elements_created=elements_created,
      mappings_created=mappings_created,
      frameworks=frameworks,
      unresolved=unresolved,
    )

    initialize_chart_of_accounts_response.additional_properties = d
    return initialize_chart_of_accounts_response

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
