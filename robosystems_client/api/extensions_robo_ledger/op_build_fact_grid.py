from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_view_request import CreateViewRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.operation_envelope import OperationEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: CreateViewRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/extensions/roboledger/{graph_id}/operations/build-fact-grid".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | OperationEnvelope | None:
  if response.status_code == 200:
    response_200 = OperationEnvelope.from_dict(response.json())

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
) -> Response[HTTPValidationError | OperationEnvelope]:
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
  body: CreateViewRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | OperationEnvelope]:
  """Build Fact Grid

   Build a multi-dimensional fact grid against the graph schema.

  Queries `Fact` nodes by element qnames or canonical concepts with
  optional filters for periods, entities, filing form, fiscal context,
  and period type. Returns a deduplicated pivot table plus optional
  summary statistics.

  This is a graph-database read — the query runs against LadybugDB,
  not the extensions OLTP database. The same operation works for
  roboledger tenant graphs (post-materialization) and the SEC shared
  repository (which uses the same XBRL hypercube schema).

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (CreateViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | OperationEnvelope]
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
  body: CreateViewRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> HTTPValidationError | OperationEnvelope | None:
  """Build Fact Grid

   Build a multi-dimensional fact grid against the graph schema.

  Queries `Fact` nodes by element qnames or canonical concepts with
  optional filters for periods, entities, filing form, fiscal context,
  and period type. Returns a deduplicated pivot table plus optional
  summary statistics.

  This is a graph-database read — the query runs against LadybugDB,
  not the extensions OLTP database. The same operation works for
  roboledger tenant graphs (post-materialization) and the SEC shared
  repository (which uses the same XBRL hypercube schema).

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (CreateViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | OperationEnvelope
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
  body: CreateViewRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | OperationEnvelope]:
  """Build Fact Grid

   Build a multi-dimensional fact grid against the graph schema.

  Queries `Fact` nodes by element qnames or canonical concepts with
  optional filters for periods, entities, filing form, fiscal context,
  and period type. Returns a deduplicated pivot table plus optional
  summary statistics.

  This is a graph-database read — the query runs against LadybugDB,
  not the extensions OLTP database. The same operation works for
  roboledger tenant graphs (post-materialization) and the SEC shared
  repository (which uses the same XBRL hypercube schema).

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (CreateViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | OperationEnvelope]
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
  body: CreateViewRequest,
  idempotency_key: None | str | Unset = UNSET,
) -> HTTPValidationError | OperationEnvelope | None:
  """Build Fact Grid

   Build a multi-dimensional fact grid against the graph schema.

  Queries `Fact` nodes by element qnames or canonical concepts with
  optional filters for periods, entities, filing form, fiscal context,
  and period type. Returns a deduplicated pivot table plus optional
  summary statistics.

  This is a graph-database read — the query runs against LadybugDB,
  not the extensions OLTP database. The same operation works for
  roboledger tenant graphs (post-materialization) and the SEC shared
  repository (which uses the same XBRL hypercube schema).

  Args:
      graph_id (str):
      idempotency_key (None | str | Unset):
      body (CreateViewRequest):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | OperationEnvelope
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      idempotency_key=idempotency_key,
    )
  ).parsed
