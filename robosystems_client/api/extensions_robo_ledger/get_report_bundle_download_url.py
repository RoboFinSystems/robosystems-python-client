from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_report_bundle_download_url_report_bundle_download_response import (
  GetReportBundleDownloadUrlReportBundleDownloadResponse,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  report_id: str,
  *,
  format_: str | Unset = "jsonld",
  expires_in: int | Unset = 300,
) -> dict[str, Any]:

  params: dict[str, Any] = {}

  params["format"] = format_

  params["expires_in"] = expires_in

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/extensions/roboledger/{graph_id}/reports/{report_id}/download".format(
      graph_id=quote(str(graph_id), safe=""),
      report_id=quote(str(report_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
  GetReportBundleDownloadUrlReportBundleDownloadResponse | HTTPValidationError | None
):
  if response.status_code == 200:
    response_200 = GetReportBundleDownloadUrlReportBundleDownloadResponse.from_dict(
      response.json()
    )

    return response_200

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
  GetReportBundleDownloadUrlReportBundleDownloadResponse | HTTPValidationError
]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  report_id: str,
  *,
  client: AuthenticatedClient,
  format_: str | Unset = "jsonld",
  expires_in: int | Unset = 300,
) -> Response[
  GetReportBundleDownloadUrlReportBundleDownloadResponse | HTTPValidationError
]:
  """Download Report bundle

   Return the published Report's serialization bundle. ``format=jsonld`` (default) returns a JSON
  envelope containing a short-lived presigned URL to the stamped JSON-LD bundle in S3.
  ``format=xbrl-2.1`` rebuilds the bundle on-demand and streams an XBRL 2.1 zip directly. 404 when the
  Report has no stamped bundle (published before the serialization feature shipped — JSON-LD only).

  Args:
      graph_id (str):
      report_id (str): Report identifier (rpt_-prefixed ULID).
      format_ (str | Unset): Serialization flavor. ``jsonld`` returns a presigned URL to the
          stored JSON-LD bundle; ``xbrl-2.1`` streams a freshly-emitted XBRL zip directly. Other RDF
          / XBRL flavors slot in as their producers ship. Default: 'jsonld'.
      expires_in (int | Unset): Presigned URL lifetime in seconds (min 60, max 3600). Ignored
          for XBRL flavors (streamed directly, no URL). Default: 300.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[GetReportBundleDownloadUrlReportBundleDownloadResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    report_id=report_id,
    format_=format_,
    expires_in=expires_in,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  report_id: str,
  *,
  client: AuthenticatedClient,
  format_: str | Unset = "jsonld",
  expires_in: int | Unset = 300,
) -> (
  GetReportBundleDownloadUrlReportBundleDownloadResponse | HTTPValidationError | None
):
  """Download Report bundle

   Return the published Report's serialization bundle. ``format=jsonld`` (default) returns a JSON
  envelope containing a short-lived presigned URL to the stamped JSON-LD bundle in S3.
  ``format=xbrl-2.1`` rebuilds the bundle on-demand and streams an XBRL 2.1 zip directly. 404 when the
  Report has no stamped bundle (published before the serialization feature shipped — JSON-LD only).

  Args:
      graph_id (str):
      report_id (str): Report identifier (rpt_-prefixed ULID).
      format_ (str | Unset): Serialization flavor. ``jsonld`` returns a presigned URL to the
          stored JSON-LD bundle; ``xbrl-2.1`` streams a freshly-emitted XBRL zip directly. Other RDF
          / XBRL flavors slot in as their producers ship. Default: 'jsonld'.
      expires_in (int | Unset): Presigned URL lifetime in seconds (min 60, max 3600). Ignored
          for XBRL flavors (streamed directly, no URL). Default: 300.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      GetReportBundleDownloadUrlReportBundleDownloadResponse | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    report_id=report_id,
    client=client,
    format_=format_,
    expires_in=expires_in,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  report_id: str,
  *,
  client: AuthenticatedClient,
  format_: str | Unset = "jsonld",
  expires_in: int | Unset = 300,
) -> Response[
  GetReportBundleDownloadUrlReportBundleDownloadResponse | HTTPValidationError
]:
  """Download Report bundle

   Return the published Report's serialization bundle. ``format=jsonld`` (default) returns a JSON
  envelope containing a short-lived presigned URL to the stamped JSON-LD bundle in S3.
  ``format=xbrl-2.1`` rebuilds the bundle on-demand and streams an XBRL 2.1 zip directly. 404 when the
  Report has no stamped bundle (published before the serialization feature shipped — JSON-LD only).

  Args:
      graph_id (str):
      report_id (str): Report identifier (rpt_-prefixed ULID).
      format_ (str | Unset): Serialization flavor. ``jsonld`` returns a presigned URL to the
          stored JSON-LD bundle; ``xbrl-2.1`` streams a freshly-emitted XBRL zip directly. Other RDF
          / XBRL flavors slot in as their producers ship. Default: 'jsonld'.
      expires_in (int | Unset): Presigned URL lifetime in seconds (min 60, max 3600). Ignored
          for XBRL flavors (streamed directly, no URL). Default: 300.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[GetReportBundleDownloadUrlReportBundleDownloadResponse | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    report_id=report_id,
    format_=format_,
    expires_in=expires_in,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  report_id: str,
  *,
  client: AuthenticatedClient,
  format_: str | Unset = "jsonld",
  expires_in: int | Unset = 300,
) -> (
  GetReportBundleDownloadUrlReportBundleDownloadResponse | HTTPValidationError | None
):
  """Download Report bundle

   Return the published Report's serialization bundle. ``format=jsonld`` (default) returns a JSON
  envelope containing a short-lived presigned URL to the stamped JSON-LD bundle in S3.
  ``format=xbrl-2.1`` rebuilds the bundle on-demand and streams an XBRL 2.1 zip directly. 404 when the
  Report has no stamped bundle (published before the serialization feature shipped — JSON-LD only).

  Args:
      graph_id (str):
      report_id (str): Report identifier (rpt_-prefixed ULID).
      format_ (str | Unset): Serialization flavor. ``jsonld`` returns a presigned URL to the
          stored JSON-LD bundle; ``xbrl-2.1`` streams a freshly-emitted XBRL zip directly. Other RDF
          / XBRL flavors slot in as their producers ship. Default: 'jsonld'.
      expires_in (int | Unset): Presigned URL lifetime in seconds (min 60, max 3600). Ignored
          for XBRL flavors (streamed directly, no URL). Default: 300.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      GetReportBundleDownloadUrlReportBundleDownloadResponse | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      report_id=report_id,
      client=client,
      format_=format_,
      expires_in=expires_in,
    )
  ).parsed
