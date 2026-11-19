from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportConceptRow")


@_attrs_define
class ReportConceptRow:
  """A concept the report uses that the library may not have.

  Attributes:
      qname (str): Prefixed name, e.g. `rs-gaap:Assets` for a library concept or `kpi:Headcount` for one of the firm's
          own. A prefix other than a library's must be bound in `namespaces`.
      label (None | str | Unset): The line's wording in the report.
      kind (str | Unset): The value's type: `monetary`, `shares`, `percent`, `pure`, `decimal`, `integer`, `string`,
          `text_block`, `date` or `boolean`. Default: 'monetary'.
      period_type (None | str | Unset): `instant` for a balance at a date, `duration` for a flow over a period.
      balance (None | str | Unset): `debit` or `credit`, when monetary.
      abstract (bool | Unset): True for a heading that carries no value of its own. Default: False.
  """

  qname: str
  label: None | str | Unset = UNSET
  kind: str | Unset = "monetary"
  period_type: None | str | Unset = UNSET
  balance: None | str | Unset = UNSET
  abstract: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    qname = self.qname

    label: None | str | Unset
    if isinstance(self.label, Unset):
      label = UNSET
    else:
      label = self.label

    kind = self.kind

    period_type: None | str | Unset
    if isinstance(self.period_type, Unset):
      period_type = UNSET
    else:
      period_type = self.period_type

    balance: None | str | Unset
    if isinstance(self.balance, Unset):
      balance = UNSET
    else:
      balance = self.balance

    abstract = self.abstract

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "qname": qname,
      }
    )
    if label is not UNSET:
      field_dict["label"] = label
    if kind is not UNSET:
      field_dict["kind"] = kind
    if period_type is not UNSET:
      field_dict["period_type"] = period_type
    if balance is not UNSET:
      field_dict["balance"] = balance
    if abstract is not UNSET:
      field_dict["abstract"] = abstract

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    qname = d.pop("qname")

    def _parse_label(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    label = _parse_label(d.pop("label", UNSET))

    kind = d.pop("kind", UNSET)

    def _parse_period_type(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    period_type = _parse_period_type(d.pop("period_type", UNSET))

    def _parse_balance(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    balance = _parse_balance(d.pop("balance", UNSET))

    abstract = d.pop("abstract", UNSET)

    report_concept_row = cls(
      qname=qname,
      label=label,
      kind=kind,
      period_type=period_type,
      balance=balance,
      abstract=abstract,
    )

    report_concept_row.additional_properties = d
    return report_concept_row

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
