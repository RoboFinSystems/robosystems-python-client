"""Authentication Integration for RoboSystems Client Extensions

Provides proper integration with the generated Client authentication system.
"""

from typing import Dict, Any
from ..client import Client, AuthenticatedClient
from .extensions import RoboSystemsExtensions, RoboSystemsExtensionConfig


class AuthenticatedExtensions(RoboSystemsExtensions):
  """Extensions with proper authentication integration"""

  def __init__(
    self, api_key: str, config: RoboSystemsExtensionConfig = None, base_url: str = None
  ):
    """Initialize extensions with API key authentication

    Args:
        api_key: RoboSystems API key
        config: Extension configuration
        base_url: API base URL (defaults to production)
    """
    if config is None:
      config = RoboSystemsExtensionConfig()

    # Set base URL
    if base_url:
      config.base_url = base_url
    elif not config.base_url:
      config.base_url = "https://api.robosystems.ai"

    # Add authentication headers
    if not config.headers:
      config.headers = {}
    config.headers["X-API-Key"] = api_key
    config.headers["Authorization"] = f"Bearer {api_key}"

    # Store the token for later use by child clients
    self._token = api_key

    super().__init__(config)

    # Store authenticated client for SDK operations
    self._authenticated_client = AuthenticatedClient(
      base_url=config.base_url, token=api_key, headers=config.headers
    )

  @property
  def authenticated_client(self) -> AuthenticatedClient:
    """Get the authenticated client for direct SDK operations"""
    return self._authenticated_client

  def execute_cypher_query(
    self, graph_id: str, query: str, parameters: Dict[str, Any] = None
  ):
    """Execute Cypher query using authenticated SDK client"""
    from ..api.query.execute_cypher_query import sync_detailed
    from ..models.cypher_query_request import CypherQueryRequest

    request = CypherQueryRequest(query=query, parameters=parameters or {})

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


class CookieAuthExtensions(RoboSystemsExtensions):
  """Extensions with cookie-based authentication"""

  def __init__(
    self,
    cookies: Dict[str, str],
    config: RoboSystemsExtensionConfig = None,
    base_url: str = None,
  ):
    """Initialize extensions with cookie authentication

    Args:
        cookies: Authentication cookies (e.g., {'auth-token': 'token_value'})
        config: Extension configuration
        base_url: API base URL
    """
    if config is None:
      config = RoboSystemsExtensionConfig()

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


class TokenExtensions(RoboSystemsExtensions):
  """Extensions with JWT/Bearer token authentication"""

  def __init__(
    self, token: str, config: RoboSystemsExtensionConfig = None, base_url: str = None
  ):
    """Initialize extensions with JWT token

    Args:
        token: JWT or Bearer token
        config: Extension configuration
        base_url: API base URL
    """
    if config is None:
      config = RoboSystemsExtensionConfig()

    if base_url:
      config.base_url = base_url
    elif not config.base_url:
      config.base_url = "https://api.robosystems.ai"

    # Add authentication headers
    if not config.headers:
      config.headers = {}
    config.headers["Authorization"] = f"Bearer {token}"

    # Store the token for later use by child clients
    self._token = token

    super().__init__(config)

    # Store authenticated client
    self._authenticated_client = AuthenticatedClient(
      base_url=config.base_url, token=token, headers=config.headers
    )

  @property
  def authenticated_client(self) -> AuthenticatedClient:
    """Get the authenticated client"""
    return self._authenticated_client


def create_extensions(auth_method: str, **kwargs) -> RoboSystemsExtensions:
  """Factory function to create extensions with proper authentication

  Args:
      auth_method: 'api_key', 'cookie', or 'token'
      **kwargs: Authentication parameters

  Returns:
      Configured extensions instance

  Examples:
      # API Key authentication
      ext = create_extensions('api_key', api_key='your-key', base_url='https://api.robosystems.ai')

      # Cookie authentication
      ext = create_extensions('cookie', cookies={'auth-token': 'token'})

      # JWT Token authentication
      ext = create_extensions('token', token='jwt-token')
  """
  if auth_method == "api_key":
    api_key = kwargs.pop("api_key")
    return AuthenticatedExtensions(api_key, **kwargs)

  elif auth_method == "cookie":
    cookies = kwargs.pop("cookies")
    return CookieAuthExtensions(cookies, **kwargs)

  elif auth_method == "token":
    token = kwargs.pop("token")
    return TokenExtensions(token, **kwargs)

  else:
    raise ValueError(
      f"Unknown auth method: {auth_method}. Use 'api_key', 'cookie', or 'token'"
    )


# Example usage functions
def create_production_extensions(api_key: str) -> AuthenticatedExtensions:
  """Create extensions for production environment"""
  return AuthenticatedExtensions(
    api_key=api_key,
    config=RoboSystemsExtensionConfig(
      base_url="https://api.robosystems.ai", max_retries=3, retry_delay=2000, timeout=60
    ),
  )


def create_development_extensions(api_key: str) -> AuthenticatedExtensions:
  """Create extensions for development environment"""
  return AuthenticatedExtensions(
    api_key=api_key,
    config=RoboSystemsExtensionConfig(
      base_url="http://localhost:8000", max_retries=5, retry_delay=1000, timeout=30
    ),
  )
