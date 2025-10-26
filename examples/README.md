# RoboSystems Python Client Examples

This directory contains examples demonstrating how to use the RoboSystems Python Client SDK for various common workflows.

## Prerequisites

```bash
# Basic installation (for querying only)
pip install robosystems-client

# With table ingestion support (for uploading Parquet files)
pip install robosystems-client[tables]

# Or install all optional features
pip install robosystems-client[all]
```

## Examples

### 1. Basic Query (`basic_query.py`)

**Demonstrates:** Simple querying of an existing graph

The simplest way to get started with the RoboSystems Python SDK. This example shows how to:
- Initialize the SDK with an API key
- Execute Cypher queries against a graph
- Display query results

**Usage:**
```bash
python examples/basic_query.py \
  --api-key YOUR_API_KEY \
  --graph-id YOUR_GRAPH_ID \
  --base-url http://localhost:8000
```

**Key Features:**
- Minimal setup
- Multiple query examples (count nodes, list labels, sample data)
- Proper error handling
- Clean resource management

---

### 2. End-to-End Workflow (`e2e_workflow.py`)

**Demonstrates:** Complete workflow from user creation to querying

This comprehensive example shows the full RoboSystems workflow:
- User creation and authentication
- API key generation
- Graph creation
- Parquet file upload to staging tables
- Table ingestion into the graph
- Querying the populated graph

**Usage:**

**With new user creation:**
```bash
python examples/e2e_workflow.py
```
This will auto-generate credentials and walk through the entire setup.

**With existing API key:**
```bash
python examples/e2e_workflow.py --api-key YOUR_API_KEY
```

**Custom configuration:**
```bash
python examples/e2e_workflow.py \
  --name "John Doe" \
  --email "john@example.com" \
  --password "YourSecurePassword123!" \
  --base-url http://localhost:8000
```

**Key Features:**
- Automated user setup
- Sample data generation (creates Parquet files)
- **TableIngestClient** extension usage for simplified uploads
- Progress callbacks
- LocalStack URL auto-fix for local development
- Multiple query examples

---

## Extension Features Demonstrated

### TableIngestClient

The examples showcase the new `TableIngestClient` extension which dramatically simplifies the table upload process:

**Before (Raw API calls - 3 steps):**
```python
# Step 1: Get presigned upload URL
response = client.post(f"{base_url}/v1/graphs/{graph_id}/tables/{table_name}/files", ...)
upload_url = response.json()["upload_url"]
file_id = response.json()["file_id"]

# Step 2: Upload to S3
with open(file_path, "rb") as f:
    s3_client.put(upload_url, data=f.read())

# Step 3: Update file metadata
client.patch(f"{base_url}/v1/graphs/{graph_id}/tables/files/{file_id}", ...)
```

**After (SDK with TableIngestClient):**
```python
from robosystems_client.extensions import UploadOptions

# All 3 steps in one call!
upload_result = extensions.tables.upload_parquet_file(
    graph_id,
    table_name,
    file_path,
    UploadOptions(on_progress=lambda msg: print(msg))
)
```

**Additional TableIngestClient Methods:**
- `list_staging_tables(graph_id)` - List all staging tables
- `ingest_all_tables(graph_id, options)` - Ingest tables into graph
- `upload_and_ingest(graph_id, table_name, file_path, ...)` - Upload + ingest in one call

---

## Common Patterns

### Initializing the SDK

```python
from robosystems_client.extensions import (
    RoboSystemsExtensions,
    RoboSystemsExtensionConfig,
)

# With API key
config = RoboSystemsExtensionConfig(
    base_url="http://localhost:8000",
    headers={"X-API-Key": "your-api-key"}
)
extensions = RoboSystemsExtensions(config)

# Always close when done
extensions.close()
```

### Uploading Data

```python
from robosystems_client.extensions import UploadOptions, IngestOptions
from pathlib import Path

# Upload a parquet file
upload_options = UploadOptions(
    on_progress=lambda msg: print(f"Upload: {msg}"),
    fix_localstack_url=True  # Auto-fix for local development
)

result = extensions.tables.upload_parquet_file(
    graph_id="your-graph-id",
    table_name="Entity",
    file_path=Path("data/entities.parquet"),
    options=upload_options
)

if result.success:
    print(f"✅ Uploaded {result.row_count:,} rows")
else:
    print(f"❌ Upload failed: {result.error}")

# Ingest the uploaded tables
ingest_options = IngestOptions(
    ignore_errors=True,  # Continue on errors
    rebuild=False,       # Don't rebuild existing data
    on_progress=lambda msg: print(f"Ingest: {msg}")
)

ingest_result = extensions.tables.ingest_all_tables(
    graph_id="your-graph-id",
    options=ingest_options
)
```

### Querying Data

```python
# Simple query
result = extensions.query.query(
    graph_id="your-graph-id",
    query="MATCH (n:Entity) RETURN count(n) AS total"
)

print(f"Total nodes: {result.data[0]['total']}")

# Query with parameters
result = extensions.query.query(
    graph_id="your-graph-id",
    query="MATCH (n:Entity) WHERE n.ticker = $ticker RETURN n",
    parameters={"ticker": "AAPL"}
)

for node in result.data:
    print(f"Found: {node}")
```

## Environment Variables

You can also use environment variables for configuration:

```bash
export ROBOSYSTEMS_API_URL="http://localhost:8000"
export ROBOSYSTEMS_API_KEY="your-api-key"
export ROBOSYSTEMS_GRAPH_ID="your-graph-id"
```

Then reference them in your code:
```python
import os

config = RoboSystemsExtensionConfig(
    base_url=os.getenv("ROBOSYSTEMS_API_URL", "http://localhost:8000"),
    headers={"X-API-Key": os.getenv("ROBOSYSTEMS_API_KEY")}
)
```

## Comparison with Raw API Approach

| Operation | Raw httpx Calls | SDK with Extensions | Lines of Code Reduction |
|-----------|----------------|---------------------|------------------------|
| Upload file to table | ~25 lines (3 API calls) | ~6 lines (1 method) | **76% reduction** |
| Query graph | ~10 lines | ~3 lines | **70% reduction** |
| List tables | ~8 lines | ~2 lines | **75% reduction** |

**Benefits of Using the SDK:**
- Type-safe model classes
- Automatic error handling
- Progress callbacks
- Connection pooling
- Cleaner, more maintainable code
- Built-in support for async operations

## Additional Resources

- **API Documentation:** https://api.robosystems.ai/docs
- **Main Repository:** https://github.com/RoboSystems/robosystems-python-client
- **Extension Documentation:** See `robosystems_client/extensions/README.md`

## Getting Help

If you encounter issues:
1. Check the error message and stack trace
2. Verify your API key and graph ID are correct
3. Ensure the API server is running (for local development)
4. Check the API documentation for endpoint changes
5. Open an issue on GitHub with a minimal reproducible example

## Contributing

Have a useful example to share? Contributions are welcome!

1. Fork the repository
2. Create a new example file following the existing patterns
3. Update this README with your example
4. Submit a pull request

---

**Happy coding with RoboSystems! 🤖**
