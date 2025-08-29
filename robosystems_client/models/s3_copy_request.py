from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.s3_copy_request_file_format import S3CopyRequestFileFormat
from ..models.s3_copy_request_s3_url_style_type_0 import S3CopyRequestS3UrlStyleType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="S3CopyRequest")


@_attrs_define
class S3CopyRequest:
  r"""Request model for S3 copy operations.

  Copies data from S3 buckets into graph database tables using user-provided
  AWS credentials. Supports various file formats and bulk loading options.

      Attributes:
          table_name (str): Target Kuzu table name
          s3_path (str): Full S3 path (s3://bucket/key or s3://bucket/prefix/*.parquet)
          s3_access_key_id (str): AWS access key ID for S3 access
          s3_secret_access_key (str): AWS secret access key for S3 access
          ignore_errors (Union[Unset, bool]): Skip duplicate/invalid rows (enables upsert-like behavior) Default: True.
          extended_timeout (Union[Unset, bool]): Use extended timeout for large datasets Default: False.
          validate_schema (Union[Unset, bool]): Validate source schema against target table Default: True.
          source_type (Union[Literal['s3'], Unset]): Source type identifier Default: 's3'.
          s3_session_token (Union[None, Unset, str]): AWS session token (for temporary credentials)
          s3_region (Union[None, Unset, str]): S3 region Default: 'us-east-1'.
          s3_endpoint (Union[None, Unset, str]): Custom S3 endpoint (for S3-compatible storage)
          s3_url_style (Union[None, S3CopyRequestS3UrlStyleType0, Unset]): S3 URL style (vhost or path)
          file_format (Union[Unset, S3CopyRequestFileFormat]): File format of the S3 data Default:
              S3CopyRequestFileFormat.PARQUET.
          csv_delimiter (Union[None, Unset, str]): CSV delimiter Default: ','.
          csv_header (Union[None, Unset, bool]): CSV has header row Default: True.
          csv_quote (Union[None, Unset, str]): CSV quote character Default: '\\"'.
          csv_escape (Union[None, Unset, str]): CSV escape character Default: '\\'.
          csv_skip (Union[None, Unset, int]): Number of rows to skip Default: 0.
          allow_moved_paths (Union[None, Unset, bool]): Allow moved paths for Iceberg tables Default: False.
          max_file_size_gb (Union[None, Unset, int]): Maximum total file size limit in GB Default: 10.
  """

  table_name: str
  s3_path: str
  s3_access_key_id: str
  s3_secret_access_key: str
  ignore_errors: Union[Unset, bool] = True
  extended_timeout: Union[Unset, bool] = False
  validate_schema: Union[Unset, bool] = True
  source_type: Union[Literal["s3"], Unset] = "s3"
  s3_session_token: Union[None, Unset, str] = UNSET
  s3_region: Union[None, Unset, str] = "us-east-1"
  s3_endpoint: Union[None, Unset, str] = UNSET
  s3_url_style: Union[None, S3CopyRequestS3UrlStyleType0, Unset] = UNSET
  file_format: Union[Unset, S3CopyRequestFileFormat] = S3CopyRequestFileFormat.PARQUET
  csv_delimiter: Union[None, Unset, str] = ","
  csv_header: Union[None, Unset, bool] = True
  csv_quote: Union[None, Unset, str] = '\\"'
  csv_escape: Union[None, Unset, str] = "\\"
  csv_skip: Union[None, Unset, int] = 0
  allow_moved_paths: Union[None, Unset, bool] = False
  max_file_size_gb: Union[None, Unset, int] = 10
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    table_name = self.table_name

    s3_path = self.s3_path

    s3_access_key_id = self.s3_access_key_id

    s3_secret_access_key = self.s3_secret_access_key

    ignore_errors = self.ignore_errors

    extended_timeout = self.extended_timeout

    validate_schema = self.validate_schema

    source_type = self.source_type

    s3_session_token: Union[None, Unset, str]
    if isinstance(self.s3_session_token, Unset):
      s3_session_token = UNSET
    else:
      s3_session_token = self.s3_session_token

    s3_region: Union[None, Unset, str]
    if isinstance(self.s3_region, Unset):
      s3_region = UNSET
    else:
      s3_region = self.s3_region

    s3_endpoint: Union[None, Unset, str]
    if isinstance(self.s3_endpoint, Unset):
      s3_endpoint = UNSET
    else:
      s3_endpoint = self.s3_endpoint

    s3_url_style: Union[None, Unset, str]
    if isinstance(self.s3_url_style, Unset):
      s3_url_style = UNSET
    elif isinstance(self.s3_url_style, S3CopyRequestS3UrlStyleType0):
      s3_url_style = self.s3_url_style.value
    else:
      s3_url_style = self.s3_url_style

    file_format: Union[Unset, str] = UNSET
    if not isinstance(self.file_format, Unset):
      file_format = self.file_format.value

    csv_delimiter: Union[None, Unset, str]
    if isinstance(self.csv_delimiter, Unset):
      csv_delimiter = UNSET
    else:
      csv_delimiter = self.csv_delimiter

    csv_header: Union[None, Unset, bool]
    if isinstance(self.csv_header, Unset):
      csv_header = UNSET
    else:
      csv_header = self.csv_header

    csv_quote: Union[None, Unset, str]
    if isinstance(self.csv_quote, Unset):
      csv_quote = UNSET
    else:
      csv_quote = self.csv_quote

    csv_escape: Union[None, Unset, str]
    if isinstance(self.csv_escape, Unset):
      csv_escape = UNSET
    else:
      csv_escape = self.csv_escape

    csv_skip: Union[None, Unset, int]
    if isinstance(self.csv_skip, Unset):
      csv_skip = UNSET
    else:
      csv_skip = self.csv_skip

    allow_moved_paths: Union[None, Unset, bool]
    if isinstance(self.allow_moved_paths, Unset):
      allow_moved_paths = UNSET
    else:
      allow_moved_paths = self.allow_moved_paths

    max_file_size_gb: Union[None, Unset, int]
    if isinstance(self.max_file_size_gb, Unset):
      max_file_size_gb = UNSET
    else:
      max_file_size_gb = self.max_file_size_gb

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "table_name": table_name,
        "s3_path": s3_path,
        "s3_access_key_id": s3_access_key_id,
        "s3_secret_access_key": s3_secret_access_key,
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
    if s3_session_token is not UNSET:
      field_dict["s3_session_token"] = s3_session_token
    if s3_region is not UNSET:
      field_dict["s3_region"] = s3_region
    if s3_endpoint is not UNSET:
      field_dict["s3_endpoint"] = s3_endpoint
    if s3_url_style is not UNSET:
      field_dict["s3_url_style"] = s3_url_style
    if file_format is not UNSET:
      field_dict["file_format"] = file_format
    if csv_delimiter is not UNSET:
      field_dict["csv_delimiter"] = csv_delimiter
    if csv_header is not UNSET:
      field_dict["csv_header"] = csv_header
    if csv_quote is not UNSET:
      field_dict["csv_quote"] = csv_quote
    if csv_escape is not UNSET:
      field_dict["csv_escape"] = csv_escape
    if csv_skip is not UNSET:
      field_dict["csv_skip"] = csv_skip
    if allow_moved_paths is not UNSET:
      field_dict["allow_moved_paths"] = allow_moved_paths
    if max_file_size_gb is not UNSET:
      field_dict["max_file_size_gb"] = max_file_size_gb

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    table_name = d.pop("table_name")

    s3_path = d.pop("s3_path")

    s3_access_key_id = d.pop("s3_access_key_id")

    s3_secret_access_key = d.pop("s3_secret_access_key")

    ignore_errors = d.pop("ignore_errors", UNSET)

    extended_timeout = d.pop("extended_timeout", UNSET)

    validate_schema = d.pop("validate_schema", UNSET)

    source_type = cast(Union[Literal["s3"], Unset], d.pop("source_type", UNSET))
    if source_type != "s3" and not isinstance(source_type, Unset):
      raise ValueError(f"source_type must match const 's3', got '{source_type}'")

    def _parse_s3_session_token(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    s3_session_token = _parse_s3_session_token(d.pop("s3_session_token", UNSET))

    def _parse_s3_region(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    s3_region = _parse_s3_region(d.pop("s3_region", UNSET))

    def _parse_s3_endpoint(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    s3_endpoint = _parse_s3_endpoint(d.pop("s3_endpoint", UNSET))

    def _parse_s3_url_style(
      data: object,
    ) -> Union[None, S3CopyRequestS3UrlStyleType0, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        s3_url_style_type_0 = S3CopyRequestS3UrlStyleType0(data)

        return s3_url_style_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, S3CopyRequestS3UrlStyleType0, Unset], data)

    s3_url_style = _parse_s3_url_style(d.pop("s3_url_style", UNSET))

    _file_format = d.pop("file_format", UNSET)
    file_format: Union[Unset, S3CopyRequestFileFormat]
    if isinstance(_file_format, Unset):
      file_format = UNSET
    else:
      file_format = S3CopyRequestFileFormat(_file_format)

    def _parse_csv_delimiter(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    csv_delimiter = _parse_csv_delimiter(d.pop("csv_delimiter", UNSET))

    def _parse_csv_header(data: object) -> Union[None, Unset, bool]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, bool], data)

    csv_header = _parse_csv_header(d.pop("csv_header", UNSET))

    def _parse_csv_quote(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    csv_quote = _parse_csv_quote(d.pop("csv_quote", UNSET))

    def _parse_csv_escape(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    csv_escape = _parse_csv_escape(d.pop("csv_escape", UNSET))

    def _parse_csv_skip(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    csv_skip = _parse_csv_skip(d.pop("csv_skip", UNSET))

    def _parse_allow_moved_paths(data: object) -> Union[None, Unset, bool]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, bool], data)

    allow_moved_paths = _parse_allow_moved_paths(d.pop("allow_moved_paths", UNSET))

    def _parse_max_file_size_gb(data: object) -> Union[None, Unset, int]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, int], data)

    max_file_size_gb = _parse_max_file_size_gb(d.pop("max_file_size_gb", UNSET))

    s3_copy_request = cls(
      table_name=table_name,
      s3_path=s3_path,
      s3_access_key_id=s3_access_key_id,
      s3_secret_access_key=s3_secret_access_key,
      ignore_errors=ignore_errors,
      extended_timeout=extended_timeout,
      validate_schema=validate_schema,
      source_type=source_type,
      s3_session_token=s3_session_token,
      s3_region=s3_region,
      s3_endpoint=s3_endpoint,
      s3_url_style=s3_url_style,
      file_format=file_format,
      csv_delimiter=csv_delimiter,
      csv_header=csv_header,
      csv_quote=csv_quote,
      csv_escape=csv_escape,
      csv_skip=csv_skip,
      allow_moved_paths=allow_moved_paths,
      max_file_size_gb=max_file_size_gb,
    )

    s3_copy_request.additional_properties = d
    return s3_copy_request

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
