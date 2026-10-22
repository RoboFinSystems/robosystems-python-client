from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.journal_entry_response import JournalEntryResponse


T = TypeVar("T", bound="OwnershipChangeResponse")


@_attrs_define
class OwnershipChangeResponse:
  """A change in the parent's share of a member as recorded: the draft in
  the consolidation entity its close posts.

      Attributes:
          entity_id (str): The member.
          entity_name (str): The member's name.
          period (str): The first month the new share holds.
          from_pct (float): The parent's share the month before.
          to_pct (float): The parent's share from `period`.
          consideration (int): Cents paid to the outside owners.
          book_value (int): Cents: the share bought of the member's capital, which the investment elimination moves from
              the outside owners to the parent.
          earnings_transferred (int): Cents: the share bought of the member's results since it joined, moved from the
              outside owners' interest to the parent.
          equity_adjustment (int): Cents taken from the parent's equity: the price above the carrying amount of what was
              bought (negative when it paid less).
          entry (JournalEntryResponse): The common response shape for journal entry write operations.
          premium_transferred (int | Unset): Cents: the share bought of the outside owners' interest beyond their share of
              book value (from the acquisition at fair value, or its step-ups), moved to the parent. Default: 0.
          replaced (bool | Unset): True when it replaced an earlier draft for the month. Default: False.
  """

  entity_id: str
  entity_name: str
  period: str
  from_pct: float
  to_pct: float
  consideration: int
  book_value: int
  earnings_transferred: int
  equity_adjustment: int
  entry: JournalEntryResponse
  premium_transferred: int | Unset = 0
  replaced: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    entity_name = self.entity_name

    period = self.period

    from_pct = self.from_pct

    to_pct = self.to_pct

    consideration = self.consideration

    book_value = self.book_value

    earnings_transferred = self.earnings_transferred

    equity_adjustment = self.equity_adjustment

    entry = self.entry.to_dict()

    premium_transferred = self.premium_transferred

    replaced = self.replaced

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "entity_name": entity_name,
        "period": period,
        "from_pct": from_pct,
        "to_pct": to_pct,
        "consideration": consideration,
        "book_value": book_value,
        "earnings_transferred": earnings_transferred,
        "equity_adjustment": equity_adjustment,
        "entry": entry,
      }
    )
    if premium_transferred is not UNSET:
      field_dict["premium_transferred"] = premium_transferred
    if replaced is not UNSET:
      field_dict["replaced"] = replaced

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.journal_entry_response import JournalEntryResponse

    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    entity_name = d.pop("entity_name")

    period = d.pop("period")

    from_pct = d.pop("from_pct")

    to_pct = d.pop("to_pct")

    consideration = d.pop("consideration")

    book_value = d.pop("book_value")

    earnings_transferred = d.pop("earnings_transferred")

    equity_adjustment = d.pop("equity_adjustment")

    entry = JournalEntryResponse.from_dict(d.pop("entry"))

    premium_transferred = d.pop("premium_transferred", UNSET)

    replaced = d.pop("replaced", UNSET)

    ownership_change_response = cls(
      entity_id=entity_id,
      entity_name=entity_name,
      period=period,
      from_pct=from_pct,
      to_pct=to_pct,
      consideration=consideration,
      book_value=book_value,
      earnings_transferred=earnings_transferred,
      equity_adjustment=equity_adjustment,
      entry=entry,
      premium_transferred=premium_transferred,
      replaced=replaced,
    )

    ownership_change_response.additional_properties = d
    return ownership_change_response

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
