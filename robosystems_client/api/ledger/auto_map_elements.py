from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  mapping_id: str,
) -> dict[str, Any]:
  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/ledger/{graph_id}/mappings/{mapping_id}/auto-map".format(
      graph_id=quote(str(graph_id), safe=""),
      mapping_id=quote(str(mapping_id), safe=""),
    ),
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
  if response.status_code == 202:
    response_202 = response.json()
    return response_202

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
  return Response(
    status_code=HTTPStatus(response.status_code),
    content=response.content,
    headers=response.headers,
    parsed=_parse_response(client=client, response=response),
  )


def sync_detailed(
  graph_id: str,
  mapping_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError]:
  """Auto-Map Elements via AI

   Trigger autonomous CoA → GAAP mapping via background worker.

  Uses Bedrock AI to classify and map unmapped Chart of Accounts elements
  to US GAAP reporting concepts. Returns a 202 with operation_id for
  SSE progress tracking.

  Confidence thresholds:
  - ≥0.90: auto-approved mapping
  - 0.70-0.89: flagged for review
  - <0.70: skipped (left unmapped)

  Args:
      graph_id (str):
      mapping_id (str): Mapping structure ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    mapping_id=mapping_id,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  mapping_id: str,
  *,
  client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
  """Auto-Map Elements via AI

   Trigger autonomous CoA → GAAP mapping via background worker.

  Uses Bedrock AI to classify and map unmapped Chart of Accounts elements
  to US GAAP reporting concepts. Returns a 202 with operation_id for
  SSE progress tracking.

  Confidence thresholds:
  - ≥0.90: auto-approved mapping
  - 0.70-0.89: flagged for review
  - <0.70: skipped (left unmapped)

  Args:
      graph_id (str):
      mapping_id (str): Mapping structure ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError
  """

  return sync_detailed(
    graph_id=graph_id,
    mapping_id=mapping_id,
    client=client,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  mapping_id: str,
  *,
  client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError]:
  """Auto-Map Elements via AI

   Trigger autonomous CoA → GAAP mapping via background worker.

  Uses Bedrock AI to classify and map unmapped Chart of Accounts elements
  to US GAAP reporting concepts. Returns a 202 with operation_id for
  SSE progress tracking.

  Confidence thresholds:
  - ≥0.90: auto-approved mapping
  - 0.70-0.89: flagged for review
  - <0.70: skipped (left unmapped)

  Args:
      graph_id (str):
      mapping_id (str): Mapping structure ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    mapping_id=mapping_id,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  mapping_id: str,
  *,
  client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
  """Auto-Map Elements via AI

   Trigger autonomous CoA → GAAP mapping via background worker.

  Uses Bedrock AI to classify and map unmapped Chart of Accounts elements
  to US GAAP reporting concepts. Returns a 202 with operation_id for
  SSE progress tracking.

  Confidence thresholds:
  - ≥0.90: auto-approved mapping
  - 0.70-0.89: flagged for review
  - <0.70: skipped (left unmapped)

  Args:
      graph_id (str):
      mapping_id (str): Mapping structure ID

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      mapping_id=mapping_id,
      client=client,
    )
  ).parsed
