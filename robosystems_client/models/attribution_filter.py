from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.line_item_metadata_predicate import LineItemMetadataPredicate


T = TypeVar("T", bound="AttributionFilter")


@_attrs_define
class AttributionFilter:
  """One flow-concept attribution rule on a rollforward IB.

  Pairs a target concept (the flow leaf the matched amount counts
  toward) with a predicate (which LineItems match). The rollforward's
  ``attribution_filters: list[AttributionFilter]`` declares every flow
  the BS source decomposes into; the renderer evaluates them all per
  period.

  ``target_element_id`` is resolved at create time from ``target_qname``
  via the rs-gaap library + tenant taxonomy lookup. Authors only need
  to provide the qname; the element_id is filled in by the create
  handler and the resolved value is what the envelope round-trips.

      Attributes:
          target_qname (str): QName of the flow concept this filter produces facts for — e.g. ``rs-
              gaap:ProceedsFromIssuanceOfCommonStock``. Resolved to ``target_element_id`` at create time.
          predicate (LineItemMetadataPredicate): Filter ledger LineItems whose ``metadata_[field]`` is in ``values``.

              The single predicate kind shipped in Phase 2 MVP. Sufficient for any
              source taxonomy that stamps a flow-tag column on each transaction
              line — mini's ``TransactionDescriptionCode``, future XBRL GL
              ``GenericFlowCategory`` columns, custom tenant tags.

              ``field`` is the JSONB key under ``line_items.metadata`` (e.g.
              ``"transaction_description_code"``). ``values`` is the set of values
              that route to the filter's target concept; matched LineItems aggregate
              signed into the attributed fact for the period.
          target_element_id (None | str | Unset): Resolved element id for ``target_qname``. Null at create time; populated
              by the handler before persistence. Round-tripped in the envelope.
  """

  target_qname: str
  predicate: LineItemMetadataPredicate
  target_element_id: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    target_qname = self.target_qname

    predicate = self.predicate.to_dict()

    target_element_id: None | str | Unset
    if isinstance(self.target_element_id, Unset):
      target_element_id = UNSET
    else:
      target_element_id = self.target_element_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "target_qname": target_qname,
        "predicate": predicate,
      }
    )
    if target_element_id is not UNSET:
      field_dict["target_element_id"] = target_element_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.line_item_metadata_predicate import LineItemMetadataPredicate

    d = dict(src_dict)
    target_qname = d.pop("target_qname")

    predicate = LineItemMetadataPredicate.from_dict(d.pop("predicate"))

    def _parse_target_element_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    target_element_id = _parse_target_element_id(d.pop("target_element_id", UNSET))

    attribution_filter = cls(
      target_qname=target_qname,
      predicate=predicate,
      target_element_id=target_element_id,
    )

    attribution_filter.additional_properties = d
    return attribution_filter

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
