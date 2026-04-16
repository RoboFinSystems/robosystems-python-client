"""JWT Token validation and management utilities for RoboSystems SDK

Provides comprehensive JWT handling, validation, and extraction utilities.
"""

import base64
import json
import os
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, Union
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class TokenSource(Enum):
  """Sources where tokens can be extracted from"""

  HEADER = "header"
  COOKIE = "cookie"
  ENVIRONMENT = "environment"
  CONFIG = "config"


def validate_jwt_format(token: Optional[str]) -> bool:
  """Validate JWT token format (basic validation without cryptographic verification)

  Args:
      token: JWT token string to validate

  Returns:
      True if token appears to be valid JWT format

  Example:
      >>> validate_jwt_format("eyJhbGc.eyJzdWI.SflKxwRJSM")
      True
      >>> validate_jwt_format("invalid-token")
      False
  """
  if not token or not isinstance(token, str):
    return False

  try:
    # JWT should have exactly 3 parts: header.payload.signature
    parts = token.split(".")
    if len(parts) != 3:
      return False

    # Each part should be base64url encoded
    for part in parts[:2]:  # Check header and payload only
      # Add padding if needed
      padding = 4 - (len(part) % 4)
      if padding != 4:
        part += "=" * padding

      try:
        # Try to decode base64
        base64.urlsafe_b64decode(part)
      except Exception:
        return False

    return True
  except Exception:
    return False


def extract_jwt_from_header(
  auth_header: Optional[Union[str, Dict[str, str]]],
) -> Optional[str]:
  """Extract JWT token from Authorization header

  Args:
      auth_header: Authorization header value (e.g., "Bearer token123") or headers dict

  Returns:
      JWT token if found, None otherwise

  Example:
      >>> extract_jwt_from_header("Bearer eyJhbGc.eyJzdWI.SflKxwRJSM")
      "eyJhbGc.eyJzdWI.SflKxwRJSM"
      >>> extract_jwt_from_header({"Authorization": "Bearer token123"})
      "token123"
  """
  if not auth_header:
    return None

  # Handle dict of headers
  if isinstance(auth_header, dict):
    auth_value = auth_header.get("Authorization") or auth_header.get("authorization")
    if not auth_value:
      return None
    auth_header = auth_value

  # Extract token from Bearer scheme
  if isinstance(auth_header, str):
    auth_header = auth_header.strip()
    if auth_header.startswith("Bearer "):
      token = auth_header[7:].strip()
      return token if token else None
    elif auth_header.startswith("bearer "):  # Case insensitive
      token = auth_header[7:].strip()
      return token if token else None

  return None


def decode_jwt_payload(token: str, verify: bool = False) -> Optional[Dict[str, Any]]:
  """Decode JWT payload without verification (for reading claims only)

  Args:
      token: JWT token to decode
      verify: If True, will validate format first (default: False)

  Returns:
      Decoded payload as dictionary, None if invalid

  Note:
      This does NOT verify the signature. Use only for reading non-sensitive claims.

  Example:
      >>> payload = decode_jwt_payload("eyJhbGc.eyJzdWI.SflKxwRJSM")
      >>> payload.get("sub")  # Get subject claim
  """
  if verify and not validate_jwt_format(token):
    return None

  try:
    # Split token and get payload (second part)
    parts = token.split(".")
    if len(parts) != 3:
      return None

    payload_part = parts[1]

    # Add padding if needed
    padding = 4 - (len(payload_part) % 4)
    if padding != 4:
      payload_part += "=" * padding

    # Decode base64url
    payload_bytes = base64.urlsafe_b64decode(payload_part)
    payload = json.loads(payload_bytes.decode("utf-8"))

    return payload
  except Exception as e:
    logger.debug(f"Failed to decode JWT payload: {e}")
    return None


def is_jwt_expired(token: str, buffer_seconds: int = 60) -> bool:
  """Check if JWT token is expired based on exp claim

  Args:
      token: JWT token to check
      buffer_seconds: Consider expired if expiring within this many seconds (default: 60)

  Returns:
      True if token is expired or expiring soon

  Example:
      >>> is_jwt_expired("eyJhbGc.eyJleHAiOjE2MzA0MjU2MDB9.SflKxwRJSM")
      True  # If current time is past exp claim
  """
  payload = decode_jwt_payload(token)
  if not payload:
    return True

  exp = payload.get("exp")
  if not exp:
    # No expiration claim, consider as non-expiring
    return False

  try:
    exp_datetime = datetime.fromtimestamp(exp)
    buffer = timedelta(seconds=buffer_seconds)
    return datetime.now() >= (exp_datetime - buffer)
  except Exception:
    return True


def get_jwt_claims(token: str) -> Optional[Dict[str, Any]]:
  """Get all claims from JWT token

  Args:
      token: JWT token

  Returns:
      Dictionary of all claims, None if invalid

  Example:
      >>> claims = get_jwt_claims(token)
      >>> user_id = claims.get("user_id")
      >>> roles = claims.get("roles", [])
  """
  return decode_jwt_payload(token)


def get_jwt_expiration(token: str) -> Optional[datetime]:
  """Get expiration datetime from JWT token

  Args:
      token: JWT token

  Returns:
      Expiration datetime, None if no exp claim or invalid

  Example:
      >>> exp = get_jwt_expiration(token)
      >>> if exp and exp > datetime.now():
      ...     print(f"Token valid until {exp}")
  """
  payload = decode_jwt_payload(token)
  if not payload:
    return None

  exp = payload.get("exp")
  if not exp:
    return None

  try:
    return datetime.fromtimestamp(exp)
  except Exception:
    return None


def extract_token_from_environment(env_var: str = "ROBOSYSTEMS_TOKEN") -> Optional[str]:
  """Extract JWT token from environment variable

  Args:
      env_var: Environment variable name (default: ROBOSYSTEMS_TOKEN)

  Returns:
      JWT token if found and valid format, None otherwise

  Example:
      >>> os.environ["ROBOSYSTEMS_TOKEN"] = "eyJhbGc..."
      >>> token = extract_token_from_environment()
  """
  token = os.environ.get(env_var)
  if token and validate_jwt_format(token):
    return token
  return None


def extract_token_from_cookie(
  cookies: Dict[str, str], cookie_name: str = "auth-token"
) -> Optional[str]:
  """Extract JWT token from cookies

  Args:
      cookies: Dictionary of cookies
      cookie_name: Name of cookie containing token (default: auth-token)

  Returns:
      JWT token if found, None otherwise

  Example:
      >>> cookies = {"auth-token": "eyJhbGc..."}
      >>> token = extract_token_from_cookie(cookies)
  """
  token = cookies.get(cookie_name)
  if token and validate_jwt_format(token):
    return token
  return None


def find_valid_token(*sources: Union[str, Dict[str, str], None]) -> Optional[str]:
  """Find first valid JWT token from multiple sources

  Args:
      *sources: Variable number of potential token sources
                (strings, dicts with Authorization header, etc.)

  Returns:
      First valid JWT token found, None if none found

  Example:
      >>> token = find_valid_token(
      ...     os.environ.get("TOKEN"),
      ...     headers,
      ...     cookies.get("auth-token"),
      ...     config.get("token")
      ... )
  """
  for source in sources:
    if not source:
      continue

    # Direct token string
    if isinstance(source, str):
      if validate_jwt_format(source):
        return source

    # Headers dict
    elif isinstance(source, dict):
      # Try as headers
      token = extract_jwt_from_header(source)
      if token and validate_jwt_format(token):
        return token

      # Try as cookies
      for key in ["auth-token", "auth_token", "token", "jwt"]:
        token = source.get(key)
        if token and validate_jwt_format(token):
          return token

  return None


class TokenManager:
  """Manages JWT tokens with automatic refresh and validation"""

  def __init__(
    self,
    token: Optional[str] = None,
    refresh_callback: Optional[callable] = None,
    auto_refresh: bool = True,
    refresh_buffer: int = 300,
  ):
    """Initialize token manager

    Args:
        token: Initial JWT token
        refresh_callback: Callback to refresh token when expired
        auto_refresh: Automatically refresh before expiration
        refresh_buffer: Seconds before expiration to trigger refresh (default: 300)
    """
    self._token = token
    self._refresh_callback = refresh_callback
    self._auto_refresh = auto_refresh
    self._refresh_buffer = refresh_buffer

  @property
  def token(self) -> Optional[str]:
    """Get current token, refreshing if needed"""
    if self._auto_refresh and self._token and self._refresh_callback:
      if is_jwt_expired(self._token, self._refresh_buffer):
        self.refresh()
    return self._token

  @token.setter
  def token(self, value: Optional[str]):
    """Set new token"""
    if value and not validate_jwt_format(value):
      raise ValueError("Invalid JWT token format")
    self._token = value

  def refresh(self) -> Optional[str]:
    """Refresh token using callback"""
    if not self._refresh_callback:
      raise RuntimeError("No refresh callback configured")

    try:
      new_token = self._refresh_callback()
      if new_token and validate_jwt_format(new_token):
        self._token = new_token
        logger.info("Token refreshed successfully")
        return new_token
    except Exception as e:
      logger.error(f"Token refresh failed: {e}")

    return None

  def is_valid(self) -> bool:
    """Check if current token is valid"""
    return bool(
      self._token
      and validate_jwt_format(self._token)
      and not is_jwt_expired(self._token, 0)
    )

  def get_claims(self) -> Optional[Dict[str, Any]]:
    """Get claims from current token"""
    if self._token:
      return get_jwt_claims(self._token)
    return None

  def get_expiration(self) -> Optional[datetime]:
    """Get expiration time of current token"""
    if self._token:
      return get_jwt_expiration(self._token)
    return None


# Convenience function for quick token extraction from client config
def extract_token_from_client(client) -> Optional[str]:
  """Extract JWT token from RoboSystems client configuration

  Args:
      client: RoboSystems client instance

  Returns:
      JWT token if found, None otherwise
  """
  # Try to get from authenticated client
  if hasattr(client, "token"):
    return client.token

  # Try from headers
  if hasattr(client, "_headers"):
    token = extract_jwt_from_header(client._headers)
    if token:
      return token

  # Try from config
  if hasattr(client, "config"):
    config = client.config
    if isinstance(config, dict):
      # Direct token
      if config.get("token"):
        return config["token"]
      # From headers in config
      if config.get("headers"):
        return extract_jwt_from_header(config["headers"])

  return None
