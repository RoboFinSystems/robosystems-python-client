from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.invoice import Invoice


T = TypeVar("T", bound="InvoicesResponse")


@_attrs_define
class InvoicesResponse:
  """Response for invoice list.

  Attributes:
      invoices (list['Invoice']): List of invoices
      total_count (int): Total number of invoices
      has_more (bool): Whether more invoices are available
  """

  invoices: list["Invoice"]
  total_count: int
  has_more: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    invoices = []
    for invoices_item_data in self.invoices:
      invoices_item = invoices_item_data.to_dict()
      invoices.append(invoices_item)

    total_count = self.total_count

    has_more = self.has_more

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "invoices": invoices,
        "total_count": total_count,
        "has_more": has_more,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.invoice import Invoice

    d = dict(src_dict)
    invoices = []
    _invoices = d.pop("invoices")
    for invoices_item_data in _invoices:
      invoices_item = Invoice.from_dict(invoices_item_data)

      invoices.append(invoices_item)

    total_count = d.pop("total_count")

    has_more = d.pop("has_more")

    invoices_response = cls(
      invoices=invoices,
      total_count=total_count,
      has_more=has_more,
    )

    invoices_response.additional_properties = d
    return invoices_response

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
