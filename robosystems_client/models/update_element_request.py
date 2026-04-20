from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_element_request_balance_type_type_0 import (
  UpdateElementRequestBalanceTypeType0,
)
from ..models.update_element_request_period_type_type_0 import (
  UpdateElementRequestPeriodTypeType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateElementRequest")


@_attrs_define
class UpdateElementRequest:
  """Update mutable fields on an element. `taxonomy_id` and `source` are
  immutable. `parent_id` honors `model_dump(exclude_unset=True)` semantics:
  omit the field to leave unchanged, pass `null` to clear the parent
  (make root).

      Attributes:
          element_id (str):
          code (None | str | Unset):
          name (None | str | Unset):
          description (None | str | Unset):
          balance_type (None | Unset | UpdateElementRequestBalanceTypeType0):
          period_type (None | Unset | UpdateElementRequestPeriodTypeType0):
          parent_id (None | str | Unset):
          currency (None | str | Unset):
  """

  element_id: str
  code: None | str | Unset = UNSET
  name: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  balance_type: None | Unset | UpdateElementRequestBalanceTypeType0 = UNSET
  period_type: None | Unset | UpdateElementRequestPeriodTypeType0 = UNSET
  parent_id: None | str | Unset = UNSET
  currency: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    code: None | str | Unset
    if isinstance(self.code, Unset):
      code = UNSET
    else:
      code = self.code

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

    balance_type: None | str | Unset
    if isinstance(self.balance_type, Unset):
      balance_type = UNSET
    elif isinstance(self.balance_type, UpdateElementRequestBalanceTypeType0):
      balance_type = self.balance_type.value
    else:
      balance_type = self.balance_type

    period_type: None | str | Unset
    if isinstance(self.period_type, Unset):
      period_type = UNSET
    elif isinstance(self.period_type, UpdateElementRequestPeriodTypeType0):
      period_type = self.period_type.value
    else:
      period_type = self.period_type

    parent_id: None | str | Unset
    if isinstance(self.parent_id, Unset):
      parent_id = UNSET
    else:
      parent_id = self.parent_id

    currency: None | str | Unset
    if isinstance(self.currency, Unset):
      currency = UNSET
    else:
      currency = self.currency

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
      }
    )
    if code is not UNSET:
      field_dict["code"] = code
    if name is not UNSET:
      field_dict["name"] = name
    if description is not UNSET:
      field_dict["description"] = description
    if balance_type is not UNSET:
      field_dict["balance_type"] = balance_type
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if parent_id is not UNSET:
      field_dict["parent_id"] = parent_id
    if currency is not UNSET:
      field_dict["currency"] = currency

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    def _parse_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    code = _parse_code(d.pop("code", UNSET))

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

    def _parse_balance_type(
      data: object,
    ) -> None | Unset | UpdateElementRequestBalanceTypeType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        balance_type_type_0 = UpdateElementRequestBalanceTypeType0(data)

        return balance_type_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateElementRequestBalanceTypeType0, data)

    balance_type = _parse_balance_type(d.pop("balance_type", UNSET))

    def _parse_period_type(
      data: object,
    ) -> None | Unset | UpdateElementRequestPeriodTypeType0:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        period_type_type_0 = UpdateElementRequestPeriodTypeType0(data)

        return period_type_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | Unset | UpdateElementRequestPeriodTypeType0, data)

    period_type = _parse_period_type(d.pop("period_type", UNSET))

    def _parse_parent_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

    def _parse_currency(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    currency = _parse_currency(d.pop("currency", UNSET))

    update_element_request = cls(
      element_id=element_id,
      code=code,
      name=name,
      description=description,
      balance_type=balance_type,
      period_type=period_type,
      parent_id=parent_id,
      currency=currency,
    )

    update_element_request.additional_properties = d
    return update_element_request

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
