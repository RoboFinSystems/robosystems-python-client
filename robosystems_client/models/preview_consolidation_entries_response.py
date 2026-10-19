from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.consolidation_proposal import ConsolidationProposal
  from ..models.consolidation_reconciling_item import ConsolidationReconcilingItem
  from ..models.consolidation_residual import ConsolidationResidual


T = TypeVar("T", bound="PreviewConsolidationEntriesResponse")


@_attrs_define
class PreviewConsolidationEntriesResponse:
  """The consolidating entries a month needs, computed from the books.

  Attributes:
      period (str): The month, as YYYY-MM.
      period_start (datetime.date): The month's first day.
      period_end (datetime.date): The month's last day.
      consolidation_entity_id (str): The entity the entries post in.
      up_to_date (bool): True when nothing is withheld or left out and the consolidation entity holds what the month
          needs, posted or in the month's drafts (then `proposals` lists what the drafts hold). A closed month is up to
          date as posted; read `closed` first.
      proposals (list[ConsolidationProposal] | Unset): The entries to post; empty when the month is up to date.
      residuals (list[ConsolidationResidual] | Unset): Differences withheld from the proposals until explained.
      reconciling_items (list[ConsolidationReconcilingItem] | Unset): Intercompany figures the two sides do not agree
          on.
      notes (list[str] | Unset): Anything the engine left out, and why.
      closed (bool | Unset): True when the consolidation entity has closed the month: its entries are as posted, and
          nothing is recomputed. Default: False.
      drafted_entry_ids (list[str] | Unset): The month's drafts propose-consolidation-entries wrote, waiting for the
          consolidation entity's close to post them.
  """

  period: str
  period_start: datetime.date
  period_end: datetime.date
  consolidation_entity_id: str
  up_to_date: bool
  proposals: list[ConsolidationProposal] | Unset = UNSET
  residuals: list[ConsolidationResidual] | Unset = UNSET
  reconciling_items: list[ConsolidationReconcilingItem] | Unset = UNSET
  notes: list[str] | Unset = UNSET
  closed: bool | Unset = False
  drafted_entry_ids: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period = self.period

    period_start = self.period_start.isoformat()

    period_end = self.period_end.isoformat()

    consolidation_entity_id = self.consolidation_entity_id

    up_to_date = self.up_to_date

    proposals: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.proposals, Unset):
      proposals = []
      for proposals_item_data in self.proposals:
        proposals_item = proposals_item_data.to_dict()
        proposals.append(proposals_item)

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

    closed = self.closed

    drafted_entry_ids: list[str] | Unset = UNSET
    if not isinstance(self.drafted_entry_ids, Unset):
      drafted_entry_ids = self.drafted_entry_ids

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
        "period_start": period_start,
        "period_end": period_end,
        "consolidation_entity_id": consolidation_entity_id,
        "up_to_date": up_to_date,
      }
    )
    if proposals is not UNSET:
      field_dict["proposals"] = proposals
    if residuals is not UNSET:
      field_dict["residuals"] = residuals
    if reconciling_items is not UNSET:
      field_dict["reconciling_items"] = reconciling_items
    if notes is not UNSET:
      field_dict["notes"] = notes
    if closed is not UNSET:
      field_dict["closed"] = closed
    if drafted_entry_ids is not UNSET:
      field_dict["drafted_entry_ids"] = drafted_entry_ids

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.consolidation_proposal import ConsolidationProposal
    from ..models.consolidation_reconciling_item import ConsolidationReconcilingItem
    from ..models.consolidation_residual import ConsolidationResidual

    d = dict(src_dict)
    period = d.pop("period")

    period_start = datetime.date.fromisoformat(d.pop("period_start"))

    period_end = datetime.date.fromisoformat(d.pop("period_end"))

    consolidation_entity_id = d.pop("consolidation_entity_id")

    up_to_date = d.pop("up_to_date")

    _proposals = d.pop("proposals", UNSET)
    proposals: list[ConsolidationProposal] | Unset = UNSET
    if _proposals is not UNSET:
      proposals = []
      for proposals_item_data in _proposals:
        proposals_item = ConsolidationProposal.from_dict(proposals_item_data)

        proposals.append(proposals_item)

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

    closed = d.pop("closed", UNSET)

    drafted_entry_ids = cast(list[str], d.pop("drafted_entry_ids", UNSET))

    preview_consolidation_entries_response = cls(
      period=period,
      period_start=period_start,
      period_end=period_end,
      consolidation_entity_id=consolidation_entity_id,
      up_to_date=up_to_date,
      proposals=proposals,
      residuals=residuals,
      reconciling_items=reconciling_items,
      notes=notes,
      closed=closed,
      drafted_entry_ids=drafted_entry_ids,
    )

    preview_consolidation_entries_response.additional_properties = d
    return preview_consolidation_entries_response

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
