from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.holding_response import HoldingResponse


T = TypeVar("T", bound="HoldingsListResponse")


@_attrs_define
class HoldingsListResponse:
  """
  Attributes:
      holdings (list[HoldingResponse]):
      total_entities (int):
      total_positions (int):
  """

  holdings: list[HoldingResponse]
  total_entities: int
  total_positions: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    holdings = []
    for holdings_item_data in self.holdings:
      holdings_item = holdings_item_data.to_dict()
      holdings.append(holdings_item)

    total_entities = self.total_entities

    total_positions = self.total_positions

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "holdings": holdings,
        "total_entities": total_entities,
        "total_positions": total_positions,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.holding_response import HoldingResponse

    d = dict(src_dict)
    holdings = []
    _holdings = d.pop("holdings")
    for holdings_item_data in _holdings:
      holdings_item = HoldingResponse.from_dict(holdings_item_data)

      holdings.append(holdings_item)

    total_entities = d.pop("total_entities")

    total_positions = d.pop("total_positions")

    holdings_list_response = cls(
      holdings=holdings,
      total_entities=total_entities,
      total_positions=total_positions,
    )

    holdings_list_response.additional_properties = d
    return holdings_list_response

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
