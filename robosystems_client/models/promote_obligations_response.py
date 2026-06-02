from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.promote_obligations_response_errors_item import (
    PromoteObligationsResponseErrorsItem,
  )


T = TypeVar("T", bound="PromoteObligationsResponse")


@_attrs_define
class PromoteObligationsResponse:
  """Counts from a single on-demand promotion sweep.

  Attributes:
      classified_count (int): Matured obligations flipped pending → classified.
      dispatched_count (int): Obligations whose closing entry was drafted this run.
      error_count (int): Per-obligation handler errors (non-fatal).
      classified_event_ids (list[str] | Unset):
      errors (list[PromoteObligationsResponseErrorsItem] | Unset): Per-obligation errors as {event_id, error}; the
          sweep continues past them.
  """

  classified_count: int
  dispatched_count: int
  error_count: int
  classified_event_ids: list[str] | Unset = UNSET
  errors: list[PromoteObligationsResponseErrorsItem] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    classified_count = self.classified_count

    dispatched_count = self.dispatched_count

    error_count = self.error_count

    classified_event_ids: list[str] | Unset = UNSET
    if not isinstance(self.classified_event_ids, Unset):
      classified_event_ids = self.classified_event_ids

    errors: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.errors, Unset):
      errors = []
      for errors_item_data in self.errors:
        errors_item = errors_item_data.to_dict()
        errors.append(errors_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "classified_count": classified_count,
        "dispatched_count": dispatched_count,
        "error_count": error_count,
      }
    )
    if classified_event_ids is not UNSET:
      field_dict["classified_event_ids"] = classified_event_ids
    if errors is not UNSET:
      field_dict["errors"] = errors

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.promote_obligations_response_errors_item import (
      PromoteObligationsResponseErrorsItem,
    )

    d = dict(src_dict)
    classified_count = d.pop("classified_count")

    dispatched_count = d.pop("dispatched_count")

    error_count = d.pop("error_count")

    classified_event_ids = cast(list[str], d.pop("classified_event_ids", UNSET))

    _errors = d.pop("errors", UNSET)
    errors: list[PromoteObligationsResponseErrorsItem] | Unset = UNSET
    if _errors is not UNSET:
      errors = []
      for errors_item_data in _errors:
        errors_item = PromoteObligationsResponseErrorsItem.from_dict(errors_item_data)

        errors.append(errors_item)

    promote_obligations_response = cls(
      classified_count=classified_count,
      dispatched_count=dispatched_count,
      error_count=error_count,
      classified_event_ids=classified_event_ids,
      errors=errors,
    )

    promote_obligations_response.additional_properties = d
    return promote_obligations_response

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
