from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.portfolio_block_position_add import PortfolioBlockPositionAdd
  from ..models.portfolio_block_position_dispose import PortfolioBlockPositionDispose
  from ..models.portfolio_block_position_update import PortfolioBlockPositionUpdate


T = TypeVar("T", bound="PortfolioBlockPositions")


@_attrs_define
class PortfolioBlockPositions:
  """Position deltas applied atomically inside `update-portfolio-block`.

  Attributes:
      add (list[PortfolioBlockPositionAdd] | Unset): New positions to mint inside this portfolio. Each references an
          existing `security_id`.
      update (list[PortfolioBlockPositionUpdate] | Unset): Patches to existing positions, addressed by position `id`.
          Unset fields on each entry are left unchanged.
      dispose (list[PortfolioBlockPositionDispose] | Unset): Positions to soft-dispose, addressed by position `id`.
          Status flips to `disposed` and `disposition_date` is stamped.
  """

  add: list[PortfolioBlockPositionAdd] | Unset = UNSET
  update: list[PortfolioBlockPositionUpdate] | Unset = UNSET
  dispose: list[PortfolioBlockPositionDispose] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    add: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.add, Unset):
      add = []
      for add_item_data in self.add:
        add_item = add_item_data.to_dict()
        add.append(add_item)

    update: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.update, Unset):
      update = []
      for update_item_data in self.update:
        update_item = update_item_data.to_dict()
        update.append(update_item)

    dispose: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.dispose, Unset):
      dispose = []
      for dispose_item_data in self.dispose:
        dispose_item = dispose_item_data.to_dict()
        dispose.append(dispose_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if add is not UNSET:
      field_dict["add"] = add
    if update is not UNSET:
      field_dict["update"] = update
    if dispose is not UNSET:
      field_dict["dispose"] = dispose

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.portfolio_block_position_add import PortfolioBlockPositionAdd
    from ..models.portfolio_block_position_dispose import PortfolioBlockPositionDispose
    from ..models.portfolio_block_position_update import PortfolioBlockPositionUpdate

    d = dict(src_dict)
    _add = d.pop("add", UNSET)
    add: list[PortfolioBlockPositionAdd] | Unset = UNSET
    if _add is not UNSET:
      add = []
      for add_item_data in _add:
        add_item = PortfolioBlockPositionAdd.from_dict(add_item_data)

        add.append(add_item)

    _update = d.pop("update", UNSET)
    update: list[PortfolioBlockPositionUpdate] | Unset = UNSET
    if _update is not UNSET:
      update = []
      for update_item_data in _update:
        update_item = PortfolioBlockPositionUpdate.from_dict(update_item_data)

        update.append(update_item)

    _dispose = d.pop("dispose", UNSET)
    dispose: list[PortfolioBlockPositionDispose] | Unset = UNSET
    if _dispose is not UNSET:
      dispose = []
      for dispose_item_data in _dispose:
        dispose_item = PortfolioBlockPositionDispose.from_dict(dispose_item_data)

        dispose.append(dispose_item)

    portfolio_block_positions = cls(
      add=add,
      update=update,
      dispose=dispose,
    )

    portfolio_block_positions.additional_properties = d
    return portfolio_block_positions

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
