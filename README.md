# RoboSystems Python Client

[![PyPI version](https://badge.fury.io/py/robosystems-client.svg)](https://pypi.org/project/robosystems-client/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python Client for the RoboSystems Financial Knowledge Graph API. Access comprehensive financial data including accounting records, SEC filings, and advanced graph analytics through a type-safe, async-ready Python interface.

## Features

- **Type-safe API client** with full type hints and Pydantic models
- **Async/await support** for high-performance applications  
- **Multi-tenant support** with graph-scoped operations
- **Authentication handling** with API key and SSO support
- **Comprehensive error handling** with custom exceptions
- **Pagination support** for large data sets
- **Streaming query support** for memory-efficient processing of large result sets
- **Financial AI Agent** integration for natural language queries

## Installation

```bash
pip install robosystems-client
```

## Quick Start

```python
from robosystems_client import RoboSystemsSDK
from robosystems_client.api.query import execute_cypher_query
from robosystems_client.models import CypherQueryRequest

# Initialize the SDK
sdk = RoboSystemsSDK(
    base_url="https://api.robosystems.ai",
    token="your-api-key",
    auth_header_name="X-API-Key",
    prefix=""  # No prefix needed for API key
)

# Async usage (recommended)
import asyncio

async def main():
    # Execute a Cypher query
    query = CypherQueryRequest(
        query="MATCH (c:Company)-[:HAS_FILING]->(f:Filing) RETURN c.name, f.form_type, f.filing_date LIMIT 10"
    )
    result = await execute_cypher_query.asyncio(graph_id="your-graph-id", client=sdk, body=query)
    
    for row in result.data:
        print(f"{row['c.name']} filed {row['f.form_type']} on {row['f.filing_date']}")

asyncio.run(main())
```

## Key API Endpoints

### Graph Queries & Analytics
```python
from robosystems_client.api.query import execute_cypher_query
from robosystems_client.api.graph_analytics import get_graph_metrics
from robosystems_client.models import CypherQueryRequest

# Execute Cypher queries with parameters
query_request = CypherQueryRequest(
    query="""MATCH (c:Company {ticker: $ticker})-[:HAS_METRIC]->(m:Metric)
             WHERE m.fiscal_year >= $start_year
             RETURN m.name, m.value, m.fiscal_year
             ORDER BY m.fiscal_year DESC""",
    parameters={"ticker": "AAPL", "start_year": 2020}
)
results = await execute_cypher_query.asyncio(
    graph_id="your-graph-id", 
    client=sdk, 
    body=query_request
)

# Get graph analytics and metrics
metrics = await get_graph_metrics.asyncio(
    graph_id="your-graph-id", 
    client=sdk
)
print(f"Total nodes: {metrics.total_nodes}")
print(f"Total relationships: {metrics.total_relationships}")
```

### Financial AI Agent
```python
from robosystems_client.api.agent import query_financial_agent
from robosystems_client.models import AgentRequest

# Natural language financial queries
agent_request = AgentRequest(
    message="What was Apple's revenue growth over the last 3 years?",
    force_extended_analysis=True,
    context={"include_schema": True}
)
agent_response = await query_financial_agent.asyncio(
    graph_id="your-graph-id", 
    client=sdk, 
    body=agent_request
)
print(f"Response: {agent_response.message}")
```

### Function Patterns

Every API endpoint provides multiple calling patterns:

- **`asyncio()`** - Async call, returns parsed response (recommended)
- **`asyncio_detailed()`** - Async call, returns full Response object  
- **`sync()`** - Synchronous call, returns parsed response
- **`sync_detailed()`** - Synchronous call, returns full Response object

## Streaming Support with Extensions

The SDK includes an extensions module with SSE (Server-Sent Events) support for real-time streaming operations:

```python
from robosystems_client.extensions import (
    SSEClient, 
    QueryClient, 
    OperationClient,
    RoboSystemsExtensions
)
from robosystems_client.models import CypherQueryRequest

# Initialize extensions
extensions = RoboSystemsExtensions()

# Use QueryClient for advanced query operations
query_client = QueryClient(sdk)

# Execute queries with the query client
query = CypherQueryRequest(
    query="""MATCH (c:Company)-[:HAS_METRIC]->(m:Metric)
             WHERE m.fiscal_year >= 2020
             RETURN c.name, m.name, m.value, m.fiscal_year
             ORDER BY c.name, m.fiscal_year""",
    parameters={}
)

# Monitor long-running operations with SSE
operation_client = OperationClient(sdk)

# Stream operation events
from robosystems_client.api.operations import stream_operation_events
await stream_operation_events.asyncio(
    operation_id="op-123",
    client=sdk
)
```

The extensions module provides:
- SSE client for real-time event streaming
- Query client with advanced query management
- Operation client for monitoring long-running tasks
- Utilities for result processing and caching

## Error Handling

```python
from robosystems_client.types import Response
from robosystems_client.errors import UnexpectedStatus
import httpx

try:
    # API calls that might fail
    result = await execute_cypher_query.asyncio(
        graph_id="your-graph-id", 
        client=sdk, 
        body=query_request
    )
except UnexpectedStatus as e:
    # Handle API errors (4xx, 5xx)
    print(f"API error: {e.status_code}")
    print(f"Error details: {e.content}")
    
    # Parse error response if JSON
    if e.status_code == 400:
        error_detail = e.content.decode('utf-8')
        print(f"Validation error: {error_detail}")
    elif e.status_code == 401:
        print("Authentication failed - check your API key")
    elif e.status_code == 403:
        print("Permission denied - check graph access")
    elif e.status_code == 429:
        print("Rate limit exceeded - retry later")
except httpx.TimeoutException:
    print("Request timed out - try again")
except httpx.NetworkError as e:
    print(f"Network error: {e}")
except Exception as e:
    print(f"Unexpected error: {type(e).__name__}: {e}")

# Using detailed responses for better error handling
from robosystems_client.api.query import execute_cypher_query

response = await execute_cypher_query.asyncio_detailed(
    graph_id="your-graph-id",
    client=sdk,
    body=query_request
)

if response.status_code == 200:
    result = response.parsed
    print(f"Success: Query executed successfully")
else:
    print(f"Failed with status {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Content: {response.content}")
```

## Development

This Client is auto-generated from the RoboSystems OpenAPI specification to ensure it stays in sync with the latest API changes.

### Setup

```bash
just venv
just install
```

### Regenerating the Client

When the API changes, regenerate the Client from the OpenAPI spec:

```bash
# From localhost (development)
just generate-client http://localhost:8000/openapi.json

# From staging
just generate-client https://staging.api.robosystems.ai/openapi.json

# From production
just generate-client https://api.robosystems.ai/openapi.json
```

### Testing

```bash
just test
just test-cov
```

### Code Quality

```bash
just lint
just format
just typecheck
```
