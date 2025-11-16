from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schema_validation_request import SchemaValidationRequest
from ...models.schema_validation_response import SchemaValidationResponse
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: SchemaValidationRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/schema/validate",
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

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Schema validation is performed against the specified graph/subgraph's current
  schema and data structure.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
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

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Schema validation is performed against the specified graph/subgraph's current
  schema and data structure.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
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
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: SchemaValidationRequest,
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

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Schema validation is performed against the specified graph/subgraph's current
  schema and data structure.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
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
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  body: SchemaValidationRequest,
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

  **Subgraph Support:**
  This endpoint accepts both parent graph IDs and subgraph IDs.
  - Parent graph: Use `graph_id` like `kg0123456789abcdef`
  - Subgraph: Use full subgraph ID like `kg0123456789abcdef_dev`
  Schema validation is performed against the specified graph/subgraph's current
  schema and data structure.

  This operation is included - no credit consumption required.

  Args:
      graph_id (str):
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
    )
  ).parsed
