from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.initialize_chart_of_accounts_request import (
  InitializeChartOfAccountsRequest,
)
from ...models.operation_envelope_initialize_chart_of_accounts_response import (
  OperationEnvelopeInitializeChartOfAccountsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: InitializeChartOfAccountsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/initialize-chart-of-accounts".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationEnvelopeInitializeChartOfAccountsResponse | None:
  if response.status_code == 200:
    response_200 = OperationEnvelopeInitializeChartOfAccountsResponse.from_dict(
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
) -> Response[ErrorResponse | OperationEnvelopeInitializeChartOfAccountsResponse]:
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
  body: InitializeChartOfAccountsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeInitializeChartOfAccountsResponse]:
  """Initialize Chart of Accounts

   Create the graph's chart of accounts from a shipped template — the fresh-company path to native
  books. Use when the graph has NO chart (a QuickBooks-synced tenant never needs this: its chart
  arrives with the sync and stays after a sever) and before connecting a bank feed, which needs a
  chart to resolve against. Templates: `saas` (subscription software), `services` (professional
  services), `product` (inventory and COGS) — the `chartTemplates` GraphQL field lists them with names
  and account counts. Creates the chart, its `coa_mapping` structure and the template's CoA → rs-gaap
  mapping associations in one transaction, with the equity rows mapped by the entity's legal form
  (`entity_type`, defaulting to the graph's primary entity). One-time: 409 once a chart exists — a
  chart is never replaced. Customize afterwards with update-taxonomy-block; accounts that carry
  activity are never deleted.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (InitializeChartOfAccountsRequest): Create the graph's chart of accounts from a
          shipped template.

          Refused (409) when the graph already has an active ``chart_of_accounts``
          taxonomy — a QuickBooks-synced tenant never needs this, and a chart is
          never replaced. The template's equity rows are mapped by the entity's
          legal form (``entity_type``: corporation / llc / partnership); omit it
          to use the graph's primary entity, falling back to corporation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeInitializeChartOfAccountsResponse]
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
  body: InitializeChartOfAccountsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeInitializeChartOfAccountsResponse | None:
  """Initialize Chart of Accounts

   Create the graph's chart of accounts from a shipped template — the fresh-company path to native
  books. Use when the graph has NO chart (a QuickBooks-synced tenant never needs this: its chart
  arrives with the sync and stays after a sever) and before connecting a bank feed, which needs a
  chart to resolve against. Templates: `saas` (subscription software), `services` (professional
  services), `product` (inventory and COGS) — the `chartTemplates` GraphQL field lists them with names
  and account counts. Creates the chart, its `coa_mapping` structure and the template's CoA → rs-gaap
  mapping associations in one transaction, with the equity rows mapped by the entity's legal form
  (`entity_type`, defaulting to the graph's primary entity). One-time: 409 once a chart exists — a
  chart is never replaced. Customize afterwards with update-taxonomy-block; accounts that carry
  activity are never deleted.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (InitializeChartOfAccountsRequest): Create the graph's chart of accounts from a
          shipped template.

          Refused (409) when the graph already has an active ``chart_of_accounts``
          taxonomy — a QuickBooks-synced tenant never needs this, and a chart is
          never replaced. The template's equity rows are mapped by the entity's
          legal form (``entity_type``: corporation / llc / partnership); omit it
          to use the graph's primary entity, falling back to corporation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeInitializeChartOfAccountsResponse
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
  body: InitializeChartOfAccountsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[ErrorResponse | OperationEnvelopeInitializeChartOfAccountsResponse]:
  """Initialize Chart of Accounts

   Create the graph's chart of accounts from a shipped template — the fresh-company path to native
  books. Use when the graph has NO chart (a QuickBooks-synced tenant never needs this: its chart
  arrives with the sync and stays after a sever) and before connecting a bank feed, which needs a
  chart to resolve against. Templates: `saas` (subscription software), `services` (professional
  services), `product` (inventory and COGS) — the `chartTemplates` GraphQL field lists them with names
  and account counts. Creates the chart, its `coa_mapping` structure and the template's CoA → rs-gaap
  mapping associations in one transaction, with the equity rows mapped by the entity's legal form
  (`entity_type`, defaulting to the graph's primary entity). One-time: 409 once a chart exists — a
  chart is never replaced. Customize afterwards with update-taxonomy-block; accounts that carry
  activity are never deleted.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (InitializeChartOfAccountsRequest): Create the graph's chart of accounts from a
          shipped template.

          Refused (409) when the graph already has an active ``chart_of_accounts``
          taxonomy — a QuickBooks-synced tenant never needs this, and a chart is
          never replaced. The template's equity rows are mapped by the entity's
          legal form (``entity_type``: corporation / llc / partnership); omit it
          to use the graph's primary entity, falling back to corporation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[ErrorResponse | OperationEnvelopeInitializeChartOfAccountsResponse]
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
  body: InitializeChartOfAccountsRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> ErrorResponse | OperationEnvelopeInitializeChartOfAccountsResponse | None:
  """Initialize Chart of Accounts

   Create the graph's chart of accounts from a shipped template — the fresh-company path to native
  books. Use when the graph has NO chart (a QuickBooks-synced tenant never needs this: its chart
  arrives with the sync and stays after a sever) and before connecting a bank feed, which needs a
  chart to resolve against. Templates: `saas` (subscription software), `services` (professional
  services), `product` (inventory and COGS) — the `chartTemplates` GraphQL field lists them with names
  and account counts. Creates the chart, its `coa_mapping` structure and the template's CoA → rs-gaap
  mapping associations in one transaction, with the equity rows mapped by the entity's legal form
  (`entity_type`, defaulting to the graph's primary entity). One-time: 409 once a chart exists — a
  chart is never replaced. Customize afterwards with update-taxonomy-block; accounts that carry
  activity are never deleted.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (InitializeChartOfAccountsRequest): Create the graph's chart of accounts from a
          shipped template.

          Refused (409) when the graph already has an active ``chart_of_accounts``
          taxonomy — a QuickBooks-synced tenant never needs this, and a chart is
          never replaced. The template's equity rows are mapped by the entity's
          legal form (``entity_type``: corporation / llc / partnership); omit it
          to use the graph's primary entity, falling back to corporation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      ErrorResponse | OperationEnvelopeInitializeChartOfAccountsResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
