"""Authentication Integration for RoboSystems Client Extensions

Provides proper integration with the generated Client authentication system.
"""

from typing import Dict, Any
from ..client import Client, AuthenticatedClient
from .facade import RoboSystemsClients, RoboSystemsClientConfig


def _apply_auth_header(headers: Dict[str, str], credential: str) -> None:
  """Set the correct auth header for a credential, routed by shape.

  The backend accepts two credential formats, and they go in DIFFERENT
  headers — not interchangeable (see ``graphql/client.py``):

  - Long-lived API keys (``rfs…`` prefix) → ``X-API-Key``. Validated
    against the api_keys table.
  - Short-lived JWTs → ``Authorization: Bearer …``. Validated by the
    JWT middleware.

  Sending a JWT as ``X-API-Key`` (or an API key as Bearer) both fail
  with 401 "Invalid API key" — so exactly one header is set, never both.
  """
  if credential.startswith("rfs"):
    headers["X-API-Key"] = credential
  else:
    headers["Authorization"] = f"Bearer {credential}"


def _build_sdk_client(base_url: str, credential: str, headers: Dict[str, str]):
  """Build an :class:`AuthenticatedClient` with prefix-routed auth.

  Mirrors ``_apply_auth_header``: ``rfs…`` keys ride in ``X-API-Key``
  (no prefix); anything else rides in ``Authorization: Bearer …``.
  """
  if credential.startswith("rfs"):
    return AuthenticatedClient(
      base_url=base_url,
      token=credential,
      prefix="",
      auth_header_name="X-API-Key",
      headers=headers,
    )
  return AuthenticatedClient(base_url=base_url, token=credential, headers=headers)


class AuthenticatedClients(RoboSystemsClients):
  """Extensions with proper authentication integration"""

  def __init__(
    self, api_key: str, config: RoboSystemsClientConfig = None, base_url: str = None
  ):
    """Initialize extensions with API key authentication

    Args:
        api_key: RoboSystems API key
        config: Extension configuration
        base_url: API base URL (defaults to production)
    """
    if config is None:
      config = RoboSystemsClientConfig()

    # Set base URL
    if base_url:
      config.base_url = base_url
    elif not config.base_url:
      config.base_url = "https://api.robosystems.ai"

    # Add the authentication header, routed by credential shape —
    # rfs… API keys go in X-API-Key, JWTs in Authorization: Bearer.
    # Never both: the copy in the wrong header is guaranteed-invalid.
    if not config.headers:
      config.headers = {}
    _apply_auth_header(config.headers, api_key)

    # Store the token for later use by child clients
    self._token = api_key

    super().__init__(config)

    # Store authenticated client for SDK operations
    self._authenticated_client = _build_sdk_client(
      config.base_url, api_key, config.headers
    )

  @property
  def authenticated_client(self) -> AuthenticatedClient:
    """Get the authenticated client for direct SDK operations"""
    return self._authenticated_client

  def execute_cypher_query(
    self, graph_id: str, query: str, parameters: Dict[str, Any] = None
  ):
    """Execute Cypher query using authenticated SDK client"""
    from ..api.query.execute_cypher import sync_detailed
    from ..models.cypher_statement_request import CypherStatementRequest

    request = CypherStatementRequest(query=query, parameters=parameters or {})

    # Execute the query
    response = sync_detailed(
      graph_id=graph_id,
      client=self._authenticated_client,
      body=request,
    )

    if response.parsed:
      return {
        "data": getattr(response.parsed, "data", []),
        "columns": getattr(response.parsed, "columns", []),
        "row_count": getattr(response.parsed, "row_count", 0),
        "execution_time_ms": getattr(response.parsed, "execution_time_ms", 0),
      }
    else:
      raise Exception(f"Query failed: {response.status_code}")


class CookieAuthClients(RoboSystemsClients):
  """Extensions with cookie-based authentication"""

  def __init__(
    self,
    cookies: Dict[str, str],
    config: RoboSystemsClientConfig = None,
    base_url: str = None,
  ):
    """Initialize extensions with cookie authentication

    Args:
        cookies: Authentication cookies (e.g., {'auth-token': 'token_value'})
        config: Extension configuration
        base_url: API base URL
    """
    if config is None:
      config = RoboSystemsClientConfig()

    if base_url:
      config.base_url = base_url
    elif not config.base_url:
      config.base_url = "https://api.robosystems.ai"

    # Extract token from cookies if present
    self._token = cookies.get("auth-token")

    super().__init__(config)

    # Store cookies for requests
    self._cookies = cookies

    # Create client with cookies
    self._client = Client(
      base_url=config.base_url, cookies=cookies, headers=config.headers or {}
    )

  @property
  def client(self) -> Client:
    """Get the client for cookie-based operations"""
    return self._client


class TokenClients(RoboSystemsClients):
  """Extensions with JWT/Bearer token authentication"""

  def __init__(
    self, token: str, config: RoboSystemsClientConfig = None, base_url: str = None
  ):
    """Initialize extensions with JWT token

    Args:
        token: JWT or Bearer token
        config: Extension configuration
        base_url: API base URL
    """
    if config is None:
      config = RoboSystemsClientConfig()

    if base_url:
      config.base_url = base_url
    elif not config.base_url:
      config.base_url = "https://api.robosystems.ai"

    # Add the authentication header, routed by credential shape.
    # JWTs (the expected input here) ride in Authorization: Bearer;
    # if a caller hands this class an rfs… API key anyway, route it
    # to X-API-Key instead of sending a guaranteed-invalid Bearer.
    if not config.headers:
      config.headers = {}
    _apply_auth_header(config.headers, token)

    # Store the token for later use by child clients
    self._token = token

    super().__init__(config)

    # Store authenticated client
    self._authenticated_client = _build_sdk_client(
      config.base_url, token, config.headers
    )

  @property
  def authenticated_client(self) -> AuthenticatedClient:
    """Get the authenticated client"""
    return self._authenticated_client


def create_clients(auth_method: str, **kwargs) -> RoboSystemsClients:
  """Factory function to create extensions with proper authentication

  Args:
      auth_method: 'api_key', 'cookie', or 'token'
      **kwargs: Authentication parameters

  Returns:
      Configured extensions instance

  Examples:
      # API Key authentication
      ext = create_clients('api_key', api_key='your-key', base_url='https://api.robosystems.ai')

      # Cookie authentication
      ext = create_clients('cookie', cookies={'auth-token': 'token'})

      # JWT Token authentication
      ext = create_clients('token', token='jwt-token')
  """
  if auth_method == "api_key":
    api_key = kwargs.pop("api_key")
    return AuthenticatedClients(api_key, **kwargs)

  elif auth_method == "cookie":
    cookies = kwargs.pop("cookies")
    return CookieAuthClients(cookies, **kwargs)

  elif auth_method == "token":
    token = kwargs.pop("token")
    return TokenClients(token, **kwargs)

  else:
    raise ValueError(
      f"Unknown auth method: {auth_method}. Use 'api_key', 'cookie', or 'token'"
    )


# Example usage functions
def create_production_clients(api_key: str) -> AuthenticatedClients:
  """Create extensions for production environment"""
  return AuthenticatedClients(
    api_key=api_key,
    config=RoboSystemsClientConfig(
      base_url="https://api.robosystems.ai", max_retries=3, retry_delay=2000, timeout=60
    ),
  )


def create_development_clients(api_key: str) -> AuthenticatedClients:
  """Create extensions for development environment"""
  return AuthenticatedClients(
    api_key=api_key,
    config=RoboSystemsClientConfig(
      base_url="http://localhost:8000", max_retries=5, retry_delay=1000, timeout=30
    ),
  )
