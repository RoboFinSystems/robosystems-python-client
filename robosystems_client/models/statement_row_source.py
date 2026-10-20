from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatementRowSource")


@_attrs_define
class StatementRowSource:
  """One account's part in a statement figure: what that account, in that
  entity's books, contributed to the column.

      Attributes:
          entity_id (str): The entity whose books hold the lines, the register to open.
          account_id (str): The account.
          name (str): The account's name.
          value (float): What the account contributed, in the figure's sign.
          code (None | str | Unset): The account's code.
  """

  entity_id: str
  account_id: str
  name: str
  value: float
  code: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    account_id = self.account_id

    name = self.name

    value = self.value

    code: None | str | Unset
    if isinstance(self.code, Unset):
      code = UNSET
    else:
      code = self.code

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "account_id": account_id,
        "name": name,
        "value": value,
      }
    )
    if code is not UNSET:
      field_dict["code"] = code

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    account_id = d.pop("account_id")

    name = d.pop("name")

    value = d.pop("value")

    def _parse_code(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    code = _parse_code(d.pop("code", UNSET))

    statement_row_source = cls(
      entity_id=entity_id,
      account_id=account_id,
      name=name,
      value=value,
      code=code,
    )

    statement_row_source.additional_properties = d
    return statement_row_source

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
