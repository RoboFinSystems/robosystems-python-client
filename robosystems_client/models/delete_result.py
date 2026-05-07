from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteResult")


@_attrs_define
class DeleteResult:
  """Shared response shape for soft-delete operations (e.g.,
  `delete-security`). `deleted=true` means a row was flipped; 404 is
  raised by the handler when no row existed.

      Attributes:
          deleted (bool): `true` when the row was soft-deleted in this call. Always `true` on a 200 response; the 404 path
              is taken instead when the row didn't exist.
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
