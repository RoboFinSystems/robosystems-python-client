from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.create_rollforward_request import CreateRollforwardRequest


T = TypeVar("T", bound="CreateRollforwardArm")


@_attrs_define
class CreateRollforwardArm:
  """Create-information-block body for ``block_type="rollforward"``.

  Carries a typed rollforward payload. The block decomposes the period
  change in a BS source element across the declared attribution
  filters.

      Attributes:
          block_type (Literal['rollforward']): Discriminator value selecting this arm.
          payload (CreateRollforwardRequest): Create a rollforward Information Block.

              Mirrors :class:`CreateScheduleRequest` in shape. The block decomposes
              the period change in ``bs_source_qname`` across the declared
              attribution filters. Residual (Δ BS - Σ filter matches) falls back to
              the default change tag — or, if no default is declared, surfaces as
              an unattributed fact tagged with a synthetic residual concept.
  """

  block_type: Literal["rollforward"]
  payload: CreateRollforwardRequest
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
    from ..models.create_rollforward_request import CreateRollforwardRequest

    d = dict(src_dict)
    block_type = cast(Literal["rollforward"], d.pop("block_type"))
    if block_type != "rollforward":
      raise ValueError(f"block_type must match const 'rollforward', got '{block_type}'")

    payload = CreateRollforwardRequest.from_dict(d.pop("payload"))

    create_rollforward_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    create_rollforward_arm.additional_properties = d
    return create_rollforward_arm

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
