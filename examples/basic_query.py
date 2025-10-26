"""
Simple example of querying a RoboSystems graph using the Python SDK.

This example demonstrates the simplest way to execute queries against
an existing graph using the RoboSystems Python Client SDK.

Usage:
    python examples/basic_query.py --api-key <your-api-key> --graph-id <graph-id>
"""

import argparse
import json
import sys

from robosystems_client.extensions import (
  RoboSystemsExtensions,
  RoboSystemsExtensionConfig,
)


def run_query_example(
  api_key: str, graph_id: str, base_url: str = "http://localhost:8000"
):
  """Run simple query examples against a graph."""
  print("\n" + "=" * 60)
  print("🔍 RoboSystems Query Example (SDK)")
  print("=" * 60)

  # Initialize extensions with API key
  config = RoboSystemsExtensionConfig(base_url=base_url, headers={"X-API-Key": api_key})
  extensions = RoboSystemsExtensions(config)

  # Example queries
  queries = [
    {"name": "Count all nodes", "query": "MATCH (n) RETURN count(n) AS total_nodes"},
    {
      "name": "Count nodes by label",
      "query": "MATCH (n) RETURN labels(n) AS label, count(n) AS count ORDER BY count DESC LIMIT 10",
    },
    {"name": "Sample nodes", "query": "MATCH (n) RETURN n LIMIT 5"},
  ]

  for example in queries:
    print(f"\n📊 {example['name']}")
    print(f"   Query: {example['query']}")

    try:
      # Execute the query
      result = extensions.query.query(graph_id, example["query"])

      # Display results
      if hasattr(result, "data") and result.data:
        print(f"   ✅ Returned {len(result.data)} records")

        # Pretty print results
        if len(result.data) <= 10:
          print("   Results:")
          print("   " + json.dumps(result.data, indent=4).replace("\n", "\n   "))
        else:
          print(f"   Showing first 10 of {len(result.data)} records:")
          print("   " + json.dumps(result.data[:10], indent=4).replace("\n", "\n   "))
      else:
        print("   ⚠️  No results returned")

    except Exception as e:
      print(f"   ❌ Query failed: {e}")

  # Cleanup
  extensions.close()

  print("\n" + "=" * 60)
  print("✅ Query examples complete!")
  print("=" * 60 + "\n")


def main():
  parser = argparse.ArgumentParser(description="Simple RoboSystems query example")
  parser.add_argument("--api-key", required=True, help="Your RoboSystems API key")
  parser.add_argument("--graph-id", required=True, help="The graph ID to query")
  parser.add_argument(
    "--base-url",
    default="http://localhost:8000",
    help="API base URL (default: http://localhost:8000)",
  )

  args = parser.parse_args()

  try:
    run_query_example(args.api_key, args.graph_id, args.base_url)
  except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback

    traceback.print_exc()
    sys.exit(1)


if __name__ == "__main__":
  main()
