from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.update_information_block_request_payload import (
    UpdateInformationBlockRequestPayload,
  )


T = TypeVar("T", bound="UpdateInformationBlockRequest")


@_attrs_define
class UpdateInformationBlockRequest:
  """Generic update request — mirrors :class:`CreateInformationBlockRequest`.

  Validated against the registry entry's ``update_request_model``.
  Block types that don't support updates (e.g. the statement family,
  whose Structures are library-seeded) surface ``NotImplementedError``
  from their dispatch handler, which the registrar maps to HTTP 501.

      Attributes:
          block_type (str): Block type discriminator. Must match a registered entry.
          payload (UpdateInformationBlockRequestPayload | Unset): Block-type-specific update payload. Typically carries
              the structure_id plus whichever fields are editable for this block type. Shape-validated against the registry
              entry's `update_request_model` at dispatch time.
  """

  block_type: str
  payload: UpdateInformationBlockRequestPayload | Unset = UNSET
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
    from ..models.update_information_block_request_payload import (
      UpdateInformationBlockRequestPayload,
    )

    d = dict(src_dict)
    block_type = d.pop("block_type")

    _payload = d.pop("payload", UNSET)
    payload: UpdateInformationBlockRequestPayload | Unset
    if isinstance(_payload, Unset):
      payload = UNSET
    else:
      payload = UpdateInformationBlockRequestPayload.from_dict(_payload)

    update_information_block_request = cls(
      block_type=block_type,
      payload=payload,
    )

    update_information_block_request.additional_properties = d
    return update_information_block_request

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
