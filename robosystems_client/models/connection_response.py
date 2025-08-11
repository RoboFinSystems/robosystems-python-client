from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_response_provider import ConnectionResponseProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.connection_response_metadata import ConnectionResponseMetadata


T = TypeVar("T", bound="ConnectionResponse")


@_attrs_define
class ConnectionResponse:
  """Connection response model.

  Attributes:
      connection_id (str): Unique connection identifier
      provider (ConnectionResponseProvider): Connection provider type
      entity_id (str): Entity identifier
      status (str): Connection status
      created_at (str): Creation timestamp
      metadata (ConnectionResponseMetadata): Provider-specific metadata
      updated_at (Union[None, Unset, str]): Last update timestamp
      last_sync (Union[None, Unset, str]): Last sync timestamp
  """

  connection_id: str
  provider: ConnectionResponseProvider
  entity_id: str
  status: str
  created_at: str
  metadata: "ConnectionResponseMetadata"
  updated_at: Union[None, Unset, str] = UNSET
  last_sync: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    connection_id = self.connection_id

    provider = self.provider.value

    entity_id = self.entity_id

    status = self.status

    created_at = self.created_at

    metadata = self.metadata.to_dict()

    updated_at: Union[None, Unset, str]
    if isinstance(self.updated_at, Unset):
      updated_at = UNSET
    else:
      updated_at = self.updated_at

    last_sync: Union[None, Unset, str]
    if isinstance(self.last_sync, Unset):
      last_sync = UNSET
    else:
      last_sync = self.last_sync

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "connection_id": connection_id,
        "provider": provider,
        "entity_id": entity_id,
        "status": status,
        "created_at": created_at,
        "metadata": metadata,
      }
    )
    if updated_at is not UNSET:
      field_dict["updated_at"] = updated_at
    if last_sync is not UNSET:
      field_dict["last_sync"] = last_sync

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.connection_response_metadata import ConnectionResponseMetadata

    d = dict(src_dict)
    connection_id = d.pop("connection_id")

    provider = ConnectionResponseProvider(d.pop("provider"))

    entity_id = d.pop("entity_id")

    status = d.pop("status")

    created_at = d.pop("created_at")

    metadata = ConnectionResponseMetadata.from_dict(d.pop("metadata"))

    def _parse_updated_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

    def _parse_last_sync(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    last_sync = _parse_last_sync(d.pop("last_sync", UNSET))

    connection_response = cls(
      connection_id=connection_id,
      provider=provider,
      entity_id=entity_id,
      status=status,
      created_at=created_at,
      metadata=metadata,
      updated_at=updated_at,
      last_sync=last_sync,
    )

    connection_response.additional_properties = d
    return connection_response

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
