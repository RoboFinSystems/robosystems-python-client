from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.element_update_patch_metadata_type_0 import (
    ElementUpdatePatchMetadataType0,
  )


T = TypeVar("T", bound="ElementUpdatePatch")


@_attrs_define
class ElementUpdatePatch:
  """Partial-update patch for a single element, keyed by qname.

  Attributes:
      qname (str): qname identifier of the element to update.
      name (None | str | Unset):
      description (None | str | Unset):
      trait (None | str | Unset):
      balance_type (None | str | Unset):
      period_type (None | str | Unset):
      is_monetary (bool | None | Unset):
      code (None | str | Unset):
      parent_ref (None | str | Unset):
      metadata (ElementUpdatePatchMetadataType0 | None | Unset):
  """

  qname: str
  name: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  trait: None | str | Unset = UNSET
  balance_type: None | str | Unset = UNSET
  period_type: None | str | Unset = UNSET
  is_monetary: bool | None | Unset = UNSET
  code: None | str | Unset = UNSET
  parent_ref: None | str | Unset = UNSET
  metadata: ElementUpdatePatchMetadataType0 | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.element_update_patch_metadata_type_0 import (
      ElementUpdatePatchMetadataType0,
    )

    qname = self.qname

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    trait: None | str | Unset
    if isinstance(self.trait, Unset):
      trait = UNSET
    else:
      trait = self.trait

    balance_type: None | str | Unset
    if isinstance(self.balance_type, Unset):
      balance_type = UNSET
    else:
      balance_type = self.balance_type

    period_type: None | str | Unset
    if isinstance(self.period_type, Unset):
      period_type = UNSET
    else:
      period_type = self.period_type

    is_monetary: bool | None | Unset
    if isinstance(self.is_monetary, Unset):
      is_monetary = UNSET
    else:
      is_monetary = self.is_monetary

    code: None | str | Unset
    if isinstance(self.code, Unset):
      code = UNSET
    else:
      code = self.code

    parent_ref: None | str | Unset
    if isinstance(self.parent_ref, Unset):
      parent_ref = UNSET
    else:
      parent_ref = self.parent_ref

    metadata: dict[str, Any] | None | Unset
    if isinstance(self.metadata, Unset):
      metadata = UNSET
    elif isinstance(self.metadata, ElementUpdatePatchMetadataType0):
      metadata = self.metadata.to_dict()
    else:
      metadata = self.metadata

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "qname": qname,
      }
    )
    if name is not UNSET:
      field_dict["name"] = name
    if description is not UNSET:
      field_dict["description"] = description
    if trait is not UNSET:
      field_dict["trait"] = trait
    if balance_type is not UNSET:
      field_dict["balance_type"] = balance_type
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if is_monetary is not UNSET:
      field_dict["is_monetary"] = is_monetary
    if code is not UNSET:
      field_dict["code"] = code
    if parent_ref is not UNSET:
      field_dict["parent_ref"] = parent_ref
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.element_update_patch_metadata_type_0 import (
      ElementUpdatePatchMetadataType0,
    )

    d = dict(src_dict)
    qname = d.pop("qname")

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_trait(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    trait = _parse_trait(d.pop("trait", UNSET))

    def _parse_balance_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    balance_type = _parse_balance_type(d.pop("balance_type", UNSET))

    def _parse_period_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_type = _parse_period_type(d.pop("period_type", UNSET))

    def _parse_is_monetary(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    is_monetary = _parse_is_monetary(d.pop("is_monetary", UNSET))

    def _parse_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    code = _parse_code(d.pop("code", UNSET))

    def _parse_parent_ref(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent_ref = _parse_parent_ref(d.pop("parent_ref", UNSET))

    def _parse_metadata(data: object) -> ElementUpdatePatchMetadataType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        metadata_type_0 = ElementUpdatePatchMetadataType0.from_dict(data)

        return metadata_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(ElementUpdatePatchMetadataType0 | None | Unset, data)

    metadata = _parse_metadata(d.pop("metadata", UNSET))

    element_update_patch = cls(
      qname=qname,
      name=name,
      description=description,
      trait=trait,
      balance_type=balance_type,
      period_type=period_type,
      is_monetary=is_monetary,
      code=code,
      parent_ref=parent_ref,
      metadata=metadata,
    )

    element_update_patch.additional_properties = d
    return element_update_patch

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
