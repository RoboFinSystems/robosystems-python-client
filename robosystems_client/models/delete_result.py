from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteResult")


@_attrs_define
class DeleteResult:
  """Shared response shape for delete / soft-delete operations.

  ``deleted=True`` means the operation succeeded (a row was deleted or
  flipped). A row that never existed gets a 404 — this shape never carries
  "not found".

  Defined once here, and used by both roboledger and roboinvestor, so the
  OpenAPI components key resolves to a single schema.

      Attributes:
          deleted (bool): `true` when the row was deleted in this call. Always `true` today — 404 covers the not-found
              case at the HTTP layer rather than via this field.
  """

  deleted: bool
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    deleted = self.deleted

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "deleted": deleted,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    deleted = d.pop("deleted")

    delete_result = cls(
      deleted=deleted,
    )

    delete_result.additional_properties = d
    return delete_result

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
