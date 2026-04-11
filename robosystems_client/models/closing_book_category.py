from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.closing_book_item import ClosingBookItem


T = TypeVar("T", bound="ClosingBookCategory")


@_attrs_define
class ClosingBookCategory:
  """
  Attributes:
      label (str):
      items (list[ClosingBookItem]):
  """

  label: str
  items: list[ClosingBookItem]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    label = self.label

    items = []
    for items_item_data in self.items:
      items_item = items_item_data.to_dict()
      items.append(items_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "label": label,
        "items": items,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.closing_book_item import ClosingBookItem

    d = dict(src_dict)
    label = d.pop("label")

    items = []
    _items = d.pop("items")
    for items_item_data in _items:
      items_item = ClosingBookItem.from_dict(items_item_data)

      items.append(items_item)

    closing_book_category = cls(
      label=label,
      items=items,
    )

    closing_book_category.additional_properties = d
    return closing_book_category

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
