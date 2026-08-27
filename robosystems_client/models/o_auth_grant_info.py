from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthGrantInfo")


@_attrs_define
class OAuthGrantInfo:
  """A connected app: one OAuth consent for one client on one graph.

  Attributes:
      id (str): Grant ID
      client_name (str): The connected client's display name
      client_is_trusted (bool): Whether the client is on the trusted list (pre-registered, or a known metadata-
          document host). Untrusted clients registered themselves.
      graph_id (str): The one graph this consent reaches
      resource (str): The MCP URL the grant's tokens are bound to (their audience)
      scope (str): Granted scopes, space-separated
      created_at (str): When the user consented
      client_uri (None | str | Unset): The client's homepage, if declared
      graph_name (None | str | Unset): The graph's display name, when the graph still exists
      last_used_at (None | str | Unset): Last token use, if any
  """

  id: str
  client_name: str
  client_is_trusted: bool
  graph_id: str
  resource: str
  scope: str
  created_at: str
  client_uri: None | str | Unset = UNSET
  graph_name: None | str | Unset = UNSET
  last_used_at: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    client_name = self.client_name

    client_is_trusted = self.client_is_trusted

    graph_id = self.graph_id

    resource = self.resource

    scope = self.scope

    created_at = self.created_at

    client_uri: None | str | Unset
    if isinstance(self.client_uri, Unset):
      client_uri = UNSET
    else:
      client_uri = self.client_uri

    graph_name: None | str | Unset
    if isinstance(self.graph_name, Unset):
      graph_name = UNSET
    else:
      graph_name = self.graph_name

    last_used_at: None | str | Unset
    if isinstance(self.last_used_at, Unset):
      last_used_at = UNSET
    else:
      last_used_at = self.last_used_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "client_name": client_name,
        "client_is_trusted": client_is_trusted,
        "graph_id": graph_id,
        "resource": resource,
        "scope": scope,
        "created_at": created_at,
      }
    )
    if client_uri is not UNSET:
      field_dict["client_uri"] = client_uri
    if graph_name is not UNSET:
      field_dict["graph_name"] = graph_name
    if last_used_at is not UNSET:
      field_dict["last_used_at"] = last_used_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    client_name = d.pop("client_name")

    client_is_trusted = d.pop("client_is_trusted")

    graph_id = d.pop("graph_id")

    resource = d.pop("resource")

    scope = d.pop("scope")

    created_at = d.pop("created_at")

    def _parse_client_uri(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    client_uri = _parse_client_uri(d.pop("client_uri", UNSET))

    def _parse_graph_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    graph_name = _parse_graph_name(d.pop("graph_name", UNSET))

    def _parse_last_used_at(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

    o_auth_grant_info = cls(
      id=id,
      client_name=client_name,
      client_is_trusted=client_is_trusted,
      graph_id=graph_id,
      resource=resource,
      scope=scope,
      created_at=created_at,
      client_uri=client_uri,
      graph_name=graph_name,
      last_used_at=last_used_at,
    )

    o_auth_grant_info.additional_properties = d
    return o_auth_grant_info

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
