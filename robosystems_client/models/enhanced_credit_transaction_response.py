from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.enhanced_credit_transaction_response_metadata import (
    EnhancedCreditTransactionResponseMetadata,
  )


T = TypeVar("T", bound="EnhancedCreditTransactionResponse")


@_attrs_define
class EnhancedCreditTransactionResponse:
  """Enhanced credit transaction response with more details.

  Attributes:
      id (str):
      type_ (str):
      amount (float):
      description (str):
      metadata (EnhancedCreditTransactionResponseMetadata):
      created_at (str):
      operation_id (Union[None, Unset, str]):
      idempotency_key (Union[None, Unset, str]):
      request_id (Union[None, Unset, str]):
      user_id (Union[None, Unset, str]):
  """

  id: str
  type_: str
  amount: float
  description: str
  metadata: "EnhancedCreditTransactionResponseMetadata"
  created_at: str
  operation_id: Union[None, Unset, str] = UNSET
  idempotency_key: Union[None, Unset, str] = UNSET
  request_id: Union[None, Unset, str] = UNSET
  user_id: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    id = self.id

    type_ = self.type_

    amount = self.amount

    description = self.description

    metadata = self.metadata.to_dict()

    created_at = self.created_at

    operation_id: Union[None, Unset, str]
    if isinstance(self.operation_id, Unset):
      operation_id = UNSET
    else:
      operation_id = self.operation_id

    idempotency_key: Union[None, Unset, str]
    if isinstance(self.idempotency_key, Unset):
      idempotency_key = UNSET
    else:
      idempotency_key = self.idempotency_key

    request_id: Union[None, Unset, str]
    if isinstance(self.request_id, Unset):
      request_id = UNSET
    else:
      request_id = self.request_id

    user_id: Union[None, Unset, str]
    if isinstance(self.user_id, Unset):
      user_id = UNSET
    else:
      user_id = self.user_id

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "id": id,
        "type": type_,
        "amount": amount,
        "description": description,
        "metadata": metadata,
        "created_at": created_at,
      }
    )
    if operation_id is not UNSET:
      field_dict["operation_id"] = operation_id
    if idempotency_key is not UNSET:
      field_dict["idempotency_key"] = idempotency_key
    if request_id is not UNSET:
      field_dict["request_id"] = request_id
    if user_id is not UNSET:
      field_dict["user_id"] = user_id

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.enhanced_credit_transaction_response_metadata import (
      EnhancedCreditTransactionResponseMetadata,
    )

    d = dict(src_dict)
    id = d.pop("id")

    type_ = d.pop("type")

    amount = d.pop("amount")

    description = d.pop("description")

    metadata = EnhancedCreditTransactionResponseMetadata.from_dict(d.pop("metadata"))

    created_at = d.pop("created_at")

    def _parse_operation_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    operation_id = _parse_operation_id(d.pop("operation_id", UNSET))

    def _parse_idempotency_key(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    idempotency_key = _parse_idempotency_key(d.pop("idempotency_key", UNSET))

    def _parse_request_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    request_id = _parse_request_id(d.pop("request_id", UNSET))

    def _parse_user_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    user_id = _parse_user_id(d.pop("user_id", UNSET))

    enhanced_credit_transaction_response = cls(
      id=id,
      type_=type_,
      amount=amount,
      description=description,
      metadata=metadata,
      created_at=created_at,
      operation_id=operation_id,
      idempotency_key=idempotency_key,
      request_id=request_id,
      user_id=user_id,
    )

    enhanced_credit_transaction_response.additional_properties = d
    return enhanced_credit_transaction_response

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
