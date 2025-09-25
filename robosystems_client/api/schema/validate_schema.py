from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schema_validation_request import SchemaValidationRequest
from ...models.schema_validation_response import SchemaValidationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  body: SchemaValidationRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}
  if not isinstance(authorization, Unset):
    headers["authorization"] = authorization

  params: dict[str, Any] = {}

  json_token: Union[None, Unset, str]
  if isinstance(token, Unset):
    json_token = UNSET
  else:
    json_token = token
  params["token"] = json_token

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/schema/validate",
    "params": params,
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SchemaValidationResponse]]:
  if response.status_code == 200:
    response_200 = SchemaValidationResponse.from_dict(response.json())

    return response_200
  if response.status_code == 400:
    response_400 = ErrorResponse.from_dict(response.json())

    return response_400
  if response.status_code == 403:
    response_403 = ErrorResponse.from_dict(response.json())

    return response_403
  if response.status_code == 422:
    response_422 = ErrorResponse.from_dict(response.json())

    return response_422
  if response.status_code == 500:
    response_500 = ErrorResponse.from_dict(response.json())

    return response_500
  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, SchemaValidationResponse]]:
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
  body: SchemaValidationRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, SchemaValidationResponse]]:
  """Validate Schema

   Validate a custom schema definition before deployment.

  This endpoint performs comprehensive validation including:
  - **Structure Validation**: Ensures proper JSON/YAML format
  - **Type Checking**: Validates data types (STRING, INT, DOUBLE, etc.)
  - **Constraint Verification**: Checks primary keys and unique constraints
  - **Relationship Integrity**: Validates node references in relationships
  - **Naming Conventions**: Ensures valid identifiers
  - **Compatibility**: Checks against existing extensions if specified

  Supported formats:
  - JSON schema definitions
  - YAML schema definitions
  - Direct dictionary format

  Validation helps prevent:
  - Schema deployment failures
  - Data integrity issues
  - Performance problems
  - Naming conflicts

  This operation is FREE - no credit consumption required.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (SchemaValidationRequest): Request model for schema validation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, SchemaValidationResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    token=token,
    authorization=authorization,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: SchemaValidationRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, SchemaValidationResponse]]:
  """Validate Schema

   Validate a custom schema definition before deployment.

  This endpoint performs comprehensive validation including:
  - **Structure Validation**: Ensures proper JSON/YAML format
  - **Type Checking**: Validates data types (STRING, INT, DOUBLE, etc.)
  - **Constraint Verification**: Checks primary keys and unique constraints
  - **Relationship Integrity**: Validates node references in relationships
  - **Naming Conventions**: Ensures valid identifiers
  - **Compatibility**: Checks against existing extensions if specified

  Supported formats:
  - JSON schema definitions
  - YAML schema definitions
  - Direct dictionary format

  Validation helps prevent:
  - Schema deployment failures
  - Data integrity issues
  - Performance problems
  - Naming conflicts

  This operation is FREE - no credit consumption required.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (SchemaValidationRequest): Request model for schema validation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, SchemaValidationResponse]
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    body=body,
    token=token,
    authorization=authorization,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: SchemaValidationRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, SchemaValidationResponse]]:
  """Validate Schema

   Validate a custom schema definition before deployment.

  This endpoint performs comprehensive validation including:
  - **Structure Validation**: Ensures proper JSON/YAML format
  - **Type Checking**: Validates data types (STRING, INT, DOUBLE, etc.)
  - **Constraint Verification**: Checks primary keys and unique constraints
  - **Relationship Integrity**: Validates node references in relationships
  - **Naming Conventions**: Ensures valid identifiers
  - **Compatibility**: Checks against existing extensions if specified

  Supported formats:
  - JSON schema definitions
  - YAML schema definitions
  - Direct dictionary format

  Validation helps prevent:
  - Schema deployment failures
  - Data integrity issues
  - Performance problems
  - Naming conflicts

  This operation is FREE - no credit consumption required.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (SchemaValidationRequest): Request model for schema validation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[ErrorResponse, SchemaValidationResponse]]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    body=body,
    token=token,
    authorization=authorization,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: SchemaValidationRequest,
  token: Union[None, Unset, str] = UNSET,
  authorization: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, SchemaValidationResponse]]:
  """Validate Schema

   Validate a custom schema definition before deployment.

  This endpoint performs comprehensive validation including:
  - **Structure Validation**: Ensures proper JSON/YAML format
  - **Type Checking**: Validates data types (STRING, INT, DOUBLE, etc.)
  - **Constraint Verification**: Checks primary keys and unique constraints
  - **Relationship Integrity**: Validates node references in relationships
  - **Naming Conventions**: Ensures valid identifiers
  - **Compatibility**: Checks against existing extensions if specified

  Supported formats:
  - JSON schema definitions
  - YAML schema definitions
  - Direct dictionary format

  Validation helps prevent:
  - Schema deployment failures
  - Data integrity issues
  - Performance problems
  - Naming conflicts

  This operation is FREE - no credit consumption required.

  Args:
      graph_id (str): Graph database identifier
      token (Union[None, Unset, str]): JWT token for SSE authentication
      authorization (Union[None, Unset, str]):
      body (SchemaValidationRequest): Request model for schema validation.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[ErrorResponse, SchemaValidationResponse]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
      token=token,
      authorization=authorization,
    )
  ).parsed
