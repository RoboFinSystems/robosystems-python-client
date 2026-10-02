from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reconciliation_preview_response_method import (
  ReconciliationPreviewResponseMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.reconciliation_row import ReconciliationRow


T = TypeVar("T", bound="ReconciliationPreviewResponse")


@_attrs_define
class ReconciliationPreviewResponse:
  """The comparison for one period end. Nothing is written.

  Attributes:
      period (str):
      as_of (datetime.date): The period's last day.
      fiscal_year_start (datetime.date): Income-statement accounts are compared from this date to `as_of`.
      method (ReconciliationPreviewResponseMethod):
      source (str): The system the independent side was read from.
      accounts_compared (int): Accounts with a balance on either side; zero on both is left out.
      accounts_tied (int):
      accounts_different (int): Every account that does not tie, whatever the reason.
      total_difference (float): Sum of the absolute differences across accounts, not a net figure: one missing
          transaction counts on each account it touches.
      rows (list[ReconciliationRow]): Accounts that do not tie, largest difference first; tied accounts follow when
          `include_tied` is set.
      report_basis (None | str | Unset): Accounting basis the source reported on.
      last_sync_at (datetime.datetime | None | Unset): When the source was last synced. A difference on a sync older
          than the period end may be activity not yet synced, not a fault in the mirror.
      notes (list[str] | Unset): How the comparison was made, and anything that qualifies it.
  """

  period: str
  as_of: datetime.date
  fiscal_year_start: datetime.date
  method: ReconciliationPreviewResponseMethod
  source: str
  accounts_compared: int
  accounts_tied: int
  accounts_different: int
  total_difference: float
  rows: list[ReconciliationRow]
  report_basis: None | str | Unset = UNSET
  last_sync_at: datetime.datetime | None | Unset = UNSET
  notes: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period = self.period

    as_of = self.as_of.isoformat()

    fiscal_year_start = self.fiscal_year_start.isoformat()

    method = self.method.value

    source = self.source

    accounts_compared = self.accounts_compared

    accounts_tied = self.accounts_tied

    accounts_different = self.accounts_different

    total_difference = self.total_difference

    rows = []
    for rows_item_data in self.rows:
      rows_item = rows_item_data.to_dict()
      rows.append(rows_item)

    report_basis: None | str | Unset
    if isinstance(self.report_basis, Unset):
      report_basis = UNSET
    else:
      report_basis = self.report_basis

    last_sync_at: None | str | Unset
    if isinstance(self.last_sync_at, Unset):
      last_sync_at = UNSET
    elif isinstance(self.last_sync_at, datetime.datetime):
      last_sync_at = self.last_sync_at.isoformat()
    else:
      last_sync_at = self.last_sync_at

    notes: list[str] | Unset = UNSET
    if not isinstance(self.notes, Unset):
      notes = self.notes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
        "as_of": as_of,
        "fiscal_year_start": fiscal_year_start,
        "method": method,
        "source": source,
        "accounts_compared": accounts_compared,
        "accounts_tied": accounts_tied,
        "accounts_different": accounts_different,
        "total_difference": total_difference,
        "rows": rows,
      }
    )
    if report_basis is not UNSET:
      field_dict["report_basis"] = report_basis
    if last_sync_at is not UNSET:
      field_dict["last_sync_at"] = last_sync_at
    if notes is not UNSET:
      field_dict["notes"] = notes

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.reconciliation_row import ReconciliationRow

    d = dict(src_dict)
    period = d.pop("period")

    as_of = datetime.date.fromisoformat(d.pop("as_of"))

    fiscal_year_start = datetime.date.fromisoformat(d.pop("fiscal_year_start"))

    method = ReconciliationPreviewResponseMethod(d.pop("method"))

    source = d.pop("source")

    accounts_compared = d.pop("accounts_compared")

    accounts_tied = d.pop("accounts_tied")

    accounts_different = d.pop("accounts_different")

    total_difference = d.pop("total_difference")

    rows = []
    _rows = d.pop("rows")
    for rows_item_data in _rows:
      rows_item = ReconciliationRow.from_dict(rows_item_data)

      rows.append(rows_item)

    def _parse_report_basis(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    report_basis = _parse_report_basis(d.pop("report_basis", UNSET))

    def _parse_last_sync_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        last_sync_at_type_0 = datetime.datetime.fromisoformat(data)

        return last_sync_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    last_sync_at = _parse_last_sync_at(d.pop("last_sync_at", UNSET))

    notes = cast(list[str], d.pop("notes", UNSET))

    reconciliation_preview_response = cls(
      period=period,
      as_of=as_of,
      fiscal_year_start=fiscal_year_start,
      method=method,
      source=source,
      accounts_compared=accounts_compared,
      accounts_tied=accounts_tied,
      accounts_different=accounts_different,
      total_difference=total_difference,
      rows=rows,
      report_basis=report_basis,
      last_sync_at=last_sync_at,
      notes=notes,
    )

    reconciliation_preview_response.additional_properties = d
    return reconciliation_preview_response

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
