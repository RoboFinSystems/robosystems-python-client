from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_type import OrgType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOrgRequest")


@_attrs_define
class CreateOrgRequest:
  """Request to create an organization.

  Attributes:
      name (str):
      org_type (Union[Unset, OrgType]):
  """

  name: str
  org_type: Union[Unset, OrgType] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    org_type: Union[Unset, str] = UNSET
    if not isinstance(self.org_type, Unset):
      org_type = self.org_type.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
      }
    )
    if org_type is not UNSET:
      field_dict["org_type"] = org_type

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    _org_type = d.pop("org_type", UNSET)
    org_type: Union[Unset, OrgType]
    if isinstance(_org_type, Unset):
      org_type = UNSET
    else:
      org_type = OrgType(_org_type)

    create_org_request = cls(
      name=name,
      org_type=org_type,
    )

    create_org_request.additional_properties = d
    return create_org_request

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
