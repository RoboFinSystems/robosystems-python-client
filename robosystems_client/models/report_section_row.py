from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_section_row_layout_type_0 import ReportSectionRowLayoutType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.report_line_row import ReportLineRow


T = TypeVar("T", bound="ReportSectionRow")


@_attrs_define
class ReportSectionRow:
  """A statement or a table of the report.

  Attributes:
      name (str): The section's title, e.g. `Balance Sheet`.
      block_type (None | str | Unset): `balance_sheet`, `income_statement`, `cash_flow_statement` or
          `equity_statement` for a primary statement; omit for any other table.
      head (None | str | Unset): An abstract concept the section's top lines hang from. Required when a top line has
          nothing beneath it, as in a flat KPI table.
      layout (None | ReportSectionRowLayoutType0 | Unset): `library` lays a `balance_sheet` or an `income_statement`
          out from the library: every value sent for a concept the statement places becomes a line under the nearest line
          above it that also has a value, and each total is checked against the lines beneath it. `given` uses `lines`
          exactly as sent. Omitted, it is `library` when there are no `lines` and `given` when there are.
      lines (list[ReportLineRow] | Unset): The lines, in order. With `layout: library` these are only the lines the
          library cannot place, or places differently than the document: a concept of the firm's own, each with the
          `parent` it sits under (a line of the statement that has a value) and its `weight`. A line given here replaces
          the library's placement of that concept.
  """

  name: str
  block_type: None | str | Unset = UNSET
  head: None | str | Unset = UNSET
  layout: None | ReportSectionRowLayoutType0 | Unset = UNSET
  lines: list[ReportLineRow] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    block_type: None | str | Unset
    if isinstance(self.block_type, Unset):
      block_type = UNSET
    else:
      block_type = self.block_type

    head: None | str | Unset
    if isinstance(self.head, Unset):
      head = UNSET
    else:
      head = self.head

    layout: None | str | Unset
    if isinstance(self.layout, Unset):
      layout = UNSET
    elif isinstance(self.layout, ReportSectionRowLayoutType0):
      layout = self.layout.value
    else:
      layout = self.layout

    lines: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.lines, Unset):
      lines = []
      for lines_item_data in self.lines:
        lines_item = lines_item_data.to_dict()
        lines.append(lines_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
      }
    )
    if block_type is not UNSET:
      field_dict["block_type"] = block_type
    if head is not UNSET:
      field_dict["head"] = head
    if layout is not UNSET:
      field_dict["layout"] = layout
    if lines is not UNSET:
      field_dict["lines"] = lines

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.report_line_row import ReportLineRow

    d = dict(src_dict)
    name = d.pop("name")

    def _parse_block_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    block_type = _parse_block_type(d.pop("block_type", UNSET))

    def _parse_head(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    head = _parse_head(d.pop("head", UNSET))

    def _parse_layout(data: object) -> None | ReportSectionRowLayoutType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        layout_type_0 = ReportSectionRowLayoutType0(data)

        return layout_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ReportSectionRowLayoutType0 | Unset, data)

    layout = _parse_layout(d.pop("layout", UNSET))

    _lines = d.pop("lines", UNSET)
    lines: list[ReportLineRow] | Unset = UNSET
    if _lines is not UNSET:
      lines = []
      for lines_item_data in _lines:
        lines_item = ReportLineRow.from_dict(lines_item_data)

        lines.append(lines_item)

    report_section_row = cls(
      name=name,
      block_type=block_type,
      head=head,
      layout=layout,
      lines=lines,
    )

    report_section_row.additional_properties = d
    return report_section_row

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
