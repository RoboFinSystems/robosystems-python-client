from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.accept_suggestion_line import AcceptSuggestionLine


T = TypeVar("T", bound="AcceptSuggestionsResponse")


@_attrs_define
class AcceptSuggestionsResponse:
  """The batch's counts, and every line it looked at.

  Attributes:
      selected (int): Lines the filters matched, before the limit.
      classified (int): Lines classified to their suggestion and left to post.
      committed (int): Lines classified to their suggestion and posted.
      skipped (int): Lines not taken, each with a reason.
      truncated (bool): More lines matched than the limit allowed in this call.
      dry_run (bool): Nothing was written.
      lines (list[AcceptSuggestionLine]): Each line looked at, oldest first.
  """

  selected: int
  classified: int
  committed: int
  skipped: int
  truncated: bool
  dry_run: bool
  lines: list[AcceptSuggestionLine]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    selected = self.selected

    classified = self.classified

    committed = self.committed

    skipped = self.skipped

    truncated = self.truncated

    dry_run = self.dry_run

    lines = []
    for lines_item_data in self.lines:
      lines_item = lines_item_data.to_dict()
      lines.append(lines_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "selected": selected,
        "classified": classified,
        "committed": committed,
        "skipped": skipped,
        "truncated": truncated,
        "dry_run": dry_run,
        "lines": lines,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.accept_suggestion_line import AcceptSuggestionLine

    d = dict(src_dict)
    selected = d.pop("selected")

    classified = d.pop("classified")

    committed = d.pop("committed")

    skipped = d.pop("skipped")

    truncated = d.pop("truncated")

    dry_run = d.pop("dry_run")

    lines = []
    _lines = d.pop("lines")
    for lines_item_data in _lines:
      lines_item = AcceptSuggestionLine.from_dict(lines_item_data)

      lines.append(lines_item)

    accept_suggestions_response = cls(
      selected=selected,
      classified=classified,
      committed=committed,
      skipped=skipped,
      truncated=truncated,
      dry_run=dry_run,
      lines=lines,
    )

    accept_suggestions_response.additional_properties = d
    return accept_suggestions_response

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
