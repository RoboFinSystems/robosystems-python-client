from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcceptSuggestionsRequest")


@_attrs_define
class AcceptSuggestionsRequest:
  """Take the suggestion on every open bank line the filters select.

  Attributes:
      entity_id (None | str | Unset): The entity whose inbox to act on. Omit for the group parent.
      event_ids (list[str] | None | Unset): Explicit lines, as from the inbox's multi-select; each is answered, even
          one that cannot be taken. The other filters still narrow them.
      source (None | str | Unset): Only lines from this feed (`plaid`, `mercury`).
      agent_id (None | str | Unset): Only one counterparty's lines.
      suggestion_source (None | str | Unset): Only lines whose suggestion came from here: `agent_default` (the
          counterparty's learned default), `tier0` (the bank's category) or `ai`.
      occurred_from (datetime.date | None | Unset): Only lines dated on or after this day.
      occurred_to (datetime.date | None | Unset): Only lines dated on or before this day.
      commit (bool | Unset): Post each taken line as well (captured → committed). Off, the lines are classified and
          wait for a person to post them. Default: False.
      limit (int | Unset): At most this many lines per call, oldest first; `truncated` in the response says whether
          more matched. Default: 200.
      dry_run (bool | Unset): Report what each line would do without writing. A closed month is found only when a line
          actually posts, so a real run can still skip one a dry run counted. Default: False.
  """

  entity_id: None | str | Unset = UNSET
  event_ids: list[str] | None | Unset = UNSET
  source: None | str | Unset = UNSET
  agent_id: None | str | Unset = UNSET
  suggestion_source: None | str | Unset = UNSET
  occurred_from: datetime.date | None | Unset = UNSET
  occurred_to: datetime.date | None | Unset = UNSET
  commit: bool | Unset = False
  limit: int | Unset = 200
  dry_run: bool | Unset = False

  def to_dict(self) -> dict[str, Any]:
    entity_id: None | str | Unset
    if isinstance(self.entity_id, Unset):
      entity_id = UNSET
    else:
      entity_id = self.entity_id

    event_ids: list[str] | None | Unset
    if isinstance(self.event_ids, Unset):
      event_ids = UNSET
    elif isinstance(self.event_ids, list):
      event_ids = self.event_ids

    else:
      event_ids = self.event_ids

    source: None | str | Unset
    if isinstance(self.source, Unset):
      source = UNSET
    else:
      source = self.source

    agent_id: None | str | Unset
    if isinstance(self.agent_id, Unset):
      agent_id = UNSET
    else:
      agent_id = self.agent_id

    suggestion_source: None | str | Unset
    if isinstance(self.suggestion_source, Unset):
      suggestion_source = UNSET
    else:
      suggestion_source = self.suggestion_source

    occurred_from: None | str | Unset
    if isinstance(self.occurred_from, Unset):
      occurred_from = UNSET
    elif isinstance(self.occurred_from, datetime.date):
      occurred_from = self.occurred_from.isoformat()
    else:
      occurred_from = self.occurred_from

    occurred_to: None | str | Unset
    if isinstance(self.occurred_to, Unset):
      occurred_to = UNSET
    elif isinstance(self.occurred_to, datetime.date):
      occurred_to = self.occurred_to.isoformat()
    else:
      occurred_to = self.occurred_to

    commit = self.commit

    limit = self.limit

    dry_run = self.dry_run

    field_dict: dict[str, Any] = {}

    field_dict.update({})
    if entity_id is not UNSET:
      field_dict["entity_id"] = entity_id
    if event_ids is not UNSET:
      field_dict["event_ids"] = event_ids
    if source is not UNSET:
      field_dict["source"] = source
    if agent_id is not UNSET:
      field_dict["agent_id"] = agent_id
    if suggestion_source is not UNSET:
      field_dict["suggestion_source"] = suggestion_source
    if occurred_from is not UNSET:
      field_dict["occurred_from"] = occurred_from
    if occurred_to is not UNSET:
      field_dict["occurred_to"] = occurred_to
    if commit is not UNSET:
      field_dict["commit"] = commit
    if limit is not UNSET:
      field_dict["limit"] = limit
    if dry_run is not UNSET:
      field_dict["dry_run"] = dry_run

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)

    def _parse_entity_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

    def _parse_event_ids(data: object) -> list[str] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        event_ids_type_0 = cast(list[str], data)

        return event_ids_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[str] | None | Unset, data)

    event_ids = _parse_event_ids(d.pop("event_ids", UNSET))

    def _parse_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    source = _parse_source(d.pop("source", UNSET))

    def _parse_agent_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

    def _parse_suggestion_source(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    suggestion_source = _parse_suggestion_source(d.pop("suggestion_source", UNSET))

    def _parse_occurred_from(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        occurred_from_type_0 = datetime.date.fromisoformat(data)

        return occurred_from_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    occurred_from = _parse_occurred_from(d.pop("occurred_from", UNSET))

    def _parse_occurred_to(data: object) -> datetime.date | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        occurred_to_type_0 = datetime.date.fromisoformat(data)

        return occurred_to_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(datetime.date | None | Unset, data)

    occurred_to = _parse_occurred_to(d.pop("occurred_to", UNSET))

    commit = d.pop("commit", UNSET)

    limit = d.pop("limit", UNSET)

    dry_run = d.pop("dry_run", UNSET)

    accept_suggestions_request = cls(
      entity_id=entity_id,
      event_ids=event_ids,
      source=source,
      agent_id=agent_id,
      suggestion_source=suggestion_source,
      occurred_from=occurred_from,
      occurred_to=occurred_to,
      commit=commit,
      limit=limit,
      dry_run=dry_run,
    )

    return accept_suggestions_request
