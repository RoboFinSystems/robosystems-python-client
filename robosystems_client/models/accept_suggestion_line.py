from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.accept_suggestion_line_outcome import AcceptSuggestionLineOutcome
from ..types import UNSET, Unset

T = TypeVar("T", bound="AcceptSuggestionLine")


@_attrs_define
class AcceptSuggestionLine:
  """What the batch did with one line.

  Attributes:
      event_id (str): The line.
      outcome (AcceptSuggestionLineOutcome): What happened to it.
      reason (None | str | Unset): Why a skipped line was not taken: `not_open` (already classified, posted or
          retracted), `no_suggestion` (nothing to take, or a name that matches no account), `source_changed` (the feed
          changed it after capture), `suggestion_changed` (a line taken earlier in the batch moved the counterparty's
          default, so this one's suggestion is not the one selected; review it again), `closed_period`, `locked` (another
          process holds it; retry), or `refused` (the handler would not post the choice).
      detail (None | str | Unset): The refusal's own words, when there was one.
      element_id (None | str | Unset): The account the suggestion names.
      description (None | str | Unset): The line's description.
  """

  event_id: str
  outcome: AcceptSuggestionLineOutcome
  reason: None | str | Unset = UNSET
  detail: None | str | Unset = UNSET
  element_id: None | str | Unset = UNSET
  description: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    event_id = self.event_id

    outcome = self.outcome.value

    reason: None | str | Unset
    if isinstance(self.reason, Unset):
      reason = UNSET
    else:
      reason = self.reason

    detail: None | str | Unset
    if isinstance(self.detail, Unset):
      detail = UNSET
    else:
      detail = self.detail

    element_id: None | str | Unset
    if isinstance(self.element_id, Unset):
      element_id = UNSET
    else:
      element_id = self.element_id

    description: None | str | Unset
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "event_id": event_id,
        "outcome": outcome,
      }
    )
    if reason is not UNSET:
      field_dict["reason"] = reason
    if detail is not UNSET:
      field_dict["detail"] = detail
    if element_id is not UNSET:
      field_dict["element_id"] = element_id
    if description is not UNSET:
      field_dict["description"] = description

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    event_id = d.pop("event_id")

    outcome = AcceptSuggestionLineOutcome(d.pop("outcome"))

    def _parse_reason(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reason = _parse_reason(d.pop("reason", UNSET))

    def _parse_detail(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    detail = _parse_detail(d.pop("detail", UNSET))

    def _parse_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    element_id = _parse_element_id(d.pop("element_id", UNSET))

    def _parse_description(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    description = _parse_description(d.pop("description", UNSET))

    accept_suggestion_line = cls(
      event_id=event_id,
      outcome=outcome,
      reason=reason,
      detail=detail,
      element_id=element_id,
      description=description,
    )

    accept_suggestion_line.additional_properties = d
    return accept_suggestion_line

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
