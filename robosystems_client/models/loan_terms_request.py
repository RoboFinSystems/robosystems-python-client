from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.loan_terms_request_day_count import LoanTermsRequestDayCount
from ..models.loan_terms_request_payment_frequency import (
  LoanTermsRequestPaymentFrequency,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoanTermsRequest")


@_attrs_define
class LoanTermsRequest:
  """The terms a loan schedule's amortization table is computed from.

  Attributes:
      principal (int): Principal drawn, in cents.
      annual_rate (float): Annual interest rate as a fraction: 0.099 for 9.9%.
      start_date (datetime.date): The day the principal was drawn; interest accrues from it. Falls in the schedule's
          first month.
      note_element_id (str): The liability account the principal is carried in. The schedule states its balance each
          period, which the schedule reconciliation compares with the ledger.
      day_count (LoanTermsRequestDayCount | Unset): How a period's interest counts days: `30/360` (every whole month
          is 30 days), `actual/365` or `actual/360` (the days elapsed, over a 365- or 360-day year; actual/360 is the
          usual bank line of credit). Default: LoanTermsRequestDayCount.VALUE_0.
      payment_frequency (LoanTermsRequestPaymentFrequency | Unset): How often a payment falls due. A payment is
          applied at the end of the month it falls in. Default: LoanTermsRequestPaymentFrequency.MONTHLY.
      first_payment_date (datetime.date | None | Unset): The first payment's date. Omit for one frequency after the
          schedule's first month.
      payment_amount (int | None | Unset): Each scheduled payment in cents, interest included. Omit for the level
          payment that retires the principal by `maturity_date`, or for the accrued interest when `interest_only`.
      interest_only (bool | Unset): Payments settle interest only; the principal is due at maturity. Default: False.
      maturity_date (datetime.date | None | Unset): When the remaining principal is due: it is repaid in that month,
          which is the schedule's last. Omit for a line of credit with no maturity, whose balance carries past the
          schedule.
      capitalize_interest (bool | Unset): Interest is added to the note rather than accrued apart (a PIK note): the
          balance grows by each period's interest, and payments reduce it whole. Default: False.
      current_portion_element_id (None | str | Unset): A current-liability account for the principal due within twelve
          months. When set, each period's entry also reclasses between it and `note_element_id` so it holds the next
          twelve months' principal.
  """

  principal: int
  annual_rate: float
  start_date: datetime.date
  note_element_id: str
  day_count: LoanTermsRequestDayCount | Unset = LoanTermsRequestDayCount.VALUE_0
  payment_frequency: LoanTermsRequestPaymentFrequency | Unset = (
    LoanTermsRequestPaymentFrequency.MONTHLY
  )
  first_payment_date: datetime.date | None | Unset = UNSET
  payment_amount: int | None | Unset = UNSET
  interest_only: bool | Unset = False
  maturity_date: datetime.date | None | Unset = UNSET
  capitalize_interest: bool | Unset = False
  current_portion_element_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    principal = self.principal

    annual_rate = self.annual_rate

    start_date = self.start_date.isoformat()

    note_element_id = self.note_element_id

    day_count: str | Unset = UNSET
    if not isinstance(self.day_count, Unset):
      day_count = self.day_count.value

    payment_frequency: str | Unset = UNSET
    if not isinstance(self.payment_frequency, Unset):
      payment_frequency = self.payment_frequency.value

    first_payment_date: None | str | Unset
    if isinstance(self.first_payment_date, Unset):
      first_payment_date = UNSET
    elif isinstance(self.first_payment_date, datetime.date):
      first_payment_date = self.first_payment_date.isoformat()
    else:
      first_payment_date = self.first_payment_date

    payment_amount: int | None | Unset
    if isinstance(self.payment_amount, Unset):
      payment_amount = UNSET
    else:
      payment_amount = self.payment_amount

    interest_only = self.interest_only

    maturity_date: None | str | Unset
    if isinstance(self.maturity_date, Unset):
      maturity_date = UNSET
    elif isinstance(self.maturity_date, datetime.date):
      maturity_date = self.maturity_date.isoformat()
    else:
      maturity_date = self.maturity_date

    capitalize_interest = self.capitalize_interest

    current_portion_element_id: None | str | Unset
    if isinstance(self.current_portion_element_id, Unset):
      current_portion_element_id = UNSET
    else:
      current_portion_element_id = self.current_portion_element_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "principal": principal,
        "annual_rate": annual_rate,
        "start_date": start_date,
        "note_element_id": note_element_id,
      }
    )
    if day_count is not UNSET:
      field_dict["day_count"] = day_count
    if payment_frequency is not UNSET:
      field_dict["payment_frequency"] = payment_frequency
    if first_payment_date is not UNSET:
      field_dict["first_payment_date"] = first_payment_date
    if payment_amount is not UNSET:
      field_dict["payment_amount"] = payment_amount
    if interest_only is not UNSET:
      field_dict["interest_only"] = interest_only
    if maturity_date is not UNSET:
      field_dict["maturity_date"] = maturity_date
    if capitalize_interest is not UNSET:
      field_dict["capitalize_interest"] = capitalize_interest
    if current_portion_element_id is not UNSET:
      field_dict["current_portion_element_id"] = current_portion_element_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    principal = d.pop("principal")

    annual_rate = d.pop("annual_rate")

    start_date = datetime.date.fromisoformat(d.pop("start_date"))

    note_element_id = d.pop("note_element_id")

    _day_count = d.pop("day_count", UNSET)
    day_count: LoanTermsRequestDayCount | Unset
    if isinstance(_day_count, Unset):
      day_count = UNSET
    else:
      day_count = LoanTermsRequestDayCount(_day_count)

    _payment_frequency = d.pop("payment_frequency", UNSET)
    payment_frequency: LoanTermsRequestPaymentFrequency | Unset
    if isinstance(_payment_frequency, Unset):
      payment_frequency = UNSET
    else:
      payment_frequency = LoanTermsRequestPaymentFrequency(_payment_frequency)

    def _parse_first_payment_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        first_payment_date_type_0 = datetime.date.fromisoformat(data)

        return first_payment_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    first_payment_date = _parse_first_payment_date(d.pop("first_payment_date", UNSET))

    def _parse_payment_amount(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    payment_amount = _parse_payment_amount(d.pop("payment_amount", UNSET))

    interest_only = d.pop("interest_only", UNSET)

    def _parse_maturity_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        maturity_date_type_0 = datetime.date.fromisoformat(data)

        return maturity_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    maturity_date = _parse_maturity_date(d.pop("maturity_date", UNSET))

    capitalize_interest = d.pop("capitalize_interest", UNSET)

    def _parse_current_portion_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    current_portion_element_id = _parse_current_portion_element_id(
      d.pop("current_portion_element_id", UNSET)
    )

    loan_terms_request = cls(
      principal=principal,
      annual_rate=annual_rate,
      start_date=start_date,
      note_element_id=note_element_id,
      day_count=day_count,
      payment_frequency=payment_frequency,
      first_payment_date=first_payment_date,
      payment_amount=payment_amount,
      interest_only=interest_only,
      maturity_date=maturity_date,
      capitalize_interest=capitalize_interest,
      current_portion_element_id=current_portion_element_id,
    )

    loan_terms_request.additional_properties = d
    return loan_terms_request

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
