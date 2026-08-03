from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.org_invitation_response import OrgInvitationResponse


T = TypeVar("T", bound="OrgInvitationListResponse")


@_attrs_define
class OrgInvitationListResponse:
  """List of pending organization invitations response.

  Attributes:
      invitations (list[OrgInvitationResponse]):
      total (int):
      org_id (str):
  """

  invitations: list[OrgInvitationResponse]
  total: int
  org_id: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    invitations = []
    for invitations_item_data in self.invitations:
      invitations_item = invitations_item_data.to_dict()
      invitations.append(invitations_item)

    total = self.total

    org_id = self.org_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "invitations": invitations,
        "total": total,
        "org_id": org_id,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.org_invitation_response import OrgInvitationResponse

    d = dict(src_dict)
    invitations = []
    _invitations = d.pop("invitations")
    for invitations_item_data in _invitations:
      invitations_item = OrgInvitationResponse.from_dict(invitations_item_data)

      invitations.append(invitations_item)

    total = d.pop("total")

    org_id = d.pop("org_id")

    org_invitation_list_response = cls(
      invitations=invitations,
      total=total,
      org_id=org_id,
    )

    org_invitation_list_response.additional_properties = d
    return org_invitation_list_response

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
