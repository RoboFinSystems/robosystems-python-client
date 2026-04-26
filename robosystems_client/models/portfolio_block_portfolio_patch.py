from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortfolioBlockPortfolioPatch")


@_attrs_define
class PortfolioBlockPortfolioPatch:
  """Patchable portfolio fields on `update-portfolio-block`. Unset fields ignored.

  Attributes:
      name (None | str | Unset):
      description (None | str | Unset):
      strategy (None | str | Unset):
      inception_date (datetime.date | None | Unset):
      base_currency (None | str | Unset):
      entity_id (None | str | Unset):
  """

  name: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  strategy: None | str | Unset = UNSET
  inception_date: datetime.date | None | Unset = UNSET
  base_currency: None | str | Unset = UNSET
  entity_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
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

    base_currency: None | str | Unset
    if isinstance(self.base_currency, Unset):
      base_currency = UNSET
    else:
      base_currency = self.base_currency

    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if name is not UNSET:
      field_dict["name"] = name
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

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

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

    def _parse_base_currency(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    base_currency = _parse_base_currency(d.pop("base_currency", UNSET))

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    portfolio_block_portfolio_patch = cls(
      name=name,
      description=description,
      strategy=strategy,
      inception_date=inception_date,
      base_currency=base_currency,
      entity_id=entity_id,
    )

    portfolio_block_portfolio_patch.additional_properties = d
    return portfolio_block_portfolio_patch

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
