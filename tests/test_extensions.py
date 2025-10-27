"""Integration tests for RoboSystemsExtensions."""

import pytest
from robosystems_client.extensions import (
  RoboSystemsExtensions,
  RoboSystemsExtensionConfig,
  TableIngestClient,
  QueryClient,
  OperationClient,
  GraphClient,
)


@pytest.mark.unit
class TestRoboSystemsExtensions:
  """Test suite for RoboSystemsExtensions integration."""

  def test_extensions_initialization_default(self):
    """Test default initialization of extensions."""
    extensions = RoboSystemsExtensions()

    assert extensions.config["base_url"] == "http://localhost:8000"
    assert isinstance(extensions.query, QueryClient)
    assert isinstance(extensions.operations, OperationClient)
    assert isinstance(extensions.tables, TableIngestClient)
    assert isinstance(extensions.graphs, GraphClient)

    # Cleanup
    extensions.close()

  def test_extensions_initialization_with_config(self):
    """Test initialization with custom config."""
    config = RoboSystemsExtensionConfig(
      base_url="https://api.robosystems.ai",
      headers={"X-API-Key": "test-key-123"},
      max_retries=3,
      retry_delay=500,
    )

    extensions = RoboSystemsExtensions(config)

    assert extensions.config["base_url"] == "https://api.robosystems.ai"
    assert extensions.config["headers"]["X-API-Key"] == "test-key-123"
    assert extensions.config["max_retries"] == 3
    assert extensions.config["retry_delay"] == 500

    extensions.close()

  def test_extensions_initialization_with_token(self):
    """Test initialization with JWT token in headers."""
    config = RoboSystemsExtensionConfig(
      base_url="https://api.robosystems.ai",
      headers={"Authorization": "Bearer jwt-token-123"},
    )

    extensions = RoboSystemsExtensions(config)

    assert "Authorization" in extensions.config["headers"]

    extensions.close()

  def test_config_dict_format(self):
    """Test that config is properly formatted as dict."""
    config = RoboSystemsExtensionConfig(
      base_url="https://api.robosystems.ai",
      headers={"Custom-Header": "value"},
    )

    extensions = RoboSystemsExtensions(config)

    # Config should be a dict
    assert isinstance(extensions.config, dict)
    assert "base_url" in extensions.config
    assert "headers" in extensions.config

    extensions.close()

  def test_query_client_receives_config(self):
    """Test that QueryClient receives proper config."""
    config = RoboSystemsExtensionConfig(
      base_url="https://api.robosystems.ai",
      headers={"X-API-Key": "test-token"},
    )

    extensions = RoboSystemsExtensions(config)

    assert extensions.query.base_url == "https://api.robosystems.ai"
    assert "X-API-Key" in extensions.query.headers

    extensions.close()

  def test_operation_client_receives_config(self):
    """Test that OperationClient receives proper config."""
    config = RoboSystemsExtensionConfig(
      base_url="https://api.robosystems.ai",
      headers={"X-API-Key": "test-token"},
    )

    extensions = RoboSystemsExtensions(config)

    assert extensions.operations.base_url == "https://api.robosystems.ai"
    assert "X-API-Key" in extensions.operations.headers

    extensions.close()

  def test_table_ingest_client_receives_config(self):
    """Test that TableIngestClient receives proper config."""
    config = RoboSystemsExtensionConfig(
      base_url="https://api.robosystems.ai",
      headers={"X-API-Key": "test-token"},
    )

    extensions = RoboSystemsExtensions(config)

    assert extensions.tables.base_url == "https://api.robosystems.ai"
    assert "X-API-Key" in extensions.tables.headers

    extensions.close()

  def test_graph_client_receives_config(self):
    """Test that GraphClient receives proper config."""
    config = RoboSystemsExtensionConfig(
      base_url="https://api.robosystems.ai",
      headers={"X-API-Key": "test-token"},
    )

    extensions = RoboSystemsExtensions(config)

    assert extensions.graphs.base_url == "https://api.robosystems.ai"
    assert "X-API-Key" in extensions.graphs.headers

    extensions.close()

  def test_multiple_extensions_instances(self):
    """Test that multiple extension instances can coexist."""
    ext1 = RoboSystemsExtensions(
      RoboSystemsExtensionConfig(base_url="http://localhost:8000")
    )
    ext2 = RoboSystemsExtensions(
      RoboSystemsExtensionConfig(base_url="https://api.robosystems.ai")
    )

    assert ext1.config["base_url"] == "http://localhost:8000"
    assert ext2.config["base_url"] == "https://api.robosystems.ai"

    # Close both
    ext1.close()
    ext2.close()


@pytest.mark.unit
class TestRoboSystemsExtensionConfig:
  """Test suite for RoboSystemsExtensionConfig dataclass."""

  def test_config_defaults(self):
    """Test default configuration values."""
    config = RoboSystemsExtensionConfig()

    assert config.base_url is None  # Default is None, set in Extensions class
    assert config.headers is None
    assert config.max_retries == 5
    assert config.retry_delay == 1000
    assert config.timeout == 30

  def test_config_custom_values(self):
    """Test custom configuration values."""
    config = RoboSystemsExtensionConfig(
      base_url="https://custom.api.com",
      headers={"Authorization": "Bearer token"},
      max_retries=10,
      retry_delay=2000,
      timeout=60,
    )

    assert config.base_url == "https://custom.api.com"
    assert config.headers == {"Authorization": "Bearer token"}
    assert config.max_retries == 10
    assert config.retry_delay == 2000
    assert config.timeout == 60

  def test_config_to_dict(self):
    """Test converting config to dictionary."""
    config = RoboSystemsExtensionConfig(
      base_url="https://api.robosystems.ai",
      headers={"X-API-Key": "test-key"},
    )

    # The Extensions class converts this to dict internally
    extensions = RoboSystemsExtensions(config)
    config_dict = extensions.config

    assert isinstance(config_dict, dict)
    assert config_dict["base_url"] == "https://api.robosystems.ai"
    assert config_dict["headers"]["X-API-Key"] == "test-key"

    extensions.close()
