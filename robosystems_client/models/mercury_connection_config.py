from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MercuryConnectionConfig")


@_attrs_define
class MercuryConnectionConfig:
  """Mercury bank-feed connection configuration.

  A bank feed is native accounting: the graph must already have a chart of
  accounts and no live QuickBooks connection. Over OAuth (the hosted
  default) the connection is created ``pending_oauth`` and activated by the
  callback. ``api_key`` — a personal **read-only** Mercury token — connects
  at once without a browser round-trip, but only on deployments that turn
  on ``MERCURY_API_KEY_CONNECTIONS_ENABLED`` (self-hosted and local); the
  hosted product refuses it.

      Attributes:
          since_date (datetime.date | None | Unset): First day of the backfill (ISO 8601). Defaults to 1 January of last
              year. Incremental syncs never look back before it.
          include_treasury (bool | Unset): Capture treasury-account activity alongside checking/savings. Default: True.
          api_key (None | str | Unset): A personal read-only Mercury API token, for deployments that allow the api_key
              credential mode. Omit to connect over OAuth.
  """

  since_date: datetime.date | None | Unset = UNSET
  include_treasury: bool | Unset = True
  api_key: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    since_date: None | str | Unset
    if isinstance(self.since_date, Unset):
      since_date = UNSET
    elif isinstance(self.since_date, datetime.date):
      since_date = self.since_date.isoformat()
    else:
      since_date = self.since_date

    include_treasury = self.include_treasury

    api_key: None | str | Unset
    if isinstance(self.api_key, Unset):
      api_key = UNSET
    else:
      api_key = self.api_key

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if since_date is not UNSET:
      field_dict["since_date"] = since_date
    if include_treasury is not UNSET:
      field_dict["include_treasury"] = include_treasury
    if api_key is not UNSET:
      field_dict["api_key"] = api_key

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_since_date(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        since_date_type_0 = datetime.date.fromisoformat(data)

        return since_date_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    since_date = _parse_since_date(d.pop("since_date", UNSET))

    include_treasury = d.pop("include_treasury", UNSET)

    def _parse_api_key(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    api_key = _parse_api_key(d.pop("api_key", UNSET))

    mercury_connection_config = cls(
      since_date=since_date,
      include_treasury=include_treasury,
      api_key=api_key,
    )

    mercury_connection_config.additional_properties = d
    return mercury_connection_config

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
