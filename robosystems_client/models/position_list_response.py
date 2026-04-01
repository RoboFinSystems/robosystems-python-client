from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.pagination_info import PaginationInfo
  from ..models.position_response import PositionResponse


T = TypeVar("T", bound="PositionListResponse")


@_attrs_define
class PositionListResponse:
  """
  Attributes:
      positions (list[PositionResponse]):
      pagination (PaginationInfo): Pagination information for list responses. Example: {'has_more': True, 'limit': 20,
          'offset': 0, 'total': 100}.
  """

  positions: list[PositionResponse]
  pagination: PaginationInfo
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    positions = []
    for positions_item_data in self.positions:
      positions_item = positions_item_data.to_dict()
      positions.append(positions_item)

    pagination = self.pagination.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "positions": positions,
        "pagination": pagination,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.pagination_info import PaginationInfo
    from ..models.position_response import PositionResponse

    d = dict(src_dict)
    positions = []
    _positions = d.pop("positions")
    for positions_item_data in _positions:
      positions_item = PositionResponse.from_dict(positions_item_data)

      positions.append(positions_item)

    pagination = PaginationInfo.from_dict(d.pop("pagination"))

    position_list_response = cls(
      positions=positions,
      pagination=pagination,
    )

    position_list_response.additional_properties = d
    return position_list_response

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
