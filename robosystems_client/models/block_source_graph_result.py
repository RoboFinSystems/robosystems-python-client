from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.blocked_source_graph_response import BlockedSourceGraphResponse


T = TypeVar("T", bound="BlockSourceGraphResult")


@_attrs_define
class BlockSourceGraphResult:
  """Outcome of a block, including anything the purge removed.

  Attributes:
      block (BlockedSourceGraphResponse): One blocked source graph.
      already_blocked (bool | Unset): True when the source was already blocked and this call was a no-op apart from
          any purge. Default: False.
      purged_report_count (int | Unset): Number of previously-shared reports deleted from this graph. Zero unless
          `purge` was set. Default: 0.
  """

  block: BlockedSourceGraphResponse
  already_blocked: bool | Unset = False
  purged_report_count: int | Unset = 0
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    block = self.block.to_dict()

    already_blocked = self.already_blocked

    purged_report_count = self.purged_report_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "block": block,
      }
    )
    if already_blocked is not UNSET:
      field_dict["already_blocked"] = already_blocked
    if purged_report_count is not UNSET:
      field_dict["purged_report_count"] = purged_report_count

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.blocked_source_graph_response import BlockedSourceGraphResponse

    d = dict(src_dict)
    block = BlockedSourceGraphResponse.from_dict(d.pop("block"))

    already_blocked = d.pop("already_blocked", UNSET)

    purged_report_count = d.pop("purged_report_count", UNSET)

    block_source_graph_result = cls(
      block=block,
      already_blocked=already_blocked,
      purged_report_count=purged_report_count,
    )

    block_source_graph_result.additional_properties = d
    return block_source_graph_result

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
