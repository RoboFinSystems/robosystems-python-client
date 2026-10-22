from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.derecognized_balance import DerecognizedBalance
  from ..models.journal_entry_response import JournalEntryResponse


T = TypeVar("T", bound="DeconsolidationResponse")


@_attrs_define
class DeconsolidationResponse:
  """A member's leaving as recorded: the draft in the consolidation entity
  its close posts, dated the first day of the month after the member's
  last.

      Attributes:
          entity_id (str): The member that left.
          entity_name (str): The member's name.
          left_on (datetime.date): The day it left, as the entity records.
          period (str): The month the entry is dated in, as YYYY-MM: the first the group reads without the member.
          consideration (int): Cents the parent received.
          gain_loss (int): Cents, a gain positive: the group's adjustment to the parent's own gain or loss on the sale, so
              the consolidated gain is the consideration less the carrying amount of what left (ASC 810).
          entry (JournalEntryResponse): The common response shape for journal entry write operations.
          derecognized (list[DerecognizedBalance] | Unset): What the consolidation entity held for the member beyond the
              eliminations its leaving reverses on their own, each taken off.
          earnings_restored (int | Unset): Cents: the member's results since it joined, credited to the group's equity as
              they leave with its books; they were the group's income. Zero for an equity-method member, whose books were
              never summed. Default: 0.
          replaced (bool | Unset): True when it replaced an earlier draft of the deconsolidation. Default: False.
  """

  entity_id: str
  entity_name: str
  left_on: datetime.date
  period: str
  consideration: int
  gain_loss: int
  entry: JournalEntryResponse
  derecognized: list[DerecognizedBalance] | Unset = UNSET
  earnings_restored: int | Unset = 0
  replaced: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    entity_name = self.entity_name

    left_on = self.left_on.isoformat()

    period = self.period

    consideration = self.consideration

    gain_loss = self.gain_loss

    entry = self.entry.to_dict()

    derecognized: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.derecognized, Unset):
      derecognized = []
      for derecognized_item_data in self.derecognized:
        derecognized_item = derecognized_item_data.to_dict()
        derecognized.append(derecognized_item)

    earnings_restored = self.earnings_restored

    replaced = self.replaced

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "entity_name": entity_name,
        "left_on": left_on,
        "period": period,
        "consideration": consideration,
        "gain_loss": gain_loss,
        "entry": entry,
      }
    )
    if derecognized is not UNSET:
      field_dict["derecognized"] = derecognized
    if earnings_restored is not UNSET:
      field_dict["earnings_restored"] = earnings_restored
    if replaced is not UNSET:
      field_dict["replaced"] = replaced

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.derecognized_balance import DerecognizedBalance
    from ..models.journal_entry_response import JournalEntryResponse

    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    entity_name = d.pop("entity_name")

    left_on = datetime.date.fromisoformat(d.pop("left_on"))

    period = d.pop("period")

    consideration = d.pop("consideration")

    gain_loss = d.pop("gain_loss")

    entry = JournalEntryResponse.from_dict(d.pop("entry"))

    _derecognized = d.pop("derecognized", UNSET)
    derecognized: list[DerecognizedBalance] | Unset = UNSET
    if _derecognized is not UNSET:
      derecognized = []
      for derecognized_item_data in _derecognized:
        derecognized_item = DerecognizedBalance.from_dict(derecognized_item_data)

        derecognized.append(derecognized_item)

    earnings_restored = d.pop("earnings_restored", UNSET)

    replaced = d.pop("replaced", UNSET)

    deconsolidation_response = cls(
      entity_id=entity_id,
      entity_name=entity_name,
      left_on=left_on,
      period=period,
      consideration=consideration,
      gain_loss=gain_loss,
      entry=entry,
      derecognized=derecognized,
      earnings_restored=earnings_restored,
      replaced=replaced,
    )

    deconsolidation_response.additional_properties = d
    return deconsolidation_response

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
