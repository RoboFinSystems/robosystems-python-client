from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.portfolio_block_portfolio_patch import PortfolioBlockPortfolioPatch
  from ..models.portfolio_block_positions import PortfolioBlockPositions


T = TypeVar("T", bound="UpdatePortfolioBlockOperation")


@_attrs_define
class UpdatePortfolioBlockOperation:
  """CQRS body for `POST /operations/update-portfolio-block`.

  Carries an optional patch to portfolio fields and three position
  delta lists (`add` / `update` / `dispose`). All apply atomically
  with the portfolio patch — partial failures roll back.

      Attributes:
          portfolio_id (str): Target portfolio ID.
          portfolio (PortfolioBlockPortfolioPatch | Unset): Patchable portfolio fields on `update-portfolio-block`. Unset
              fields ignored.
          positions (PortfolioBlockPositions | Unset): Position deltas applied atomically inside `update-portfolio-block`.
  """

  portfolio_id: str
  portfolio: PortfolioBlockPortfolioPatch | Unset = UNSET
  positions: PortfolioBlockPositions | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    portfolio_id = self.portfolio_id

    portfolio: dict[str, Any] | Unset = UNSET
    if not isinstance(self.portfolio, Unset):
      portfolio = self.portfolio.to_dict()

    positions: dict[str, Any] | Unset = UNSET
    if not isinstance(self.positions, Unset):
      positions = self.positions.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "portfolio_id": portfolio_id,
      }
    )
    if portfolio is not UNSET:
      field_dict["portfolio"] = portfolio
    if positions is not UNSET:
      field_dict["positions"] = positions

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.portfolio_block_portfolio_patch import PortfolioBlockPortfolioPatch
    from ..models.portfolio_block_positions import PortfolioBlockPositions

    d = dict(src_dict)
    portfolio_id = d.pop("portfolio_id")

    _portfolio = d.pop("portfolio", UNSET)
    portfolio: PortfolioBlockPortfolioPatch | Unset
    if isinstance(_portfolio, Unset):
      portfolio = UNSET
    else:
      portfolio = PortfolioBlockPortfolioPatch.from_dict(_portfolio)

    _positions = d.pop("positions", UNSET)
    positions: PortfolioBlockPositions | Unset
    if isinstance(_positions, Unset):
      positions = UNSET
    else:
      positions = PortfolioBlockPositions.from_dict(_positions)

    update_portfolio_block_operation = cls(
      portfolio_id=portfolio_id,
      portfolio=portfolio,
      positions=positions,
    )

    update_portfolio_block_operation.additional_properties = d
    return update_portfolio_block_operation

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
