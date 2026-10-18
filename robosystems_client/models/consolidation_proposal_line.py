from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsolidationProposalLine")


@_attrs_define
class ConsolidationProposalLine:
  """One line of a proposed consolidating entry, in the consolidation
  entity's chart.

      Attributes:
          element_id (str): The consolidation entity's account.
          account_name (str): The account's name.
          concept (str): The rs-gaap concept the account maps to.
          debit_amount (int | Unset): Debit, in cents. Default: 0.
          credit_amount (int | Unset): Credit, in cents. Default: 0.
          flow_qname (None | str | Unset): The cash flow row the line offsets, when it eliminates one: the row the
              member's own line produced, so the consolidated cash flow nets it.
  """

  element_id: str
  account_name: str
  concept: str
  debit_amount: int | Unset = 0
  credit_amount: int | Unset = 0
  flow_qname: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    element_id = self.element_id

    account_name = self.account_name

    concept = self.concept

    debit_amount = self.debit_amount

    credit_amount = self.credit_amount

    flow_qname: None | str | Unset
    if isinstance(self.flow_qname, Unset):
      flow_qname = UNSET
    else:
      flow_qname = self.flow_qname

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "element_id": element_id,
        "account_name": account_name,
        "concept": concept,
      }
    )
    if debit_amount is not UNSET:
      field_dict["debit_amount"] = debit_amount
    if credit_amount is not UNSET:
      field_dict["credit_amount"] = credit_amount
    if flow_qname is not UNSET:
      field_dict["flow_qname"] = flow_qname

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    element_id = d.pop("element_id")

    account_name = d.pop("account_name")

    concept = d.pop("concept")

    debit_amount = d.pop("debit_amount", UNSET)

    credit_amount = d.pop("credit_amount", UNSET)

    def _parse_flow_qname(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    flow_qname = _parse_flow_qname(d.pop("flow_qname", UNSET))

    consolidation_proposal_line = cls(
      element_id=element_id,
      account_name=account_name,
      concept=concept,
      debit_amount=debit_amount,
      credit_amount=credit_amount,
      flow_qname=flow_qname,
    )

    consolidation_proposal_line.additional_properties = d
    return consolidation_proposal_line

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
