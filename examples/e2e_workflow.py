"""
End-to-end workflow demonstration using RoboSystems Python Client SDK.

This script demonstrates the complete RoboSystems workflow:
1. User creation (or use existing API key)
2. Graph creation
3. Parquet file upload to staging tables
4. Data ingestion into graph
5. Graph querying

Usage:
    python examples/e2e_workflow.py --api-key <key>  # Use existing API key
    python examples/e2e_workflow.py                  # Create new user
    python examples/e2e_workflow.py --use-buffer     # Use in-memory buffer instead of file

Dependencies:
    pip install robosystems-client[tables]
"""

import argparse
import json
import secrets
import string
import sys
import time
from pathlib import Path
from typing import Optional

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from robosystems_client import Client
from robosystems_client.extensions import (
  RoboSystemsExtensions,
  RoboSystemsExtensionConfig,
  UploadOptions,
  IngestOptions,
)
from robosystems_client.api.auth.register_user import sync_detailed as register
from robosystems_client.api.auth.login_user import sync_detailed as login
from robosystems_client.api.user.create_user_api_key import (
  sync_detailed as create_api_key,
)
from robosystems_client.api.graphs.create_graph import sync_detailed as create_graph
from robosystems_client.models.register_request import RegisterRequest
from robosystems_client.models.login_request import LoginRequest
from robosystems_client.models.create_api_key_request import CreateAPIKeyRequest
from robosystems_client.models.create_graph_request import CreateGraphRequest
from robosystems_client.models.graph_metadata import GraphMetadata


def generate_secure_password(length: int = 16) -> str:
  """Generate a cryptographically secure password."""
  chars_per_type = length // 4
  password = (
    "".join(secrets.choice(string.ascii_lowercase) for _ in range(chars_per_type))
    + "".join(secrets.choice(string.ascii_uppercase) for _ in range(chars_per_type))
    + "".join(secrets.choice(string.digits) for _ in range(chars_per_type))
    + "".join(secrets.choice("!@#$%^&*") for _ in range(chars_per_type))
  )
  password_list = list(password)
  secrets.SystemRandom().shuffle(password_list)
  return "".join(password_list)


def create_sample_dataframe(num_rows: int = 100) -> pd.DataFrame:
  """Create a sample DataFrame with entity data."""
  return pd.DataFrame(
    {
      "identifier": [f"entity_{i:03d}" for i in range(1, num_rows + 1)],
      "uri": [None] * num_rows,
      "scheme": [None] * num_rows,
      "cik": [None] * num_rows,
      "ticker": [f"TKR{i}" if i % 10 == 0 else None for i in range(1, num_rows + 1)],
      "exchange": [None] * num_rows,
      "name": [f"Entity_{i}" for i in range(1, num_rows + 1)],
      "legal_name": [None] * num_rows,
      "industry": [None] * num_rows,
      "entity_type": [None] * num_rows,
      "sic": [None] * num_rows,
      "sic_description": [None] * num_rows,
      "category": [f"Category_{i % 5}" for i in range(1, num_rows + 1)],
      "state_of_incorporation": [None] * num_rows,
      "fiscal_year_end": [None] * num_rows,
      "ein": [None] * num_rows,
      "tax_id": [None] * num_rows,
      "lei": [None] * num_rows,
      "phone": [None] * num_rows,
      "website": [None] * num_rows,
      "status": [None] * num_rows,
      "is_parent": pd.Series([None] * num_rows, dtype="boolean"),
      "parent_entity_id": [None] * num_rows,
      "created_at": pd.date_range("2025-01-01", periods=num_rows, freq="h").strftime(
        "%Y-%m-%d %H:%M:%S"
      ),
      "updated_at": [None] * num_rows,
    }
  )


def create_sample_parquet(output_path: Path, num_rows: int = 100):
  """Create a sample Parquet file with entity data."""
  print(f"\n📄 Creating sample Parquet file with {num_rows} rows...")

  df = create_sample_dataframe(num_rows)
  table = pa.Table.from_pandas(df)
  pq.write_table(table, output_path)

  print(f"✅ Created {output_path.name} ({output_path.stat().st_size:,} bytes)")
  return df


def setup_user_and_api_key(
  base_url: str,
  name: Optional[str] = None,
  email: Optional[str] = None,
  password: Optional[str] = None,
) -> str:
  """Create a new user and generate an API key."""
  client = Client(base_url=base_url)

  # Generate credentials if not provided
  if not name or not email or not password:
    timestamp = int(time.time())
    name = name or f"Demo User {timestamp}"
    email = email or f"demo_{timestamp}@example.com"
    password = password or generate_secure_password()

    print("\n📧 Auto-generated credentials:")
    print(f"   Name: {name}")
    print(f"   Email: {email}")
    print(f"   Password: {password}")

  # Create user
  print("\n🔐 Creating new user...")
  user_create = RegisterRequest(name=name, email=email, password=password)
  response = register(client=client, body=user_create)
  if not response.parsed:
    raise Exception("Failed to create user")
  print(f"✅ User created: {name} ({email})")

  # Login
  print("\n🔑 Logging in...")
  user_login = LoginRequest(email=email, password=password)
  response = login(client=client, body=user_login)
  if not response.parsed:
    raise Exception("Failed to login")
  token = response.parsed.token
  print("✅ Login successful")

  # Create API key
  print("\n🔑 Creating API key...")
  api_key_create = CreateAPIKeyRequest(name=f"E2E Demo Key - {name}")
  response = create_api_key(client=client, token=token, body=api_key_create)
  if not response.parsed:
    raise Exception("Failed to create API key")
  api_key = response.parsed.key
  print(f"✅ API key created: {api_key[:20]}...")

  return api_key


def create_demo_graph(base_url: str, api_key: str) -> str:
  """Create a new graph for the demo."""
  client = Client(base_url=base_url, headers={"X-API-Key": api_key})

  graph_name = f"demo_graph_{int(time.time())}"
  print(f"\n📊 Creating graph: {graph_name}...")

  metadata = GraphMetadata(
    graph_name=graph_name,
    description=f"E2E workflow demo graph - {graph_name}",
  )
  graph_create = CreateGraphRequest(metadata=metadata)

  response = create_graph(client=client, body=graph_create)

  if not response.parsed:
    error_msg = f"Failed to create graph. Status: {response.status_code}"
    if hasattr(response, "content"):
      error_msg += f", Response: {response.content}"
    raise Exception(error_msg)

  # Handle async graph creation
  # Response can be either a dict or an object
  if isinstance(response.parsed, dict):
    graph_id = response.parsed.get("graph_id")
    operation_id = response.parsed.get("operation_id")
  else:
    graph_id = getattr(response.parsed, "graph_id", None)
    operation_id = getattr(response.parsed, "operation_id", None)

  if graph_id:
    print(f"✅ Graph created: {graph_id}")
    return graph_id
  elif operation_id:
    print(f"⚠️  Graph creation queued. Operation ID: {operation_id}")
    print("   Polling for completion...")

    # Use simple polling for fast operations like graph creation
    # (SSE connection establishment takes longer than graph creation itself ~0.3s)
    from robosystems_client.api.operations.get_operation_status import (
      sync_detailed as get_status,
    )

    max_attempts = 20
    for attempt in range(max_attempts):
      time.sleep(0.5)  # Poll every 500ms

      status_response = get_status(operation_id=operation_id, client=client)

      if status_response.parsed:
        # Response is stored in additional_properties dict
        status = status_response.parsed["status"]
        print(f"   Status: {status}")

        if status == "completed":
          result = status_response.parsed["result"]
          if isinstance(result, dict):
            graph_id = result.get("graph_id")
          else:
            graph_id = getattr(result, "graph_id", None)

          if graph_id:
            print(f"✅ Graph created: {graph_id}")
            return graph_id
          else:
            raise Exception("Operation completed but no graph_id in result")

        elif status == "failed":
          error = (
            status_response.parsed.get("error")
            if isinstance(status_response.parsed, dict)
            else status_response.parsed["error"]
            if "error" in status_response.parsed
            else "Unknown error"
          )
          raise Exception(f"Graph creation failed: {error}")

    raise Exception(f"Graph creation timed out after {max_attempts * 0.5}s")
  else:
    raise Exception(
      f"Unexpected response from graph creation. Response: {response.parsed}"
    )


def run_workflow(
  base_url: str = "http://localhost:8000",
  name: Optional[str] = None,
  email: Optional[str] = None,
  password: Optional[str] = None,
  api_key: Optional[str] = None,
  graph_id: Optional[str] = None,  # Reuse existing graph
  use_buffer: bool = False,  # Use buffer instead of file path
):
  """Run the complete E2E workflow."""
  print("\n" + "=" * 60)
  print("🤖 RoboSystems E2E Workflow Demo (SDK Version)")
  print("=" * 60)

  # Step 1: Get or create API key
  if api_key:
    print("\n✅ Using provided API key")
  else:
    api_key = setup_user_and_api_key(base_url, name, email, password)

  # Step 2: Create or reuse graph
  if graph_id:
    print(f"\n✅ Using existing graph: {graph_id}")
  else:
    graph_id = create_demo_graph(base_url, api_key)

  # Step 3: Initialize extensions with API key
  config = RoboSystemsExtensionConfig(base_url=base_url, headers={"X-API-Key": api_key})
  extensions = RoboSystemsExtensions(config)

  # Step 4: Create and upload sample data
  table_name = "Entity"

  if use_buffer:
    # Buffer-based approach (no disk I/O required)
    print("\n📄 Creating sample Parquet data in-memory (50 rows)...")

    df = create_sample_dataframe(num_rows=50)

    # Convert to Parquet in-memory
    from io import BytesIO

    buffer = BytesIO()
    table = pa.Table.from_pandas(df)
    pq.write_table(table, buffer)
    buffer.seek(0)

    print(f"✅ Created in-memory buffer ({len(buffer.getvalue()):,} bytes)")

    # Step 5: Upload from buffer
    upload_options = UploadOptions(
      on_progress=lambda msg: print(f"   {msg}"),
      fix_localstack_url=True,
      file_name="sample_data.parquet",  # Override file name for buffer
    )

    upload_result = extensions.tables.upload_parquet_file(
      graph_id, table_name, buffer, upload_options
    )
  else:
    # File-based approach (traditional)
    temp_dir = Path("/tmp/robosystems_demo")
    temp_dir.mkdir(exist_ok=True)
    parquet_file = temp_dir / "sample_data.parquet"

    _df = create_sample_parquet(parquet_file, num_rows=50)

    # Step 5: Upload parquet file using the new TableIngestClient
    upload_options = UploadOptions(
      on_progress=lambda msg: print(f"   {msg}"),
      fix_localstack_url=True,
    )

    upload_result = extensions.tables.upload_parquet_file(
      graph_id, table_name, parquet_file, upload_options
    )

  if not upload_result.success:
    print(f"❌ Upload failed: {upload_result.error}")
    sys.exit(1)

  # Step 6: List staging tables
  print("\n📋 Listing staging tables...")
  tables = extensions.tables.list_staging_tables(graph_id)

  if tables:
    print("\nStaging Tables:")
    print(
      f"{'Table Name':<20} {'Row Count':<12} {'File Count':<12} {'Size (bytes)':<15}"
    )
    print("-" * 60)
    for tbl in tables:
      print(
        f"{tbl.table_name:<20} {tbl.row_count:<12} {tbl.file_count:<12} {tbl.total_size_bytes:>14,}"
      )
  else:
    print("No tables found")

  # Step 7: Ingest tables
  print("\n⚙️  Ingesting all tables to graph...")
  ingest_options = IngestOptions(
    ignore_errors=True, rebuild=False, on_progress=lambda msg: print(f"   {msg}")
  )

  ingest_result = extensions.tables.ingest_all_tables(graph_id, ingest_options)

  if not ingest_result.get("success"):
    print(f"❌ Ingestion failed: {ingest_result.get('error')}")
    sys.exit(1)

  # Step 8: Query the graph
  queries = [
    "MATCH (n:Entity) RETURN count(n) AS total_nodes",
    "MATCH (n:Entity) RETURN n.identifier, n.name, n.ticker, n.category LIMIT 5",
    "MATCH (n:Entity) WHERE n.ticker IS NOT NULL RETURN n.identifier, n.name, n.ticker ORDER BY n.identifier DESC LIMIT 10",
  ]

  for query in queries:
    print(f"\n🔍 Executing query: {query}")
    result = extensions.query.query(graph_id, query)

    if hasattr(result, "data") and result.data:
      print(f"✅ Query returned {len(result.data)} records")
      if len(result.data) <= 10:
        print(json.dumps(result.data, indent=2))
      else:
        print(f"Showing first 10 of {len(result.data)} records:")
        print(json.dumps(result.data[:10], indent=2))
    else:
      print("❌ Query returned no results or error")

  # Cleanup
  extensions.close()
  if not use_buffer:
    parquet_file.unlink()

  print("\n" + "=" * 60)
  print("✅ E2E Workflow Complete!")
  print("=" * 60)
  print(f"\n📊 Graph ID: {graph_id}")
  print(f"🔑 API Key: {api_key}")
  if use_buffer:
    print("💡 Note: Used in-memory buffer (no /tmp file created)")
  print("\n💡 You can continue querying this graph using the API key\n")


def main():
  parser = argparse.ArgumentParser(
    description="RoboSystems E2E workflow demonstration using SDK"
  )
  parser.add_argument(
    "--api-key",
    help="Use existing API key (skip user creation)",
  )
  parser.add_argument(
    "--name",
    help="Name for new user (auto-generated if not provided)",
  )
  parser.add_argument(
    "--email",
    help="Email for new user (auto-generated if not provided)",
  )
  parser.add_argument(
    "--password",
    help="Password for new user (auto-generated if not provided)",
  )
  parser.add_argument(
    "--base-url",
    default="http://localhost:8000",
    help="API base URL (default: http://localhost:8000)",
  )
  parser.add_argument(
    "--use-buffer",
    action="store_true",
    help="Use in-memory buffer instead of file path (demonstrates buffer upload)",
  )

  args = parser.parse_args()

  try:
    run_workflow(
      base_url=args.base_url,
      name=args.name,
      email=args.email,
      password=args.password,
      api_key=args.api_key,
      use_buffer=args.use_buffer,
    )
  except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback

    traceback.print_exc()
    sys.exit(1)


if __name__ == "__main__":
  main()
