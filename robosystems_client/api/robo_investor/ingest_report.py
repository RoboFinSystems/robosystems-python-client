from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.ingest_report_request import IngestReportRequest
from ...models.operation_envelope_ingest_report_response import (
  OperationEnvelopeIngestReportResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: IngestReportRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboinvestor/{graph_id}/operations/ingest-report".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeIngestReportResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeIngestReportResponse.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = ErrorResponse.from_dict(response.json())

    return response_401

  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403

  if response.status_code == 404:
    response_404 = ErrorResponse.from_dict(response.json())

    return response_404

  if response.status_code == 409:
    response_409 = ErrorResponse.from_dict(response.json())

    return response_409

  if response.status_code == 422:
    response_422 = ErrorResponse.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = ErrorResponse.from_dict(response.json())

    return response_429

  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | OperationEnvelopeIngestReportResponse]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: IngestReportRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeIngestReportResponse]:
  """Ingest Report

   Load a report a company sent onto its entity. Give the report as `holon` (the text of a
  `.holon.jsonld` file), as `tavi` (the text of a `.tavi.json` compiled model) or as `report` (rows
  read from a PDF or a workbook: each value with the page or cell it came from). Rows and a Tavi model
  are turned into a holon here. For rows, a balance sheet or an income statement named without its
  lines is laid out from the library, so only the values need sending. The holon is checked before
  anything is written: every value resolves, duplicate values agree, every total foots to its terms,
  and total assets equal total liabilities and equity. A report that fails is refused with each reason
  and nothing is loaded. One that passes is stored as the record of what was received, and its facts
  become queryable from every holding in the company. A second ingest for the same entity, period end
  and kind replaces the first. Set `dry_run` to run the checks and see what would load without
  writing.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (IngestReportRequest): CQRS body for `POST /operations/ingest-report`.

          Give exactly one of `holon` (a report file already in the holon format),
          `tavi` (a Tavi compiled model) or `report` (rows read from a PDF or a
          workbook, which the server assembles into a holon). Every route ends in a
          holon that is checked, stored as the record of what was received, and
          loaded onto the entity.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeIngestReportResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    idempotency_key=idempotency_key,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: IngestReportRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeIngestReportResponse | None:
  """Ingest Report

   Load a report a company sent onto its entity. Give the report as `holon` (the text of a
  `.holon.jsonld` file), as `tavi` (the text of a `.tavi.json` compiled model) or as `report` (rows
  read from a PDF or a workbook: each value with the page or cell it came from). Rows and a Tavi model
  are turned into a holon here. For rows, a balance sheet or an income statement named without its
  lines is laid out from the library, so only the values need sending. The holon is checked before
  anything is written: every value resolves, duplicate values agree, every total foots to its terms,
  and total assets equal total liabilities and equity. A report that fails is refused with each reason
  and nothing is loaded. One that passes is stored as the record of what was received, and its facts
  become queryable from every holding in the company. A second ingest for the same entity, period end
  and kind replaces the first. Set `dry_run` to run the checks and see what would load without
  writing.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (IngestReportRequest): CQRS body for `POST /operations/ingest-report`.

          Give exactly one of `holon` (a report file already in the holon format),
          `tavi` (a Tavi compiled model) or `report` (rows read from a PDF or a
          workbook, which the server assembles into a holon). Every route ends in a
          holon that is checked, stored as the record of what was received, and
          loaded onto the entity.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeIngestReportResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
    idempotency_key=idempotency_key,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: IngestReportRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeIngestReportResponse]:
  """Ingest Report

   Load a report a company sent onto its entity. Give the report as `holon` (the text of a
  `.holon.jsonld` file), as `tavi` (the text of a `.tavi.json` compiled model) or as `report` (rows
  read from a PDF or a workbook: each value with the page or cell it came from). Rows and a Tavi model
  are turned into a holon here. For rows, a balance sheet or an income statement named without its
  lines is laid out from the library, so only the values need sending. The holon is checked before
  anything is written: every value resolves, duplicate values agree, every total foots to its terms,
  and total assets equal total liabilities and equity. A report that fails is refused with each reason
  and nothing is loaded. One that passes is stored as the record of what was received, and its facts
  become queryable from every holding in the company. A second ingest for the same entity, period end
  and kind replaces the first. Set `dry_run` to run the checks and see what would load without
  writing.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (IngestReportRequest): CQRS body for `POST /operations/ingest-report`.

          Give exactly one of `holon` (a report file already in the holon format),
          `tavi` (a Tavi compiled model) or `report` (rows read from a PDF or a
          workbook, which the server assembles into a holon). Every route ends in a
          holon that is checked, stored as the record of what was received, and
          loaded onto the entity.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeIngestReportResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    idempotency_key=idempotency_key,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: IngestReportRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeIngestReportResponse | None:
  """Ingest Report

   Load a report a company sent onto its entity. Give the report as `holon` (the text of a
  `.holon.jsonld` file), as `tavi` (the text of a `.tavi.json` compiled model) or as `report` (rows
  read from a PDF or a workbook: each value with the page or cell it came from). Rows and a Tavi model
  are turned into a holon here. For rows, a balance sheet or an income statement named without its
  lines is laid out from the library, so only the values need sending. The holon is checked before
  anything is written: every value resolves, duplicate values agree, every total foots to its terms,
  and total assets equal total liabilities and equity. A report that fails is refused with each reason
  and nothing is loaded. One that passes is stored as the record of what was received, and its facts
  become queryable from every holding in the company. A second ingest for the same entity, period end
  and kind replaces the first. Set `dry_run` to run the checks and see what would load without
  writing.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (IngestReportRequest): CQRS body for `POST /operations/ingest-report`.

          Give exactly one of `holon` (a report file already in the holon format),
          `tavi` (a Tavi compiled model) or `report` (rows read from a PDF or a
          workbook, which the server assembles into a holon). Every route ends in a
          holon that is checked, stored as the record of what was received, and
          loaded onto the entity.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeIngestReportResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
