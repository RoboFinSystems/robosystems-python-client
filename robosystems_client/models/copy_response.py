from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.copy_response_status import CopyResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.copy_response_error_details_type_0 import CopyResponseErrorDetailsType0


T = TypeVar("T", bound="CopyResponse")


@_attrs_define
class CopyResponse:
  """Response model for copy operations.

  Attributes:
      status (CopyResponseStatus): Operation status
      source_type (str): Type of source that was copied from
      execution_time_ms (float): Total execution time in milliseconds
      message (str): Human-readable status message
      rows_imported (Union[None, Unset, int]): Number of rows successfully imported
      rows_skipped (Union[None, Unset, int]): Number of rows skipped due to errors (when ignore_errors=true)
      warnings (Union[None, Unset, list[str]]): List of warnings encountered during import
      error_details (Union['CopyResponseErrorDetailsType0', None, Unset]): Detailed error information if operation
          failed
      bytes_processed (Union[None, Unset, int]): Total bytes processed from source
  """

  status: CopyResponseStatus
  source_type: str
  execution_time_ms: float
  message: str
  rows_imported: Union[None, Unset, int] = UNSET
  rows_skipped: Union[None, Unset, int] = UNSET
  warnings: Union[None, Unset, list[str]] = UNSET
  error_details: Union["CopyResponseErrorDetailsType0", None, Unset] = UNSET
  bytes_processed: Union[None, Unset, int] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.copy_response_error_details_type_0 import (
      CopyResponseErrorDetailsType0,
    )

    status = self.status.value

    source_type = self.source_type

    execution_time_ms = self.execution_time_ms

    message = self.message

    rows_imported: Union[None, Unset, int]
    if isinstance(self.rows_imported, Unset):
      rows_imported = UNSET
    else:
      rows_imported = self.rows_imported

    rows_skipped: Union[None, Unset, int]
    if isinstance(self.rows_skipped, Unset):
      rows_skipped = UNSET
    else:
      rows_skipped = self.rows_skipped

    warnings: Union[None, Unset, list[str]]
    if isinstance(self.warnings, Unset):
      warnings = UNSET
    elif isinstance(self.warnings, list):
      warnings = self.warnings

    else:
      warnings = self.warnings

    error_details: Union[None, Unset, dict[str, Any]]
    if isinstance(self.error_details, Unset):
      error_details = UNSET
    elif isinstance(self.error_details, CopyResponseErrorDetailsType0):
      error_details = self.error_details.to_dict()
    else:
      error_details = self.error_details

    bytes_processed: Union[None, Unset, int]
    if isinstance(self.bytes_processed, Unset):
      bytes_processed = UNSET
    else:
      bytes_processed = self.bytes_processed

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "status": status,
        "source_type": source_type,
        "execution_time_ms": execution_time_ms,
        "message": message,
      }
    )
    if rows_imported is not UNSET:
      field_dict["rows_imported"] = rows_imported
    if rows_skipped is not UNSET:
      field_dict["rows_skipped"] = rows_skipped
    if warnings is not UNSET:
      field_dict["warnings"] = warnings
    if error_details is not UNSET:
      field_dict["error_details"] = error_details
    if bytes_processed is not UNSET:
      field_dict["bytes_processed"] = bytes_processed

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.copy_response_error_details_type_0 import (
      CopyResponseErrorDetailsType0,
    )

    d = dict(src_dict)
    status = CopyResponseStatus(d.pop("status"))

    source_type = d.pop("source_type")

    execution_time_ms = d.pop("execution_time_ms")

    message = d.pop("message")

    def _parse_rows_imported(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    rows_imported = _parse_rows_imported(d.pop("rows_imported", UNSET))

    def _parse_rows_skipped(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    rows_skipped = _parse_rows_skipped(d.pop("rows_skipped", UNSET))

    def _parse_warnings(data: object) -> Union[None, Unset, list[str]]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        warnings_type_0 = cast(list[str], data)

        return warnings_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, list[str]], data)

    warnings = _parse_warnings(d.pop("warnings", UNSET))

    def _parse_error_details(
      data: object,
    ) -> Union["CopyResponseErrorDetailsType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        error_details_type_0 = CopyResponseErrorDetailsType0.from_dict(data)

        return error_details_type_0
      except:  # noqa: E722
        pass
      return cast(Union["CopyResponseErrorDetailsType0", None, Unset], data)

    error_details = _parse_error_details(d.pop("error_details", UNSET))

    def _parse_bytes_processed(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    bytes_processed = _parse_bytes_processed(d.pop("bytes_processed", UNSET))

    copy_response = cls(
      status=status,
      source_type=source_type,
      execution_time_ms=execution_time_ms,
      message=message,
      rows_imported=rows_imported,
      rows_skipped=rows_skipped,
      warnings=warnings,
      error_details=error_details,
      bytes_processed=bytes_processed,
    )

    copy_response.additional_properties = d
    return copy_response

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
