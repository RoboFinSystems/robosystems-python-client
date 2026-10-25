from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LearnClassificationDefaultsRequest")


@_attrs_define
class LearnClassificationDefaultsRequest:
  """Seed counterparty defaults from the bank lines already committed.

  Attributes:
      dry_run (bool | Unset): Report what would be learned without writing it. Default: False.
  """

  dry_run: bool | Unset = False

  def to_dict(self) -> dict[str, Any]:
    dry_run = self.dry_run

    field_dict: dict[str, Any] = {}

    field_dict.update({})
    if dry_run is not UNSET:
      field_dict["dry_run"] = dry_run

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    dry_run = d.pop("dry_run", UNSET)

    learn_classification_defaults_request = cls(
      dry_run=dry_run,
    )

    return learn_classification_defaults_request
