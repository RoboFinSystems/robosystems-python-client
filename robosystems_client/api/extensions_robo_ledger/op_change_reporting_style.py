from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_reporting_style_request import ChangeReportingStyleRequest
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_change_reporting_style_response import (
  OperationEnvelopeChangeReportingStyleResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: ChangeReportingStyleRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/change-reporting-style".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeChangeReportingStyleResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeChangeReportingStyleResponse.from_dict(
      response.json()
    )

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
) -> Response[ErrorResponse | OperationEnvelopeChangeReportingStyleResponse]:
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
  body: ChangeReportingStyleRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeChangeReportingStyleResponse]:
  """Change Reporting Style

   Switch the reporting entity's Reporting Style — how its statements are laid out (equity-form, close-
  target concept, per-statement Networks). Validates that the target Style has a complete composition
  in the tenant schema, then flips `entities.reporting_style_id`. Omit `entity_id` to target the
  graph's primary entity. Filed Reports are unaffected (their FactSet rows pin their structures at
  create-time); new reports use the new Style. Idempotent on the same id.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ChangeReportingStyleRequest): Switch a reporting entity's Reporting Style.

          The Reporting Style governs how the entity's statements are laid out
          (equity-form, close-target concept, per-statement Networks). It's
          validated against the tenant schema — the target must be a renderable
          Style with a complete composition — before the switch is applied.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeChangeReportingStyleResponse]
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
  body: ChangeReportingStyleRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeChangeReportingStyleResponse | None:
  """Change Reporting Style

   Switch the reporting entity's Reporting Style — how its statements are laid out (equity-form, close-
  target concept, per-statement Networks). Validates that the target Style has a complete composition
  in the tenant schema, then flips `entities.reporting_style_id`. Omit `entity_id` to target the
  graph's primary entity. Filed Reports are unaffected (their FactSet rows pin their structures at
  create-time); new reports use the new Style. Idempotent on the same id.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ChangeReportingStyleRequest): Switch a reporting entity's Reporting Style.

          The Reporting Style governs how the entity's statements are laid out
          (equity-form, close-target concept, per-statement Networks). It's
          validated against the tenant schema — the target must be a renderable
          Style with a complete composition — before the switch is applied.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeChangeReportingStyleResponse
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
  body: ChangeReportingStyleRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeChangeReportingStyleResponse]:
  """Change Reporting Style

   Switch the reporting entity's Reporting Style — how its statements are laid out (equity-form, close-
  target concept, per-statement Networks). Validates that the target Style has a complete composition
  in the tenant schema, then flips `entities.reporting_style_id`. Omit `entity_id` to target the
  graph's primary entity. Filed Reports are unaffected (their FactSet rows pin their structures at
  create-time); new reports use the new Style. Idempotent on the same id.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ChangeReportingStyleRequest): Switch a reporting entity's Reporting Style.

          The Reporting Style governs how the entity's statements are laid out
          (equity-form, close-target concept, per-statement Networks). It's
          validated against the tenant schema — the target must be a renderable
          Style with a complete composition — before the switch is applied.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeChangeReportingStyleResponse]
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
  body: ChangeReportingStyleRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeChangeReportingStyleResponse | None:
  """Change Reporting Style

   Switch the reporting entity's Reporting Style — how its statements are laid out (equity-form, close-
  target concept, per-statement Networks). Validates that the target Style has a complete composition
  in the tenant schema, then flips `entities.reporting_style_id`. Omit `entity_id` to target the
  graph's primary entity. Filed Reports are unaffected (their FactSet rows pin their structures at
  create-time); new reports use the new Style. Idempotent on the same id.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ChangeReportingStyleRequest): Switch a reporting entity's Reporting Style.

          The Reporting Style governs how the entity's statements are laid out
          (equity-form, close-target concept, per-statement Networks). It's
          validated against the tenant schema — the target must be a renderable
          Style with a complete composition — before the switch is applied.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeChangeReportingStyleResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
