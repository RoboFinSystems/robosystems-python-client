from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.operation_error_detail_type_1 import OperationErrorDetailType1


T = TypeVar("T", bound="OperationError")


@_attrs_define
class OperationError:
  """Error envelope returned by extensions operation endpoints. Shape aligns with FastAPI's default error detail plus an
  optional `operation_id` for audit correlation.

      Attributes:
          detail (OperationErrorDetailType1 | str | Unset): Human-readable error detail or structured payload
          operation_id (str | Unset): op_-prefixed ULID if the dispatcher minted one before the failure (async ops,
              idempotency conflicts, etc.)
  """

  detail: OperationErrorDetailType1 | str | Unset = UNSET
  operation_id: str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.operation_error_detail_type_1 import OperationErrorDetailType1

    detail: dict[str, Any] | str | Unset
    if isinstance(self.detail, Unset):
      detail = UNSET
    elif isinstance(self.detail, OperationErrorDetailType1):
      detail = self.detail.to_dict()
    else:
      detail = self.detail

    operation_id = self.operation_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if detail is not UNSET:
      field_dict["detail"] = detail
    if operation_id is not UNSET:
      field_dict["operation_id"] = operation_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.operation_error_detail_type_1 import OperationErrorDetailType1

    d = dict(src_dict)

    def _parse_detail(data: object) -> OperationErrorDetailType1 | str | Unset:
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        detail_type_1 = OperationErrorDetailType1.from_dict(data)

        return detail_type_1
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(OperationErrorDetailType1 | str | Unset, data)

    detail = _parse_detail(d.pop("detail", UNSET))

    operation_id = d.pop("operation_id", UNSET)

    operation_error = cls(
      detail=detail,
      operation_id=operation_id,
    )

    operation_error.additional_properties = d
    return operation_error

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
