from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareResultItem")


@_attrs_define
class ShareResultItem:
  """Per-target outcome of a `share-report` call.

  Attributes:
      target_graph_id (str): Recipient graph ID (a publish-list member).
      status (str): `shared` when the copy succeeded; `error` when this target failed (other targets may still have
          succeeded).
      error (None | str | Unset): Error message when `status='error'`, else null.
      fact_count (int | Unset): Number of facts copied into the target on success. Default: 0.
  """

  target_graph_id: str
  status: str
  error: None | str | Unset = UNSET
  fact_count: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    target_graph_id = self.target_graph_id

    status = self.status

    error: None | str | Unset
    if isinstance(self.error, Unset):
      error = UNSET
    else:
      error = self.error

    fact_count = self.fact_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "target_graph_id": target_graph_id,
        "status": status,
      }
    )
    if error is not UNSET:
      field_dict["error"] = error
    if fact_count is not UNSET:
      field_dict["fact_count"] = fact_count

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    target_graph_id = d.pop("target_graph_id")

    status = d.pop("status")

    def _parse_error(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    error = _parse_error(d.pop("error", UNSET))

    fact_count = d.pop("fact_count", UNSET)

    share_result_item = cls(
      target_graph_id=target_graph_id,
      status=status,
      error=error,
      fact_count=fact_count,
    )

    share_result_item.additional_properties = d
    return share_result_item

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
