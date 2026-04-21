from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.create_information_block_request_payload import (
    CreateInformationBlockRequestPayload,
  )


T = TypeVar("T", bound="CreateInformationBlockRequest")


@_attrs_define
class CreateInformationBlockRequest:
  """Generic create request — discriminator + typed-at-dispatch payload.

  ``block_type`` selects the registry entry. ``payload`` is validated
  against ``BlockTypeRegistryEntry.create_request_model`` (e.g.
  :class:`CreateScheduleRequest` for ``block_type='schedule'``) by the
  command dispatcher. Chosen over a Pydantic discriminated union on the
  top-level request so adding a block type is one registry line, not a
  union-arm edit at the request-model layer.

      Attributes:
          block_type (str): Block type discriminator. Must match a registered entry in
              robosystems.operations.information_block.registry.REGISTRY.
          payload (CreateInformationBlockRequestPayload | Unset): Block-type-specific creation payload. Shape-validated
              against the registry entry's `create_request_model` at dispatch time; the validation error surfaces as a 422 at
              the API boundary.
  """

  block_type: str
  payload: CreateInformationBlockRequestPayload | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    block_type = self.block_type

    payload: dict[str, Any] | Unset = UNSET
    if not isinstance(self.payload, Unset):
      payload = self.payload.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "block_type": block_type,
      }
    )
    if payload is not UNSET:
      field_dict["payload"] = payload

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.create_information_block_request_payload import (
      CreateInformationBlockRequestPayload,
    )

    d = dict(src_dict)
    block_type = d.pop("block_type")

    _payload = d.pop("payload", UNSET)
    payload: CreateInformationBlockRequestPayload | Unset
    if isinstance(_payload, Unset):
      payload = UNSET
    else:
      payload = CreateInformationBlockRequestPayload.from_dict(_payload)

    create_information_block_request = cls(
      block_type=block_type,
      payload=payload,
    )

    create_information_block_request.additional_properties = d
    return create_information_block_request

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
