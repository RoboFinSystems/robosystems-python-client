from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.payment_method import PaymentMethod


T = TypeVar("T", bound="UpdatePaymentMethodResponse")


@_attrs_define
class UpdatePaymentMethodResponse:
  """Response for payment method update.

  Attributes:
      message (str): Success message
      payment_method (PaymentMethod): Payment method information.
  """

  message: str
  payment_method: "PaymentMethod"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    message = self.message

    payment_method = self.payment_method.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "message": message,
        "payment_method": payment_method,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.payment_method import PaymentMethod

    d = dict(src_dict)
    message = d.pop("message")

    payment_method = PaymentMethod.from_dict(d.pop("payment_method"))

    update_payment_method_response = cls(
      message=message,
      payment_method=payment_method,
    )

    update_payment_method_response.additional_properties = d
    return update_payment_method_response

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
