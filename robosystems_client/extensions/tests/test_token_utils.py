"""Tests for JWT token utilities"""

import pytest
from datetime import datetime, timedelta
import json
import base64
import os

from robosystems_client.extensions.token_utils import (
  validate_jwt_format,
  extract_jwt_from_header,
  decode_jwt_payload,
  is_jwt_expired,
  get_jwt_claims,
  get_jwt_expiration,
  extract_token_from_environment,
  extract_token_from_cookie,
  find_valid_token,
  TokenManager,
)


def create_test_jwt(payload: dict = None, exp_delta_seconds: int = 3600) -> str:
  """Create a test JWT token"""
  header = {"alg": "HS256", "typ": "JWT"}

  if payload is None:
    payload = {
      "sub": "test_user",
      "user_id": "123",
      "exp": int((datetime.now() + timedelta(seconds=exp_delta_seconds)).timestamp()),
    }

  # Encode header and payload
  header_b64 = (
    base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
  )

  payload_b64 = (
    base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
  )

  # Create fake signature
  signature = "test_signature_123"

  return f"{header_b64}.{payload_b64}.{signature}"


class TestJWTValidation:
  """Test JWT format validation"""

  def test_validate_jwt_format_valid(self):
    """Test validation of valid JWT format"""
    token = create_test_jwt()
    assert validate_jwt_format(token) is True

  def test_validate_jwt_format_invalid(self):
    """Test validation of invalid JWT formats"""
    # Missing parts
    assert validate_jwt_format("header.payload") is False
    # Wrong format
    assert validate_jwt_format("not-a-jwt") is False
    # Empty
    assert validate_jwt_format("") is False
    # None
    assert validate_jwt_format(None) is False
    # Not a string
    assert validate_jwt_format(123) is False

  def test_validate_jwt_with_padding(self):
    """Test JWT validation handles padding correctly"""
    # JWT with different padding requirements
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.signature"
    assert validate_jwt_format(token) is True


class TestJWTExtraction:
  """Test JWT extraction from various sources"""

  def test_extract_jwt_from_header_bearer(self):
    """Test extraction from Bearer authorization header"""
    token = create_test_jwt()

    # Standard Bearer format
    assert extract_jwt_from_header(f"Bearer {token}") == token
    # Case insensitive
    assert extract_jwt_from_header(f"bearer {token}") == token
    # Extra spaces
    assert extract_jwt_from_header(f"Bearer  {token}  ") == token

  def test_extract_jwt_from_header_dict(self):
    """Test extraction from headers dictionary"""
    token = create_test_jwt()

    headers = {"Authorization": f"Bearer {token}"}
    assert extract_jwt_from_header(headers) == token

    # Case variation
    headers = {"authorization": f"Bearer {token}"}
    assert extract_jwt_from_header(headers) == token

  def test_extract_jwt_from_header_invalid(self):
    """Test extraction returns None for invalid inputs"""
    assert extract_jwt_from_header(None) is None
    assert extract_jwt_from_header("") is None
    assert extract_jwt_from_header("NotBearer token") is None
    assert extract_jwt_from_header({"Other": "header"}) is None


class TestJWTDecoding:
  """Test JWT payload decoding"""

  def test_decode_jwt_payload(self):
    """Test decoding JWT payload"""
    payload = {"sub": "test_user", "user_id": "123", "roles": ["admin", "user"]}
    token = create_test_jwt(payload)

    decoded = decode_jwt_payload(token)
    assert decoded["sub"] == "test_user"
    assert decoded["user_id"] == "123"
    assert decoded["roles"] == ["admin", "user"]

  def test_decode_jwt_payload_invalid(self):
    """Test decoding invalid JWT returns None"""
    assert decode_jwt_payload("invalid.token") is None
    assert decode_jwt_payload("") is None

  def test_get_jwt_claims(self):
    """Test getting all claims from JWT"""
    payload = {"claim1": "value1", "claim2": "value2"}
    token = create_test_jwt(payload)

    claims = get_jwt_claims(token)
    assert claims["claim1"] == "value1"
    assert claims["claim2"] == "value2"


class TestJWTExpiration:
  """Test JWT expiration checking"""

  def test_is_jwt_expired_not_expired(self):
    """Test checking non-expired token"""
    # Token expires in 1 hour
    token = create_test_jwt(exp_delta_seconds=3600)
    assert is_jwt_expired(token) is False

  def test_is_jwt_expired_expired(self):
    """Test checking expired token"""
    # Token expired 1 hour ago
    token = create_test_jwt(exp_delta_seconds=-3600)
    assert is_jwt_expired(token) is True

  def test_is_jwt_expired_with_buffer(self):
    """Test expiration with buffer time"""
    # Token expires in 30 seconds
    token = create_test_jwt(exp_delta_seconds=30)
    # With 60 second buffer, should be considered expired
    assert is_jwt_expired(token, buffer_seconds=60) is True
    # With no buffer, should not be expired
    assert is_jwt_expired(token, buffer_seconds=0) is False

  def test_get_jwt_expiration(self):
    """Test getting expiration datetime"""
    exp_time = datetime.now() + timedelta(hours=1)
    payload = {"exp": int(exp_time.timestamp())}
    token = create_test_jwt(payload)

    exp = get_jwt_expiration(token)
    assert exp is not None
    # Allow 1 second difference for test execution
    assert abs((exp - exp_time).total_seconds()) < 1


class TestTokenExtraction:
  """Test token extraction from various sources"""

  def test_extract_token_from_environment(self):
    """Test extracting token from environment variable"""
    token = create_test_jwt()
    os.environ["ROBOSYSTEMS_TOKEN"] = token

    try:
      assert extract_token_from_environment() == token
      # Custom env var
      os.environ["CUSTOM_TOKEN"] = token
      assert extract_token_from_environment("CUSTOM_TOKEN") == token
    finally:
      # Clean up
      os.environ.pop("ROBOSYSTEMS_TOKEN", None)
      os.environ.pop("CUSTOM_TOKEN", None)

  def test_extract_token_from_cookie(self):
    """Test extracting token from cookies"""
    token = create_test_jwt()
    cookies = {"auth-token": token}

    assert extract_token_from_cookie(cookies) == token
    # Custom cookie name
    cookies = {"session_token": token}
    assert extract_token_from_cookie(cookies, "session_token") == token
    # Missing cookie
    assert extract_token_from_cookie({}) is None

  def test_find_valid_token(self):
    """Test finding first valid token from multiple sources"""
    token = create_test_jwt()

    # Found in second source
    result = find_valid_token(None, "invalid-token", token, "another-invalid")
    assert result == token

    # Found in headers dict
    headers = {"Authorization": f"Bearer {token}"}
    result = find_valid_token(None, headers)
    assert result == token

    # Not found
    result = find_valid_token(None, "", "invalid")
    assert result is None


class TestTokenManager:
  """Test TokenManager class"""

  def test_token_manager_basic(self):
    """Test basic TokenManager functionality"""
    token = create_test_jwt()
    manager = TokenManager(token)

    assert manager.token == token
    assert manager.is_valid() is True

    claims = manager.get_claims()
    assert claims["sub"] == "test_user"

  def test_token_manager_refresh(self):
    """Test token refresh functionality"""
    old_token = create_test_jwt(exp_delta_seconds=30)
    new_token = create_test_jwt(exp_delta_seconds=3600)

    def refresh_callback():
      return new_token

    manager = TokenManager(
      old_token, refresh_callback=refresh_callback, auto_refresh=True, refresh_buffer=60
    )

    # Token should be refreshed automatically
    assert manager.token == new_token

  def test_token_manager_invalid_token(self):
    """Test TokenManager with invalid token"""
    manager = TokenManager()

    with pytest.raises(ValueError):
      manager.token = "invalid-token"

    assert manager.is_valid() is False
    assert manager.get_claims() is None
    assert manager.get_expiration() is None

  def test_token_manager_manual_refresh(self):
    """Test manual token refresh"""
    token = create_test_jwt()
    new_token = create_test_jwt(exp_delta_seconds=7200)

    manager = TokenManager(
      token, refresh_callback=lambda: new_token, auto_refresh=False
    )

    assert manager.token == token
    refreshed = manager.refresh()
    assert refreshed == new_token
    assert manager.token == new_token
