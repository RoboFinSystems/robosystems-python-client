from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutStatusResponse")


@_attrs_define
class CheckoutStatusResponse:
  """Status of a checkout session.

  Attributes:
      status (str): Checkout status: 'pending_payment', 'provisioning', 'completed', 'failed'
      subscription_id (str): Internal subscription ID
      resource_id (Union[None, Unset, str]): Resource ID (graph_id for both graphs and repositories) once provisioned.
          For repositories, this is the repository slug (e.g., 'sec')
      operation_id (Union[None, Unset, str]): SSE operation ID for monitoring provisioning progress
      error (Union[None, Unset, str]): Error message if checkout failed
  """

  status: str
  subscription_id: str
  resource_id: Union[None, Unset, str] = UNSET
  operation_id: Union[None, Unset, str] = UNSET
  error: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    status = self.status

    subscription_id = self.subscription_id

    resource_id: Union[None, Unset, str]
    if isinstance(self.resource_id, Unset):
      resource_id = UNSET
    else:
      resource_id = self.resource_id

    operation_id: Union[None, Unset, str]
    if isinstance(self.operation_id, Unset):
      operation_id = UNSET
    else:
      operation_id = self.operation_id

    error: Union[None, Unset, str]
    if isinstance(self.error, Unset):
      error = UNSET
    else:
      error = self.error

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "status": status,
        "subscription_id": subscription_id,
      }
    )
    if resource_id is not UNSET:
      field_dict["resource_id"] = resource_id
    if operation_id is not UNSET:
      field_dict["operation_id"] = operation_id
    if error is not UNSET:
      field_dict["error"] = error

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    status = d.pop("status")

    subscription_id = d.pop("subscription_id")

    def _parse_resource_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    resource_id = _parse_resource_id(d.pop("resource_id", UNSET))

    def _parse_operation_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    operation_id = _parse_operation_id(d.pop("operation_id", UNSET))

    def _parse_error(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    error = _parse_error(d.pop("error", UNSET))

    checkout_status_response = cls(
      status=status,
      subscription_id=subscription_id,
      resource_id=resource_id,
      operation_id=operation_id,
      error=error,
    )

    checkout_status_response.additional_properties = d
    return checkout_status_response

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
