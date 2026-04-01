from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortfolioResponse")


@_attrs_define
class PortfolioResponse:
  """
  Attributes:
      id (str):
      name (str):
      base_currency (str):
      created_at (datetime.datetime):
      updated_at (datetime.datetime):
      description (None | str | Unset):
      strategy (None | str | Unset):
      inception_date (datetime.date | None | Unset):
  """

  id: str
  name: str
  base_currency: str
  created_at: datetime.datetime
  updated_at: datetime.datetime
  description: None | str | Unset = UNSET
  strategy: None | str | Unset = UNSET
  inception_date: datetime.date | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    name = self.name

    base_currency = self.base_currency

    created_at = self.created_at.isoformat()

    updated_at = self.updated_at.isoformat()

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

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "name": name,
        "base_currency": base_currency,
        "created_at": created_at,
        "updated_at": updated_at,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if strategy is not UNSET:
      field_dict["strategy"] = strategy
    if inception_date is not UNSET:
      field_dict["inception_date"] = inception_date

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    name = d.pop("name")

    base_currency = d.pop("base_currency")

    created_at = isoparse(d.pop("created_at"))

    updated_at = isoparse(d.pop("updated_at"))

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

    portfolio_response = cls(
      id=id,
      name=name,
      base_currency=base_currency,
      created_at=created_at,
      updated_at=updated_at,
      description=description,
      strategy=strategy,
      inception_date=inception_date,
    )

    portfolio_response.additional_properties = d
    return portfolio_response

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
