"""Integration Tests for RoboSystems Client Extensions

These tests demonstrate real usage patterns and verify the extensions work correctly
with the generated Client.
"""

import pytest
import time
from unittest.mock import Mock, patch
from datetime import datetime

# Import extensions
from robosystems_client.extensions import (
  RoboSystemsExtensionConfig,
  QueryBuilder,
  CacheManager,
  ProgressTracker,
  AuthenticatedExtensions,
  create_extensions,
  SSEClient,
  SSEConfig,
  EventType,
  QueryClient,
  estimate_query_cost,
  validate_cypher_query,
  format_duration,
)


class TestAuthenticatedIntegration:
  """Test authenticated extensions integration"""

  @pytest.fixture
  def mock_api_key(self):
    return "test_api_key_12345"

  @pytest.fixture
  def extensions(self, mock_api_key):
    return AuthenticatedExtensions(
      api_key=mock_api_key,
      config=RoboSystemsExtensionConfig(
        base_url="https://api.test.robosystems.ai", timeout=30
      ),
    )

  def test_authenticated_extensions_initialization(self, extensions, mock_api_key):
    """Test that authenticated extensions initialize correctly"""
    assert extensions.config["base_url"] == "https://api.test.robosystems.ai"
    assert extensions.config["headers"]["X-API-Key"] == mock_api_key
    assert extensions.config["headers"]["Authorization"] == f"Bearer {mock_api_key}"

  def test_create_extensions_factory(self, mock_api_key):
    """Test the extensions factory function"""
    # API Key method
    ext = create_extensions(
      "api_key", api_key=mock_api_key, base_url="https://api.test.robosystems.ai"
    )
    assert isinstance(ext, AuthenticatedExtensions)

    # Cookie method
    ext = create_extensions(
      "cookie",
      cookies={"auth-token": "cookie_token"},
      base_url="https://api.test.robosystems.ai",
    )
    assert ext.config["base_url"] == "https://api.test.robosystems.ai"

    # Token method
    ext = create_extensions(
      "token", token="jwt_token_here", base_url="https://api.test.robosystems.ai"
    )
    assert ext.config["headers"]["Authorization"] == "Bearer jwt_token_here"

  @patch("robosystems_client.api.query.execute_cypher_query.sync_detailed")
  def test_cypher_query_execution(self, mock_sync_detailed, extensions):
    """Test executing Cypher queries through authenticated client"""
    # Mock the response
    mock_response = Mock()
    mock_response.parsed = Mock()
    mock_response.parsed.data = [{"name": "Company A", "revenue": 1000000}]
    mock_response.parsed.columns = ["name", "revenue"]
    mock_response.parsed.row_count = 1
    mock_response.parsed.execution_time_ms = 150
    mock_sync_detailed.return_value = mock_response

    result = extensions.execute_cypher_query(
      graph_id="test_graph",
      query="MATCH (c:Company) RETURN c.name, c.revenue",
      parameters={"limit": 10},
    )

    assert result["data"] == [{"name": "Company A", "revenue": 1000000}]
    assert result["columns"] == ["name", "revenue"]
    assert result["row_count"] == 1
    assert result["execution_time_ms"] == 150

    # Verify the SDK was called correctly
    mock_sync_detailed.assert_called_once()


class TestSSEIntegration:
  """Test SSE client integration"""

  @pytest.fixture
  def sse_config(self):
    return SSEConfig(
      base_url="https://api.test.robosystems.ai", max_retries=2, timeout=10
    )

  @pytest.fixture
  def sse_client(self, sse_config):
    return SSEClient(sse_config)

  def test_sse_event_parsing(self, sse_client):
    """Test proper SSE event parsing according to specification"""
    events_received = []

    def event_handler(data):
      events_received.append(data)

    sse_client.on(EventType.OPERATION_PROGRESS.value, event_handler)

    # Test multiline event parsing
    event_buffer = {
      "event": "operation_progress",
      "data": ['{"message": "Step 1 complete"}', '{"percentage": 25}'],
      "id": "123",
      "retry": None,
    }

    sse_client._dispatch_event(event_buffer)

    # Should receive the parsed event
    assert len(events_received) == 1
    # Note: Real SSE data would be joined with newlines, this tests the parsing logic

  def test_sse_connection_management(self, sse_client):
    """Test SSE connection lifecycle"""
    assert not sse_client.is_connected()

    # Test event listener registration
    handler = Mock()
    sse_client.on("test_event", handler)

    # Test event emission
    sse_client.emit("test_event", {"test": "data"})
    handler.assert_called_once_with({"test": "data"})

    # Test cleanup
    sse_client.close()
    assert sse_client.closed


class TestQueryIntegration:
  """Test query client integration"""

  @pytest.fixture
  def query_client(self):
    return QueryClient({"base_url": "https://api.test.robosystems.ai"})

  def test_query_builder_integration(self):
    """Test QueryBuilder creates valid queries"""
    builder = QueryBuilder()
    query, params = (
      builder.match("(c:Company)")
      .where("c.revenue > $min_revenue")
      .return_("c.name", "c.revenue")
      .limit(10)
      .with_param("min_revenue", 100000)
      .build()
    )

    # Validate the query
    validation = validate_cypher_query(query)
    assert validation["valid"]

    # Estimate cost
    cost = estimate_query_cost(query, params)
    assert cost["complexity_category"] in ["low", "medium", "high", "very_high"]
    assert cost["complexity_score"] > 0

    # Test parameters
    assert params["min_revenue"] == 100000

  def test_query_validation_integration(self):
    """Test query validation with various query types"""
    test_cases = [
      # Valid queries
      ("MATCH (n) RETURN n", True),
      ("MATCH (c:Company) WHERE c.revenue > 1000 RETURN c.name", True),
      ("CREATE (n:Test) RETURN n", True),
      # Invalid queries
      ("MATCH (n RETURN n", False),  # Missing closing parenthesis
      ("", False),  # Empty query
      ("MATCH [n] RETURN n", False),  # Wrong bracket type
    ]

    for query, should_be_valid in test_cases:
      result = validate_cypher_query(query)
      assert result["valid"] == should_be_valid, f"Query '{query}' validation failed"

  def test_query_cost_estimation_accuracy(self):
    """Test query cost estimation provides reasonable results"""
    queries = [
      # Simple query - should be low cost
      ("MATCH (n:Company) RETURN n.name LIMIT 10", "low"),
      # Complex query - should be higher cost
      (
        "MATCH (c:Company)-[:HAS_TRANSACTION]->(t:Transaction) "
        + "WHERE c.revenue > 1000000 "
        + "WITH c, COUNT(t) as tx_count "
        + "ORDER BY tx_count DESC "
        + "RETURN c.name, tx_count",
        "high",
      ),
      # Very complex query
      (
        "MATCH (c:Company)-[:HAS_TRANSACTION]->(t:Transaction) "
        + "MATCH (c)-[:LOCATED_IN]->(l:Location) "
        + "MATCH (c)-[:HAS_SUBSIDIARY]->(s:Company) "
        + "WHERE c.revenue > 1000000 AND t.amount > 10000 "
        + "WITH c, l, COUNT(t) as tx_count, SUM(t.amount) as total_amount, "
        + "     AVG(t.amount) as avg_amount, MAX(t.amount) as max_amount "
        + "ORDER BY total_amount DESC, tx_count DESC "
        + "RETURN c.name, l.city, tx_count, total_amount, avg_amount",
        "very_high",
      ),
    ]

    for query, expected_complexity in queries:
      result = estimate_query_cost(query)
      actual_complexity = result["complexity_category"]

      # Allow some flexibility in complexity categorization
      complexity_levels = ["low", "medium", "high", "very_high"]
      expected_idx = complexity_levels.index(expected_complexity)
      actual_idx = complexity_levels.index(actual_complexity)

      # Should be within 1 level of expected
      assert abs(actual_idx - expected_idx) <= 1, (
        f"Query complexity mismatch: expected {expected_complexity}, got {actual_complexity}"
      )


class TestCacheIntegration:
  """Test cache manager integration"""

  @pytest.fixture
  def cache_manager(self):
    return CacheManager(max_size=10, ttl_seconds=5)

  def test_cache_lifecycle(self, cache_manager):
    """Test complete cache lifecycle"""
    graph_id = "test_graph"
    query = "MATCH (n:Company) RETURN COUNT(n)"

    # Cache miss initially
    result = cache_manager.get(graph_id, query)
    assert result is None

    # Store result
    test_result = {"count": 100, "execution_time_ms": 50}
    cache_manager.set(graph_id, query, test_result)

    # Cache hit
    cached_result = cache_manager.get(graph_id, query)
    assert cached_result == test_result

    # Test with parameters
    query_with_params = (
      "MATCH (n:Company) WHERE n.revenue > $min_revenue RETURN COUNT(n)"
    )
    params = {"min_revenue": 100000}

    cache_manager.set(graph_id, query_with_params, test_result, params)
    cached_with_params = cache_manager.get(graph_id, query_with_params, params)
    assert cached_with_params == test_result

    # Different parameters should be cache miss
    different_params = {"min_revenue": 200000}
    cache_miss = cache_manager.get(graph_id, query_with_params, different_params)
    assert cache_miss is None

  def test_cache_eviction(self, cache_manager):
    """Test LRU eviction works correctly"""
    # Fill cache to capacity
    for i in range(10):
      cache_manager.set(f"graph_{i}", f"query_{i}", f"result_{i}")

    assert len(cache_manager.cache) == 10

    # Access first few items to make them recently used
    for i in range(3):
      cache_manager.get(f"graph_{i}", f"query_{i}")

    # Add one more item - should evict least recently used
    cache_manager.set("graph_new", "query_new", "result_new")

    assert len(cache_manager.cache) == 10  # Still at max capacity

    # Recently accessed items should still be there
    assert cache_manager.get("graph_0", "query_0") == "result_0"
    assert cache_manager.get("graph_1", "query_1") == "result_1"
    assert cache_manager.get("graph_2", "query_2") == "result_2"

    # New item should be there
    assert cache_manager.get("graph_new", "query_new") == "result_new"

  def test_cache_expiration(self, cache_manager):
    """Test cache TTL expiration"""
    graph_id = "test_graph"
    query = "MATCH (n) RETURN COUNT(n)"
    result = {"count": 50}

    # Store with short TTL
    cache_manager.set(graph_id, query, result)

    # Should be available immediately
    assert cache_manager.get(graph_id, query) == result

    # Wait for expiration (TTL is 5 seconds in fixture)
    time.sleep(6)

    # Should be expired now
    expired_result = cache_manager.get(graph_id, query)
    assert expired_result is None


class TestProgressTracking:
  """Test progress tracking integration"""

  def test_progress_tracker_lifecycle(self):
    """Test complete progress tracking"""
    operation_id = "test_operation_123"
    tracker = ProgressTracker(operation_id)
    tracker.set_total_steps(5)

    # Simulate progress updates
    steps = [
      ("Initializing...", 0),
      ("Loading data...", 20),
      ("Processing...", 60),
      ("Finalizing...", 90),
      ("Complete", 100),
    ]

    for i, (message, percentage) in enumerate(steps, 1):
      tracker.update(message, percentage, step=i)
      time.sleep(0.1)  # Small delay to see time progression

    # Verify final state
    summary = tracker.get_summary()
    assert summary["operation_id"] == operation_id
    assert summary["current_step"] == 5
    assert summary["total_steps"] == 5
    assert summary["latest_message"] == "Complete"
    assert summary["percentage_complete"] == 100
    assert summary["total_updates"] == 5

    # Check elapsed time is reasonable
    elapsed_time = tracker.get_elapsed_time()
    assert elapsed_time.total_seconds() >= 0.5  # At least the sleep time

  def test_estimated_completion(self):
    """Test progress estimation"""
    tracker = ProgressTracker("test_op")

    # No estimation without progress
    assert tracker.get_estimated_completion() is None

    # Add progress
    tracker.update("50% complete", 50.0)

    # Should have an estimation now
    estimation = tracker.get_estimated_completion()
    assert estimation is not None
    assert isinstance(estimation, datetime)


class TestUtilityIntegration:
  """Test utility function integration"""

  def test_duration_formatting(self):
    """Test duration formatting utility"""
    test_cases = [(100, "100ms"), (1500, "1.5s"), (65000, "1m 5s"), (3661000, "1h 1m")]

    for ms, expected in test_cases:
      result = format_duration(ms)
      assert result == expected, (
        f"Duration {ms}ms formatted as '{result}', expected '{expected}'"
      )

  def test_end_to_end_query_workflow(self):
    """Test complete query workflow with utilities"""
    # Build query
    builder = QueryBuilder()
    query, params = (
      builder.match("(c:Company)-[:LOCATED_IN]->(l:Location)")
      .where("c.revenue > $min_revenue")
      .where("l.country = $country")
      .return_("c.name", "c.revenue", "l.city")
      .order_by("c.revenue DESC")
      .limit(25)
      .with_param("min_revenue", 1000000)
      .with_param("country", "USA")
      .build()
    )

    # Validate query
    validation = validate_cypher_query(query)
    assert validation["valid"], f"Generated query is invalid: {validation['issues']}"

    # Estimate cost
    cost = estimate_query_cost(query, params)
    assert cost["complexity_score"] > 0
    assert len(cost["cost_factors"]) > 0

    # Cache the estimated result
    cache = CacheManager()
    mock_result = {
      "data": [{"name": "TechCorp", "revenue": 5000000, "city": "San Francisco"}],
      "columns": ["name", "revenue", "city"],
      "row_count": 1,
      "execution_time_ms": 250,
    }

    cache.set("production_graph", query, mock_result, params)

    # Retrieve from cache
    cached = cache.get("production_graph", query, params)
    assert cached == mock_result

    # Test execution time formatting
    formatted_time = format_duration(mock_result["execution_time_ms"])
    assert formatted_time == "250ms"


# Integration test runner
def run_integration_tests():
  """Run all integration tests manually (for environments without pytest)"""
  print("Running RoboSystems Client Extensions Integration Tests...")

  # Test classes to run
  test_classes = [
    TestAuthenticatedIntegration(),
    TestSSEIntegration(),
    TestQueryIntegration(),
    TestCacheIntegration(),
    TestProgressTracking(),
    TestUtilityIntegration(),
  ]

  total_tests = 0
  passed_tests = 0

  for test_instance in test_classes:
    class_name = test_instance.__class__.__name__
    print(f"\n--- {class_name} ---")

    # Get all test methods
    test_methods = [
      method
      for method in dir(test_instance)
      if method.startswith("test_") and callable(getattr(test_instance, method))
    ]

    for method_name in test_methods:
      total_tests += 1
      try:
        # Create fixtures if needed
        if hasattr(test_instance, "mock_api_key"):
          test_instance.mock_api_key = lambda: "test_key_123"

        # Run the test
        test_method = getattr(test_instance, method_name)
        test_method()

        print(f"  ✓ {method_name}")
        passed_tests += 1

      except Exception as e:
        print(f"  ✗ {method_name}: {e}")

  print(f"\nIntegration Tests Completed: {passed_tests}/{total_tests} passed")
  return passed_tests == total_tests


if __name__ == "__main__":
  success = run_integration_tests()
  exit(0 if success else 1)
