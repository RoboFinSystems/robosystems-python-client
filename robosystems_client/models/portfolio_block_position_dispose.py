from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortfolioBlockPositionDispose")


@_attrs_define
class PortfolioBlockPositionDispose:
  """Dispose-by-id for an existing position in `update-portfolio-block`.

  Soft-delete: status flips to `disposed` and `disposition_date` is
  stamped. `disposition_reason`, when supplied, is recorded under
  `metadata.disposition_reason`.

      Attributes:
          id (str):
          disposition_reason (None | str | Unset):
  """

  id: str
  disposition_reason: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    disposition_reason: None | str | Unset
    if isinstance(self.disposition_reason, Unset):
      disposition_reason = UNSET
    else:
      disposition_reason = self.disposition_reason

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
      }
    )
    if disposition_reason is not UNSET:
      field_dict["disposition_reason"] = disposition_reason

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    id = d.pop("id")

    def _parse_disposition_reason(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    disposition_reason = _parse_disposition_reason(d.pop("disposition_reason", UNSET))

    portfolio_block_position_dispose = cls(
      id=id,
      disposition_reason=disposition_reason,
    )

    portfolio_block_position_dispose.additional_properties = d
    return portfolio_block_position_dispose

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
