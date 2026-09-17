from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.information_block_response_ancestors_type_0_item import (
    InformationBlockResponseAncestorsType0Item,
  )
  from ..models.information_block_response_axes_type_0_item import (
    InformationBlockResponseAxesType0Item,
  )
  from ..models.information_block_response_block import InformationBlockResponseBlock
  from ..models.information_block_response_calculation_type_0_item import (
    InformationBlockResponseCalculationType0Item,
  )
  from ..models.information_block_response_columns_item import (
    InformationBlockResponseColumnsItem,
  )
  from ..models.information_block_response_rows_item import (
    InformationBlockResponseRowsItem,
  )
  from ..models.information_block_response_text_type_0_item import (
    InformationBlockResponseTextType0Item,
  )
  from ..models.resolved_report_info import ResolvedReportInfo


T = TypeVar("T", bound="InformationBlockResponse")


@_attrs_define
class InformationBlockResponse:
  """The information-block view op's result: xbrlkit's block, stamped.

  Attributes:
      graph_id (str):
      report_id (str):
      block (InformationBlockResponseBlock):
      resolved_report (None | ResolvedReportInfo | Unset):
      columns (list[InformationBlockResponseColumnsItem] | Unset):
      axes (list[InformationBlockResponseAxesType0Item] | None | Unset):
      rows (list[InformationBlockResponseRowsItem] | Unset):
      row_count (int | None | Unset):
      truncated (bool | None | Unset):
      offset (int | None | Unset):
      ancestors (list[InformationBlockResponseAncestorsType0Item] | None | Unset):
      next_offset (int | None | Unset):
      calculation (list[InformationBlockResponseCalculationType0Item] | None | Unset):
      text (list[InformationBlockResponseTextType0Item] | None | Unset):
      note (None | str | Unset):
  """

  graph_id: str
  report_id: str
  block: InformationBlockResponseBlock
  resolved_report: None | ResolvedReportInfo | Unset = UNSET
  columns: list[InformationBlockResponseColumnsItem] | Unset = UNSET
  axes: list[InformationBlockResponseAxesType0Item] | None | Unset = UNSET
  rows: list[InformationBlockResponseRowsItem] | Unset = UNSET
  row_count: int | None | Unset = UNSET
  truncated: bool | None | Unset = UNSET
  offset: int | None | Unset = UNSET
  ancestors: list[InformationBlockResponseAncestorsType0Item] | None | Unset = UNSET
  next_offset: int | None | Unset = UNSET
  calculation: list[InformationBlockResponseCalculationType0Item] | None | Unset = UNSET
  text: list[InformationBlockResponseTextType0Item] | None | Unset = UNSET
  note: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.resolved_report_info import ResolvedReportInfo

    graph_id = self.graph_id

    report_id = self.report_id

    block = self.block.to_dict()

    resolved_report: dict[str, Any] | None | Unset
    if isinstance(self.resolved_report, Unset):
      resolved_report = UNSET
    elif isinstance(self.resolved_report, ResolvedReportInfo):
      resolved_report = self.resolved_report.to_dict()
    else:
      resolved_report = self.resolved_report

    columns: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.columns, Unset):
      columns = []
      for columns_item_data in self.columns:
        columns_item = columns_item_data.to_dict()
        columns.append(columns_item)

    axes: list[dict[str, Any]] | None | Unset
    if isinstance(self.axes, Unset):
      axes = UNSET
    elif isinstance(self.axes, list):
      axes = []
      for axes_type_0_item_data in self.axes:
        axes_type_0_item = axes_type_0_item_data.to_dict()
        axes.append(axes_type_0_item)

    else:
      axes = self.axes

    rows: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.rows, Unset):
      rows = []
      for rows_item_data in self.rows:
        rows_item = rows_item_data.to_dict()
        rows.append(rows_item)

    row_count: int | None | Unset
    if isinstance(self.row_count, Unset):
      row_count = UNSET
    else:
      row_count = self.row_count

    truncated: bool | None | Unset
    if isinstance(self.truncated, Unset):
      truncated = UNSET
    else:
      truncated = self.truncated

    offset: int | None | Unset
    if isinstance(self.offset, Unset):
      offset = UNSET
    else:
      offset = self.offset

    ancestors: list[dict[str, Any]] | None | Unset
    if isinstance(self.ancestors, Unset):
      ancestors = UNSET
    elif isinstance(self.ancestors, list):
      ancestors = []
      for ancestors_type_0_item_data in self.ancestors:
        ancestors_type_0_item = ancestors_type_0_item_data.to_dict()
        ancestors.append(ancestors_type_0_item)

    else:
      ancestors = self.ancestors

    next_offset: int | None | Unset
    if isinstance(self.next_offset, Unset):
      next_offset = UNSET
    else:
      next_offset = self.next_offset

    calculation: list[dict[str, Any]] | None | Unset
    if isinstance(self.calculation, Unset):
      calculation = UNSET
    elif isinstance(self.calculation, list):
      calculation = []
      for calculation_type_0_item_data in self.calculation:
        calculation_type_0_item = calculation_type_0_item_data.to_dict()
        calculation.append(calculation_type_0_item)

    else:
      calculation = self.calculation

    text: list[dict[str, Any]] | None | Unset
    if isinstance(self.text, Unset):
      text = UNSET
    elif isinstance(self.text, list):
      text = []
      for text_type_0_item_data in self.text:
        text_type_0_item = text_type_0_item_data.to_dict()
        text.append(text_type_0_item)

    else:
      text = self.text

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
        "block": block,
      }
    )
    if resolved_report is not UNSET:
      field_dict["resolved_report"] = resolved_report
    if columns is not UNSET:
      field_dict["columns"] = columns
    if axes is not UNSET:
      field_dict["axes"] = axes
    if rows is not UNSET:
      field_dict["rows"] = rows
    if row_count is not UNSET:
      field_dict["row_count"] = row_count
    if truncated is not UNSET:
      field_dict["truncated"] = truncated
    if offset is not UNSET:
      field_dict["offset"] = offset
    if ancestors is not UNSET:
      field_dict["ancestors"] = ancestors
    if next_offset is not UNSET:
      field_dict["next_offset"] = next_offset
    if calculation is not UNSET:
      field_dict["calculation"] = calculation
    if text is not UNSET:
      field_dict["text"] = text
    if note is not UNSET:
      field_dict["note"] = note

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.information_block_response_ancestors_type_0_item import (
      InformationBlockResponseAncestorsType0Item,
    )
    from ..models.information_block_response_axes_type_0_item import (
      InformationBlockResponseAxesType0Item,
    )
    from ..models.information_block_response_block import InformationBlockResponseBlock
    from ..models.information_block_response_calculation_type_0_item import (
      InformationBlockResponseCalculationType0Item,
    )
    from ..models.information_block_response_columns_item import (
      InformationBlockResponseColumnsItem,
    )
    from ..models.information_block_response_rows_item import (
      InformationBlockResponseRowsItem,
    )
    from ..models.information_block_response_text_type_0_item import (
      InformationBlockResponseTextType0Item,
    )
    from ..models.resolved_report_info import ResolvedReportInfo

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    report_id = d.pop("report_id")

    block = InformationBlockResponseBlock.from_dict(d.pop("block"))

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

    _columns = d.pop("columns", UNSET)
    columns: list[InformationBlockResponseColumnsItem] | Unset = UNSET
    if _columns is not UNSET:
      columns = []
      for columns_item_data in _columns:
        columns_item = InformationBlockResponseColumnsItem.from_dict(columns_item_data)

        columns.append(columns_item)

    def _parse_axes(
      data: object,
    ) -> list[InformationBlockResponseAxesType0Item] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        axes_type_0 = []
        _axes_type_0 = data
        for axes_type_0_item_data in _axes_type_0:
          axes_type_0_item = InformationBlockResponseAxesType0Item.from_dict(
            axes_type_0_item_data
          )

          axes_type_0.append(axes_type_0_item)

        return axes_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[InformationBlockResponseAxesType0Item] | None | Unset, data)

    axes = _parse_axes(d.pop("axes", UNSET))

    _rows = d.pop("rows", UNSET)
    rows: list[InformationBlockResponseRowsItem] | Unset = UNSET
    if _rows is not UNSET:
      rows = []
      for rows_item_data in _rows:
        rows_item = InformationBlockResponseRowsItem.from_dict(rows_item_data)

        rows.append(rows_item)

    def _parse_row_count(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    row_count = _parse_row_count(d.pop("row_count", UNSET))

    def _parse_truncated(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    truncated = _parse_truncated(d.pop("truncated", UNSET))

    def _parse_offset(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    offset = _parse_offset(d.pop("offset", UNSET))

    def _parse_ancestors(
      data: object,
    ) -> list[InformationBlockResponseAncestorsType0Item] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        ancestors_type_0 = []
        _ancestors_type_0 = data
        for ancestors_type_0_item_data in _ancestors_type_0:
          ancestors_type_0_item = InformationBlockResponseAncestorsType0Item.from_dict(
            ancestors_type_0_item_data
          )

          ancestors_type_0.append(ancestors_type_0_item)

        return ancestors_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[InformationBlockResponseAncestorsType0Item] | None | Unset, data)

    ancestors = _parse_ancestors(d.pop("ancestors", UNSET))

    def _parse_next_offset(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    next_offset = _parse_next_offset(d.pop("next_offset", UNSET))

    def _parse_calculation(
      data: object,
    ) -> list[InformationBlockResponseCalculationType0Item] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        calculation_type_0 = []
        _calculation_type_0 = data
        for calculation_type_0_item_data in _calculation_type_0:
          calculation_type_0_item = (
            InformationBlockResponseCalculationType0Item.from_dict(
              calculation_type_0_item_data
            )
          )

          calculation_type_0.append(calculation_type_0_item)

        return calculation_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(
        list[InformationBlockResponseCalculationType0Item] | None | Unset, data
      )

    calculation = _parse_calculation(d.pop("calculation", UNSET))

    def _parse_text(
      data: object,
    ) -> list[InformationBlockResponseTextType0Item] | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        text_type_0 = []
        _text_type_0 = data
        for text_type_0_item_data in _text_type_0:
          text_type_0_item = InformationBlockResponseTextType0Item.from_dict(
            text_type_0_item_data
          )

          text_type_0.append(text_type_0_item)

        return text_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(list[InformationBlockResponseTextType0Item] | None | Unset, data)

    text = _parse_text(d.pop("text", UNSET))

    def _parse_note(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    note = _parse_note(d.pop("note", UNSET))

    information_block_response = cls(
      graph_id=graph_id,
      report_id=report_id,
      block=block,
      resolved_report=resolved_report,
      columns=columns,
      axes=axes,
      rows=rows,
      row_count=row_count,
      truncated=truncated,
      offset=offset,
      ancestors=ancestors,
      next_offset=next_offset,
      calculation=calculation,
      text=text,
      note=note,
    )

    information_block_response.additional_properties = d
    return information_block_response

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
