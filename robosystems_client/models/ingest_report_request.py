from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.report_rows_input import ReportRowsInput


T = TypeVar("T", bound="IngestReportRequest")


@_attrs_define
class IngestReportRequest:
  """CQRS body for `POST /operations/ingest-report`.

  Give exactly one of `holon` (a report file already in the holon format),
  `tavi` (a Tavi compiled model) or `report` (rows read from a PDF or a
  workbook, which the server assembles into a holon). Every route ends in a
  holon that is checked, stored as the record of what was received, and
  loaded onto the entity.

      Attributes:
          entity_id (str): The entity the report is about (see `create-issuer`).
          holon (None | str | Unset): The text of a `.holon.jsonld` report file.
          tavi (None | str | Unset): The text of a `.tavi.json` compiled model. It is converted to a holon, which is what
              is stored.
          report (None | ReportRowsInput | Unset): The report as rows.
          name (None | str | Unset): A display name for the report.
          require_source (bool | Unset): Refuse the report unless every value names its source. Default: False.
          dry_run (bool | Unset): Check the report and say what would load, without writing anything. Default: False.
  """

  entity_id: str
  holon: None | str | Unset = UNSET
  tavi: None | str | Unset = UNSET
  report: None | ReportRowsInput | Unset = UNSET
  name: None | str | Unset = UNSET
  require_source: bool | Unset = False
  dry_run: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.report_rows_input import ReportRowsInput

    entity_id = self.entity_id

    holon: None | str | Unset
    if isinstance(self.holon, Unset):
      holon = UNSET
    else:
      holon = self.holon

    tavi: None | str | Unset
    if isinstance(self.tavi, Unset):
      tavi = UNSET
    else:
      tavi = self.tavi

    report: dict[str, Any] | None | Unset
    if isinstance(self.report, Unset):
      report = UNSET
    elif isinstance(self.report, ReportRowsInput):
      report = self.report.to_dict()
    else:
      report = self.report

    name: None | str | Unset
    if isinstance(self.name, Unset):
      name = UNSET
    else:
      name = self.name

    require_source = self.require_source

    dry_run = self.dry_run

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
      }
    )
    if holon is not UNSET:
      field_dict["holon"] = holon
    if tavi is not UNSET:
      field_dict["tavi"] = tavi
    if report is not UNSET:
      field_dict["report"] = report
    if name is not UNSET:
      field_dict["name"] = name
    if require_source is not UNSET:
      field_dict["require_source"] = require_source
    if dry_run is not UNSET:
      field_dict["dry_run"] = dry_run

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.report_rows_input import ReportRowsInput

    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    def _parse_holon(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    holon = _parse_holon(d.pop("holon", UNSET))

    def _parse_tavi(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    tavi = _parse_tavi(d.pop("tavi", UNSET))

    def _parse_report(data: object) -> None | ReportRowsInput | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        report_type_0 = ReportRowsInput.from_dict(data)

        return report_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | ReportRowsInput | Unset, data)

    report = _parse_report(d.pop("report", UNSET))

    def _parse_name(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    name = _parse_name(d.pop("name", UNSET))

    require_source = d.pop("require_source", UNSET)

    dry_run = d.pop("dry_run", UNSET)

    ingest_report_request = cls(
      entity_id=entity_id,
      holon=holon,
      tavi=tavi,
      report=report,
      name=name,
      require_source=require_source,
      dry_run=dry_run,
    )

    ingest_report_request.additional_properties = d
    return ingest_report_request

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
