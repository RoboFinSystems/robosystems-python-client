from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaidConnectionConfig")


@_attrs_define
class PlaidConnectionConfig:
  """Plaid bank-feed connection configuration.

  A bank feed is native accounting: the graph must already have a chart of
  accounts and no live QuickBooks connection. The connection is created
  `pending_oauth`; `POST /oauth/init` returns a `link_token` for Plaid
  Link, and the `public_token` Link hands back completes it through
  `POST /oauth/callback/plaid` (as `code`). One connection per institution
  login; a graph can hold several.

      Attributes:
          since_date (datetime.date | None | Unset): First day of the backfill (ISO 8601), and how much history Plaid is
              asked to pull for the new Item (at most two years). Defaults to 1 January of last year.
  """

  since_date: datetime.date | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    since_date: None | str | Unset
    if isinstance(self.since_date, Unset):
      since_date = UNSET
    elif isinstance(self.since_date, datetime.date):
      since_date = self.since_date.isoformat()
    else:
      since_date = self.since_date

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if since_date is not UNSET:
      field_dict["since_date"] = since_date

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

    plaid_connection_config = cls(
      since_date=since_date,
    )

    plaid_connection_config.additional_properties = d
    return plaid_connection_config

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
