from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockSourceGraphOperation")


@_attrs_define
class BlockSourceGraphOperation:
  """Bar a graph from sharing reports into this one.

  Attributes:
      source_graph_id (str): Graph ID to block. Read it off the `source_graph_id` provenance field of a report that
          was shared to you.
      reason (None | str | Unset): Free-form note for your own records. Never disclosed to the sender.
      purge (bool | Unset): Also delete every report already shared in from this source, with their fact sets and
          facts. Reports you authored are never touched. Default: False.
  """

  source_graph_id: str
  reason: None | str | Unset = UNSET
  purge: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    source_graph_id = self.source_graph_id

    reason: None | str | Unset
    if isinstance(self.reason, Unset):
      reason = UNSET
    else:
      reason = self.reason

    purge = self.purge

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "source_graph_id": source_graph_id,
      }
    )
    if reason is not UNSET:
      field_dict["reason"] = reason
    if purge is not UNSET:
      field_dict["purge"] = purge

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    source_graph_id = d.pop("source_graph_id")

    def _parse_reason(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reason = _parse_reason(d.pop("reason", UNSET))

    purge = d.pop("purge", UNSET)

    block_source_graph_operation = cls(
      source_graph_id=source_graph_id,
      reason=reason,
      purge=purge,
    )

    block_source_graph_operation.additional_properties = d
    return block_source_graph_operation

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
