from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.statement_dimension_column import StatementDimensionColumn


T = TypeVar("T", bound="StatementDimensionResponse")


@_attrs_define
class StatementDimensionResponse:
  """How a statement was sliced, and whether the slice ties out.

  Attributes:
      type_ (str): The axis the statement was sliced by.
      member_id (None | str | Unset): The one member read, when the statement was filtered to one; null when it was
          read by column.
      columns (list[StatementDimensionColumn] | Unset): Read by column: one per member, then Unallocated, then Total,
          aligned with each row's `values` and with `periods`. Empty when filtered to one member.
      ties_out (bool | None | Unset): Read by column: whether every row's members plus Unallocated equal its Total.
          Null when filtered to one member.
      differences (list[str] | Unset): The rows whose members plus Unallocated miss the Total, by qname.
  """

  type_: str
  member_id: None | str | Unset = UNSET
  columns: list[StatementDimensionColumn] | Unset = UNSET
  ties_out: bool | None | Unset = UNSET
  differences: list[str] | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    type_ = self.type_

    member_id: None | str | Unset
    if isinstance(self.member_id, Unset):
      member_id = UNSET
    else:
      member_id = self.member_id

    columns: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(self.columns, Unset):
      columns = []
      for columns_item_data in self.columns:
        columns_item = columns_item_data.to_dict()
        columns.append(columns_item)

    ties_out: bool | None | Unset
    if isinstance(self.ties_out, Unset):
      ties_out = UNSET
    else:
      ties_out = self.ties_out

    differences: list[str] | Unset = UNSET
    if not isinstance(self.differences, Unset):
      differences = self.differences

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "type": type_,
      }
    )
    if member_id is not UNSET:
      field_dict["member_id"] = member_id
    if columns is not UNSET:
      field_dict["columns"] = columns
    if ties_out is not UNSET:
      field_dict["ties_out"] = ties_out
    if differences is not UNSET:
      field_dict["differences"] = differences

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.statement_dimension_column import StatementDimensionColumn

    d = dict(src_dict)
    type_ = d.pop("type")

    def _parse_member_id(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    member_id = _parse_member_id(d.pop("member_id", UNSET))

    _columns = d.pop("columns", UNSET)
    columns: list[StatementDimensionColumn] | Unset = UNSET
    if _columns is not UNSET:
      columns = []
      for columns_item_data in _columns:
        columns_item = StatementDimensionColumn.from_dict(columns_item_data)

        columns.append(columns_item)

    def _parse_ties_out(data: object) -> bool | None | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(bool | None | Unset, data)

    ties_out = _parse_ties_out(d.pop("ties_out", UNSET))

    differences = cast(list[str], d.pop("differences", UNSET))

    statement_dimension_response = cls(
      type_=type_,
      member_id=member_id,
      columns=columns,
      ties_out=ties_out,
      differences=differences,
    )

    statement_dimension_response.additional_properties = d
    return statement_dimension_response

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
