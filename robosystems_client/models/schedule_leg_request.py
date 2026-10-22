from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_leg_request_amount_source import ScheduleLegRequestAmountSource
from ..models.schedule_leg_request_side import ScheduleLegRequestSide

T = TypeVar("T", bound="ScheduleLegRequest")


@_attrs_define
class ScheduleLegRequest:
  """One line of the entry a loan schedule drafts each period.

  Attributes:
      element_id (str): CoA element id the line posts to.
      side (ScheduleLegRequestSide): The line's side.
      amount_source (ScheduleLegRequestAmountSource): The amortization-table column the line takes each period:
          `interest` (accrued in the period), `interest_paid` (accrued interest settled by the period's payment),
          `principal` (principal repaid), `payment` (interest_paid + principal).
  """

  element_id: str
  side: ScheduleLegRequestSide
  amount_source: ScheduleLegRequestAmountSource
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    side = self.side.value

    amount_source = self.amount_source.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "side": side,
        "amount_source": amount_source,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    side = ScheduleLegRequestSide(d.pop("side"))

    amount_source = ScheduleLegRequestAmountSource(d.pop("amount_source"))

    schedule_leg_request = cls(
      element_id=element_id,
      side=side,
      amount_source=amount_source,
    )

    schedule_leg_request.additional_properties = d
    return schedule_leg_request

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
