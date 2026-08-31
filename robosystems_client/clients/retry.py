"""Rate-limit-aware HTTP client used by the hand-written facades.

The API rate-limits per user per endpoint category and answers an
exhausted budget with ``429`` plus ``Retry-After`` / ``X-RateLimit-*``
headers. That rejection is raised by a request dependency *before* the
endpoint handler runs, so the request had no effect and is always safe
to replay — including a ``POST`` carrying no idempotency key. Nothing
other than ``429`` is retried here, precisely because nothing else
carries that guarantee.

The motivating case is a bulk backfill: an integrator loading a year of
history through per-event write calls runs at the category budget for
minutes at a time, and without this a burst of rejections turns into
silently missing rows.
"""

from __future__ import annotations

import random
import time
from typing import Any

import httpx

from ..client import AuthenticatedClient, Client

RETRY_STATUS_CODES = frozenset({429})

DEFAULT_MAX_RETRIES = 5
DEFAULT_RETRY_DELAY_MS = 1000
MAX_BACKOFF_SECONDS = 30.0


def retry_after_seconds(response: httpx.Response) -> float | None:
  """Parse ``Retry-After`` as a delta-seconds value, or ``None``.

  The API always sends the numeric form. The HTTP-date form is ignored
  rather than parsed, since treating an unreadable value as "no hint"
  degrades to plain backoff instead of to a wrong sleep.
  """
  raw = response.headers.get("retry-after")
  if not raw:
    return None
  try:
    value = float(raw.strip())
  except ValueError:
    return None
  return value if value >= 0 else None


def backoff_seconds(
  attempt: int, retry_delay_ms: int, retry_after: float | None
) -> float:
  """Seconds to wait before replaying a rate-limited request.

  Exponential with full jitter, and ``Retry-After`` applied as a
  *ceiling* rather than as the sleep itself. The limiter is a sliding
  window, so ``Retry-After`` reports the whole window — the worst case
  for a client that filled its budget instantaneously. A caller that
  merely ran at the sustained rate has slots freeing up within a second
  or two, and obeying the header literally would turn a handful of
  rejections into minutes of idling.
  """
  ceiling = (retry_delay_ms / 1000.0) * (2**attempt)
  ceiling = min(ceiling, MAX_BACKOFF_SECONDS)
  if retry_after is not None:
    ceiling = min(ceiling, retry_after)
  return random.uniform(ceiling / 2.0, ceiling)


def _is_replayable(request: httpx.Request) -> bool:
  """Whether ``request`` can be sent a second time.

  httpx buffers byte and JSON bodies onto the request at construction
  and leaves streaming bodies unread; a streamed body is consumed by
  the first attempt, so replaying it would send an empty payload.
  """
  return hasattr(request, "_content")


class RetryingClient(httpx.Client):
  """``httpx.Client`` that replays rate-limited requests.

  Subclassed rather than installed as a custom transport on purpose:
  httpx disables environment proxy detection whenever ``transport=`` is
  supplied (``allow_env_proxies = trust_env and transport is None``),
  so a transport-level retry would quietly break proxied callers.
  Overriding :meth:`send` leaves proxy, mount, redirect and TLS
  handling exactly as httpx configures it.
  """

  def __init__(
    self,
    *args: Any,
    max_retries: int = DEFAULT_MAX_RETRIES,
    retry_delay_ms: int = DEFAULT_RETRY_DELAY_MS,
    **kwargs: Any,
  ) -> None:
    super().__init__(*args, **kwargs)
    self._max_retries = max(0, int(max_retries))
    self._retry_delay_ms = max(1, int(retry_delay_ms))

  def send(self, request: httpx.Request, **kwargs: Any) -> httpx.Response:
    for attempt in range(self._max_retries):
      response = super().send(request, **kwargs)
      if response.status_code not in RETRY_STATUS_CODES or not _is_replayable(request):
        return response
      delay = backoff_seconds(
        attempt, self._retry_delay_ms, retry_after_seconds(response)
      )
      # The rejection body is small and goes unused, but it holds the
      # connection open until it is drained.
      response.read()
      response.close()
      time.sleep(delay)
    return super().send(request, **kwargs)


def build_httpx_client(
  *,
  base_url: str,
  headers: dict[str, str] | None = None,
  timeout: Any = None,
  config: dict[str, Any] | None = None,
) -> RetryingClient:
  """Build a :class:`RetryingClient` honoring a facade's config dict.

  ``max_retries`` / ``retry_delay`` come from
  :class:`~.facade.RoboSystemsClientConfig`; facades built from a bare
  dict (the demo scripts, the integration template) fall back to the
  defaults.
  """
  config = config or {}
  return RetryingClient(
    base_url=base_url,
    headers=headers or {},
    timeout=timeout,
    max_retries=config.get("max_retries", DEFAULT_MAX_RETRIES),
    retry_delay_ms=config.get("retry_delay", DEFAULT_RETRY_DELAY_MS),
  )


def retrying_authenticated_client(
  *,
  base_url: str,
  token: str,
  headers: dict[str, str] | None = None,
  auth_header_name: str = "X-API-Key",
  prefix: str = "",
  config: dict[str, Any] | None = None,
) -> AuthenticatedClient:
  """An :class:`AuthenticatedClient` whose transport replays 429s.

  Mirrors what ``AuthenticatedClient.get_httpx_client()`` would build —
  including stamping the credential onto the header the caller named —
  and installs it through the public ``set_httpx_client`` hook, so the
  generated ``api/`` layer is untouched and survives ``just
  generate-sdk``.

  ``timeout`` is left unset to match the generated client's own
  default; callers that need one set it on the facade.
  """
  request_headers = dict(headers or {})
  request_headers[auth_header_name] = f"{prefix} {token}" if prefix else token
  client = AuthenticatedClient(
    base_url=base_url,
    token=token,
    prefix=prefix,
    auth_header_name=auth_header_name,
    headers=dict(headers or {}),
  )
  return client.set_httpx_client(
    build_httpx_client(
      base_url=base_url, headers=request_headers, timeout=None, config=config
    )
  )


def retrying_client(
  *,
  base_url: str,
  headers: dict[str, str] | None = None,
  config: dict[str, Any] | None = None,
) -> Client:
  """A plain :class:`Client` whose transport replays 429s.

  The unauthenticated sibling of :func:`retrying_authenticated_client`,
  for the facades that resolve their credential themselves and pass it
  in ``headers`` (query / operator / operations) rather than letting
  ``AuthenticatedClient`` stamp it. Those paths are rate-limited like
  any other — Cypher queries, operator runs and operation-status polls
  each draw on their own category budget — so they need the same replay.
  """
  return Client(
    base_url=base_url,
    headers=dict(headers or {}),
  ).set_httpx_client(
    build_httpx_client(
      base_url=base_url, headers=headers or {}, timeout=None, config=config
    )
  )
