from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortfolioBlockPortfolioFields")


@_attrs_define
class PortfolioBlockPortfolioFields:
  """Fields settable on the portfolio core when creating a block.

  Attributes:
      name (str): Display name for the portfolio. 1-200 characters.
      description (None | str | Unset): Free-text description of the portfolio.
      strategy (None | str | Unset): Free-text strategy classification (e.g. `value`, `growth`, `income`). Open
          vocabulary.
      inception_date (datetime.date | None | Unset): Date the portfolio was established (YYYY-MM-DD).
      base_currency (str | Unset): ISO 4217 currency code used for portfolio-level aggregates (e.g.
          `total_cost_basis_dollars`). Default: 'USD'.
      entity_id (None | str | Unset): ID of the owning entity (e.g. fund, trust, or person). Optional — leave unset
          for unattributed portfolios.
  """

  name: str
  description: None | str | Unset = UNSET
  strategy: None | str | Unset = UNSET
  inception_date: datetime.date | None | Unset = UNSET
  base_currency: str | Unset = "USD"
  entity_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    strategy: None | str | Unset
    if isinstance(self.strategy, Unset):
      strategy = UNSET
    else:
      strategy = self.strategy

    inception_date: None | str | Unset
    if isinstance(self.inception_date, Unset):
      inception_date = UNSET
    elif isinstance(self.inception_date, datetime.date):
      inception_date = self.inception_date.isoformat()
    else:
      inception_date = self.inception_date

    base_currency = self.base_currency

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if strategy is not UNSET:
      field_dict["strategy"] = strategy
    if inception_date is not UNSET:
      field_dict["inception_date"] = inception_date
    if base_currency is not UNSET:
      field_dict["base_currency"] = base_currency
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_strategy(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    strategy = _parse_strategy(d.pop("strategy", UNSET))

    def _parse_inception_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        inception_date_type_0 = isoparse(data).date()

        return inception_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    inception_date = _parse_inception_date(d.pop("inception_date", UNSET))

    base_currency = d.pop("base_currency", UNSET)

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    portfolio_block_portfolio_fields = cls(
      name=name,
      description=description,
      strategy=strategy,
      inception_date=inception_date,
      base_currency=base_currency,
      entity_id=entity_id,
    )

    portfolio_block_portfolio_fields.additional_properties = d
    return portfolio_block_portfolio_fields

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
