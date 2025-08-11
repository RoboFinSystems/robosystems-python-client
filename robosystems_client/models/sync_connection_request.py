from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.sync_connection_request_sync_options_type_0 import (
    SyncConnectionRequestSyncOptionsType0,
  )


T = TypeVar("T", bound="SyncConnectionRequest")


@_attrs_define
class SyncConnectionRequest:
  """Request to sync a connection.

  Attributes:
      full_sync (Union[Unset, bool]): Perform full sync vs incremental Default: False.
      sync_options (Union['SyncConnectionRequestSyncOptionsType0', None, Unset]): Provider-specific sync options
  """

  full_sync: Union[Unset, bool] = False
  sync_options: Union["SyncConnectionRequestSyncOptionsType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.sync_connection_request_sync_options_type_0 import (
      SyncConnectionRequestSyncOptionsType0,
    )

    full_sync = self.full_sync

    sync_options: Union[None, Unset, dict[str, Any]]
    if isinstance(self.sync_options, Unset):
      sync_options = UNSET
    elif isinstance(self.sync_options, SyncConnectionRequestSyncOptionsType0):
      sync_options = self.sync_options.to_dict()
    else:
      sync_options = self.sync_options

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if full_sync is not UNSET:
      field_dict["full_sync"] = full_sync
    if sync_options is not UNSET:
      field_dict["sync_options"] = sync_options

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.sync_connection_request_sync_options_type_0 import (
      SyncConnectionRequestSyncOptionsType0,
    )

    d = dict(src_dict)
    full_sync = d.pop("full_sync", UNSET)

    def _parse_sync_options(
      data: object,
    ) -> Union["SyncConnectionRequestSyncOptionsType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        sync_options_type_0 = SyncConnectionRequestSyncOptionsType0.from_dict(data)

        return sync_options_type_0
      except:  # noqa: E722
        pass
      return cast(Union["SyncConnectionRequestSyncOptionsType0", None, Unset], data)

    sync_options = _parse_sync_options(d.pop("sync_options", UNSET))

    sync_connection_request = cls(
      full_sync=full_sync,
      sync_options=sync_options,
    )

    sync_connection_request.additional_properties = d
    return sync_connection_request

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
