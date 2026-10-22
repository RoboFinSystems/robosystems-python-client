from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_roll_forward_row_scope import ScheduleRollForwardRowScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleRollForwardRow")


@_attrs_define
class ScheduleRollForwardRow:
  """One period of a previewed schedule: the balance it carries, and what
  moves it.

      Attributes:
          period_start (datetime.date):
          period_end (datetime.date):
          opening (float): The carried balance at the period's start.
          amount (float): What the period recognizes: the entry's debit amount.
          closing (float): The carried balance at the period's end.
          scope (ScheduleRollForwardRowScope): `historical` for a month already in the books' history, which the schedule
              records but never drafts; `in_scope` for one a close drafts.
          interest (float | None | Unset): Loan schedules: interest accrued.
          payment (float | None | Unset): Loan schedules: the payment.
          principal (float | None | Unset): Loan schedules: principal repaid.
          current_portion (float | None | Unset): Loan schedules with a current-portion account: the principal due in the
              next twelve months.
  """

  period_start: datetime.date
  period_end: datetime.date
  opening: float
  amount: float
  closing: float
  scope: ScheduleRollForwardRowScope
  interest: float | None | Unset = UNSET
  payment: float | None | Unset = UNSET
  principal: float | None | Unset = UNSET
  current_portion: float | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    opening = self.opening

    amount = self.amount

    closing = self.closing

    scope = self.scope.value

    interest: float | None | Unset
    if isinstance(self.interest, Unset):
      interest = UNSET
    else:
      interest = self.interest

    payment: float | None | Unset
    if isinstance(self.payment, Unset):
      payment = UNSET
    else:
      payment = self.payment

    principal: float | None | Unset
    if isinstance(self.principal, Unset):
      principal = UNSET
    else:
      principal = self.principal

    current_portion: float | None | Unset
    if isinstance(self.current_portion, Unset):
      current_portion = UNSET
    else:
      current_portion = self.current_portion

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period_start": period_start,
        "period_end": period_end,
        "opening": opening,
        "amount": amount,
        "closing": closing,
        "scope": scope,
      }
    )
    if interest is not UNSET:
      field_dict["interest"] = interest
    if payment is not UNSET:
      field_dict["payment"] = payment
    if principal is not UNSET:
      field_dict["principal"] = principal
    if current_portion is not UNSET:
      field_dict["current_portion"] = current_portion

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    period_start = datetime.date.fromisoformat(d.pop("period_start"))

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    opening = d.pop("opening")

    amount = d.pop("amount")

    closing = d.pop("closing")

    scope = ScheduleRollForwardRowScope(d.pop("scope"))

    def _parse_interest(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    interest = _parse_interest(d.pop("interest", UNSET))

    def _parse_payment(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    payment = _parse_payment(d.pop("payment", UNSET))

    def _parse_principal(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    principal = _parse_principal(d.pop("principal", UNSET))

    def _parse_current_portion(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    current_portion = _parse_current_portion(d.pop("current_portion", UNSET))

    schedule_roll_forward_row = cls(
      period_start=period_start,
      period_end=period_end,
      opening=opening,
      amount=amount,
      closing=closing,
      scope=scope,
      interest=interest,
      payment=payment,
      principal=principal,
      current_portion=current_portion,
    )

    schedule_roll_forward_row.additional_properties = d
    return schedule_roll_forward_row

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
