from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.ceremony_options_response_options import CeremonyOptionsResponseOptions


T = TypeVar("T", bound="CeremonyOptionsResponse")


@_attrs_define
class CeremonyOptionsResponse:
  """WebAuthn options for the browser, verbatim from the RP library.

  Attributes:
      options (CeremonyOptionsResponseOptions): PublicKeyCredential options (browser JSON, opaque)
  """

  options: CeremonyOptionsResponseOptions
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    options = self.options.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "options": options,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.ceremony_options_response_options import (
      CeremonyOptionsResponseOptions,
    )

    d = dict(src_dict)
    options = CeremonyOptionsResponseOptions.from_dict(d.pop("options"))

    ceremony_options_response = cls(
      options=options,
    )

    ceremony_options_response.additional_properties = d
    return ceremony_options_response

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
