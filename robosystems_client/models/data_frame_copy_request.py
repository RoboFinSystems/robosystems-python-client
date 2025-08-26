from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_frame_copy_request_format import DataFrameCopyRequestFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataFrameCopyRequest")


@_attrs_define
class DataFrameCopyRequest:
  """Request model for DataFrame copy operations (future).

  Attributes:
      table_name (str): Target Kuzu table name
      data_reference (str): Reference to uploaded DataFrame data
      ignore_errors (Union[Unset, bool]): Skip duplicate/invalid rows (enables upsert-like behavior) Default: True.
      extended_timeout (Union[Unset, bool]): Use extended timeout for large datasets Default: False.
      validate_schema (Union[Unset, bool]): Validate source schema against target table Default: True.
      source_type (Union[Literal['dataframe'], Unset]): Source type identifier Default: 'dataframe'.
      format_ (Union[Unset, DataFrameCopyRequestFormat]): DataFrame format Default: DataFrameCopyRequestFormat.PANDAS.
  """

  table_name: str
  data_reference: str
  ignore_errors: Union[Unset, bool] = True
  extended_timeout: Union[Unset, bool] = False
  validate_schema: Union[Unset, bool] = True
  source_type: Union[Literal["dataframe"], Unset] = "dataframe"
  format_: Union[Unset, DataFrameCopyRequestFormat] = DataFrameCopyRequestFormat.PANDAS
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    table_name = self.table_name

    data_reference = self.data_reference

    ignore_errors = self.ignore_errors

    extended_timeout = self.extended_timeout

    validate_schema = self.validate_schema

    source_type = self.source_type

    format_: Union[Unset, str] = UNSET
    if not isinstance(self.format_, Unset):
      format_ = self.format_.value

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "table_name": table_name,
        "data_reference": data_reference,
      }
    )
    if ignore_errors is not UNSET:
      field_dict["ignore_errors"] = ignore_errors
    if extended_timeout is not UNSET:
      field_dict["extended_timeout"] = extended_timeout
    if validate_schema is not UNSET:
      field_dict["validate_schema"] = validate_schema
    if source_type is not UNSET:
      field_dict["source_type"] = source_type
    if format_ is not UNSET:
      field_dict["format"] = format_

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    table_name = d.pop("table_name")

    data_reference = d.pop("data_reference")

    ignore_errors = d.pop("ignore_errors", UNSET)

    extended_timeout = d.pop("extended_timeout", UNSET)

    validate_schema = d.pop("validate_schema", UNSET)

    source_type = cast(Union[Literal["dataframe"], Unset], d.pop("source_type", UNSET))
    if source_type != "dataframe" and not isinstance(source_type, Unset):
      raise ValueError(f"source_type must match const 'dataframe', got '{source_type}'")

    _format_ = d.pop("format", UNSET)
    format_: Union[Unset, DataFrameCopyRequestFormat]
    if isinstance(_format_, Unset):
      format_ = UNSET
    else:
      format_ = DataFrameCopyRequestFormat(_format_)

    data_frame_copy_request = cls(
      table_name=table_name,
      data_reference=data_reference,
      ignore_errors=ignore_errors,
      extended_timeout=extended_timeout,
      validate_schema=validate_schema,
      source_type=source_type,
      format_=format_,
    )

    data_frame_copy_request.additional_properties = d
    return data_frame_copy_request

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
