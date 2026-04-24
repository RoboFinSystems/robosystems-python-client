from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisposeScheduleRequest")


@_attrs_define
class DisposeScheduleRequest:
  """Dispose a schedule early — combines truncation with a disposal closing entry.

  Computes net book value from the schedule's own facts, truncates forward
  periods, and creates a balanced disposal entry in one atomic operation.
  Use when an asset is sold or abandoned before the schedule runs to completion.

      Attributes:
          structure_id (str): Target schedule structure ID.
          disposal_date (datetime.date): Last day of the final period (month-end). Forward facts past this date are
              deleted; the disposal entry is posted on this date.
          memo (str): Memo for the disposal closing entry.
          reason (str): Reason for disposal (audit trail).
          sale_proceeds (int | None | Unset): Cash received from the sale in cents. None or 0 for abandonment (no cash
              received). If provided, `proceeds_element_id` is required.
          proceeds_element_id (None | str | Unset): Element to debit for sale proceeds (e.g., Cash or AR). Required when
              sale_proceeds > 0.
          gain_loss_element_id (None | str | Unset): Element for gain or loss on disposal. Required when net book value >
              0 after applying sale proceeds. Optional when asset is fully depreciated (NBV = 0, no gain/loss line needed).
  """

  structure_id: str
  disposal_date: datetime.date
  memo: str
  reason: str
  sale_proceeds: int | None | Unset = UNSET
  proceeds_element_id: None | str | Unset = UNSET
  gain_loss_element_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    disposal_date = self.disposal_date.isoformat()

    memo = self.memo

    reason = self.reason

    sale_proceeds: int | None | Unset
    if isinstance(self.sale_proceeds, Unset):
      sale_proceeds = UNSET
    else:
      sale_proceeds = self.sale_proceeds

    proceeds_element_id: None | str | Unset
    if isinstance(self.proceeds_element_id, Unset):
      proceeds_element_id = UNSET
    else:
      proceeds_element_id = self.proceeds_element_id

    gain_loss_element_id: None | str | Unset
    if isinstance(self.gain_loss_element_id, Unset):
      gain_loss_element_id = UNSET
    else:
      gain_loss_element_id = self.gain_loss_element_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "disposal_date": disposal_date,
        "memo": memo,
        "reason": reason,
      }
    )
    if sale_proceeds is not UNSET:
      field_dict["sale_proceeds"] = sale_proceeds
    if proceeds_element_id is not UNSET:
      field_dict["proceeds_element_id"] = proceeds_element_id
    if gain_loss_element_id is not UNSET:
      field_dict["gain_loss_element_id"] = gain_loss_element_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    disposal_date = isoparse(d.pop("disposal_date")).date()

    memo = d.pop("memo")

    reason = d.pop("reason")

    def _parse_sale_proceeds(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    sale_proceeds = _parse_sale_proceeds(d.pop("sale_proceeds", UNSET))

    def _parse_proceeds_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    proceeds_element_id = _parse_proceeds_element_id(
      d.pop("proceeds_element_id", UNSET)
    )

    def _parse_gain_loss_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    gain_loss_element_id = _parse_gain_loss_element_id(
      d.pop("gain_loss_element_id", UNSET)
    )

    dispose_schedule_request = cls(
      structure_id=structure_id,
      disposal_date=disposal_date,
      memo=memo,
      reason=reason,
      sale_proceeds=sale_proceeds,
      proceeds_element_id=proceeds_element_id,
      gain_loss_element_id=gain_loss_element_id,
    )

    dispose_schedule_request.additional_properties = d
    return dispose_schedule_request

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
