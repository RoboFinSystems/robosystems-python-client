from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

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
      full_rebuild (bool | Unset): Pull complete history from the provider, ignoring lookback window. Takes precedence
          over since_date. Default: False.
      since_date (datetime.date | None | Unset): Sync data from this date forward (ISO 8601). Ignored if
          full_rebuild=True. If neither set, provider default applies (e.g., QuickBooks: 60 days).
      sync_options (None | SyncConnectionRequestSyncOptionsType0 | Unset): Provider-specific sync options (escape
          hatch for fields not exposed at the top level).
  """

  full_rebuild: bool | Unset = False
  since_date: datetime.date | None | Unset = UNSET
  sync_options: None | SyncConnectionRequestSyncOptionsType0 | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.sync_connection_request_sync_options_type_0 import (
      SyncConnectionRequestSyncOptionsType0,
    )

    full_rebuild = self.full_rebuild

    since_date: None | str | Unset
    if isinstance(self.since_date, Unset):
      since_date = UNSET
    elif isinstance(self.since_date, datetime.date):
      since_date = self.since_date.isoformat()
    else:
      since_date = self.since_date

    sync_options: dict[str, Any] | None | Unset
    if isinstance(self.sync_options, Unset):
      sync_options = UNSET
    elif isinstance(self.sync_options, SyncConnectionRequestSyncOptionsType0):
      sync_options = self.sync_options.to_dict()
    else:
      sync_options = self.sync_options

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if full_rebuild is not UNSET:
      field_dict["full_rebuild"] = full_rebuild
    if since_date is not UNSET:
      field_dict["since_date"] = since_date
    if sync_options is not UNSET:
      field_dict["sync_options"] = sync_options

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.sync_connection_request_sync_options_type_0 import (
      SyncConnectionRequestSyncOptionsType0,
    )

    d = dict(src_dict)
    full_rebuild = d.pop("full_rebuild", UNSET)

    def _parse_since_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        since_date_type_0 = isoparse(data).date()

        return since_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    since_date = _parse_since_date(d.pop("since_date", UNSET))

    def _parse_sync_options(
      data: object,
    ) -> None | SyncConnectionRequestSyncOptionsType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        sync_options_type_0 = SyncConnectionRequestSyncOptionsType0.from_dict(data)

        return sync_options_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | SyncConnectionRequestSyncOptionsType0 | Unset, data)

    sync_options = _parse_sync_options(d.pop("sync_options", UNSET))

    sync_connection_request = cls(
      full_rebuild=full_rebuild,
      since_date=since_date,
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
