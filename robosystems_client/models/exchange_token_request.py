from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.exchange_token_request_metadata_type_0 import (
    ExchangeTokenRequestMetadataType0,
  )


T = TypeVar("T", bound="ExchangeTokenRequest")


@_attrs_define
class ExchangeTokenRequest:
  """Exchange temporary token for permanent credentials.

  Attributes:
      connection_id (str): Connection ID to update
      public_token (str): Temporary token from embedded auth
      metadata (Union['ExchangeTokenRequestMetadataType0', None, Unset]): Provider-specific metadata
  """

  connection_id: str
  public_token: str
  metadata: Union["ExchangeTokenRequestMetadataType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.exchange_token_request_metadata_type_0 import (
      ExchangeTokenRequestMetadataType0,
    )

    connection_id = self.connection_id

    public_token = self.public_token

    metadata: Union[None, Unset, dict[str, Any]]
    if isinstance(self.metadata, Unset):
      metadata = UNSET
    elif isinstance(self.metadata, ExchangeTokenRequestMetadataType0):
      metadata = self.metadata.to_dict()
    else:
      metadata = self.metadata

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "connection_id": connection_id,
        "public_token": public_token,
      }
    )
    if metadata is not UNSET:
      field_dict["metadata"] = metadata

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.exchange_token_request_metadata_type_0 import (
      ExchangeTokenRequestMetadataType0,
    )

    d = dict(src_dict)
    connection_id = d.pop("connection_id")

    public_token = d.pop("public_token")

    def _parse_metadata(
      data: object,
    ) -> Union["ExchangeTokenRequestMetadataType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        metadata_type_0 = ExchangeTokenRequestMetadataType0.from_dict(data)

        return metadata_type_0
      except:  # noqa: E722
        pass
      return cast(Union["ExchangeTokenRequestMetadataType0", None, Unset], data)

    metadata = _parse_metadata(d.pop("metadata", UNSET))

    exchange_token_request = cls(
      connection_id=connection_id,
      public_token=public_token,
      metadata=metadata,
    )

    exchange_token_request.additional_properties = d
    return exchange_token_request

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
