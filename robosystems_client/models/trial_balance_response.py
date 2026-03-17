from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.trial_balance_row import TrialBalanceRow


T = TypeVar("T", bound="TrialBalanceResponse")


@_attrs_define
class TrialBalanceResponse:
  """
  Attributes:
      rows (list[TrialBalanceRow]):
      total_debits (float):
      total_credits (float):
  """

  rows: list[TrialBalanceRow]
  total_debits: float
  total_credits: float
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    rows = []
    for rows_item_data in self.rows:
      rows_item = rows_item_data.to_dict()
      rows.append(rows_item)

    total_debits = self.total_debits

    total_credits = self.total_credits

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "rows": rows,
        "total_debits": total_debits,
        "total_credits": total_credits,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.trial_balance_row import TrialBalanceRow

    d = dict(src_dict)
    rows = []
    _rows = d.pop("rows")
    for rows_item_data in _rows:
      rows_item = TrialBalanceRow.from_dict(rows_item_data)

      rows.append(rows_item)

    total_debits = d.pop("total_debits")

    total_credits = d.pop("total_credits")

    trial_balance_response = cls(
      rows=rows,
      total_debits=total_debits,
      total_credits=total_credits,
    )

    trial_balance_response.additional_properties = d
    return trial_balance_response

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
