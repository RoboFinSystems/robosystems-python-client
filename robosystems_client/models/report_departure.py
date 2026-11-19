from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_departure_kind import ReportDepartureKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportDeparture")


@_attrs_define
class ReportDeparture:
  """One place a report sent as rows arranges a primary statement differently
  than the library does.

      Attributes:
          section (str): The section it is in.
          kind (ReportDepartureKind): moved: a library concept sits under a different line, or with a different sign, than
              the library gives it. placed: a library concept the library does not put on this statement was given a line.
              own_subtotal: a concept of the firm's own has library concepts beneath it. own_layout: the whole statement came
              with its own lines.
          detail (str): The departure as a sentence.
          concept (None | str | Unset): The concept, when it is about one.
          library_parent (None | str | Unset): For `moved`: the line the library puts it under.
          parent (None | str | Unset): The line the report puts it under.
  """

  section: str
  kind: ReportDepartureKind
  detail: str
  concept: None | str | Unset = UNSET
  library_parent: None | str | Unset = UNSET
  parent: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    section = self.section

    kind = self.kind.value

    detail = self.detail

    concept: None | str | Unset
    if isinstance(self.concept, Unset):
      concept = UNSET
    else:
      concept = self.concept

    library_parent: None | str | Unset
    if isinstance(self.library_parent, Unset):
      library_parent = UNSET
    else:
      library_parent = self.library_parent

    parent: None | str | Unset
    if isinstance(self.parent, Unset):
      parent = UNSET
    else:
      parent = self.parent

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "section": section,
        "kind": kind,
        "detail": detail,
      }
    )
    if concept is not UNSET:
      field_dict["concept"] = concept
    if library_parent is not UNSET:
      field_dict["library_parent"] = library_parent
    if parent is not UNSET:
      field_dict["parent"] = parent

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    section = d.pop("section")

    kind = ReportDepartureKind(d.pop("kind"))

    detail = d.pop("detail")

    def _parse_concept(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    concept = _parse_concept(d.pop("concept", UNSET))

    def _parse_library_parent(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    library_parent = _parse_library_parent(d.pop("library_parent", UNSET))

    def _parse_parent(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    parent = _parse_parent(d.pop("parent", UNSET))

    report_departure = cls(
      section=section,
      kind=kind,
      detail=detail,
      concept=concept,
      library_parent=library_parent,
      parent=parent,
    )

    report_departure.additional_properties = d
    return report_departure

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
