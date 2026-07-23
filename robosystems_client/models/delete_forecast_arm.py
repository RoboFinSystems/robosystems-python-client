from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.delete_forecast_request import DeleteForecastRequest


T = TypeVar("T", bound="DeleteForecastArm")


@_attrs_define
class DeleteForecastArm:
  """Delete-information-block body for ``block_type="forecast"``.

  Removes the scenario's entire parallel universe — the lever FactSet
  and every computed scenario FactSet. Actuals are never touched.

      Attributes:
          block_type (Literal['forecast']): Discriminator value selecting this arm.
          payload (DeleteForecastRequest): Delete a forecast block.

              Removes the scenario's entire parallel universe: the lever FactSet
              AND every computed scenario FactSet (the forward statement/metric
              months keyed by this scenario). Actuals are never touched.
  """

  block_type: Literal["forecast"]
  payload: DeleteForecastRequest
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    block_type = self.block_type

    payload = self.payload.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "block_type": block_type,
        "payload": payload,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.delete_forecast_request import DeleteForecastRequest

    d = dict(src_dict)
    block_type = cast(Literal["forecast"], d.pop("block_type"))
    if block_type != "forecast":
      raise ValueError(f"block_type must match const 'forecast', got '{block_type}'")

    payload = DeleteForecastRequest.from_dict(d.pop("payload"))

    delete_forecast_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    delete_forecast_arm.additional_properties = d
    return delete_forecast_arm

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
