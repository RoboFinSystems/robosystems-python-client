from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.consolidation_proposal_adjustment_kind import (
  ConsolidationProposalAdjustmentKind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.consolidation_proposal_line import ConsolidationProposalLine


T = TypeVar("T", bound="ConsolidationProposal")


@_attrs_define
class ConsolidationProposal:
  """One consolidating entry the month needs: the difference between the
  balance this kind of adjustment should hold for the member at the month
  end and what the consolidation entity already holds for it.

      Attributes:
          adjustment_kind (ConsolidationProposalAdjustmentKind): What the entry adjusts.
          adjusts_entity_id (str): The entity whose figures the entry adjusts.
          adjusts_entity_name (str): That entity's name.
          posting_date (datetime.date): The month's last day; for an opening, the eve of the consolidation entity's first
              month.
          memo (str): The entry's memo.
          basis (str): How the amounts were computed.
          lines (list[ConsolidationProposalLine]): The entry's lines; they balance.
          opening (bool | Unset): Part of the consolidation entity's opening balance: what the members' history before the
              group's first month already needed eliminated, so the consolidated statements open on it rather than move by it.
              Proposing records it, posted, replacing the earlier one until the first close. Default: False.
  """

  adjustment_kind: ConsolidationProposalAdjustmentKind
  adjusts_entity_id: str
  adjusts_entity_name: str
  posting_date: datetime.date
  memo: str
  basis: str
  lines: list[ConsolidationProposalLine]
  opening: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    adjustment_kind = self.adjustment_kind.value

    adjusts_entity_id = self.adjusts_entity_id

    adjusts_entity_name = self.adjusts_entity_name

    posting_date = self.posting_date.isoformat()

    memo = self.memo

    basis = self.basis

    lines = []
    for lines_item_data in self.lines:
      lines_item = lines_item_data.to_dict()
      lines.append(lines_item)

    opening = self.opening

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "adjustment_kind": adjustment_kind,
        "adjusts_entity_id": adjusts_entity_id,
        "adjusts_entity_name": adjusts_entity_name,
        "posting_date": posting_date,
        "memo": memo,
        "basis": basis,
        "lines": lines,
      }
    )
    if opening is not UNSET:
      field_dict["opening"] = opening

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.consolidation_proposal_line import ConsolidationProposalLine

    d = dict(src_dict)
    adjustment_kind = ConsolidationProposalAdjustmentKind(d.pop("adjustment_kind"))

    adjusts_entity_id = d.pop("adjusts_entity_id")

    adjusts_entity_name = d.pop("adjusts_entity_name")

    posting_date = datetime.date.fromisoformat(d.pop("posting_date"))

    memo = d.pop("memo")

    basis = d.pop("basis")

    lines = []
    _lines = d.pop("lines")
    for lines_item_data in _lines:
      lines_item = ConsolidationProposalLine.from_dict(lines_item_data)

      lines.append(lines_item)

    opening = d.pop("opening", UNSET)

    consolidation_proposal = cls(
      adjustment_kind=adjustment_kind,
      adjusts_entity_id=adjusts_entity_id,
      adjusts_entity_name=adjusts_entity_name,
      posting_date=posting_date,
      memo=memo,
      basis=basis,
      lines=lines,
      opening=opening,
    )

    consolidation_proposal.additional_properties = d
    return consolidation_proposal

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
