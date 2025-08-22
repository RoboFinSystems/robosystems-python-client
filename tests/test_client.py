"""Test the RoboSystems Client."""

from robosystems_client import RoboSystemsSDK, AuthenticatedClient, Client


def test_sdk_import():
  """Test that we can import the SDK classes."""
  assert RoboSystemsSDK is not None
  assert AuthenticatedClient is not None
  assert Client is not None


def test_robosystems_sdk_alias():
  """Test that RoboSystemsSDK is an alias for AuthenticatedClient."""
  assert RoboSystemsSDK is AuthenticatedClient


def test_sdk_initialization():
  """Test that we can initialize an SDK."""
  sdk = RoboSystemsSDK(base_url="https://api.robosystems.ai", token="test-api-key")
  # Access base_url through the private attribute since it's not exposed publicly
  assert sdk._base_url == "https://api.robosystems.ai"
  assert sdk.token == "test-api-key"


def test_sdk_authentication_headers():
  """Test that authentication headers are set correctly."""
  sdk = RoboSystemsSDK(
    base_url="https://api.robosystems.ai",
    token="test-api-key",
    auth_header_name="X-API-Key",
    prefix="",
  )
  assert sdk.auth_header_name == "X-API-Key"
  assert sdk.prefix == ""
  assert sdk.token == "test-api-key"
