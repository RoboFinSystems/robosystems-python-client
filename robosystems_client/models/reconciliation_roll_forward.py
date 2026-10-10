from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconciliationRollForward")


@_attrs_define
class ReconciliationRollForward:
  """A statement carried from its ending date to the period's last day on a
  bank-fed account, where every line the feed brought is the bank's own.

      Attributes:
          statement_as_of (datetime.date): The statement's ending date.
          through (datetime.date): The period's last day.
          bank_lines (int): Booked feed lines dated after the statement, to the period end.
          bank_activity (float): Their net effect on the account, debit-positive.
          bank_balance (float): The statement balance carried to the period end by those lines: what the bank held then,
              debit-positive.
          ledger_balance (float): The ledger's balance at the period end, as the close will leave it, debit-positive.
          outstanding (float): Ledger lines not from the feed and dated on or before the period end, net: the ledger minus
              the carried bank balance.
          feed_balance (float | None | Unset): A cross-check, never the figure reconciled: the bank feed's own balance
              from the first reading on or after the period end, less the booked feed lines between the period end and that
              reading. Null when the feed has no reading within ten days.
          feed_balance_read_on (datetime.date | None | Unset): The day of the feed reading `feed_balance` starts from.
  """

  statement_as_of: datetime.date
  through: datetime.date
  bank_lines: int
  bank_activity: float
  bank_balance: float
  ledger_balance: float
  outstanding: float
  feed_balance: float | None | Unset = UNSET
  feed_balance_read_on: datetime.date | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    statement_as_of = self.statement_as_of.isoformat()

    through = self.through.isoformat()

    bank_lines = self.bank_lines

    bank_activity = self.bank_activity

    bank_balance = self.bank_balance

    ledger_balance = self.ledger_balance

    outstanding = self.outstanding

    feed_balance: float | None | Unset
    if isinstance(self.feed_balance, Unset):
      feed_balance = UNSET
    else:
      feed_balance = self.feed_balance

    feed_balance_read_on: None | str | Unset
    if isinstance(self.feed_balance_read_on, Unset):
      feed_balance_read_on = UNSET
    elif isinstance(self.feed_balance_read_on, datetime.date):
      feed_balance_read_on = self.feed_balance_read_on.isoformat()
    else:
      feed_balance_read_on = self.feed_balance_read_on

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "statement_as_of": statement_as_of,
        "through": through,
        "bank_lines": bank_lines,
        "bank_activity": bank_activity,
        "bank_balance": bank_balance,
        "ledger_balance": ledger_balance,
        "outstanding": outstanding,
      }
    )
    if feed_balance is not UNSET:
      field_dict["feed_balance"] = feed_balance
    if feed_balance_read_on is not UNSET:
      field_dict["feed_balance_read_on"] = feed_balance_read_on

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    statement_as_of = datetime.date.fromisoformat(d.pop("statement_as_of"))

    through = datetime.date.fromisoformat(d.pop("through"))

    bank_lines = d.pop("bank_lines")

    bank_activity = d.pop("bank_activity")

    bank_balance = d.pop("bank_balance")

    ledger_balance = d.pop("ledger_balance")

    outstanding = d.pop("outstanding")

    def _parse_feed_balance(data: object) -> float | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(float | None | Unset, data)

    feed_balance = _parse_feed_balance(d.pop("feed_balance", UNSET))

    def _parse_feed_balance_read_on(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        feed_balance_read_on_type_0 = datetime.date.fromisoformat(data)

        return feed_balance_read_on_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    feed_balance_read_on = _parse_feed_balance_read_on(
      d.pop("feed_balance_read_on", UNSET)
    )

    reconciliation_roll_forward = cls(
      statement_as_of=statement_as_of,
      through=through,
      bank_lines=bank_lines,
      bank_activity=bank_activity,
      bank_balance=bank_balance,
      ledger_balance=ledger_balance,
      outstanding=outstanding,
      feed_balance=feed_balance,
      feed_balance_read_on=feed_balance_read_on,
    )

    reconciliation_roll_forward.additional_properties = d
    return reconciliation_roll_forward

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
