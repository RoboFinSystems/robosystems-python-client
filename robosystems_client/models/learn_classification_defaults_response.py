from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LearnClassificationDefaultsResponse")


@_attrs_define
class LearnClassificationDefaultsResponse:
  """What seeding the defaults learned.

  Attributes:
      agents_learned (int): Counterparties given a default from their committed lines.
      agents_kept (int): Counterparties that already had a default, left as they were.
      lines_read (int): Committed lines classified to a single account that were read.
      open_lines_resuggested (int): Still-open lines whose suggestion changed as a result.
      dry_run (bool):
  """

  agents_learned: int
  agents_kept: int
  lines_read: int
  open_lines_resuggested: int
  dry_run: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    agents_learned = self.agents_learned

    agents_kept = self.agents_kept

    lines_read = self.lines_read

    open_lines_resuggested = self.open_lines_resuggested

    dry_run = self.dry_run

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "agents_learned": agents_learned,
        "agents_kept": agents_kept,
        "lines_read": lines_read,
        "open_lines_resuggested": open_lines_resuggested,
        "dry_run": dry_run,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    agents_learned = d.pop("agents_learned")

    agents_kept = d.pop("agents_kept")

    lines_read = d.pop("lines_read")

    open_lines_resuggested = d.pop("open_lines_resuggested")

    dry_run = d.pop("dry_run")

    learn_classification_defaults_response = cls(
      agents_learned=agents_learned,
      agents_kept=agents_kept,
      lines_read=lines_read,
      open_lines_resuggested=open_lines_resuggested,
      dry_run=dry_run,
    )

    learn_classification_defaults_response.additional_properties = d
    return learn_classification_defaults_response

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
