import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
  """Standard error response format used across all API endpoints.

  This model ensures consistent error responses for SDK generation
  and client error handling.

      Example:
          {'code': 'RESOURCE_NOT_FOUND', 'detail': 'Resource not found', 'request_id': 'req_1234567890abcdef',
              'timestamp': '2024-01-01T00:00:00Z'}

      Attributes:
          detail (str): Human-readable error message explaining what went wrong
          code (Union[None, Unset, str]): Machine-readable error code for programmatic handling
          request_id (Union[None, Unset, str]): Unique request ID for tracking and debugging
          timestamp (Union[None, Unset, datetime.datetime]): Timestamp when the error occurred
  """

  detail: str
  code: Union[None, Unset, str] = UNSET
  request_id: Union[None, Unset, str] = UNSET
  timestamp: Union[None, Unset, datetime.datetime] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    detail = self.detail

    code: Union[None, Unset, str]
    if isinstance(self.code, Unset):
      code = UNSET
    else:
      code = self.code

    request_id: Union[None, Unset, str]
    if isinstance(self.request_id, Unset):
      request_id = UNSET
    else:
      request_id = self.request_id

    timestamp: Union[None, Unset, str]
    if isinstance(self.timestamp, Unset):
      timestamp = UNSET
    elif isinstance(self.timestamp, datetime.datetime):
      timestamp = self.timestamp.isoformat()
    else:
      timestamp = self.timestamp

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "detail": detail,
      }
    )
    if code is not UNSET:
      field_dict["code"] = code
    if request_id is not UNSET:
      field_dict["request_id"] = request_id
    if timestamp is not UNSET:
      field_dict["timestamp"] = timestamp

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    detail = d.pop("detail")

    def _parse_code(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    code = _parse_code(d.pop("code", UNSET))

    def _parse_request_id(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    request_id = _parse_request_id(d.pop("request_id", UNSET))

    def _parse_timestamp(data: object) -> Union[None, Unset, datetime.datetime]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        timestamp_type_0 = isoparse(data)

        return timestamp_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, datetime.datetime], data)

    timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

    error_response = cls(
      detail=detail,
      code=code,
      request_id=request_id,
      timestamp=timestamp,
    )

    error_response.additional_properties = d
    return error_response

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
