from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.describe_filing_response_counts_type_0 import (
    DescribeFilingResponseCountsType0,
  )
  from ..models.describe_filing_response_entity_type_0 import (
    DescribeFilingResponseEntityType0,
  )
  from ..models.describe_filing_response_filing_type_0 import (
    DescribeFilingResponseFilingType0,
  )
  from ..models.describe_filing_response_profile_type_0 import (
    DescribeFilingResponseProfileType0,
  )
  from ..models.describe_filing_response_resolved_report_type_0 import (
    DescribeFilingResponseResolvedReportType0,
  )
  from ..models.describe_filing_response_sections_type_0 import (
    DescribeFilingResponseSectionsType0,
  )


T = TypeVar("T", bound="DescribeFilingResponse")


@_attrs_define
class DescribeFilingResponse:
  """The describe-filing view op's result: xbrlkit's layout of the filing.

  Attributes:
      graph_id (str):
      report_id (None | str | Unset):
      accession (None | str | Unset):
      resolved_report (DescribeFilingResponseResolvedReportType0 | None | Unset):
      profile (DescribeFilingResponseProfileType0 | None | Unset):
      filing (DescribeFilingResponseFilingType0 | None | Unset):
      entity (DescribeFilingResponseEntityType0 | None | Unset):
      counts (DescribeFilingResponseCountsType0 | None | Unset):
      sections (DescribeFilingResponseSectionsType0 | None | Unset):
  """

  graph_id: str
  report_id: None | str | Unset = UNSET
  accession: None | str | Unset = UNSET
  resolved_report: DescribeFilingResponseResolvedReportType0 | None | Unset = UNSET
  profile: DescribeFilingResponseProfileType0 | None | Unset = UNSET
  filing: DescribeFilingResponseFilingType0 | None | Unset = UNSET
  entity: DescribeFilingResponseEntityType0 | None | Unset = UNSET
  counts: DescribeFilingResponseCountsType0 | None | Unset = UNSET
  sections: DescribeFilingResponseSectionsType0 | None | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.describe_filing_response_counts_type_0 import (
      DescribeFilingResponseCountsType0,
    )
    from ..models.describe_filing_response_entity_type_0 import (
      DescribeFilingResponseEntityType0,
    )
    from ..models.describe_filing_response_filing_type_0 import (
      DescribeFilingResponseFilingType0,
    )
    from ..models.describe_filing_response_profile_type_0 import (
      DescribeFilingResponseProfileType0,
    )
    from ..models.describe_filing_response_resolved_report_type_0 import (
      DescribeFilingResponseResolvedReportType0,
    )
    from ..models.describe_filing_response_sections_type_0 import (
      DescribeFilingResponseSectionsType0,
    )

    graph_id = self.graph_id

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
    elif isinstance(self.resolved_report, DescribeFilingResponseResolvedReportType0):
      resolved_report = self.resolved_report.to_dict()
    else:
      resolved_report = self.resolved_report

    profile: dict[str, Any] | None | Unset
    if isinstance(self.profile, Unset):
      profile = UNSET
    elif isinstance(self.profile, DescribeFilingResponseProfileType0):
      profile = self.profile.to_dict()
    else:
      profile = self.profile

    filing: dict[str, Any] | None | Unset
    if isinstance(self.filing, Unset):
      filing = UNSET
    elif isinstance(self.filing, DescribeFilingResponseFilingType0):
      filing = self.filing.to_dict()
    else:
      filing = self.filing

    entity: dict[str, Any] | None | Unset
    if isinstance(self.entity, Unset):
      entity = UNSET
    elif isinstance(self.entity, DescribeFilingResponseEntityType0):
      entity = self.entity.to_dict()
    else:
      entity = self.entity

    counts: dict[str, Any] | None | Unset
    if isinstance(self.counts, Unset):
      counts = UNSET
    elif isinstance(self.counts, DescribeFilingResponseCountsType0):
      counts = self.counts.to_dict()
    else:
      counts = self.counts

    sections: dict[str, Any] | None | Unset
    if isinstance(self.sections, Unset):
      sections = UNSET
    elif isinstance(self.sections, DescribeFilingResponseSectionsType0):
      sections = self.sections.to_dict()
    else:
      sections = self.sections

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
      }
    )
    if report_id is not UNSET:
      field_dict["report_id"] = report_id
    if accession is not UNSET:
      field_dict["accession"] = accession
    if resolved_report is not UNSET:
      field_dict["resolved_report"] = resolved_report
    if profile is not UNSET:
      field_dict["profile"] = profile
    if filing is not UNSET:
      field_dict["filing"] = filing
    if entity is not UNSET:
      field_dict["entity"] = entity
    if counts is not UNSET:
      field_dict["counts"] = counts
    if sections is not UNSET:
      field_dict["sections"] = sections

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.describe_filing_response_counts_type_0 import (
      DescribeFilingResponseCountsType0,
    )
    from ..models.describe_filing_response_entity_type_0 import (
      DescribeFilingResponseEntityType0,
    )
    from ..models.describe_filing_response_filing_type_0 import (
      DescribeFilingResponseFilingType0,
    )
    from ..models.describe_filing_response_profile_type_0 import (
      DescribeFilingResponseProfileType0,
    )
    from ..models.describe_filing_response_resolved_report_type_0 import (
      DescribeFilingResponseResolvedReportType0,
    )
    from ..models.describe_filing_response_sections_type_0 import (
      DescribeFilingResponseSectionsType0,
    )

    d = dict(src_dict)
    graph_id = d.pop("graph_id")

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
    ) -> DescribeFilingResponseResolvedReportType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        resolved_report_type_0 = DescribeFilingResponseResolvedReportType0.from_dict(
          data
        )

        return resolved_report_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(DescribeFilingResponseResolvedReportType0 | None | Unset, data)

    resolved_report = _parse_resolved_report(d.pop("resolved_report", UNSET))

    def _parse_profile(
      data: object,
    ) -> DescribeFilingResponseProfileType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        profile_type_0 = DescribeFilingResponseProfileType0.from_dict(data)

        return profile_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(DescribeFilingResponseProfileType0 | None | Unset, data)

    profile = _parse_profile(d.pop("profile", UNSET))

    def _parse_filing(data: object) -> DescribeFilingResponseFilingType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        filing_type_0 = DescribeFilingResponseFilingType0.from_dict(data)

        return filing_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(DescribeFilingResponseFilingType0 | None | Unset, data)

    filing = _parse_filing(d.pop("filing", UNSET))

    def _parse_entity(data: object) -> DescribeFilingResponseEntityType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        entity_type_0 = DescribeFilingResponseEntityType0.from_dict(data)

        return entity_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(DescribeFilingResponseEntityType0 | None | Unset, data)

    entity = _parse_entity(d.pop("entity", UNSET))

    def _parse_counts(data: object) -> DescribeFilingResponseCountsType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        counts_type_0 = DescribeFilingResponseCountsType0.from_dict(data)

        return counts_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(DescribeFilingResponseCountsType0 | None | Unset, data)

    counts = _parse_counts(d.pop("counts", UNSET))

    def _parse_sections(
      data: object,
    ) -> DescribeFilingResponseSectionsType0 | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        sections_type_0 = DescribeFilingResponseSectionsType0.from_dict(data)

        return sections_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(DescribeFilingResponseSectionsType0 | None | Unset, data)

    sections = _parse_sections(d.pop("sections", UNSET))

    describe_filing_response = cls(
      graph_id=graph_id,
      report_id=report_id,
      accession=accession,
      resolved_report=resolved_report,
      profile=profile,
      filing=filing,
      entity=entity,
      counts=counts,
      sections=sections,
    )

    describe_filing_response.additional_properties = d
    return describe_filing_response

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
