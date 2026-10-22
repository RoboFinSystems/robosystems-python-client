from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.journal_entry_response import JournalEntryResponse


T = TypeVar("T", bound="AcquisitionResponse")


@_attrs_define
class AcquisitionResponse:
  """A member's acquisition as recorded: the draft in the consolidation
  entity its close posts.

      Attributes:
          entity_id (str): The member.
          entity_name (str): The member's name.
          joined_on (datetime.date): When it joined the group.
          equity_at_acquisition (int): Cents: the member's equity in its opening balance.
          parent_share (int): Cents: the parent's share of that equity.
          consideration (int): Cents paid to the sellers.
          excess (int): Cents: consideration less the parent's share of the equity.
          goodwill (int): Cents of goodwill; negative for a bargain purchase gain.
          entry (JournalEntryResponse): The common response shape for journal entry write operations.
          noncontrolling_interest (int | Unset): Cents added to the outside owners' interest beyond their share of the
              member's book equity. Default: 0.
          replaced (bool | Unset): True when it replaced an earlier draft of the acquisition. Default: False.
  """

  entity_id: str
  entity_name: str
  joined_on: datetime.date
  equity_at_acquisition: int
  parent_share: int
  consideration: int
  excess: int
  goodwill: int
  entry: JournalEntryResponse
  noncontrolling_interest: int | Unset = 0
  replaced: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    entity_name = self.entity_name

    joined_on = self.joined_on.isoformat()

    equity_at_acquisition = self.equity_at_acquisition

    parent_share = self.parent_share

    consideration = self.consideration

    excess = self.excess

    goodwill = self.goodwill

    entry = self.entry.to_dict()

    noncontrolling_interest = self.noncontrolling_interest

    replaced = self.replaced

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "entity_name": entity_name,
        "joined_on": joined_on,
        "equity_at_acquisition": equity_at_acquisition,
        "parent_share": parent_share,
        "consideration": consideration,
        "excess": excess,
        "goodwill": goodwill,
        "entry": entry,
      }
    )
    if noncontrolling_interest is not UNSET:
      field_dict["noncontrolling_interest"] = noncontrolling_interest
    if replaced is not UNSET:
      field_dict["replaced"] = replaced

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.journal_entry_response import JournalEntryResponse

    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    entity_name = d.pop("entity_name")

    joined_on = datetime.date.fromisoformat(d.pop("joined_on"))

    equity_at_acquisition = d.pop("equity_at_acquisition")

    parent_share = d.pop("parent_share")

    consideration = d.pop("consideration")

    excess = d.pop("excess")

    goodwill = d.pop("goodwill")

    entry = JournalEntryResponse.from_dict(d.pop("entry"))

    noncontrolling_interest = d.pop("noncontrolling_interest", UNSET)

    replaced = d.pop("replaced", UNSET)

    acquisition_response = cls(
      entity_id=entity_id,
      entity_name=entity_name,
      joined_on=joined_on,
      equity_at_acquisition=equity_at_acquisition,
      parent_share=parent_share,
      consideration=consideration,
      excess=excess,
      goodwill=goodwill,
      entry=entry,
      noncontrolling_interest=noncontrolling_interest,
      replaced=replaced,
    )

    acquisition_response.additional_properties = d
    return acquisition_response

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
