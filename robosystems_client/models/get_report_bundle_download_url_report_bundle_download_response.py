from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetReportBundleDownloadUrlReportBundleDownloadResponse")


@_attrs_define
class GetReportBundleDownloadUrlReportBundleDownloadResponse:
  """Presigned-URL response for a Report bundle download.

  Mirrors :class:`BackupDownloadUrlResponse` in shape — the frontend
  treats both the same way (fetch, follow URL, GET the artifact).

  Only returned for RDF-family flavors (JSON-LD) where the artifact
  is stored in S3. XBRL flavors stream the binary content directly
  in the response body (no JSON wrapper).

      Attributes:
          download_url (str): Presigned URL that streams the bundle directly from S3.
          expires_at (datetime.datetime): UTC timestamp at which the presigned URL stops working.
          content_type (str): MIME type of the artifact behind the URL.
          format_ (str): Serialization flavor delivered by this URL — matches the ``format`` query parameter.
          generation_count (int): Bundle generation number stamped on the Report.
  """

  download_url: str
  expires_at: datetime.datetime
  content_type: str
  format_: str
  generation_count: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    download_url = self.download_url

    expires_at = self.expires_at.isoformat()

    content_type = self.content_type

    format_ = self.format_

    generation_count = self.generation_count

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "download_url": download_url,
        "expires_at": expires_at,
        "content_type": content_type,
        "format": format_,
        "generation_count": generation_count,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    download_url = d.pop("download_url")

    expires_at = isoparse(d.pop("expires_at"))

    content_type = d.pop("content_type")

    format_ = d.pop("format")

    generation_count = d.pop("generation_count")

    get_report_bundle_download_url_report_bundle_download_response = cls(
      download_url=download_url,
      expires_at=expires_at,
      content_type=content_type,
      format_=format_,
      generation_count=generation_count,
    )

    get_report_bundle_download_url_report_bundle_download_response.additional_properties = d
    return get_report_bundle_download_url_report_bundle_download_response

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
