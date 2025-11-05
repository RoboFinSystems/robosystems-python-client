from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.operation_costs_ai_operations import OperationCostsAiOperations
  from ..models.operation_costs_token_pricing import OperationCostsTokenPricing


T = TypeVar("T", bound="OperationCosts")


@_attrs_define
class OperationCosts:
  """Operation cost information.

  Attributes:
      description (str): Description of operation costs
      ai_operations (OperationCostsAiOperations): Base costs for AI operations
      token_pricing (OperationCostsTokenPricing): Token pricing by model
      included_operations (list[str]): Operations that don't consume credits
      notes (list[str]): Important notes about costs
  """

  description: str
  ai_operations: "OperationCostsAiOperations"
  token_pricing: "OperationCostsTokenPricing"
  included_operations: list[str]
  notes: list[str]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    description = self.description

    ai_operations = self.ai_operations.to_dict()

    token_pricing = self.token_pricing.to_dict()

    included_operations = self.included_operations

    notes = self.notes

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "description": description,
        "ai_operations": ai_operations,
        "token_pricing": token_pricing,
        "included_operations": included_operations,
        "notes": notes,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.operation_costs_ai_operations import OperationCostsAiOperations
    from ..models.operation_costs_token_pricing import OperationCostsTokenPricing

    d = dict(src_dict)
    description = d.pop("description")

    ai_operations = OperationCostsAiOperations.from_dict(d.pop("ai_operations"))

    token_pricing = OperationCostsTokenPricing.from_dict(d.pop("token_pricing"))

    included_operations = cast(list[str], d.pop("included_operations"))

    notes = cast(list[str], d.pop("notes"))

    operation_costs = cls(
      description=description,
      ai_operations=ai_operations,
      token_pricing=token_pricing,
      included_operations=included_operations,
      notes=notes,
    )

    operation_costs.additional_properties = d
    return operation_costs

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
