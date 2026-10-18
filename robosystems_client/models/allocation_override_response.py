from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AllocationOverrideResponse")


@_attrs_define
class AllocationOverrideResponse:
  """A member's allocation override for one month.

  Attributes:
      entity_id (str): The member.
      period (str): The month, as YYYY-MM.
      amount (int | None | Unset): The share, in cents, when set so.
      percentage (float | None | Unset): The share as a percentage, when set so.
      basis (None | str | Unset): Why it differs from pro rata.
      set_by (None | str | Unset): Who set it.
      cleared (bool | Unset): True when the override was removed. Default: False.
  """

  entity_id: str
  period: str
  amount: int | None | Unset = UNSET
  percentage: float | None | Unset = UNSET
  basis: None | str | Unset = UNSET
  set_by: None | str | Unset = UNSET
  cleared: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    period = self.period

    amount: int | None | Unset
    if isinstance(self.amount, Unset):
      amount = UNSET
    else:
      amount = self.amount

    percentage: float | None | Unset
    if isinstance(self.percentage, Unset):
      percentage = UNSET
    else:
      percentage = self.percentage

    basis: None | str | Unset
    if isinstance(self.basis, Unset):
      basis = UNSET
    else:
      basis = self.basis

    set_by: None | str | Unset
    if isinstance(self.set_by, Unset):
      set_by = UNSET
    else:
      set_by = self.set_by

    cleared = self.cleared

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "period": period,
      }
    )
    if amount is not UNSET:
      field_dict["amount"] = amount
    if percentage is not UNSET:
      field_dict["percentage"] = percentage
    if basis is not UNSET:
      field_dict["basis"] = basis
    if set_by is not UNSET:
      field_dict["set_by"] = set_by
    if cleared is not UNSET:
      field_dict["cleared"] = cleared

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    period = d.pop("period")

    def _parse_amount(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    amount = _parse_amount(d.pop("amount", UNSET))

    def _parse_percentage(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    percentage = _parse_percentage(d.pop("percentage", UNSET))

    def _parse_basis(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    basis = _parse_basis(d.pop("basis", UNSET))

    def _parse_set_by(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    set_by = _parse_set_by(d.pop("set_by", UNSET))

    cleared = d.pop("cleared", UNSET)

    allocation_override_response = cls(
      entity_id=entity_id,
      period=period,
      amount=amount,
      percentage=percentage,
      basis=basis,
      set_by=set_by,
      cleared=cleared,
    )

    allocation_override_response.additional_properties = d
    return allocation_override_response

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
