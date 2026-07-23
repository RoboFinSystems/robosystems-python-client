from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.create_forecast_request import CreateForecastRequest


T = TypeVar("T", bound="CreateForecastArm")


@_attrs_define
class CreateForecastArm:
  """Create-information-block body for ``block_type="forecast"``.

  Carries a typed forecast payload — the authored scenario container:
  scenario identity, horizon, base period, lever assertions on
  ``rs-driver:*`` catalog elements. Run ``compute-forecast`` after
  creating to derive the forward months.

      Attributes:
          block_type (Literal['forecast']): Discriminator value selecting this arm.
          payload (CreateForecastRequest): Create a forecast block — the authored scenario container.

              ``base_period`` defaults to the fiscal calendar's
              ``closed_through_period`` (else the newest actual report month) —
              the walk projects forward from the last closed actuals. The resolved
              value is stored in the mechanics so recompute is deterministic.
  """

  block_type: Literal["forecast"]
  payload: CreateForecastRequest
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
    from ..models.create_forecast_request import CreateForecastRequest

    d = dict(src_dict)
    block_type = cast(Literal["forecast"], d.pop("block_type"))
    if block_type != "forecast":
      raise ValueError(f"block_type must match const 'forecast', got '{block_type}'")

    payload = CreateForecastRequest.from_dict(d.pop("payload"))

    create_forecast_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    create_forecast_arm.additional_properties = d
    return create_forecast_arm

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
