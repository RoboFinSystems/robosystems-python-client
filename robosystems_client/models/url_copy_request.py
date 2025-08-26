from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.url_copy_request_file_format import URLCopyRequestFileFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.url_copy_request_headers_type_0 import URLCopyRequestHeadersType0


T = TypeVar("T", bound="URLCopyRequest")


@_attrs_define
class URLCopyRequest:
  """Request model for URL copy operations (future).

  Attributes:
      table_name (str): Target Kuzu table name
      url (str): HTTP(S) URL to the data file
      file_format (URLCopyRequestFileFormat): File format of the URL data
      ignore_errors (Union[Unset, bool]): Skip duplicate/invalid rows (enables upsert-like behavior) Default: True.
      extended_timeout (Union[Unset, bool]): Use extended timeout for large datasets Default: False.
      validate_schema (Union[Unset, bool]): Validate source schema against target table Default: True.
      source_type (Union[Literal['url'], Unset]): Source type identifier Default: 'url'.
      headers (Union['URLCopyRequestHeadersType0', None, Unset]): Optional HTTP headers for authentication
  """

  table_name: str
  url: str
  file_format: URLCopyRequestFileFormat
  ignore_errors: Union[Unset, bool] = True
  extended_timeout: Union[Unset, bool] = False
  validate_schema: Union[Unset, bool] = True
  source_type: Union[Literal["url"], Unset] = "url"
  headers: Union["URLCopyRequestHeadersType0", None, Unset] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.url_copy_request_headers_type_0 import URLCopyRequestHeadersType0

    table_name = self.table_name

    url = self.url

    file_format = self.file_format.value

    ignore_errors = self.ignore_errors

    extended_timeout = self.extended_timeout

    validate_schema = self.validate_schema

    source_type = self.source_type

    headers: Union[None, Unset, dict[str, Any]]
    if isinstance(self.headers, Unset):
      headers = UNSET
    elif isinstance(self.headers, URLCopyRequestHeadersType0):
      headers = self.headers.to_dict()
    else:
      headers = self.headers

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "table_name": table_name,
        "url": url,
        "file_format": file_format,
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
    if headers is not UNSET:
      field_dict["headers"] = headers

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.url_copy_request_headers_type_0 import URLCopyRequestHeadersType0

    d = dict(src_dict)
    table_name = d.pop("table_name")

    url = d.pop("url")

    file_format = URLCopyRequestFileFormat(d.pop("file_format"))

    ignore_errors = d.pop("ignore_errors", UNSET)

    extended_timeout = d.pop("extended_timeout", UNSET)

    validate_schema = d.pop("validate_schema", UNSET)

    source_type = cast(Union[Literal["url"], Unset], d.pop("source_type", UNSET))
    if source_type != "url" and not isinstance(source_type, Unset):
      raise ValueError(f"source_type must match const 'url', got '{source_type}'")

    def _parse_headers(
      data: object,
    ) -> Union["URLCopyRequestHeadersType0", None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        headers_type_0 = URLCopyRequestHeadersType0.from_dict(data)

        return headers_type_0
      except:  # noqa: E722
        pass
      return cast(Union["URLCopyRequestHeadersType0", None, Unset], data)

    headers = _parse_headers(d.pop("headers", UNSET))

    url_copy_request = cls(
      table_name=table_name,
      url=url,
      file_format=file_format,
      ignore_errors=ignore_errors,
      extended_timeout=extended_timeout,
      validate_schema=validate_schema,
      source_type=source_type,
      headers=headers,
    )

    url_copy_request.additional_properties = d
    return url_copy_request

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
