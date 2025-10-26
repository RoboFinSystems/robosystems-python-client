# RoboSystems Python Client Extensions

🚀 **Production-Ready Extensions** for the RoboSystems Financial Knowledge Graph API

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

The RoboSystems Python Client Extensions provide enhanced functionality for the auto-generated Python Client, adding:

- **Server-Sent Events (SSE)** streaming with automatic reconnection
- **Smart Query Execution** with automatic strategy selection
- **Operation Monitoring** for long-running operations
- **Connection Pooling** and intelligent resource management
- **Result Processing** and format conversion utilities
- **Caching** with TTL and LRU eviction
- **Full Async/Await Support** throughout

## 🚀 Quick Start

### Installation

```bash
# Install the extensions (part of the main client)
pip install robosystems-client

# Optional dependencies for enhanced features
pip install httpx pandas  # For SSE and DataFrame support
```

### Basic Usage

```python
from robosystems_client.extensions import create_production_extensions

# Initialize with API key
extensions = create_production_extensions("your-api-key-here")

# Execute a simple query
result = extensions.execute_query(
    graph_id="your_graph_id",
    query="MATCH (c:Company) RETURN c.name, c.revenue LIMIT 10"
)

print(f"Found {result.row_count} companies")
for company in result.data:
    print(f"- {company['name']}: ${company['revenue']:,}")

# Clean up
extensions.close()
```

### Streaming Large Results

```python
# Stream large datasets efficiently
query = "MATCH (t:Transaction) RETURN t.id, t.amount, t.timestamp"

for transaction in extensions.stream_query("your_graph_id", query, chunk_size=1000):
    # Process each transaction as it arrives
    process_transaction(transaction)
```

### Async Support

```python
import asyncio
from robosystems_client.extensions import AsyncRoboSystemsExtensions

async def main():
    extensions = AsyncRoboSystemsExtensions(config)
    
    # Async query execution
    result = await extensions.execute_query("graph_id", "MATCH (n) RETURN COUNT(n)")
    print(f"Total nodes: {result.data[0]['COUNT(n)']}")
    
    # Async streaming
    async for row in extensions.stream_query("graph_id", "MATCH (n) RETURN n"):
        await process_row_async(row)
    
    await extensions.close()

asyncio.run(main())
```

## 🔐 Authentication

### API Key Authentication (Recommended)

```python
from robosystems_client.extensions import AuthenticatedExtensions

extensions = AuthenticatedExtensions(
    api_key="your-api-key-here",
    base_url="https://api.robosystems.ai"
)
```

### Cookie Authentication

```python
from robosystems_client.extensions import CookieAuthExtensions

extensions = CookieAuthExtensions(
    cookies={"auth-token": "your-cookie-token"},
    base_url="https://api.robosystems.ai"
)
```

### JWT Token Authentication

```python
from robosystems_client.extensions import TokenExtensions

extensions = TokenExtensions(
    token="your-jwt-token",
    base_url="https://api.robosystems.ai"
)
```

### Environment-Specific Configurations

```python
from robosystems_client.extensions import create_extensions

# Production
prod_ext = create_extensions(
    'api_key', 
    api_key=os.getenv('ROBOSYSTEMS_API_KEY'),
    base_url="https://api.robosystems.ai"
)

# Development  
dev_ext = create_extensions(
    'api_key',
    api_key="dev-key-123",
    base_url="http://localhost:8000"
)
```

## 🛠 Advanced Features

### Query Builder

Build complex Cypher queries programmatically:

```python
from robosystems_client.extensions import QueryBuilder

builder = QueryBuilder()
query, params = (builder
    .match("(c:Company)-[:HAS_TRANSACTION]->(t:Transaction)")
    .match("(c)-[:LOCATED_IN]->(l:Location)")
    .where("c.revenue > $min_revenue")
    .where("l.country = $country")
    .return_("c.name", "c.revenue", "COUNT(t) as tx_count", "l.city")
    .order_by("tx_count DESC", "c.revenue DESC")
    .limit(50)
    .with_param("min_revenue", 1000000)
    .with_param("country", "USA")
    .build())

print("Generated Query:")
print(query)
print("Parameters:", params)
```

### Query Validation & Cost Estimation

```python
from robosystems_client.extensions import validate_cypher_query, estimate_query_cost

# Validate syntax
validation = validate_cypher_query(query)
if not validation['valid']:
    print("Query issues:", validation['issues'])

# Estimate complexity
cost = estimate_query_cost(query, params)
print(f"Complexity: {cost['complexity_category']} (score: {cost['complexity_score']})")

# Get optimization recommendations  
for rec in cost['recommendations']:
    print(f"💡 {rec}")
```

### Result Processing

Convert results to different formats:

```python
from robosystems_client.extensions import ResultProcessor

# Convert to JSON
json_output = ResultProcessor.to_json(result, pretty=True)

# Convert to CSV
csv_output = ResultProcessor.to_csv(result)

# Convert to pandas DataFrame (if pandas installed)
try:
    df = ResultProcessor.to_dataframe(result)
    print(df.head())
except ImportError:
    print("pandas not installed")
```

### Caching

Cache expensive queries automatically:

```python
from robosystems_client.extensions import CacheManager

cache = CacheManager(max_size=100, ttl_seconds=300)  # 5 minute TTL

# Cache is used automatically by extensions, or manually:
cached_result = cache.get("graph_id", query, parameters)
if not cached_result:
    result = extensions.execute_query("graph_id", query, parameters)
    cache.set("graph_id", query, result, parameters)
else:
    print("Using cached result!")

# View cache statistics
print(cache.stats())
```

### Progress Tracking

Monitor long-running operations:

```python
from robosystems_client.extensions import ProgressTracker

def progress_handler(progress):
    print(f"Step {progress.current_step}/{progress.total_steps}: {progress.message}")
    if progress.percentage:
        print(f"Progress: {progress.percentage}%")

# Monitor operation with progress callback
result = extensions.monitor_operation("operation_id", progress_handler)
print(f"Operation completed: {result.status}")
```

### SSE Streaming

Direct SSE connection for real-time events:

```python
from robosystems_client.extensions import SSEClient, SSEConfig, EventType

config = SSEConfig(base_url="https://api.robosystems.ai")
client = SSEClient(config)

# Set up event handlers
def handle_progress(data):
    print(f"Progress: {data['message']}")

def handle_data_chunk(data):
    print(f"Received {len(data.get('rows', []))} rows")

client.on(EventType.OPERATION_PROGRESS.value, handle_progress)
client.on(EventType.DATA_CHUNK.value, handle_data_chunk)

# Connect and monitor
client.connect("operation_id")

# Clean up
client.close()
```

## 📊 Examples

### Financial Data Analysis

```python
from robosystems_client.extensions import create_production_extensions, QueryBuilder

extensions = create_production_extensions(api_key)

# Find top performing companies by revenue growth
builder = QueryBuilder()
query, params = (builder
    .match("(c:Company)-[:HAS_FINANCIAL_REPORT]->(r:FinancialReport)")
    .where("r.year >= $start_year")
    .where("c.revenue > $min_revenue")
    .return_("c.name", "c.revenue", "r.year", "r.revenue_growth_rate")
    .order_by("r.revenue_growth_rate DESC")
    .limit(20)
    .with_param("start_year", 2020)
    .with_param("min_revenue", 10000000)
    .build())

result = extensions.execute_query("financial_graph", query, params)

print("Top 20 Companies by Revenue Growth:")
for company in result.data:
    print(f"- {company['name']}: {company['revenue_growth_rate']:.1f}% growth")
```

### Batch Processing with Streaming

```python
from robosystems_client.extensions import DataBatcher, format_duration
import time

# Process large transaction dataset in batches
batcher = DataBatcher(batch_size=5000, timeout_seconds=10.0)
total_processed = 0
start_time = time.time()

query = "MATCH (t:Transaction) WHERE t.amount > $min_amount RETURN t"
params = {"min_amount": 1000}

for transaction in extensions.stream_query("transactions_graph", query, params):
    batch = batcher.add(transaction)
    
    if batch:
        # Process batch
        process_transaction_batch(batch)
        total_processed += len(batch)
        
        if total_processed % 50000 == 0:
            elapsed = time.time() - start_time
            print(f"Processed {total_processed:,} transactions in {format_duration(int(elapsed * 1000))}")

# Process final batch
final_batch = batcher.flush()
if final_batch:
    process_transaction_batch(final_batch)
    total_processed += len(final_batch)

print(f"✅ Processed {total_processed:,} transactions total")
```

### Error Handling

```python
from robosystems_client.extensions import QueuedQueryError

try:
    result = extensions.execute_query("graph_id", "COMPLEX LONG RUNNING QUERY")
    print(f"Query completed: {len(result.data)} results")
    
except QueuedQueryError as e:
    print(f"Query was queued at position {e.queue_info.queue_position}")
    print(f"Estimated wait time: {e.queue_info.estimated_wait_seconds}s")
    
    # Wait for completion or cancel
    choice = input("Wait for completion? (y/n): ")
    if choice.lower() == 'y':
        result = extensions.monitor_operation(e.queue_info.operation_id)
        print(f"Query completed: {result.status}")
    else:
        cancelled = extensions.cancel_operation(e.queue_info.operation_id)
        print(f"Query cancelled: {cancelled}")
        
except Exception as e:
    print(f"Query failed: {e}")
```

## ⚡ Performance Optimization

### Connection Pooling

Extensions automatically manage SSE connections with pooling:

```python
# Configure connection limits
config = RoboSystemsExtensionConfig(
    max_retries=5,
    retry_delay=2000,  # 2 seconds
    timeout=60
)

extensions = RoboSystemsExtensions(config)
```

### Query Optimization

Use query analysis tools:

```python
from robosystems_client.extensions import estimate_query_cost, validate_cypher_query

# Analyze before execution
query = "MATCH (c:Company) WHERE c.revenue > 1000000 RETURN c"

# Check syntax
validation = validate_cypher_query(query)
if not validation['valid']:
    print("❌ Query has syntax errors:", validation['issues'])
    
# Estimate cost
cost = estimate_query_cost(query)
print(f"📊 Query complexity: {cost['complexity_category']}")

# Follow recommendations
for rec in cost['recommendations']:
    print(f"💡 Optimization tip: {rec}")

# Execute only if reasonable complexity
if cost['complexity_category'] in ['low', 'medium']:
    result = extensions.execute_query("graph_id", query)
else:
    print("⚠️ Query may be too expensive - consider optimization")
```

### Caching Strategy

```python
# Set up tiered caching
schema_cache = CacheManager(max_size=10, ttl_seconds=3600)     # 1 hour for schemas
query_cache = CacheManager(max_size=100, ttl_seconds=300)     # 5 minutes for queries
results_cache = CacheManager(max_size=1000, ttl_seconds=60)   # 1 minute for results

# Use appropriate cache based on query type
if "SCHEMA" in query.upper():
    cache = schema_cache
elif any(keyword in query.upper() for keyword in ["COUNT", "SUM", "AVG"]):
    cache = query_cache  
else:
    cache = results_cache
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python run_tests.py

# Or individual test suites
python -c "from robosystems_client.extensions.tests.test_unit import run_unit_tests; run_unit_tests()"
python -c "from robosystems_client.extensions.tests.test_integration import run_integration_tests; run_integration_tests()"
```

### Writing Tests

```python
from robosystems_client.extensions import AuthenticatedExtensions
from unittest.mock import Mock, patch

def test_query_execution():
    extensions = AuthenticatedExtensions("test-key")
    
    with patch('robosystems_client.extensions.auth_integration.sync_detailed') as mock_query:
        # Mock successful response
        mock_response = Mock()
        mock_response.parsed.data = [{"count": 100}]
        mock_query.return_value = mock_response
        
        result = extensions.execute_cypher_query("test_graph", "MATCH (n) RETURN count(n)")
        assert result["data"] == [{"count": 100}]
```

## 🔧 Configuration

### Environment Variables

```bash
# API Configuration
export ROBOSYSTEMS_API_URL="https://api.robosystems.ai"
export ROBOSYSTEMS_API_KEY="your-api-key"
export ROBOSYSTEMS_GRAPH_ID="your-graph-id"

# Connection Settings
export ROBOSYSTEMS_MAX_RETRIES="5"
export ROBOSYSTEMS_TIMEOUT="60"
export ROBOSYSTEMS_RETRY_DELAY="2000"
```

### Configuration Object

```python
from robosystems_client.extensions import RoboSystemsExtensionConfig

config = RoboSystemsExtensionConfig(
    base_url="https://api.robosystems.ai",
    headers={
        "X-Custom-Header": "value",
        "X-Client-Version": "1.0.0"
    },
    max_retries=3,
    retry_delay=1500,
    timeout=45
)

extensions = RoboSystemsExtensions(config)
```

## 📚 API Reference

### Core Classes

- **`RoboSystemsExtensions`** - Main extensions class
- **`AuthenticatedExtensions`** - API key authentication
- **`CookieAuthExtensions`** - Cookie authentication  
- **`TokenExtensions`** - JWT token authentication
- **`AsyncRoboSystemsExtensions`** - Async version

### SSE Components

- **`SSEClient`** - Server-Sent Events client
- **`SSEConfig`** - SSE configuration
- **`EventType`** - Standard event types enum

### Query Components  

- **`QueryClient`** - Enhanced query execution
- **`QueryBuilder`** - Programmatic query building
- **`QueryResult`** - Query result data structure

### Utilities

- **`ResultProcessor`** - Format conversion utilities
- **`CacheManager`** - Smart caching with LRU eviction
- **`ProgressTracker`** - Operation progress monitoring
- **`DataBatcher`** - Batch processing helper

### Functions

- **`validate_cypher_query(query)`** - Query syntax validation
- **`estimate_query_cost(query, params)`** - Complexity analysis
- **`format_duration(milliseconds)`** - Human-readable time formatting
- **`create_extensions(method, **kwargs)`** - Extensions factory

## 🐛 Troubleshooting

### Common Issues

**Import Errors**
```python
# Make sure all dependencies are installed
pip install httpx  # For SSE support
pip install pandas # For DataFrame conversion (optional)
```

**Authentication Failures**
```python
# Verify API key is valid
extensions = AuthenticatedExtensions("your-api-key")
try:
    result = extensions.execute_query("graph_id", "MATCH (n) RETURN count(n) LIMIT 1")
    print("✅ Authentication successful")
except Exception as e:
    print(f"❌ Auth failed: {e}")
```

**Connection Issues**
```python
# Check base URL and connectivity
import httpx

try:
    response = httpx.get("https://api.robosystems.ai/health", timeout=10)
    print(f"API Status: {response.status_code}")
except Exception as e:
    print(f"Connection failed: {e}")
```

**SSE Streaming Issues**
```python
# Enable debug logging for SSE events
config = SSEConfig(base_url="https://api.robosystems.ai")
client = SSEClient(config)

def debug_handler(data):
    print(f"SSE Event: {data}")

client.on("event", debug_handler)
```

### Debug Mode

```python
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)

# This will show internal HTTP requests and SSE events
extensions = AuthenticatedExtensions("your-key")
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality  
4. Run the test suite: `python run_tests.py`
5. Submit a pull request

## 📞 Support

- **API Reference**: [api.robosystems.ai](https://api.robosystems.ai)
- **Issues**: [GitHub Issues](https://github.com/RoboFinSystems/robosystems-python-client/issues)

---

**RoboSystems Python Client Extensions** - Production-ready streaming, monitoring, and query capabilities for financial knowledge graphs.
