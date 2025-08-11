from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CancellationResponse")


@_attrs_define
class CancellationResponse:
  """Response for subscription cancellation.

  Attributes:
      message (str): Cancellation confirmation message
      subscription_id (str): ID of the cancelled subscription
      cancelled_at (str): Cancellation timestamp (ISO format)
  """

  message: str
  subscription_id: str
  cancelled_at: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    message = self.message

    subscription_id = self.subscription_id

    cancelled_at = self.cancelled_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "message": message,
        "subscription_id": subscription_id,
        "cancelled_at": cancelled_at,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    message = d.pop("message")

    subscription_id = d.pop("subscription_id")

    cancelled_at = d.pop("cancelled_at")

    cancellation_response = cls(
      message=message,
      subscription_id=subscription_id,
      cancelled_at=cancelled_at,
    )

    cancellation_response.additional_properties = d
    return cancellation_response

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
