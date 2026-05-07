from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.evaluate_rules_response_summary import EvaluateRulesResponseSummary
  from ..models.verification_result_lite import VerificationResultLite


T = TypeVar("T", bound="EvaluateRulesResponse")


@_attrs_define
class EvaluateRulesResponse:
  """Response for the ``evaluate-rules`` operation.

  ``results`` is the full list of :class:`VerificationResultLite` rows
  written by this evaluation run. ``summary`` gives counts keyed by
  status for quick display without iterating the list.

      Attributes:
          structure_id (str):
          results (list[VerificationResultLite]):
          summary (EvaluateRulesResponseSummary | Unset): Status counts keyed by outcome string: ``{'pass': N, 'fail': N,
              'error': N, 'skipped': N}``.
  """

  structure_id: str
  results: list[VerificationResultLite]
  summary: EvaluateRulesResponseSummary | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    structure_id = self.structure_id

    results = []
    for results_item_data in self.results:
      results_item = results_item_data.to_dict()
      results.append(results_item)

    summary: dict[str, Any] | Unset = UNSET
    if not isinstance(self.summary, Unset):
      summary = self.summary.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "structure_id": structure_id,
        "results": results,
      }
    )
    if summary is not UNSET:
      field_dict["summary"] = summary

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.evaluate_rules_response_summary import EvaluateRulesResponseSummary
    from ..models.verification_result_lite import VerificationResultLite

    d = dict(src_dict)
    structure_id = d.pop("structure_id")

    results = []
    _results = d.pop("results")
    for results_item_data in _results:
      results_item = VerificationResultLite.from_dict(results_item_data)

      results.append(results_item)

    _summary = d.pop("summary", UNSET)
    summary: EvaluateRulesResponseSummary | Unset
    if isinstance(_summary, Unset):
      summary = UNSET
    else:
      summary = EvaluateRulesResponseSummary.from_dict(_summary)

    evaluate_rules_response = cls(
      structure_id=structure_id,
      results=results,
      summary=summary,
    )

    evaluate_rules_response.additional_properties = d
    return evaluate_rules_response

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
