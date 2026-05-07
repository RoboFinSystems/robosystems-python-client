from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeletePortfolioBlockResponse")


@_attrs_define
class DeletePortfolioBlockResponse:
  """Result envelope for `delete-portfolio-block`. `positions_deleted`
  carries the count of position rows removed alongside the portfolio.

      Attributes:
          deleted (bool): `true` when the portfolio row was removed.
          portfolio_id (str): ID of the portfolio that was deleted.
          positions_deleted (int): Count of position rows cascade-deleted with the portfolio.
  """

  deleted: bool
  portfolio_id: str
  positions_deleted: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    deleted = self.deleted

    portfolio_id = self.portfolio_id

    positions_deleted = self.positions_deleted

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "deleted": deleted,
        "portfolio_id": portfolio_id,
        "positions_deleted": positions_deleted,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    deleted = d.pop("deleted")

    portfolio_id = d.pop("portfolio_id")

    positions_deleted = d.pop("positions_deleted")

    delete_portfolio_block_response = cls(
      deleted=deleted,
      portfolio_id=portfolio_id,
      positions_deleted=positions_deleted,
    )

    delete_portfolio_block_response.additional_properties = d
    return delete_portfolio_block_response

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
