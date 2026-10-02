from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.reconciliation_summary import ReconciliationSummary


T = TypeVar("T", bound="ReconciliationListResponse")


@_attrs_define
class ReconciliationListResponse:
  """Every reconciliation's standing for one period.

  Attributes:
      period (str): The period, as YYYY-MM.
      as_of (datetime.date): The period's last day.
      reconciliations (list[ReconciliationSummary]): One entry per reconciliation block, oldest block first.
      notes (list[str] | Unset): What a refresh could not compare, such as a check skipped because its source is no
          longer connected. Empty on a plain read.
  """

  period: str
  as_of: datetime.date
  reconciliations: list[ReconciliationSummary]
  notes: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period = self.period

    as_of = self.as_of.isoformat()

    reconciliations = []
    for reconciliations_item_data in self.reconciliations:
      reconciliations_item = reconciliations_item_data.to_dict()
      reconciliations.append(reconciliations_item)

    notes: list[str] | Unset = UNSET
    if not isinstance(self.notes, Unset):
      notes = self.notes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
        "as_of": as_of,
        "reconciliations": reconciliations,
      }
    )
    if notes is not UNSET:
      field_dict["notes"] = notes

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.reconciliation_summary import ReconciliationSummary

    d = dict(src_dict)
    period = d.pop("period")

    as_of = datetime.date.fromisoformat(d.pop("as_of"))

    reconciliations = []
    _reconciliations = d.pop("reconciliations")
    for reconciliations_item_data in _reconciliations:
      reconciliations_item = ReconciliationSummary.from_dict(reconciliations_item_data)

      reconciliations.append(reconciliations_item)

    notes = cast(list[str], d.pop("notes", UNSET))

    reconciliation_list_response = cls(
      period=period,
      as_of=as_of,
      reconciliations=reconciliations,
      notes=notes,
    )

    reconciliation_list_response.additional_properties = d
    return reconciliation_list_response

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
