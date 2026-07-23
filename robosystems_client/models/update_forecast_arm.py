from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.update_forecast_request import UpdateForecastRequest


T = TypeVar("T", bound="UpdateForecastArm")


@_attrs_define
class UpdateForecastArm:
  """Update-information-block body for ``block_type="forecast"``.

  Mutable: name, scenario_kind, horizon_months, base_period, levers
  (full replace). Updating does not recompute — run ``compute-forecast``
  to refresh the scenario's derived months.

      Attributes:
          block_type (Literal['forecast']): Discriminator value selecting this arm.
          payload (UpdateForecastRequest): Update a forecast block in place.

              Mutable: name, scenario_kind, horizon_months, base_period, levers.
              ``levers`` is a **full replace** when provided (partial lever edits
              would make the asserted set ambiguous). Updating does NOT recompute —
              previously computed scenario months go stale until the next
              ``compute-forecast`` run (the compute-metrics drift semantics).
  """

  block_type: Literal["forecast"]
  payload: UpdateForecastRequest
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
    from ..models.update_forecast_request import UpdateForecastRequest

    d = dict(src_dict)
    block_type = cast(Literal["forecast"], d.pop("block_type"))
    if block_type != "forecast":
      raise ValueError(f"block_type must match const 'forecast', got '{block_type}'")

    payload = UpdateForecastRequest.from_dict(d.pop("payload"))

    update_forecast_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    update_forecast_arm.additional_properties = d
    return update_forecast_arm

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
