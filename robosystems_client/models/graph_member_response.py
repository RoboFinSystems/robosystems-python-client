from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.graph_member_response_source import GraphMemberResponseSource
from ..models.graph_role import GraphRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphMemberResponse")


@_attrs_define
class GraphMemberResponse:
  """A user with access to a graph.

  Attributes:
      user_id (str):
      name (str):
      email (str):
      role (GraphRole): Ordered per-graph roles: viewer < member < admin.
      source (GraphMemberResponseSource): 'explicit' for a direct grant; 'org_role' for implicit admin held by org
          owners/admins
      granted_at (datetime.datetime | None | Unset): When the explicit grant was created (null for implicit access)
  """

  user_id: str
  name: str
  email: str
  role: GraphRole
  source: GraphMemberResponseSource
  granted_at: datetime.datetime | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    user_id = self.user_id

    name = self.name

    email = self.email

    role = self.role.value

    source = self.source.value

    granted_at: None | str | Unset
    if isinstance(self.granted_at, Unset):
      granted_at = UNSET
    elif isinstance(self.granted_at, datetime.datetime):
      granted_at = self.granted_at.isoformat()
    else:
      granted_at = self.granted_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "user_id": user_id,
        "name": name,
        "email": email,
        "role": role,
        "source": source,
      }
    )
    if granted_at is not UNSET:
      field_dict["granted_at"] = granted_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    user_id = d.pop("user_id")

    name = d.pop("name")

    email = d.pop("email")

    role = GraphRole(d.pop("role"))

    source = GraphMemberResponseSource(d.pop("source"))

    def _parse_granted_at(data: object) -> datetime.datetime | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        granted_at_type_0 = datetime.datetime.fromisoformat(data)

        return granted_at_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.datetime | None | Unset, data)

    granted_at = _parse_granted_at(d.pop("granted_at", UNSET))

    graph_member_response = cls(
      user_id=user_id,
      name=name,
      email=email,
      role=role,
      source=source,
      granted_at=granted_at,
    )

    graph_member_response.additional_properties = d
    return graph_member_response

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
