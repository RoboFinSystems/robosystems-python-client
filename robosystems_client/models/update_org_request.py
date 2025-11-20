from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_type import OrgType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateOrgRequest")


@_attrs_define
class UpdateOrgRequest:
  """Request to update organization details.

  Attributes:
      name (None | str | Unset):
      org_type (None | OrgType | Unset):
  """

  name: None | str | Unset = UNSET
  org_type: None | OrgType | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    org_type: None | str | Unset
    if isinstance(self.org_type, Unset):
      org_type = UNSET
    elif isinstance(self.org_type, OrgType):
      org_type = self.org_type.value
    else:
      org_type = self.org_type

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if name is not UNSET:
      field_dict["name"] = name
    if org_type is not UNSET:
      field_dict["org_type"] = org_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    def _parse_org_type(data: object) -> None | OrgType | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        org_type_type_0 = OrgType(data)

        return org_type_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | OrgType | Unset, data)

    org_type = _parse_org_type(d.pop("org_type", UNSET))

    update_org_request = cls(
      name=name,
      org_type=org_type,
    )

    update_org_request.additional_properties = d
    return update_org_request

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
