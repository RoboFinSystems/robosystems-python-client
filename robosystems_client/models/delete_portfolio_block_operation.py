from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeletePortfolioBlockOperation")


@_attrs_define
class DeletePortfolioBlockOperation:
  """CQRS body for `POST /operations/delete-portfolio-block`.

  Cascade-deletes the portfolio plus all of its positions. When the
  portfolio still has active positions, the operation is rejected
  unless `confirm_active_positions=true` is set — safety belt to
  prevent accidental cascade.

      Attributes:
          portfolio_id (str): Target portfolio ID.
          confirm_active_positions (bool | Unset):  Default: False.
  """

  portfolio_id: str
  confirm_active_positions: bool | Unset = False
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    portfolio_id = self.portfolio_id

    confirm_active_positions = self.confirm_active_positions

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "portfolio_id": portfolio_id,
      }
    )
    if confirm_active_positions is not UNSET:
      field_dict["confirm_active_positions"] = confirm_active_positions

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    portfolio_id = d.pop("portfolio_id")

    confirm_active_positions = d.pop("confirm_active_positions", UNSET)

    delete_portfolio_block_operation = cls(
      portfolio_id=portfolio_id,
      confirm_active_positions=confirm_active_positions,
    )

    delete_portfolio_block_operation.additional_properties = d
    return delete_portfolio_block_operation

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
