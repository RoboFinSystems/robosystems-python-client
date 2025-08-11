"""Test the RoboSystems client."""

from robosystems_client import RoboSystemsClient, AuthenticatedClient, Client


def test_client_import():
  """Test that we can import the client classes."""
  assert RoboSystemsClient is not None
  assert AuthenticatedClient is not None
  assert Client is not None


def test_robosystems_client_alias():
  """Test that RoboSystemsClient is an alias for AuthenticatedClient."""
  assert RoboSystemsClient is AuthenticatedClient


def test_client_initialization():
  """Test that we can initialize a client."""
  client = RoboSystemsClient(
    base_url="https://api.robosystems.ai", token="test-api-key"
  )
  # Access base_url through the private attribute since it's not exposed publicly
  assert client._base_url == "https://api.robosystems.ai"
  assert client.token == "test-api-key"


def test_client_authentication_headers():
  """Test that authentication headers are set correctly."""
  client = RoboSystemsClient(
    base_url="https://api.robosystems.ai",
    token="test-api-key",
    auth_header_name="X-API-Key",
    prefix="",
  )
  assert client.auth_header_name == "X-API-Key"
  assert client.prefix == ""
  assert client.token == "test-api-key"
