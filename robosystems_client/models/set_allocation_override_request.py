from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetAllocationOverrideRequest")


@_attrs_define
class SetAllocationOverrideRequest:
  """The outside owners' share of a member's result for one month, set by a
  person in place of the pro-rata share: a preferred return, a waterfall, a
  special allocation.

      Attributes:
          entity_id (str): The member, consolidated in full.
          period (str): The month, as YYYY-MM.
          amount (int | None | Unset): The outside owners' share of the month's result, in cents; negative for a share of
              a loss.
          percentage (float | None | Unset): The outside owners' share as a percentage of the month's result.
          basis (None | str | Unset): Why the share differs from the ownership percentage; required to set one.
          clear (bool | Unset): Remove the month's override, back to the pro-rata share. Default: False.
  """

  entity_id: str
  period: str
  amount: int | None | Unset = UNSET
  percentage: float | None | Unset = UNSET
  basis: None | str | Unset = UNSET
  clear: bool | Unset = False
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

    clear = self.clear

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
    if clear is not UNSET:
      field_dict["clear"] = clear

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

    clear = d.pop("clear", UNSET)

    set_allocation_override_request = cls(
      entity_id=entity_id,
      period=period,
      amount=amount,
      percentage=percentage,
      basis=basis,
      clear=clear,
    )

    set_allocation_override_request.additional_properties = d
    return set_allocation_override_request

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
