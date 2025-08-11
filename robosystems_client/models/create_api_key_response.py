from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.api_key_info import APIKeyInfo


T = TypeVar("T", bound="CreateAPIKeyResponse")


@_attrs_define
class CreateAPIKeyResponse:
  """Response model for creating a new API key.

  Attributes:
      api_key (APIKeyInfo): API key information response model.
      key (str): The actual API key (only shown once)
  """

  api_key: "APIKeyInfo"
  key: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    api_key = self.api_key.to_dict()

    key = self.key

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "api_key": api_key,
        "key": key,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.api_key_info import APIKeyInfo

    d = dict(src_dict)
    api_key = APIKeyInfo.from_dict(d.pop("api_key"))

    key = d.pop("key")

    create_api_key_response = cls(
      api_key=api_key,
      key=key,
    )

    create_api_key_response.additional_properties = d
    return create_api_key_response

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
