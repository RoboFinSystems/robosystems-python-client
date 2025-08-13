"""Unit Tests for RoboSystems Client Extensions

Focused unit tests for individual components.
"""

import json
from datetime import datetime
from unittest.mock import Mock

import sys
import os

# Add parent directories to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from robosystems_client.extensions import (
  SSEClient,
  SSEConfig,
  SSEEvent,
  QueryBuilder,
  CacheManager,
  ProgressTracker,
  ResultProcessor,
  validate_cypher_query,
  estimate_query_cost,
  format_duration,
)


# Create QueryResult for tests since it might not be available
class QueryResult:
  def __init__(
    self, data, columns, row_count, execution_time_ms, graph_id=None, timestamp=None
  ):
    self.data = data
    self.columns = columns
    self.row_count = row_count
    self.execution_time_ms = execution_time_ms
    self.graph_id = graph_id
    self.timestamp = timestamp


class TestSSEClient:
  """Unit tests for SSE client"""

  def test_sse_event_creation(self):
    """Test SSE event data structure"""
    event = SSEEvent(event="test_event", data={"message": "test"}, id="123")

    assert event.event == "test_event"
    assert event.data == {"message": "test"}
    assert event.id == "123"
    assert isinstance(event.timestamp, datetime)

  def test_sse_config_defaults(self):
    """Test SSE configuration"""
    config = SSEConfig(base_url="https://api.test.com")

    assert config.base_url == "https://api.test.com"
    assert config.max_retries == 5
    assert config.retry_delay == 1000
    assert config.timeout == 30

  def test_event_listener_management(self):
    """Test event listener registration and removal"""
    config = SSEConfig(base_url="https://api.test.com")
    client = SSEClient(config)

    handler = Mock()

    # Add listener
    client.on("test_event", handler)
    assert "test_event" in client.listeners
    assert handler in client.listeners["test_event"]

    # Emit event
    client.emit("test_event", {"data": "test"})
    handler.assert_called_once_with({"data": "test"})

    # Remove listener
    client.off("test_event", handler)
    handler.reset_mock()

    client.emit("test_event", {"data": "test2"})
    handler.assert_not_called()

  def test_sse_event_parsing(self):
    """Test proper SSE event parsing"""
    config = SSEConfig(base_url="https://api.test.com")
    client = SSEClient(config)

    # Test multiline data parsing
    event_buffer = {
      "event": "data_chunk",
      "data": ['{"rows": [', '  {"id": 1, "name": "test"}', "]}"],
      "id": "456",
      "retry": None,
    }

    events_received = []
    client.on("data_chunk", lambda data: events_received.append(data))

    client._dispatch_event(event_buffer)

    assert len(events_received) == 1
    # Data should be parsed as JSON since it's valid JSON
    expected_data = {"rows": [{"id": 1, "name": "test"}]}
    # Should be parsed as JSON object
    assert events_received[0] == expected_data


class TestQueryBuilder:
  """Unit tests for QueryBuilder"""

  def test_basic_query_building(self):
    """Test basic query construction"""
    builder = QueryBuilder()
    query, params = builder.match("(n:Node)").return_("n.property").build()

    expected = "MATCH (n:Node)\nRETURN n.property"
    assert query == expected
    assert params == {}

  def test_complex_query_building(self):
    """Test complex query with all clauses"""
    builder = QueryBuilder()
    query, params = (
      builder.match("(a:Person)-[:KNOWS]->(b:Person)")
      .where("a.age > $min_age")
      .where("b.city = $city")
      .return_("a.name", "b.name", "a.age")
      .order_by("a.age DESC")
      .limit(10)
      .with_param("min_age", 25)
      .with_param("city", "New York")
      .build()
    )

    expected_lines = [
      "MATCH (a:Person)-[:KNOWS]->(b:Person)",
      "WHERE a.age > $min_age",
      "WHERE b.city = $city",
      "RETURN a.name, b.name, a.age",
      "ORDER BY a.age DESC",
      "LIMIT 10",
    ]
    expected = "\n".join(expected_lines)

    assert query == expected
    assert params == {"min_age": 25, "city": "New York"}

  def test_method_chaining(self):
    """Test that all methods return self for chaining"""
    builder = QueryBuilder()

    result = builder.match("(n)")
    assert result is builder

    result = result.where("n.prop = 1")
    assert result is builder

    result = result.return_("n")
    assert result is builder

    result = result.order_by("n.prop")
    assert result is builder

    result = result.limit(5)
    assert result is builder


class TestCacheManager:
  """Unit tests for CacheManager"""

  def test_cache_key_generation(self):
    """Test cache key generation"""
    cache = CacheManager()

    # Same inputs should generate same key
    key1 = cache._generate_key("graph1", "MATCH (n) RETURN n", {"param": "value"})
    key2 = cache._generate_key("graph1", "MATCH (n) RETURN n", {"param": "value"})
    assert key1 == key2

    # Different inputs should generate different keys
    key3 = cache._generate_key("graph2", "MATCH (n) RETURN n", {"param": "value"})
    assert key1 != key3

    key4 = cache._generate_key("graph1", "MATCH (m) RETURN m", {"param": "value"})
    assert key1 != key4

  def test_cache_operations(self):
    """Test basic cache operations"""
    cache = CacheManager(max_size=3, ttl_seconds=1)

    # Test cache miss
    result = cache.get("graph1", "query1")
    assert result is None

    # Test cache set/get
    test_data = {"result": "data"}
    cache.set("graph1", "query1", test_data)

    cached = cache.get("graph1", "query1")
    assert cached == test_data

    # Test stats
    stats = cache.stats()
    assert stats["total_entries"] == 1
    assert stats["active_entries"] == 1

  def test_cache_size_limit(self):
    """Test cache size enforcement"""
    cache = CacheManager(max_size=2, ttl_seconds=60)

    # Fill to capacity
    cache.set("g1", "q1", "result1")
    cache.set("g2", "q2", "result2")
    assert len(cache.cache) == 2

    # Access first item to make it recently used
    cache.get("g1", "q1")

    # Add third item - should evict least recently used (q2)
    cache.set("g3", "q3", "result3")
    assert len(cache.cache) == 2

    # First item should still be there (recently used)
    assert cache.get("g1", "q1") == "result1"

    # Second item should be evicted
    assert cache.get("g2", "q2") is None

    # Third item should be there
    assert cache.get("g3", "q3") == "result3"


class TestProgressTracker:
  """Unit tests for ProgressTracker"""

  def test_progress_initialization(self):
    """Test progress tracker initialization"""
    operation_id = "test_op_123"
    tracker = ProgressTracker(operation_id)

    assert tracker.operation_id == operation_id
    assert tracker.current_step == 0
    assert tracker.total_steps is None
    assert len(tracker.progress_history) == 0
    assert isinstance(tracker.started_at, datetime)

  def test_progress_updates(self):
    """Test progress tracking"""
    tracker = ProgressTracker("test_op")
    tracker.set_total_steps(3)

    # Update progress
    tracker.update("Step 1", 33.3, 1)
    tracker.update("Step 2", 66.6, 2)
    tracker.update("Complete", 100.0, 3)

    assert len(tracker.progress_history) == 3
    assert tracker.current_step == 3
    assert tracker.total_steps == 3

    # Check last update
    last_update = tracker.progress_history[-1]
    assert last_update["message"] == "Complete"
    assert last_update["percentage"] == 100.0
    assert last_update["step"] == 3

  def test_summary_generation(self):
    """Test progress summary"""
    tracker = ProgressTracker("summary_test")
    tracker.set_total_steps(2)
    tracker.update("Starting", 0)
    tracker.update("Finished", 100)

    summary = tracker.get_summary()

    assert summary["operation_id"] == "summary_test"
    assert summary["current_step"] == 0  # No step specified in updates
    assert summary["total_steps"] == 2
    assert summary["latest_message"] == "Finished"
    assert summary["percentage_complete"] == 100
    assert summary["total_updates"] == 2


class TestResultProcessor:
  """Unit tests for ResultProcessor"""

  def test_json_conversion(self):
    """Test JSON conversion"""
    result = QueryResult(
      data=[{"name": "Test", "value": 123}],
      columns=["name", "value"],
      row_count=1,
      execution_time_ms=100,
    )

    json_output = ResultProcessor.to_json(result)
    parsed = json.loads(json_output)

    assert parsed["data"] == [{"name": "Test", "value": 123}]
    assert parsed["columns"] == ["name", "value"]
    assert parsed["row_count"] == 1

  def test_csv_conversion(self):
    """Test CSV conversion"""
    result = QueryResult(
      data=[{"company": "A", "revenue": 1000}, {"company": "B", "revenue": 2000}],
      columns=["company", "revenue"],
      row_count=2,
      execution_time_ms=50,
    )

    csv_output = ResultProcessor.to_csv(result)
    lines = csv_output.strip().replace("\r", "").split("\n")

    assert lines[0] == "company,revenue"
    assert "A,1000" in lines[1]
    assert "B,2000" in lines[2]

  def test_csv_with_list_data(self):
    """Test CSV conversion with list data"""
    data = [["CompanyA", 1000], ["CompanyB", 2000]]
    columns = ["name", "revenue"]

    csv_output = ResultProcessor.to_csv(data, columns=columns)
    lines = csv_output.strip().replace("\r", "").split("\n")

    assert lines[0] == "name,revenue"
    assert "CompanyA,1000" in lines[1]


class TestQueryValidation:
  """Unit tests for query validation"""

  def test_valid_queries(self):
    """Test validation of valid queries"""
    valid_queries = [
      "MATCH (n) RETURN n",
      "CREATE (n:Person {name: 'John'}) RETURN n",
      "MATCH (a)-[r]->(b) DELETE r",
      "MERGE (n:Company {name: 'Acme'}) RETURN n",
      "MATCH (n) WHERE n.age > 18 RETURN n.name",
    ]

    for query in valid_queries:
      result = validate_cypher_query(query)
      assert result["valid"], f"Query should be valid: {query}"
      assert len(result["issues"]) == 0

  def test_invalid_queries(self):
    """Test validation of invalid queries"""
    invalid_queries = [
      ("MATCH (n RETURN n", "Unbalanced parentheses"),
      ("MATCH (n)-[r->(m RETURN n", "Unbalanced square brackets"),
      ("MATCH {n RETURN n", "Unbalanced curly braces"),
      ("", "Empty query"),
    ]

    for query, expected_issue in invalid_queries:
      result = validate_cypher_query(query)
      assert not result["valid"], f"Query should be invalid: {query}"
      assert len(result["issues"]) > 0

  def test_query_warnings(self):
    """Test query validation warnings"""
    # DELETE without WHERE should generate warning
    result = validate_cypher_query("MATCH (n) DELETE n")
    assert len(result["warnings"]) > 0
    assert any("DELETE without WHERE" in warning for warning in result["warnings"])


class TestQueryCostEstimation:
  """Unit tests for query cost estimation"""

  def test_simple_query_cost(self):
    """Test cost estimation for simple queries"""
    query = "MATCH (n:Person) RETURN n.name LIMIT 10"
    result = estimate_query_cost(query)

    assert result["complexity_category"] == "low"
    assert result["complexity_score"] > 0
    assert result["cost_factors"]["match_clauses"] == 1
    assert result["cost_factors"]["aggregations"] == 0

  def test_complex_query_cost(self):
    """Test cost estimation for complex queries"""
    query = """
        MATCH (c:Company)-[:HAS_TRANSACTION]->(t:Transaction)
        WHERE c.revenue > 1000000
        WITH c, COUNT(t) as tx_count, SUM(t.amount) as total_amount
        ORDER BY total_amount DESC
        MATCH (c)-[:LOCATED_IN]->(l:Location)
        RETURN c.name, tx_count, total_amount, l.city
        """

    result = estimate_query_cost(query)

    assert result["complexity_category"] in ["high", "very_high"]
    assert result["cost_factors"]["match_clauses"] == 2  # Two MATCH clauses
    assert result["cost_factors"]["aggregations"] >= 2  # COUNT and SUM
    assert result["cost_factors"]["subqueries"] >= 1  # WITH clause

  def test_query_recommendations(self):
    """Test optimization recommendations"""
    # Query without LIMIT should get recommendation
    query = "MATCH (n) RETURN n"
    result = estimate_query_cost(query)

    assert any("LIMIT" in rec for rec in result["recommendations"])

    # Query with full scan should get recommendation
    scan_query = "MATCH () RETURN count(*)"
    scan_result = estimate_query_cost(scan_query)

    assert any("full scans" in rec for rec in scan_result["recommendations"])


class TestFormatDuration:
  """Unit tests for duration formatting"""

  def test_milliseconds_formatting(self):
    """Test millisecond values"""
    assert format_duration(500) == "500ms"
    assert format_duration(999) == "999ms"

  def test_seconds_formatting(self):
    """Test second values"""
    assert format_duration(1000) == "1.0s"
    assert format_duration(1500) == "1.5s"
    assert format_duration(30000) == "30.0s"

  def test_minutes_formatting(self):
    """Test minute values"""
    assert format_duration(60000) == "1m 0s"
    assert format_duration(65000) == "1m 5s"
    assert format_duration(125000) == "2m 5s"

  def test_hours_formatting(self):
    """Test hour values"""
    assert format_duration(3600000) == "1h 0m"
    assert format_duration(3665000) == "1h 1m"
    assert format_duration(7265000) == "2h 1m"

  def test_edge_cases(self):
    """Test edge cases for duration formatting"""
    assert format_duration(0) == "0ms"

    # Test negative values (should handle gracefully)
    try:
      format_duration(-1000)
      # Should not crash
    except Exception:
      raise AssertionError(
        "Duration formatting should handle negative values gracefully"
      )

  def test_cost_with_parameters(self):
    """Test cost estimation with parameters"""
    query = "MATCH (n:Person) WHERE n.age > $min_age RETURN n"
    params = {"min_age": 18, "max_age": 65, "city": "New York"}

    result = estimate_query_cost(query, params)

    assert result["parameter_count"] == 3
    assert result["complexity_score"] > 0

  def test_optimization_recommendations(self):
    """Test optimization recommendations"""
    # Query with full scan pattern
    query = "MATCH () RETURN count(*)"
    result = estimate_query_cost(query)

    assert len(result["recommendations"]) > 0
    assert any("full scan" in rec.lower() for rec in result["recommendations"])


class TestUtilityFunctions:
  """Unit tests for utility functions"""

  def test_duration_formatting(self):
    """Test duration formatting"""
    test_cases = [
      (0, "0ms"),
      (500, "500ms"),
      (1000, "1.0s"),
      (1500, "1.5s"),
      (60000, "1m 0s"),
      (61500, "1m 1s"),
      (3600000, "1h 0m"),
      (3661500, "1h 1m"),
    ]

    for milliseconds, expected in test_cases:
      result = format_duration(milliseconds)
      assert result == expected, f"Expected {expected}, got {result}"

  def test_duration_formatting_edge_cases(self):
    """Test edge cases for duration formatting"""
    # Very large durations
    large_ms = 25 * 3600 * 1000  # 25 hours
    result = format_duration(large_ms)
    assert "25h" in result

    # Negative durations (shouldn't happen but test gracefully)
    try:
      result = format_duration(-1000)
      # Should not crash
    except Exception:
      raise AssertionError(
        "Duration formatting should handle negative values gracefully"
      )


def run_unit_tests():
  """Run all unit tests manually"""
  print("Running RoboSystems SDK Extensions Unit Tests...")

  test_classes = [
    TestSSEClient(),
    TestQueryBuilder(),
    TestCacheManager(),
    TestProgressTracker(),
    TestResultProcessor(),
    TestQueryValidation(),
    TestQueryCostEstimation(),
    TestUtilityFunctions(),
  ]

  total_tests = 0
  passed_tests = 0

  for test_instance in test_classes:
    class_name = test_instance.__class__.__name__
    print(f"\n--- {class_name} ---")

    test_methods = [
      method
      for method in dir(test_instance)
      if method.startswith("test_") and callable(getattr(test_instance, method))
    ]

    for method_name in test_methods:
      total_tests += 1
      try:
        test_method = getattr(test_instance, method_name)
        test_method()
        print(f"  ✓ {method_name}")
        passed_tests += 1
      except Exception as e:
        print(f"  ✗ {method_name}: {e}")

  print(f"\nUnit Tests Completed: {passed_tests}/{total_tests} passed")
  return passed_tests == total_tests


if __name__ == "__main__":
  success = run_unit_tests()
  exit(0 if success else 1)
