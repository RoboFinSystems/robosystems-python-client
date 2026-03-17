import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.trial_balance_response import TrialBalanceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
  graph_id: str,
  *,
  start_date: datetime.date | None | Unset = UNSET,
  end_date: datetime.date | None | Unset = UNSET,
) -> dict[str, Any]:
  params: dict[str, Any] = {}

  json_start_date: None | str | Unset
  if isinstance(start_date, Unset):
    json_start_date = UNSET
  elif isinstance(start_date, datetime.date):
    json_start_date = start_date.isoformat()
  else:
    json_start_date = start_date
  params["start_date"] = json_start_date

  json_end_date: None | str | Unset
  if isinstance(end_date, Unset):
    json_end_date = UNSET
  elif isinstance(end_date, datetime.date):
    json_end_date = end_date.isoformat()
  else:
    json_end_date = end_date
  params["end_date"] = json_end_date

  params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

  _kwargs: dict[str, Any] = {
    "method": "get",
    "url": "/v1/ledger/{graph_id}/trial-balance".format(
      graph_id=quote(str(graph_id), safe=""),
    ),
    "params": params,
  }

  return _kwargs


def _parse_response(
  *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TrialBalanceResponse | None:
  if response.status_code == 200:
    response_200 = TrialBalanceResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TrialBalanceResponse]:
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
  start_date: datetime.date | None | Unset = UNSET,
  end_date: datetime.date | None | Unset = UNSET,
) -> Response[HTTPValidationError | TrialBalanceResponse]:
  """Trial Balance

  Args:
      graph_id (str):
      start_date (datetime.date | None | Unset): Start date (inclusive)
      end_date (datetime.date | None | Unset): End date (inclusive)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | TrialBalanceResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    start_date=start_date,
    end_date=end_date,
  )

  response = client.get_httpx_client().request(
    **kwargs,
  )

  return _build_response(client=client, response=response)


def sync(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  start_date: datetime.date | None | Unset = UNSET,
  end_date: datetime.date | None | Unset = UNSET,
) -> HTTPValidationError | TrialBalanceResponse | None:
  """Trial Balance

  Args:
      graph_id (str):
      start_date (datetime.date | None | Unset): Start date (inclusive)
      end_date (datetime.date | None | Unset): End date (inclusive)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | TrialBalanceResponse
  """

  return sync_detailed(
    graph_id=graph_id,
    client=client,
    start_date=start_date,
    end_date=end_date,
  ).parsed


async def asyncio_detailed(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  start_date: datetime.date | None | Unset = UNSET,
  end_date: datetime.date | None | Unset = UNSET,
) -> Response[HTTPValidationError | TrialBalanceResponse]:
  """Trial Balance

  Args:
      graph_id (str):
      start_date (datetime.date | None | Unset): Start date (inclusive)
      end_date (datetime.date | None | Unset): End date (inclusive)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      Response[HTTPValidationError | TrialBalanceResponse]
  """

  kwargs = _get_kwargs(
    graph_id=graph_id,
    start_date=start_date,
    end_date=end_date,
  )

  response = await client.get_async_httpx_client().request(**kwargs)

  return _build_response(client=client, response=response)


async def asyncio(
  graph_id: str,
  *,
  client: AuthenticatedClient,
  start_date: datetime.date | None | Unset = UNSET,
  end_date: datetime.date | None | Unset = UNSET,
) -> HTTPValidationError | TrialBalanceResponse | None:
  """Trial Balance

  Args:
      graph_id (str):
      start_date (datetime.date | None | Unset): Start date (inclusive)
      end_date (datetime.date | None | Unset): End date (inclusive)

  Raises:
      errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
      httpx.TimeoutException: If the request takes longer than Client.timeout.

  Returns:
      HTTPValidationError | TrialBalanceResponse
  """

  return (
    await asyncio_detailed(
      graph_id=graph_id,
      client=client,
      start_date=start_date,
      end_date=end_date,
    )
  ).parsed
