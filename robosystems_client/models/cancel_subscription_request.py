from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelSubscriptionRequest")


@_attrs_define
class CancelSubscriptionRequest:
  """Request to cancel a subscription.

  Default behavior cancels at period end (soft cancel). Pass `immediate=True`
  to terminate the subscription right away — this requires `confirm` to equal
  the subscription's `resource_id` (e.g. the graph_id) as a guard against
  accidental destructive calls.

      Attributes:
          immediate (bool | Unset): If true, cancel immediately and trigger fast-path deprovisioning of the underlying
              resource (within ~10 minutes). If false (default), cancel at the end of the current billing period. Default:
              False.
          confirm (None | str | Unset): Required when immediate=True. Must equal the subscription's resource_id (e.g.
              graph_id) to confirm intent.
  """

  immediate: bool | Unset = False
  confirm: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    immediate = self.immediate

    confirm: None | str | Unset
    if isinstance(self.confirm, Unset):
      confirm = UNSET
    else:
      confirm = self.confirm

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if immediate is not UNSET:
      field_dict["immediate"] = immediate
    if confirm is not UNSET:
      field_dict["confirm"] = confirm

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    immediate = d.pop("immediate", UNSET)

    def _parse_confirm(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    confirm = _parse_confirm(d.pop("confirm", UNSET))

    cancel_subscription_request = cls(
      immediate=immediate,
      confirm=confirm,
    )

    cancel_subscription_request.additional_properties = d
    return cancel_subscription_request

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
