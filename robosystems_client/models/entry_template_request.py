from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entry_template_request_entry_type import EntryTemplateRequestEntryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.schedule_leg_request import ScheduleLegRequest


T = TypeVar("T", bound="EntryTemplateRequest")


@_attrs_define
class EntryTemplateRequest:
  """
  Attributes:
      debit_element_id (str): CoA element id to debit (e.g. Depreciation Expense). This is a chart-of-accounts element
          id — the `id` returned by get-unmapped-elements / get-graph-schema — NOT a taxonomy qname.
      credit_element_id (str): CoA element id to credit (e.g. Accumulated Depreciation). A chart-of-accounts element
          id (see get-unmapped-elements), not a taxonomy qname. A straight-line or custom schedule posts this one
          debit/credit pair; a loan schedule posts its `legs`.
      entry_type (EntryTemplateRequestEntryType | Unset): Entry type for generated entries Default:
          EntryTemplateRequestEntryType.CLOSING.
      memo_template (str | Unset): Memo template ({structure_name} is replaced) Default: ''.
      auto_reverse (bool | Unset): Auto-generate a reversing entry on the first day of the next period Default: False.
      dimension_ids (list[str] | Unset): The management dimension members (department, class, location, project) every
          entry the schedule drafts carries on both lines, one per axis: a department's depreciation lands in that
          department.
      legs (list[ScheduleLegRequest] | Unset): The lines of a loan schedule's entry (`method='effective_interest'`
          only), each taking one column of the amortization table; each period's lines must balance. Accrue interest and
          pay through the bank: debit Interest Expense and credit Accrued Interest, both `interest`. The schedule settles
          the payment itself: debit the note `principal`, debit Interest Expense `interest`, credit cash or a due-to
          `payment`. `debit_element_id` names the interest debit leg and `credit_element_id` one credit leg. Empty for
          every other method, which posts the debit/credit pair.
  """

  debit_element_id: str
  credit_element_id: str
  entry_type: EntryTemplateRequestEntryType | Unset = (
    EntryTemplateRequestEntryType.CLOSING
  )
  memo_template: str | Unset = ""
  auto_reverse: bool | Unset = False
  dimension_ids: list[str] | Unset = UNSET
  legs: list[ScheduleLegRequest] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    debit_element_id = self.debit_element_id

    credit_element_id = self.credit_element_id

    entry_type: str | Unset = UNSET
    if not isinstance(self.entry_type, Unset):
      entry_type = self.entry_type.value

    memo_template = self.memo_template

    auto_reverse = self.auto_reverse

    dimension_ids: list[str] | Unset = UNSET
    if not isinstance(self.dimension_ids, Unset):
      dimension_ids = self.dimension_ids

    legs: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.legs, Unset):
      legs = []
      for legs_item_data in self.legs:
        legs_item = legs_item_data.to_dict()
        legs.append(legs_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "debit_element_id": debit_element_id,
        "credit_element_id": credit_element_id,
      }
    )
    if entry_type is not UNSET:
      field_dict["entry_type"] = entry_type
    if memo_template is not UNSET:
      field_dict["memo_template"] = memo_template
    if auto_reverse is not UNSET:
      field_dict["auto_reverse"] = auto_reverse
    if dimension_ids is not UNSET:
      field_dict["dimension_ids"] = dimension_ids
    if legs is not UNSET:
      field_dict["legs"] = legs

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.schedule_leg_request import ScheduleLegRequest

    d = dict(src_dict)
    debit_element_id = d.pop("debit_element_id")

    credit_element_id = d.pop("credit_element_id")

    _entry_type = d.pop("entry_type", UNSET)
    entry_type: EntryTemplateRequestEntryType | Unset
    if isinstance(_entry_type, Unset):
      entry_type = UNSET
    else:
      entry_type = EntryTemplateRequestEntryType(_entry_type)

    memo_template = d.pop("memo_template", UNSET)

    auto_reverse = d.pop("auto_reverse", UNSET)

    dimension_ids = cast(list[str], d.pop("dimension_ids", UNSET))

    _legs = d.pop("legs", UNSET)
    legs: list[ScheduleLegRequest] | Unset = UNSET
    if _legs is not UNSET:
      legs = []
      for legs_item_data in _legs:
        legs_item = ScheduleLegRequest.from_dict(legs_item_data)

        legs.append(legs_item)

    entry_template_request = cls(
      debit_element_id=debit_element_id,
      credit_element_id=credit_element_id,
      entry_type=entry_type,
      memo_template=memo_template,
      auto_reverse=auto_reverse,
      dimension_ids=dimension_ids,
      legs=legs,
    )

    entry_template_request.additional_properties = d
    return entry_template_request

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
