from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.operation_envelope import OperationEnvelope
from ...models.operation_error import OperationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  force: bool | Unset = False,
  rebuild: bool | Unset = False,
  ignore_errors: bool | Unset = True,
  dry_run: bool | Unset = False,
  source: None | str | Unset = UNSET,
  materialize_embeddings: bool | Unset = False,
  idempotency_key: None | str | Unset = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(idempotency_key, Unset):
    headers["Idempotency-Key"] = idempotency_key

  params: dict[str, Any] = {}

  params["force"] = force

  params["rebuild"] = rebuild

  params["ignore_errors"] = ignore_errors

  params["dry_run"] = dry_run

  json_source: None | str | Unset
  if isinstance(source, Unset):
    json_source = UNSET
  else:
    json_source = source
  params["source"] = json_source

  params["materialize_embeddings"] = materialize_embeddings

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": "/v1/graphs/{graph_id}/operations/materialize".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | OperationEnvelope | OperationError | None:
  if response.status_code == 202:
    response_202 = OperationEnvelope.from_dict(response.json())

    return response_202

  if response.status_code == 400:
    response_400 = OperationError.from_dict(response.json())

    return response_400

  if response.status_code == 401:
    response_401 = cast(Any, None)
    return response_401

  if response.status_code == 403:
    response_403 = cast(Any, None)
    return response_403

  if response.status_code == 404:
    response_404 = OperationError.from_dict(response.json())

    return response_404

  if response.status_code == 409:
    response_409 = OperationError.from_dict(response.json())

    return response_409

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if response.status_code == 429:
    response_429 = cast(Any, None)
    return response_429

  if response.status_code == 500:
    response_500 = cast(Any, None)
    return response_500

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError | OperationEnvelope | OperationError]:
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
  force: bool | Unset = False,
  rebuild: bool | Unset = False,
  ignore_errors: bool | Unset = True,
  dry_run: bool | Unset = False,
  source: None | str | Unset = UNSET,
  materialize_embeddings: bool | Unset = False,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | OperationEnvelope | OperationError]:
  """Materialize Graph

   Materialize graph from staging tables or extensions OLTP.

  Delegates to the existing materialize_graph handler which handles
  distributed locking, source routing, and Dagster/direct dispatch.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      force (bool | Unset):  Default: False.
      rebuild (bool | Unset):  Default: False.
      ignore_errors (bool | Unset):  Default: True.
      dry_run (bool | Unset):  Default: False.
      source (None | str | Unset):
      materialize_embeddings (bool | Unset):  Default: False.
      idempotency_key (None | str | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError | OperationEnvelope | OperationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    force=force,
    rebuild=rebuild,
    ignore_errors=ignore_errors,
    dry_run=dry_run,
    source=source,
    materialize_embeddings=materialize_embeddings,
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
  force: bool | Unset = False,
  rebuild: bool | Unset = False,
  ignore_errors: bool | Unset = True,
  dry_run: bool | Unset = False,
  source: None | str | Unset = UNSET,
  materialize_embeddings: bool | Unset = False,
  idempotency_key: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | OperationEnvelope | OperationError | None:
  """Materialize Graph

   Materialize graph from staging tables or extensions OLTP.

  Delegates to the existing materialize_graph handler which handles
  distributed locking, source routing, and Dagster/direct dispatch.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      force (bool | Unset):  Default: False.
      rebuild (bool | Unset):  Default: False.
      ignore_errors (bool | Unset):  Default: True.
      dry_run (bool | Unset):  Default: False.
      source (None | str | Unset):
      materialize_embeddings (bool | Unset):  Default: False.
      idempotency_key (None | str | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError | OperationEnvelope | OperationError
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    force=force,
    rebuild=rebuild,
    ignore_errors=ignore_errors,
    dry_run=dry_run,
    source=source,
    materialize_embeddings=materialize_embeddings,
    idempotency_key=idempotency_key,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  force: bool | Unset = False,
  rebuild: bool | Unset = False,
  ignore_errors: bool | Unset = True,
  dry_run: bool | Unset = False,
  source: None | str | Unset = UNSET,
  materialize_embeddings: bool | Unset = False,
  idempotency_key: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | OperationEnvelope | OperationError]:
  """Materialize Graph

   Materialize graph from staging tables or extensions OLTP.

  Delegates to the existing materialize_graph handler which handles
  distributed locking, source routing, and Dagster/direct dispatch.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      force (bool | Unset):  Default: False.
      rebuild (bool | Unset):  Default: False.
      ignore_errors (bool | Unset):  Default: True.
      dry_run (bool | Unset):  Default: False.
      source (None | str | Unset):
      materialize_embeddings (bool | Unset):  Default: False.
      idempotency_key (None | str | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Any | HTTPValidationError | OperationEnvelope | OperationError]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    force=force,
    rebuild=rebuild,
    ignore_errors=ignore_errors,
    dry_run=dry_run,
    source=source,
    materialize_embeddings=materialize_embeddings,
    idempotency_key=idempotency_key,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  force: bool | Unset = False,
  rebuild: bool | Unset = False,
  ignore_errors: bool | Unset = True,
  dry_run: bool | Unset = False,
  source: None | str | Unset = UNSET,
  materialize_embeddings: bool | Unset = False,
  idempotency_key: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | OperationEnvelope | OperationError | None:
  """Materialize Graph

   Materialize graph from staging tables or extensions OLTP.

  Delegates to the existing materialize_graph handler which handles
  distributed locking, source routing, and Dagster/direct dispatch.

  **Idempotency**: supply an `Idempotency-Key` header to make safe retries; replays within 24 hours
  return the same envelope. Reusing the key with a different body returns HTTP 409 Conflict.

  Args:
      graph_id (str):
      force (bool | Unset):  Default: False.
      rebuild (bool | Unset):  Default: False.
      ignore_errors (bool | Unset):  Default: True.
      dry_run (bool | Unset):  Default: False.
      source (None | str | Unset):
      materialize_embeddings (bool | Unset):  Default: False.
      idempotency_key (None | str | Unset):

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Any | HTTPValidationError | OperationEnvelope | OperationError
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      force=force,
      rebuild=rebuild,
      ignore_errors=ignore_errors,
      dry_run=dry_run,
      source=source,
      materialize_embeddings=materialize_embeddings,
      idempotency_key=idempotency_key,
    )
  ).parsed
