from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageLimits")


@_attrs_define
class StorageLimits:
  """Storage limits information.

  Attributes:
      max_storage_gb (float): Maximum storage limit in GB
      approaching_limit (bool): Whether approaching storage limit (>80%)
      current_usage_gb (Union[None, Unset, float]): Current storage usage in GB
  """

  max_storage_gb: float
  approaching_limit: bool
  current_usage_gb: Union[None, Unset, float] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    max_storage_gb = self.max_storage_gb

    approaching_limit = self.approaching_limit

    current_usage_gb: Union[None, Unset, float]
    if isinstance(self.current_usage_gb, Unset):
      current_usage_gb = UNSET
    else:
      current_usage_gb = self.current_usage_gb

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "max_storage_gb": max_storage_gb,
        "approaching_limit": approaching_limit,
      }
    )
    if current_usage_gb is not UNSET:
      field_dict["current_usage_gb"] = current_usage_gb

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    max_storage_gb = d.pop("max_storage_gb")

    approaching_limit = d.pop("approaching_limit")

    def _parse_current_usage_gb(data: object) -> Union[None, Unset, float]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, float], data)

    current_usage_gb = _parse_current_usage_gb(d.pop("current_usage_gb", UNSET))

    storage_limits = cls(
      max_storage_gb=max_storage_gb,
      approaching_limit=approaching_limit,
      current_usage_gb=current_usage_gb,
    )

    storage_limits.additional_properties = d
    return storage_limits

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
