from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.success_response_data_type_0 import SuccessResponseDataType0


T = TypeVar("T", bound="SuccessResponse")


@_attrs_define
class SuccessResponse:
  """Standard success response for operations without specific return data.

  Example:
      {'data': {'deleted_count': 1}, 'message': 'Resource deleted successfully', 'success': True}

  Attributes:
      message (str): Human-readable success message
      success (Union[Unset, bool]): Indicates the operation completed successfully Default: True.
      data (Union['SuccessResponseDataType0', None, Unset]): Optional additional data related to the operation
  """

  message: str
  success: Union[Unset, bool] = True
  data: Union["SuccessResponseDataType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.success_response_data_type_0 import SuccessResponseDataType0

    message = self.message

    success = self.success

    data: Union[None, Unset, dict[str, Any]]
    if isinstance(self.data, Unset):
      data = UNSET
    elif isinstance(self.data, SuccessResponseDataType0):
      data = self.data.to_dict()
    else:
      data = self.data

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "message": message,
      }
    )
    if success is not UNSET:
      field_dict["success"] = success
    if data is not UNSET:
      field_dict["data"] = data

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.success_response_data_type_0 import SuccessResponseDataType0

    d = dict(src_dict)
    message = d.pop("message")

    success = d.pop("success", UNSET)

    def _parse_data(data: object) -> Union["SuccessResponseDataType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        data_type_0 = SuccessResponseDataType0.from_dict(data)

        return data_type_0
      except:  # noqa: E722
        pass
      return cast(Union["SuccessResponseDataType0", None, Unset], data)

    data = _parse_data(d.pop("data", UNSET))

    success_response = cls(
      message=message,
      success=success,
      data=data,
    )

    success_response.additional_properties = d
    return success_response

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
