from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.disclosures_response_blocks_type_0_item import (
    DisclosuresResponseBlocksType0Item,
  )
  from ..models.disclosures_response_disclosures_type_0_item import (
    DisclosuresResponseDisclosuresType0Item,
  )
  from ..models.resolved_report_info import ResolvedReportInfo


T = TypeVar("T", bound="DisclosuresResponse")


@_attrs_define
class DisclosuresResponse:
  """The disclosures view op's result: xbrlkit's map, stamped with the graph
  and report it was read from.

  Without ``topic``: ``disclosures`` / ``count``. With ``topic``:
  ``disclosure`` / ``category`` / ``blocks`` / ``block_count``.

      Attributes:
          graph_id (str):
          report_id (str):
          resolved_report (None | ResolvedReportInfo | Unset):
          disclosures (list[DisclosuresResponseDisclosuresType0Item] | None | Unset):
          count (int | None | Unset):
          disclosure (None | str | Unset):
          category (None | str | Unset):
          blocks (list[DisclosuresResponseBlocksType0Item] | None | Unset):
          block_count (int | None | Unset):
          note (None | str | Unset):
  """

  graph_id: str
  report_id: str
  resolved_report: None | ResolvedReportInfo | Unset = UNSET
  disclosures: list[DisclosuresResponseDisclosuresType0Item] | None | Unset = UNSET
  count: int | None | Unset = UNSET
  disclosure: None | str | Unset = UNSET
  category: None | str | Unset = UNSET
  blocks: list[DisclosuresResponseBlocksType0Item] | None | Unset = UNSET
  block_count: int | None | Unset = UNSET
  note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.resolved_report_info import ResolvedReportInfo

    graph_id = self.graph_id

    report_id = self.report_id

    resolved_report: dict[str, Any] | None | Unset
    if isinstance(self.resolved_report, Unset):
      resolved_report = UNSET
    elif isinstance(self.resolved_report, ResolvedReportInfo):
      resolved_report = self.resolved_report.to_dict()
    else:
      resolved_report = self.resolved_report

    disclosures: list[dict[str, Any]] | None | Unset
    if isinstance(self.disclosures, Unset):
      disclosures = UNSET
    elif isinstance(self.disclosures, list):
      disclosures = []
      for disclosures_type_0_item_data in self.disclosures:
        disclosures_type_0_item = disclosures_type_0_item_data.to_dict()
        disclosures.append(disclosures_type_0_item)

    else:
      disclosures = self.disclosures

    count: int | None | Unset
    if isinstance(self.count, Unset):
      count = UNSET
    else:
      count = self.count

    disclosure: None | str | Unset
    if isinstance(self.disclosure, Unset):
      disclosure = UNSET
    else:
      disclosure = self.disclosure

    category: None | str | Unset
    if isinstance(self.category, Unset):
      category = UNSET
    else:
      category = self.category

    blocks: list[dict[str, Any]] | None | Unset
    if isinstance(self.blocks, Unset):
      blocks = UNSET
    elif isinstance(self.blocks, list):
      blocks = []
      for blocks_type_0_item_data in self.blocks:
        blocks_type_0_item = blocks_type_0_item_data.to_dict()
        blocks.append(blocks_type_0_item)

    else:
      blocks = self.blocks

    block_count: int | None | Unset
    if isinstance(self.block_count, Unset):
      block_count = UNSET
    else:
      block_count = self.block_count

    note: None | str | Unset
    if isinstance(self.note, Unset):
      note = UNSET
    else:
      note = self.note

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "report_id": report_id,
      }
    )
    if resolved_report is not UNSET:
      field_dict["resolved_report"] = resolved_report
    if disclosures is not UNSET:
      field_dict["disclosures"] = disclosures
    if count is not UNSET:
      field_dict["count"] = count
    if disclosure is not UNSET:
      field_dict["disclosure"] = disclosure
    if category is not UNSET:
      field_dict["category"] = category
    if blocks is not UNSET:
      field_dict["blocks"] = blocks
    if block_count is not UNSET:
      field_dict["block_count"] = block_count
    if note is not UNSET:
      field_dict["note"] = note

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.disclosures_response_blocks_type_0_item import (
      DisclosuresResponseBlocksType0Item,
    )
    from ..models.disclosures_response_disclosures_type_0_item import (
      DisclosuresResponseDisclosuresType0Item,
    )
    from ..models.resolved_report_info import ResolvedReportInfo

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    report_id = d.pop("report_id")

    def _parse_resolved_report(data: object) -> None | ResolvedReportInfo | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        resolved_report_type_0 = ResolvedReportInfo.from_dict(data)

        return resolved_report_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ResolvedReportInfo | Unset, data)

    resolved_report = _parse_resolved_report(d.pop("resolved_report", UNSET))

    def _parse_disclosures(
      data: object,
    ) -> list[DisclosuresResponseDisclosuresType0Item] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        disclosures_type_0 = []
        _disclosures_type_0 = data
        for disclosures_type_0_item_data in _disclosures_type_0:
          disclosures_type_0_item = DisclosuresResponseDisclosuresType0Item.from_dict(
            disclosures_type_0_item_data
          )

          disclosures_type_0.append(disclosures_type_0_item)

        return disclosures_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[DisclosuresResponseDisclosuresType0Item] | None | Unset, data)

    disclosures = _parse_disclosures(d.pop("disclosures", UNSET))

    def _parse_count(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    count = _parse_count(d.pop("count", UNSET))

    def _parse_disclosure(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    disclosure = _parse_disclosure(d.pop("disclosure", UNSET))

    def _parse_category(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    category = _parse_category(d.pop("category", UNSET))

    def _parse_blocks(
      data: object,
    ) -> list[DisclosuresResponseBlocksType0Item] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        blocks_type_0 = []
        _blocks_type_0 = data
        for blocks_type_0_item_data in _blocks_type_0:
          blocks_type_0_item = DisclosuresResponseBlocksType0Item.from_dict(
            blocks_type_0_item_data
          )

          blocks_type_0.append(blocks_type_0_item)

        return blocks_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[DisclosuresResponseBlocksType0Item] | None | Unset, data)

    blocks = _parse_blocks(d.pop("blocks", UNSET))

    def _parse_block_count(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    block_count = _parse_block_count(d.pop("block_count", UNSET))

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    disclosures_response = cls(
      graph_id=graph_id,
      report_id=report_id,
      resolved_report=resolved_report,
      disclosures=disclosures,
      count=count,
      disclosure=disclosure,
      category=category,
      blocks=blocks,
      block_count=block_count,
      note=note,
    )

    disclosures_response.additional_properties = d
    return disclosures_response

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
