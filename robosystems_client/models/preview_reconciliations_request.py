from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preview_reconciliations_request_method import (
  PreviewReconciliationsRequestMethod,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewReconciliationsRequest")


@_attrs_define
class PreviewReconciliationsRequest:
  """Compare the ledger's balances at a period end with an independent source.

  Attributes:
      period (str): Period to compare at its last day, as YYYY-MM.
      method (PreviewReconciliationsRequestMethod | Unset): Which check to preview. `source_ledger` compares every
          account with the synced accounting system's own trial balance. `schedule_register` compares each asset account a
          schedule carries a balance on with what its schedules say it holds. `statement` compares each account that has a
          statement balance recorded in the period with that balance. Default:
          PreviewReconciliationsRequestMethod.SOURCE_LEDGER.
      include_tied (bool | Unset): Also return the accounts that tie. Off by default: the differences are the work,
          and the counts cover the rest. Default: False.
  """

  period: str
  method: PreviewReconciliationsRequestMethod | Unset = (
    PreviewReconciliationsRequestMethod.SOURCE_LEDGER
  )
  include_tied: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    period = self.period

    method: str | Unset = UNSET
    if not isinstance(self.method, Unset):
      method = self.method.value

    include_tied = self.include_tied

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "period": period,
      }
    )
    if method is not UNSET:
      field_dict["method"] = method
    if include_tied is not UNSET:
      field_dict["include_tied"] = include_tied

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    period = d.pop("period")

    _method = d.pop("method", UNSET)
    method: PreviewReconciliationsRequestMethod | Unset
    if isinstance(_method, Unset):
      method = UNSET
    else:
      method = PreviewReconciliationsRequestMethod(_method)

    include_tied = d.pop("include_tied", UNSET)

    preview_reconciliations_request = cls(
      period=period,
      method=method,
      include_tied=include_tied,
    )

    preview_reconciliations_request.additional_properties = d
    return preview_reconciliations_request

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
