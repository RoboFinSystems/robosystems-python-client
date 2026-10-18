from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.consolidation_reconciling_item import ConsolidationReconcilingItem
  from ..models.consolidation_residual import ConsolidationResidual
  from ..models.journal_entry_response import JournalEntryResponse


T = TypeVar("T", bound="ProposeConsolidationEntriesResponse")


@_attrs_define
class ProposeConsolidationEntriesResponse:
  """The consolidating entries drafted for a month.

  Attributes:
      period (str): The month, as YYYY-MM.
      consolidation_entity_id (str): The entity the drafts are in.
      closed (bool | Unset): True when the month is closed and nothing was drafted. Default: False.
      entries (list[JournalEntryResponse] | Unset): The drafts written; the consolidation entity's close posts them.
      replaced (int | Unset): Earlier drafts of this month's entries, replaced by these. Default: 0.
      residuals (list[ConsolidationResidual] | Unset): Differences withheld from the drafts until explained.
      reconciling_items (list[ConsolidationReconcilingItem] | Unset): Intercompany figures the two sides do not agree
          on.
      notes (list[str] | Unset): Anything the engine left out, and why.
  """

  period: str
  consolidation_entity_id: str
  closed: bool | Unset = False
  entries: list[JournalEntryResponse] | Unset = UNSET
  replaced: int | Unset = 0
  residuals: list[ConsolidationResidual] | Unset = UNSET
  reconciling_items: list[ConsolidationReconcilingItem] | Unset = UNSET
  notes: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period = self.period

    consolidation_entity_id = self.consolidation_entity_id

    closed = self.closed

    entries: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.entries, Unset):
      entries = []
      for entries_item_data in self.entries:
        entries_item = entries_item_data.to_dict()
        entries.append(entries_item)

    replaced = self.replaced

    residuals: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.residuals, Unset):
      residuals = []
      for residuals_item_data in self.residuals:
        residuals_item = residuals_item_data.to_dict()
        residuals.append(residuals_item)

    reconciling_items: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.reconciling_items, Unset):
      reconciling_items = []
      for reconciling_items_item_data in self.reconciling_items:
        reconciling_items_item = reconciling_items_item_data.to_dict()
        reconciling_items.append(reconciling_items_item)

    notes: list[str] | Unset = UNSET
    if not isinstance(self.notes, Unset):
      notes = self.notes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
        "consolidation_entity_id": consolidation_entity_id,
      }
    )
    if closed is not UNSET:
      field_dict["closed"] = closed
    if entries is not UNSET:
      field_dict["entries"] = entries
    if replaced is not UNSET:
      field_dict["replaced"] = replaced
    if residuals is not UNSET:
      field_dict["residuals"] = residuals
    if reconciling_items is not UNSET:
      field_dict["reconciling_items"] = reconciling_items
    if notes is not UNSET:
      field_dict["notes"] = notes

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.consolidation_reconciling_item import ConsolidationReconcilingItem
    from ..models.consolidation_residual import ConsolidationResidual
    from ..models.journal_entry_response import JournalEntryResponse

    d = dict(src_dict)
    period = d.pop("period")

    consolidation_entity_id = d.pop("consolidation_entity_id")

    closed = d.pop("closed", UNSET)

    _entries = d.pop("entries", UNSET)
    entries: list[JournalEntryResponse] | Unset = UNSET
    if _entries is not UNSET:
      entries = []
      for entries_item_data in _entries:
        entries_item = JournalEntryResponse.from_dict(entries_item_data)

        entries.append(entries_item)

    replaced = d.pop("replaced", UNSET)

    _residuals = d.pop("residuals", UNSET)
    residuals: list[ConsolidationResidual] | Unset = UNSET
    if _residuals is not UNSET:
      residuals = []
      for residuals_item_data in _residuals:
        residuals_item = ConsolidationResidual.from_dict(residuals_item_data)

        residuals.append(residuals_item)

    _reconciling_items = d.pop("reconciling_items", UNSET)
    reconciling_items: list[ConsolidationReconcilingItem] | Unset = UNSET
    if _reconciling_items is not UNSET:
      reconciling_items = []
      for reconciling_items_item_data in _reconciling_items:
        reconciling_items_item = ConsolidationReconcilingItem.from_dict(
          reconciling_items_item_data
        )

        reconciling_items.append(reconciling_items_item)

    notes = cast(list[str], d.pop("notes", UNSET))

    propose_consolidation_entries_response = cls(
      period=period,
      consolidation_entity_id=consolidation_entity_id,
      closed=closed,
      entries=entries,
      replaced=replaced,
      residuals=residuals,
      reconciling_items=reconciling_items,
      notes=notes,
    )

    propose_consolidation_entries_response.additional_properties = d
    return propose_consolidation_entries_response

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
