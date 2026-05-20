from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.update_rollforward_request import UpdateRollforwardRequest


T = TypeVar("T", bound="UpdateRollforwardArm")


@_attrs_define
class UpdateRollforwardArm:
  """Update-information-block body for ``block_type="rollforward"``.

  Carries a typed rollforward update payload. Mutable fields: name,
  default_change_tag_qname, attribution_filters, validation_mode.

      Attributes:
          block_type (Literal['rollforward']): Discriminator value selecting this arm.
          payload (UpdateRollforwardRequest): Update mutable fields on a rollforward block.

              Editable: name, default_change_tag_qname, attribution_filters,
              validation_mode. The BS source is fixed once the block is created
              (changing it would invalidate every previously rendered period); to
              change BS source, delete and re-create.

              **Partial-update semantics**: omitted (``None``) fields mean "leave
              unchanged" — there is no wire-level way to *clear* a previously set
              default change tag or empty the attribution_filters list via this
              endpoint. To remove the default tag entirely, delete and re-create
              the rollforward block. The asymmetry is deliberate: an explicit
              clear-sentinel adds wire-shape complexity for a use case that rarely
              arises in practice (default tags are typically set during initial
              authoring and only swapped, not removed).
  """

  block_type: Literal["rollforward"]
  payload: UpdateRollforwardRequest
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
    from ..models.update_rollforward_request import UpdateRollforwardRequest

    d = dict(src_dict)
    block_type = cast(Literal["rollforward"], d.pop("block_type"))
    if block_type != "rollforward":
      raise ValueError(f"block_type must match const 'rollforward', got '{block_type}'")

    payload = UpdateRollforwardRequest.from_dict(d.pop("payload"))

    update_rollforward_arm = cls(
      block_type=block_type,
      payload=payload,
    )

    update_rollforward_arm.additional_properties = d
    return update_rollforward_arm

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
