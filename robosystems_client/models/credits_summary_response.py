from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.add_on_credit_info import AddOnCreditInfo
  from ..models.credits_summary_response_credits_by_addon_item import (
    CreditsSummaryResponseCreditsByAddonItem,
  )


T = TypeVar("T", bound="CreditsSummaryResponse")


@_attrs_define
class CreditsSummaryResponse:
  """Response for credits summary.

  Attributes:
      add_ons (list['AddOnCreditInfo']): Credits breakdown by add-on
      total_credits (float): Total credits remaining across all subscriptions
      addon_count (int): Number of active add-ons
      credits_by_addon (Union[Unset, list['CreditsSummaryResponseCreditsByAddonItem']]): Legacy field - Credits
          breakdown by add-on
  """

  add_ons: list["AddOnCreditInfo"]
  total_credits: float
  addon_count: int
  credits_by_addon: Union[Unset, list["CreditsSummaryResponseCreditsByAddonItem"]] = (
    UNSET
  )
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    add_ons = []
    for add_ons_item_data in self.add_ons:
      add_ons_item = add_ons_item_data.to_dict()
      add_ons.append(add_ons_item)

    total_credits = self.total_credits

    addon_count = self.addon_count

    credits_by_addon: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(self.credits_by_addon, Unset):
      credits_by_addon = []
      for credits_by_addon_item_data in self.credits_by_addon:
        credits_by_addon_item = credits_by_addon_item_data.to_dict()
        credits_by_addon.append(credits_by_addon_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "add_ons": add_ons,
        "total_credits": total_credits,
        "addon_count": addon_count,
      }
    )
    if credits_by_addon is not UNSET:
      field_dict["credits_by_addon"] = credits_by_addon

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.add_on_credit_info import AddOnCreditInfo
    from ..models.credits_summary_response_credits_by_addon_item import (
      CreditsSummaryResponseCreditsByAddonItem,
    )

    d = dict(src_dict)
    add_ons = []
    _add_ons = d.pop("add_ons")
    for add_ons_item_data in _add_ons:
      add_ons_item = AddOnCreditInfo.from_dict(add_ons_item_data)

      add_ons.append(add_ons_item)

    total_credits = d.pop("total_credits")

    addon_count = d.pop("addon_count")

    credits_by_addon = []
    _credits_by_addon = d.pop("credits_by_addon", UNSET)
    for credits_by_addon_item_data in _credits_by_addon or []:
      credits_by_addon_item = CreditsSummaryResponseCreditsByAddonItem.from_dict(
        credits_by_addon_item_data
      )

      credits_by_addon.append(credits_by_addon_item)

    credits_summary_response = cls(
      add_ons=add_ons,
      total_credits=total_credits,
      addon_count=addon_count,
      credits_by_addon=credits_by_addon,
    )

    credits_summary_response.additional_properties = d
    return credits_summary_response

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
