from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_recommendation_request import AgentRecommendationRequest
from ...models.agent_recommendation_response import AgentRecommendationResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
  graph_id: str,
  *,
  body: AgentRecommendationRequest,
) -> dict[str, Any]:
  headers: dict[str, Any] = {}

  _kwargs: dict[str, Any] = {
    "method": "post",
    "url": f"/v1/graphs/{graph_id}/agent/recommend",
  }

  _kwargs["json"] = body.to_dict()

  headers["Content-Type"] = "application/json"

  _kwargs["headers"] = headers
  return _kwargs


def _parse_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AgentRecommendationResponse, Any, HTTPValidationError]]:
  if response.status_code == 200:
    response_200 = AgentRecommendationResponse.from_dict(response.json())

    return response_200

  if response.status_code == 400:
    response_400 = cast(Any, None)
    return response_400

  if response.status_code == 422:
    response_422 = HTTPValidationError.from_dict(response.json())

    return response_422

  if client.raise_on_unexpected_status:
    raise errors.UnexpectedStatus(response.status_code, response.content)
  else:
    return None


def _build_response(
  *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AgentRecommendationResponse, Any, HTTPValidationError]]:
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
  body: AgentRecommendationRequest,
) -> Response[Union[AgentRecommendationResponse, Any, HTTPValidationError]]:
  """Get agent recommendations

   Get intelligent agent recommendations for a specific query.

  **How it works:**
  1. Analyzes query content and structure
  2. Evaluates agent capabilities
  3. Calculates confidence scores
  4. Returns ranked recommendations

  **Use this when:**
  - Unsure which agent to use
  - Need to understand agent suitability
  - Want confidence scores for decision making

  Returns top agents ranked by confidence with explanations.

  Args:
      graph_id (str):
      body (AgentRecommendationRequest): Request for agent recommendations.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AgentRecommendationResponse, Any, HTTPValidationError]]
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
  body: AgentRecommendationRequest,
) -> Optional[Union[AgentRecommendationResponse, Any, HTTPValidationError]]:
  """Get agent recommendations

   Get intelligent agent recommendations for a specific query.

  **How it works:**
  1. Analyzes query content and structure
  2. Evaluates agent capabilities
  3. Calculates confidence scores
  4. Returns ranked recommendations

  **Use this when:**
  - Unsure which agent to use
  - Need to understand agent suitability
  - Want confidence scores for decision making

  Returns top agents ranked by confidence with explanations.

  Args:
      graph_id (str):
      body (AgentRecommendationRequest): Request for agent recommendations.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AgentRecommendationResponse, Any, HTTPValidationError]
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
  body: AgentRecommendationRequest,
) -> Response[Union[AgentRecommendationResponse, Any, HTTPValidationError]]:
  """Get agent recommendations

   Get intelligent agent recommendations for a specific query.

  **How it works:**
  1. Analyzes query content and structure
  2. Evaluates agent capabilities
  3. Calculates confidence scores
  4. Returns ranked recommendations

  **Use this when:**
  - Unsure which agent to use
  - Need to understand agent suitability
  - Want confidence scores for decision making

  Returns top agents ranked by confidence with explanations.

  Args:
      graph_id (str):
      body (AgentRecommendationRequest): Request for agent recommendations.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[Union[AgentRecommendationResponse, Any, HTTPValidationError]]
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
  body: AgentRecommendationRequest,
) -> Optional[Union[AgentRecommendationResponse, Any, HTTPValidationError]]:
  """Get agent recommendations

   Get intelligent agent recommendations for a specific query.

  **How it works:**
  1. Analyzes query content and structure
  2. Evaluates agent capabilities
  3. Calculates confidence scores
  4. Returns ranked recommendations

  **Use this when:**
  - Unsure which agent to use
  - Need to understand agent suitability
  - Want confidence scores for decision making

  Returns top agents ranked by confidence with explanations.

  Args:
      graph_id (str):
      body (AgentRecommendationRequest): Request for agent recommendations.

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Union[AgentRecommendationResponse, Any, HTTPValidationError]
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      body=body,
    )
  ).parsed
