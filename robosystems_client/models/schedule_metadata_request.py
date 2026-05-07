from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleMetadataRequest")


@_attrs_define
class ScheduleMetadataRequest:
  """
  Attributes:
      method (str | Unset): Calculation method. 'straight_line' (default) distributes `monthly_amount` evenly across
          periods with the final period absorbing rounding. 'custom' requires `periodic_amounts` — the generator uses
          those values verbatim instead of computing. Other strings are labels only; fact values still come from
          `monthly_amount` or `periodic_amounts`. Default: 'straight_line'.
      original_amount (int | Unset): Cost basis in cents Default: 0.
      residual_value (int | Unset): Salvage value in cents Default: 0.
      useful_life_months (int | Unset): Useful life in months Default: 0.
      asset_element_id (None | str | Unset): BS asset element for net book value
      periodic_amounts (list[int] | None | Unset): Explicit per-period amounts in cents. When set, the generator uses
          these values instead of `monthly_amount` — enabling non-straight-line schedules (effective-interest bond
          discount amortization, day-count interest accrual, variable lease payments, pre-computed effective-yield curves,
          etc.). Length must match the number of monthly periods between `period_start` and `period_end`; sum must equal
          `original_amount` exactly. The auto-generated SumEquals rule proves Σ = original regardless of the curve shape.
  """

  method: str | Unset = "straight_line"
  original_amount: int | Unset = 0
  residual_value: int | Unset = 0
  useful_life_months: int | Unset = 0
  asset_element_id: None | str | Unset = UNSET
  periodic_amounts: list[int] | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    method = self.method

    original_amount = self.original_amount

    residual_value = self.residual_value

    useful_life_months = self.useful_life_months

    asset_element_id: None | str | Unset
    if isinstance(self.asset_element_id, Unset):
      asset_element_id = UNSET
    else:
      asset_element_id = self.asset_element_id

    periodic_amounts: list[int] | None | Unset
    if isinstance(self.periodic_amounts, Unset):
      periodic_amounts = UNSET
    elif isinstance(self.periodic_amounts, list):
      periodic_amounts = self.periodic_amounts

    else:
      periodic_amounts = self.periodic_amounts

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if method is not UNSET:
      field_dict["method"] = method
    if original_amount is not UNSET:
      field_dict["original_amount"] = original_amount
    if residual_value is not UNSET:
      field_dict["residual_value"] = residual_value
    if useful_life_months is not UNSET:
      field_dict["useful_life_months"] = useful_life_months
    if asset_element_id is not UNSET:
      field_dict["asset_element_id"] = asset_element_id
    if periodic_amounts is not UNSET:
      field_dict["periodic_amounts"] = periodic_amounts

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    method = d.pop("method", UNSET)

    original_amount = d.pop("original_amount", UNSET)

    residual_value = d.pop("residual_value", UNSET)

    useful_life_months = d.pop("useful_life_months", UNSET)

    def _parse_asset_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    asset_element_id = _parse_asset_element_id(d.pop("asset_element_id", UNSET))

    def _parse_periodic_amounts(data: object) -> list[int] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        periodic_amounts_type_0 = cast(list[int], data)

        return periodic_amounts_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[int] | None | Unset, data)

    periodic_amounts = _parse_periodic_amounts(d.pop("periodic_amounts", UNSET))

    schedule_metadata_request = cls(
      method=method,
      original_amount=original_amount,
      residual_value=residual_value,
      useful_life_months=useful_life_months,
      asset_element_id=asset_element_id,
      periodic_amounts=periodic_amounts,
    )

    schedule_metadata_request.additional_properties = d
    return schedule_metadata_request

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
