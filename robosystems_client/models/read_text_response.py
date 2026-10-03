from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.read_text_response_resolved_report_type_0 import (
    ReadTextResponseResolvedReportType0,
  )


T = TypeVar("T", bound="ReadTextResponse")


@_attrs_define
class ReadTextResponse:
  """The read-text view op's result: one window of the filing's text.

  Attributes:
      graph_id (str):
      offset (int):
      length (int):
      text (str):
      text_chars (int):
      report_id (None | str | Unset):
      accession (None | str | Unset):
      resolved_report (None | ReadTextResponseResolvedReportType0 | Unset):
      next_offset (int | None | Unset):
      section (None | str | Unset):
  """

  graph_id: str
  offset: int
  length: int
  text: str
  text_chars: int
  report_id: None | str | Unset = UNSET
  accession: None | str | Unset = UNSET
  resolved_report: None | ReadTextResponseResolvedReportType0 | Unset = UNSET
  next_offset: int | None | Unset = UNSET
  section: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.read_text_response_resolved_report_type_0 import (
      ReadTextResponseResolvedReportType0,
    )

    graph_id = self.graph_id

    offset = self.offset

    length = self.length

    text = self.text

    text_chars = self.text_chars

    report_id: None | str | Unset
    if isinstance(self.report_id, Unset):
      report_id = UNSET
    else:
      report_id = self.report_id

    accession: None | str | Unset
    if isinstance(self.accession, Unset):
      accession = UNSET
    else:
      accession = self.accession

    resolved_report: dict[str, Any] | None | Unset
    if isinstance(self.resolved_report, Unset):
      resolved_report = UNSET
    elif isinstance(self.resolved_report, ReadTextResponseResolvedReportType0):
      resolved_report = self.resolved_report.to_dict()
    else:
      resolved_report = self.resolved_report

    next_offset: int | None | Unset
    if isinstance(self.next_offset, Unset):
      next_offset = UNSET
    else:
      next_offset = self.next_offset

    section: None | str | Unset
    if isinstance(self.section, Unset):
      section = UNSET
    else:
      section = self.section

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "offset": offset,
        "length": length,
        "text": text,
        "text_chars": text_chars,
      }
    )
    if report_id is not UNSET:
      field_dict["report_id"] = report_id
    if accession is not UNSET:
      field_dict["accession"] = accession
    if resolved_report is not UNSET:
      field_dict["resolved_report"] = resolved_report
    if next_offset is not UNSET:
      field_dict["next_offset"] = next_offset
    if section is not UNSET:
      field_dict["section"] = section

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.read_text_response_resolved_report_type_0 import (
      ReadTextResponseResolvedReportType0,
    )

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    offset = d.pop("offset")

    length = d.pop("length")

    text = d.pop("text")

    text_chars = d.pop("text_chars")

    def _parse_report_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    report_id = _parse_report_id(d.pop("report_id", UNSET))

    def _parse_accession(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    accession = _parse_accession(d.pop("accession", UNSET))

    def _parse_resolved_report(
      data: object,
    ) -> None | ReadTextResponseResolvedReportType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        resolved_report_type_0 = ReadTextResponseResolvedReportType0.from_dict(data)

        return resolved_report_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ReadTextResponseResolvedReportType0 | Unset, data)

    resolved_report = _parse_resolved_report(d.pop("resolved_report", UNSET))

    def _parse_next_offset(data: object) -> int | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(int | None | Unset, data)

    next_offset = _parse_next_offset(d.pop("next_offset", UNSET))

    def _parse_section(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    section = _parse_section(d.pop("section", UNSET))

    read_text_response = cls(
      graph_id=graph_id,
      offset=offset,
      length=length,
      text=text,
      text_chars=text_chars,
      report_id=report_id,
      accession=accession,
      resolved_report=resolved_report,
      next_offset=next_offset,
      section=section,
    )

    read_text_response.additional_properties = d
    return read_text_response

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
