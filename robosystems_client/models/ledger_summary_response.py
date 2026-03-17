from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerSummaryResponse")


@_attrs_define
class LedgerSummaryResponse:
  """
  Attributes:
      graph_id (str):
      account_count (int):
      transaction_count (int):
      entry_count (int):
      line_item_count (int):
      earliest_transaction_date (datetime.date | None | Unset):
      latest_transaction_date (datetime.date | None | Unset):
      connection_count (int | Unset):  Default: 0.
      last_sync_at (datetime.datetime | None | Unset):
  """

  graph_id: str
  account_count: int
  transaction_count: int
  entry_count: int
  line_item_count: int
  earliest_transaction_date: datetime.date | None | Unset = UNSET
  latest_transaction_date: datetime.date | None | Unset = UNSET
  connection_count: int | Unset = 0
  last_sync_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    account_count = self.account_count

    transaction_count = self.transaction_count

    entry_count = self.entry_count

    line_item_count = self.line_item_count

    earliest_transaction_date: None | str | Unset
    if isinstance(self.earliest_transaction_date, Unset):
      earliest_transaction_date = UNSET
    elif isinstance(self.earliest_transaction_date, datetime.date):
      earliest_transaction_date = self.earliest_transaction_date.isoformat()
    else:
      earliest_transaction_date = self.earliest_transaction_date

    latest_transaction_date: None | str | Unset
    if isinstance(self.latest_transaction_date, Unset):
      latest_transaction_date = UNSET
    elif isinstance(self.latest_transaction_date, datetime.date):
      latest_transaction_date = self.latest_transaction_date.isoformat()
    else:
      latest_transaction_date = self.latest_transaction_date

    connection_count = self.connection_count

    last_sync_at: None | str | Unset
    if isinstance(self.last_sync_at, Unset):
      last_sync_at = UNSET
    elif isinstance(self.last_sync_at, datetime.datetime):
      last_sync_at = self.last_sync_at.isoformat()
    else:
      last_sync_at = self.last_sync_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "account_count": account_count,
        "transaction_count": transaction_count,
        "entry_count": entry_count,
        "line_item_count": line_item_count,
      }
    )
    if earliest_transaction_date is not UNSET:
      field_dict["earliest_transaction_date"] = earliest_transaction_date
    if latest_transaction_date is not UNSET:
      field_dict["latest_transaction_date"] = latest_transaction_date
    if connection_count is not UNSET:
      field_dict["connection_count"] = connection_count
    if last_sync_at is not UNSET:
      field_dict["last_sync_at"] = last_sync_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    account_count = d.pop("account_count")

    transaction_count = d.pop("transaction_count")

    entry_count = d.pop("entry_count")

    line_item_count = d.pop("line_item_count")

    def _parse_earliest_transaction_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        earliest_transaction_date_type_0 = isoparse(data).date()

        return earliest_transaction_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    earliest_transaction_date = _parse_earliest_transaction_date(
      d.pop("earliest_transaction_date", UNSET)
    )

    def _parse_latest_transaction_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        latest_transaction_date_type_0 = isoparse(data).date()

        return latest_transaction_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    latest_transaction_date = _parse_latest_transaction_date(
      d.pop("latest_transaction_date", UNSET)
    )

    connection_count = d.pop("connection_count", UNSET)

    def _parse_last_sync_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        last_sync_at_type_0 = isoparse(data)

        return last_sync_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    last_sync_at = _parse_last_sync_at(d.pop("last_sync_at", UNSET))

    ledger_summary_response = cls(
      graph_id=graph_id,
      account_count=account_count,
      transaction_count=transaction_count,
      entry_count=entry_count,
      line_item_count=line_item_count,
      earliest_transaction_date=earliest_transaction_date,
      latest_transaction_date=latest_transaction_date,
      connection_count=connection_count,
      last_sync_at=last_sync_at,
    )

    ledger_summary_response.additional_properties = d
    return ledger_summary_response

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
