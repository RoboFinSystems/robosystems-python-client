from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.initialize_chart_of_accounts_request_template import (
  InitializeChartOfAccountsRequestTemplate,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InitializeChartOfAccountsRequest")


@_attrs_define
class InitializeChartOfAccountsRequest:
  """Create the graph's chart of accounts from a shipped template.

  Refused (409) when the graph already has an active ``chart_of_accounts``
  taxonomy — a QuickBooks-synced tenant never needs this, and a chart is
  never replaced. The template's equity rows are mapped by the entity's
  legal form (``entity_type``: corporation / llc / partnership); omit it
  to use the graph's primary entity, falling back to corporation.

      Attributes:
          template (InitializeChartOfAccountsRequestTemplate): Template key: `saas` (subscription software — deferred
              revenue, cost of revenue, R&D / S&M / G&A), `services` (professional services — no inventory, no COGS),
              `product` (inventory and cost of goods sold, direct + wholesale + subscription revenue).
          entity_type (None | str | Unset): Legal form for the equity mapping: `corporation`, `llc` or `partnership`.
              Defaults to the graph's primary entity, then to corporation.
          name (None | str | Unset): Chart display name. Defaults to 'Chart of Accounts'.
  """

  template: InitializeChartOfAccountsRequestTemplate
  entity_type: None | str | Unset = UNSET
  name: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    template = self.template.value

    entity_type: None | str | Unset
    if isinstance(self.entity_type, Unset):
      entity_type = UNSET
    else:
      entity_type = self.entity_type

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "template": template,
      }
    )
    if entity_type is not UNSET:
      field_dict["entity_type"] = entity_type
    if name is not UNSET:
      field_dict["name"] = name

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    template = InitializeChartOfAccountsRequestTemplate(d.pop("template"))

    def _parse_entity_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_type = _parse_entity_type(d.pop("entity_type", UNSET))

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    initialize_chart_of_accounts_request = cls(
      template=template,
      entity_type=entity_type,
      name=name,
    )

    initialize_chart_of_accounts_request.additional_properties = d
    return initialize_chart_of_accounts_request

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
