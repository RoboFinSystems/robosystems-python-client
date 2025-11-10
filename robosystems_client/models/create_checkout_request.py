from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.create_checkout_request_resource_config import (
    CreateCheckoutRequestResourceConfig,
  )


T = TypeVar("T", bound="CreateCheckoutRequest")


@_attrs_define
class CreateCheckoutRequest:
  """Request to create a checkout session for payment collection.

  Attributes:
      plan_name (str): Billing plan name (e.g., 'kuzu-standard')
      resource_type (str): Resource type ('graph' or 'repository')
      resource_config (CreateCheckoutRequestResourceConfig): Configuration for the resource to be provisioned. For
          repositories: {'repository_name': 'graph_id'} where graph_id is the repository slug (e.g., 'sec')
  """

  plan_name: str
  resource_type: str
  resource_config: "CreateCheckoutRequestResourceConfig"
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    plan_name = self.plan_name

    resource_type = self.resource_type

    resource_config = self.resource_config.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "plan_name": plan_name,
        "resource_type": resource_type,
        "resource_config": resource_config,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.create_checkout_request_resource_config import (
      CreateCheckoutRequestResourceConfig,
    )

    d = dict(src_dict)
    plan_name = d.pop("plan_name")

    resource_type = d.pop("resource_type")

    resource_config = CreateCheckoutRequestResourceConfig.from_dict(
      d.pop("resource_config")
    )

    create_checkout_request = cls(
      plan_name=plan_name,
      resource_type=resource_type,
      resource_config=resource_config,
    )

    create_checkout_request.additional_properties = d
    return create_checkout_request

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
