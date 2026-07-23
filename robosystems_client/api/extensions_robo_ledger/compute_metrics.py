from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compute_metrics_request import ComputeMetricsRequest
from ...models.error_response import ErrorResponse
from ...models.operation_envelope_compute_metrics_response import (
  OperationEnvelopeComputeMetricsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: ComputeMetricsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/compute-metrics".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeComputeMetricsResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeComputeMetricsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | OperationEnvelopeComputeMetricsResponse]:
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
  body: ComputeMetricsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeComputeMetricsResponse]:
  """Compute Metrics for a Metric Block

   Resolves the Derive rules scoped to a metric block (block_type='metric'), binds each rule's operands
  to the entity's most recent persisted report facts at period_end, evaluates, and upserts the
  period's standing factset_type='metric' FactSet — one per (structure, entity, period_end), so
  successive runs accumulate the time series and re-running a period replaces its values. Metrics with
  missing operands or undefined ratios are skipped with a reason, never errored.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ComputeMetricsRequest): Request body for the ``compute-metrics`` operation.

          Resolves the ``Derive`` rules scoped to the metric block, binds each
          rule's operands to the entity's most recent persisted report facts at
          ``period_end``, evaluates, and upserts the period's standing
          ``factset_type='metric'`` FactSet (re-running a period replaces its
          facts). One standing FactSet per (structure, entity, period_end) — the
          accumulating time series.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeComputeMetricsResponse]
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
  body: ComputeMetricsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeComputeMetricsResponse | None:
  """Compute Metrics for a Metric Block

   Resolves the Derive rules scoped to a metric block (block_type='metric'), binds each rule's operands
  to the entity's most recent persisted report facts at period_end, evaluates, and upserts the
  period's standing factset_type='metric' FactSet — one per (structure, entity, period_end), so
  successive runs accumulate the time series and re-running a period replaces its values. Metrics with
  missing operands or undefined ratios are skipped with a reason, never errored.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ComputeMetricsRequest): Request body for the ``compute-metrics`` operation.

          Resolves the ``Derive`` rules scoped to the metric block, binds each
          rule's operands to the entity's most recent persisted report facts at
          ``period_end``, evaluates, and upserts the period's standing
          ``factset_type='metric'`` FactSet (re-running a period replaces its
          facts). One standing FactSet per (structure, entity, period_end) — the
          accumulating time series.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeComputeMetricsResponse
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
  body: ComputeMetricsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeComputeMetricsResponse]:
  """Compute Metrics for a Metric Block

   Resolves the Derive rules scoped to a metric block (block_type='metric'), binds each rule's operands
  to the entity's most recent persisted report facts at period_end, evaluates, and upserts the
  period's standing factset_type='metric' FactSet — one per (structure, entity, period_end), so
  successive runs accumulate the time series and re-running a period replaces its values. Metrics with
  missing operands or undefined ratios are skipped with a reason, never errored.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ComputeMetricsRequest): Request body for the ``compute-metrics`` operation.

          Resolves the ``Derive`` rules scoped to the metric block, binds each
          rule's operands to the entity's most recent persisted report facts at
          ``period_end``, evaluates, and upserts the period's standing
          ``factset_type='metric'`` FactSet (re-running a period replaces its
          facts). One standing FactSet per (structure, entity, period_end) — the
          accumulating time series.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeComputeMetricsResponse]
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
  body: ComputeMetricsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeComputeMetricsResponse | None:
  """Compute Metrics for a Metric Block

   Resolves the Derive rules scoped to a metric block (block_type='metric'), binds each rule's operands
  to the entity's most recent persisted report facts at period_end, evaluates, and upserts the
  period's standing factset_type='metric' FactSet — one per (structure, entity, period_end), so
  successive runs accumulate the time series and re-running a period replaces its values. Metrics with
  missing operands or undefined ratios are skipped with a reason, never errored.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (ComputeMetricsRequest): Request body for the ``compute-metrics`` operation.

          Resolves the ``Derive`` rules scoped to the metric block, binds each
          rule's operands to the entity's most recent persisted report facts at
          ``period_end``, evaluates, and upserts the period's standing
          ``factset_type='metric'`` FactSet (re-running a period replaces its
          facts). One standing FactSet per (structure, entity, period_end) — the
          accumulating time series.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeComputeMetricsResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
