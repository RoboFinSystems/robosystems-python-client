"""Utility functions for RoboSystems Client Extensions

Common helper functions for working with queries, operations, and data processing.
"""

import json
import time
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
  try:
    import pandas as pd
  except ImportError:
    pd = None
from dataclasses import dataclass, asdict


@dataclass
class QueryStats:
  """Statistics for query execution"""

  total_rows: int
  execution_time_ms: int
  bytes_processed: Optional[int] = None
  peak_memory_mb: Optional[float] = None
  cache_hit: bool = False


@dataclass
class ConnectionInfo:
  """Information about SSE connection"""

  operation_id: str
  connected_at: datetime
  reconnect_count: int = 0
  last_event_id: Optional[str] = None
  total_events: int = 0


class QueryBuilder:
  """Helper class for building Cypher queries"""

  def __init__(self):
    self.query_parts: List[str] = []
    self.parameters: Dict[str, Any] = {}

  def match(self, pattern: str) -> "QueryBuilder":
    """Add MATCH clause"""
    self.query_parts.append(f"MATCH {pattern}")
    return self

  def where(self, condition: str) -> "QueryBuilder":
    """Add WHERE clause"""
    self.query_parts.append(f"WHERE {condition}")
    return self

  def return_(self, *expressions: str) -> "QueryBuilder":
    """Add RETURN clause"""
    self.query_parts.append(f"RETURN {', '.join(expressions)}")
    return self

  def limit(self, count: int) -> "QueryBuilder":
    """Add LIMIT clause"""
    self.query_parts.append(f"LIMIT {count}")
    return self

  def order_by(self, *expressions: str) -> "QueryBuilder":
    """Add ORDER BY clause"""
    self.query_parts.append(f"ORDER BY {', '.join(expressions)}")
    return self

  def with_param(self, name: str, value: Any) -> "QueryBuilder":
    """Add parameter"""
    self.parameters[name] = value
    return self

  def build(self) -> Tuple[str, Dict[str, Any]]:
    """Build the final query and parameters"""
    query = "\n".join(self.query_parts)
    return query, self.parameters.copy()


class ResultProcessor:
  """Helper for processing query results"""

  @staticmethod
  def to_dataframe(result: Any, columns: Optional[List[str]] = None) -> Any:
    """Convert results to pandas DataFrame (if pandas available)"""
    try:
      import pandas as pd  # type: ignore[import]

      if hasattr(result, "data") and hasattr(result, "columns"):
        return pd.DataFrame(result.data, columns=result.columns)
      elif isinstance(result, list) and columns:
        return pd.DataFrame(result, columns=columns)
      else:
        return pd.DataFrame(result)

    except ImportError:
      raise ImportError(
        "pandas is required for DataFrame conversion. Install with: pip install pandas"
      )

  @staticmethod
  def to_json(result, pretty: bool = True) -> str:
    """Convert results to JSON string"""
    if hasattr(result, "__dict__"):
      data = (
        asdict(result) if hasattr(result, "__dataclass_fields__") else result.__dict__
      )
    else:
      data = result

    indent = 2 if pretty else None
    return json.dumps(data, indent=indent, default=str)

  @staticmethod
  def to_csv(
    result: Any, filename: Optional[str] = None, columns: Optional[List[str]] = None
  ) -> Optional[str]:
    """Convert results to CSV format"""
    try:
      import csv
      import io

      # Extract data and columns
      if hasattr(result, "data") and hasattr(result, "columns"):
        data = result.data
        headers = result.columns
      elif isinstance(result, list) and columns:
        data = result
        headers = columns
      else:
        data = result if isinstance(result, list) else [result]
        headers = list(data[0].keys()) if data and isinstance(data[0], dict) else None

      # Create CSV
      if filename:
        with open(filename, "w", newline="", encoding="utf-8") as f:
          writer = csv.writer(f)
          if headers:
            writer.writerow(headers)

          for row in data:
            if isinstance(row, dict):
              writer.writerow([row.get(h, "") for h in headers])
            elif isinstance(row, (list, tuple)):
              writer.writerow(row)
            else:
              writer.writerow([row])
        return filename
      else:
        # Return CSV string
        output = io.StringIO()
        writer = csv.writer(output)
        if headers:
          writer.writerow(headers)

        for row in data:
          if isinstance(row, dict):
            writer.writerow([row.get(h, "") for h in headers])
          elif isinstance(row, (list, tuple)):
            writer.writerow(row)
          else:
            writer.writerow([row])

        return output.getvalue()

    except Exception as e:
      raise Exception(f"CSV conversion failed: {e}")


class CacheManager:
  """Simple in-memory cache for query results"""

  def __init__(self, max_size: int = 100, ttl_seconds: int = 300):
    self.max_size = max_size
    self.ttl_seconds = ttl_seconds
    self.cache: Dict[str, Dict[str, Any]] = {}

  def _generate_key(
    self, graph_id: str, query: str, parameters: Dict[str, Any] = None
  ) -> str:
    """Generate cache key from query components"""
    key_data = {
      "graph_id": graph_id,
      "query": query.strip(),
      "parameters": parameters or {},
    }
    key_str = json.dumps(key_data, sort_keys=True)
    return hashlib.sha256(key_str.encode()).hexdigest()[:16]

  def get(
    self, graph_id: str, query: str, parameters: Dict[str, Any] = None
  ) -> Optional[Any]:
    """Get cached result if available and not expired"""
    key = self._generate_key(graph_id, query, parameters)

    if key in self.cache:
      entry = self.cache[key]
      if datetime.now() < entry["expires_at"]:
        entry["accessed_at"] = datetime.now()
        return entry["result"]
      else:
        # Expired
        del self.cache[key]

    return None

  def set(
    self, graph_id: str, query: str, result: Any, parameters: Dict[str, Any] = None
  ) -> None:
    """Cache a result"""
    key = self._generate_key(graph_id, query, parameters)

    # Clean up if at max size
    if len(self.cache) >= self.max_size:
      self._evict_oldest()

    self.cache[key] = {
      "result": result,
      "cached_at": datetime.now(),
      "accessed_at": datetime.now(),
      "expires_at": datetime.now() + timedelta(seconds=self.ttl_seconds),
      "graph_id": graph_id,
      "query": query[:100] + "..." if len(query) > 100 else query,
    }

  def _evict_oldest(self) -> None:
    """Remove oldest accessed entry (LRU eviction)"""
    if not self.cache:
      return

    # Find the entry with the oldest accessed_at timestamp
    oldest_key = min(self.cache.keys(), key=lambda k: self.cache[k]["accessed_at"])
    del self.cache[oldest_key]

  def clear(self) -> None:
    """Clear all cached entries"""
    self.cache.clear()

  def stats(self) -> Dict[str, Any]:
    """Get cache statistics"""
    now = datetime.now()
    active_entries = sum(
      1 for entry in self.cache.values() if now < entry["expires_at"]
    )

    return {
      "total_entries": len(self.cache),
      "active_entries": active_entries,
      "expired_entries": len(self.cache) - active_entries,
      "max_size": self.max_size,
      "ttl_seconds": self.ttl_seconds,
    }


class ProgressTracker:
  """Helper for tracking operation progress"""

  def __init__(self, operation_id: str):
    self.operation_id = operation_id
    self.started_at = datetime.now()
    self.progress_history: List[Dict[str, Any]] = []
    self.current_step = 0
    self.total_steps: Optional[int] = None

  def update(
    self, message: str, percentage: Optional[float] = None, step: Optional[int] = None
  ) -> None:
    """Update progress"""
    if step is not None:
      self.current_step = step

    progress_entry = {
      "timestamp": datetime.now(),
      "message": message,
      "percentage": percentage,
      "step": self.current_step,
      "total_steps": self.total_steps,
    }

    self.progress_history.append(progress_entry)

  def set_total_steps(self, total: int) -> None:
    """Set total number of steps"""
    self.total_steps = total

  def get_elapsed_time(self) -> timedelta:
    """Get elapsed time since start"""
    return datetime.now() - self.started_at

  def get_estimated_completion(self) -> Optional[datetime]:
    """Estimate completion time based on progress"""
    if not self.progress_history:
      return None

    latest = self.progress_history[-1]

    # If we have a percentage, use it for estimation
    if (
      latest.get("percentage")
      and latest["percentage"] > 0
      and latest["percentage"] < 100
    ):
      elapsed = self.get_elapsed_time()
      estimated_total = elapsed.total_seconds() / (latest["percentage"] / 100)
      return self.started_at + timedelta(seconds=estimated_total)

    # If we have steps, use them for estimation
    if (
      self.total_steps
      and self.current_step > 0
      and self.current_step < self.total_steps
    ):
      elapsed = self.get_elapsed_time()
      estimated_total = elapsed.total_seconds() * (self.total_steps / self.current_step)
      return self.started_at + timedelta(seconds=estimated_total)

    return None

  def get_summary(self) -> Dict[str, Any]:
    """Get progress summary"""
    latest_message = (
      self.progress_history[-1]["message"] if self.progress_history else "Starting..."
    )
    latest_percentage = (
      self.progress_history[-1].get("percentage") if self.progress_history else None
    )

    return {
      "operation_id": self.operation_id,
      "started_at": self.started_at,
      "elapsed_time": str(self.get_elapsed_time()),
      "current_step": self.current_step,
      "total_steps": self.total_steps,
      "latest_message": latest_message,
      "percentage_complete": latest_percentage,
      "estimated_completion": self.get_estimated_completion(),
      "total_updates": len(self.progress_history),
    }


class DataBatcher:
  """Helper for batching streaming data"""

  def __init__(self, batch_size: int = 1000, timeout_seconds: float = 5.0):
    self.batch_size = batch_size
    self.timeout_seconds = timeout_seconds
    self.buffer: List[Any] = []
    self.last_batch_time = time.time()

  def add(self, item: Any) -> Optional[List[Any]]:
    """Add item to batch, return batch if ready"""
    self.buffer.append(item)

    # Check if batch is ready
    current_time = time.time()
    if (
      len(self.buffer) >= self.batch_size
      or current_time - self.last_batch_time >= self.timeout_seconds
    ):
      return self.flush()

    return None

  def flush(self) -> List[Any]:
    """Flush current batch"""
    if not self.buffer:
      return []

    batch = self.buffer.copy()
    self.buffer.clear()
    self.last_batch_time = time.time()
    return batch

  def is_empty(self) -> bool:
    """Check if buffer is empty"""
    return len(self.buffer) == 0


def estimate_query_cost(
  query: str, parameters: Dict[str, Any] = None
) -> Dict[str, Any]:
  """Estimate the cost/complexity of a query"""
  query_lower = query.lower()

  # Simple heuristics for query cost estimation
  cost_factors = {
    "match_clauses": query_lower.count("match"),
    "where_clauses": query_lower.count("where"),
    "join_operations": query_lower.count("join"),
    "aggregations": sum(
      query_lower.count(op) for op in ["sum(", "count(", "avg(", "max(", "min("]
    ),
    "sort_operations": query_lower.count("order by"),
    "subqueries": query_lower.count("with "),
    "full_scans": 1 if "()" in query else 0,  # Empty node pattern
  }

  # Calculate estimated complexity score
  complexity_score = (
    cost_factors["match_clauses"] * 1
    + cost_factors["where_clauses"] * 0.5
    + cost_factors["join_operations"] * 3
    + cost_factors["aggregations"] * 2
    + cost_factors["sort_operations"] * 2
    + cost_factors["subqueries"] * 1.5
    + cost_factors["full_scans"] * 5
  )

  # Estimate based on parameters
  param_complexity = 0
  if parameters:
    param_complexity = len(parameters) * 0.1

  total_complexity = complexity_score + param_complexity

  # Categorize complexity
  if total_complexity < 2:
    complexity_category = "low"
  elif total_complexity < 5:
    complexity_category = "medium"
  elif total_complexity < 10:
    complexity_category = "high"
  else:
    complexity_category = "very_high"

  return {
    "complexity_score": total_complexity,
    "complexity_category": complexity_category,
    "cost_factors": cost_factors,
    "parameter_count": len(parameters) if parameters else 0,
    "recommendations": _get_optimization_recommendations(query_lower, cost_factors),
  }


def _get_optimization_recommendations(
  query: str, cost_factors: Dict[str, int]
) -> List[str]:
  """Get optimization recommendations for a query"""
  recommendations = []

  if cost_factors["full_scans"] > 0:
    recommendations.append(
      "Consider adding more specific node labels or properties to avoid full scans"
    )

  if cost_factors["aggregations"] > 3:
    recommendations.append(
      "Multiple aggregations detected - consider breaking into separate queries"
    )

  if cost_factors["join_operations"] > 2:
    recommendations.append(
      "Complex joins detected - ensure proper indexing on join keys"
    )

  if "limit" not in query:
    recommendations.append("Consider adding LIMIT clause to prevent large result sets")

  if cost_factors["sort_operations"] > 1:
    recommendations.append(
      "Multiple ORDER BY clauses - consider consolidating or adding appropriate indexes"
    )

  return recommendations


def format_duration(milliseconds: int) -> str:
  """Format duration in milliseconds to human-readable string"""
  if milliseconds < 1000:
    return f"{milliseconds}ms"

  seconds = milliseconds / 1000
  if seconds < 60:
    return f"{seconds:.1f}s"

  minutes = seconds / 60
  if minutes < 60:
    return f"{int(minutes)}m {int(seconds % 60)}s"

  hours = minutes / 60
  return f"{int(hours)}h {int(minutes % 60)}m"


def validate_cypher_query(query: str) -> Dict[str, Any]:
  """Basic validation of Cypher query syntax"""
  issues = []
  warnings = []

  query_stripped = query.strip()
  if not query_stripped:
    issues.append("Empty query")
    return {"valid": False, "issues": issues, "warnings": warnings}

  query_lower = query_stripped.lower()

  # Check for balanced parentheses
  if query.count("(") != query.count(")"):
    issues.append("Unbalanced parentheses")

  # Check for balanced brackets
  if query.count("[") != query.count("]"):
    issues.append("Unbalanced square brackets")

  # Check for balanced braces
  if query.count("{") != query.count("}"):
    issues.append("Unbalanced curly braces")

  # Check for invalid Cypher patterns
  import re

  # In Cypher, nodes use parentheses (), not square brackets []
  # MATCH [n] is invalid, should be MATCH (n)
  if re.search(r"\b(match|create|merge)\s+\[", query_lower):
    issues.append(
      "Invalid syntax: Nodes must use parentheses (), not square brackets []"
    )

  # Check for relationship patterns without nodes
  if re.search(r"^\s*\[.*?\]\s*return", query_lower):
    issues.append("Invalid syntax: Square brackets are for relationships, not nodes")

  # Basic keyword checks
  if not any(
    keyword in query_lower
    for keyword in ["match", "create", "merge", "delete", "set", "return"]
  ):
    warnings.append("No recognized Cypher keywords found")

  # Check for potential issues
  if "delete" in query_lower and "where" not in query_lower:
    warnings.append("DELETE without WHERE clause - this will delete all matching nodes")

  if query_lower.count("match") > 5:
    warnings.append("Many MATCH clauses detected - query might be complex")

  return {"valid": len(issues) == 0, "issues": issues, "warnings": warnings}


# Export commonly used functions
__all__ = [
  "QueryBuilder",
  "ResultProcessor",
  "CacheManager",
  "ProgressTracker",
  "DataBatcher",
  "QueryStats",
  "ConnectionInfo",
  "estimate_query_cost",
  "format_duration",
  "validate_cypher_query",
]
