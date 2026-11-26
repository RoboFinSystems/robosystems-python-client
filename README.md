# RoboSystems Python Client

[![PyPI version](https://badge.fury.io/py/robosystems-client.svg)](https://pypi.org/project/robosystems-client/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**The Python client for [RoboSystems](https://github.com/RoboFinSystems/robosystems), the open-source knowledge graph for finance.** `robosystems-client` covers the whole API: the `api` and `models` packages are generated from the OpenAPI specification, and the facades in `robosystems_client.clients` sit over them and the GraphQL reads: they set the auth header, follow queued work to its result, and retry rate-limited requests.

## Install

```bash
pip install robosystems-client
```

Needs Python 3.12 or later. `pandas` is optional; only the DataFrame helpers need it.

## Authentication

Programs use an API key, created under **Settings → API keys** at [robosystems.ai](https://robosystems.ai). The clients route a credential by its shape: a key starting with `rfs` goes in the `X-API-Key` header, anything else in `Authorization: Bearer`. See [Authentication & API Keys](https://robosystems.ai/docs/technical/authentication-and-api-keys).

## Usage

The facades:

```python
from robosystems_client.clients import AuthenticatedClients

# the base URL defaults to https://api.robosystems.ai
clients = AuthenticatedClients("rfs...")

result = clients.execute_query(
  "sec",
  "MATCH (e:Entity) WHERE e.ticker = $ticker RETURN e.name, e.cik",
  {"ticker": "NVDA"},
)
trial_balance = clients.ledger.get_trial_balance("kg...", end_date="2026-03-31")
clients.close()
```

A client holds `query`, `operator`, `operations`, `graphs`, `files`, `tables`, `documents`, `ledger`, `investor` and `library`. The [facades README](robosystems_client/clients/README.md) covers each, with configuration, queued operations and errors.

The generated client has one module per API operation, each with `sync`, `sync_detailed`, `asyncio` and `asyncio_detailed`; request and response types are in `robosystems_client.models`:

```python
from robosystems_client import AuthenticatedClient
from robosystems_client.api.graphs import get_graphs

client = AuthenticatedClient(
  base_url="https://api.robosystems.ai",
  token="rfs...",
  prefix="",
  auth_header_name="X-API-Key",
)
graphs = get_graphs.sync(client=client)
```

## Versioning

Semantic versioning in two tiers. **Stable**: the facades, the root exports, the error classes, the auth configuration and the symbols the [integration template](https://github.com/RoboFinSystems/robosystems-integration-template) imports; breaking them costs a major release, after a deprecation cycle. **Generated**: the rest of `api` and `models` tracks the API and can change in a minor release, with every removal named in the [release notes](https://github.com/RoboFinSystems/robosystems-python-client/releases). See [Versioning & Compatibility](https://robosystems.ai/docs/technical/versioning-and-compatibility).

## Documentation

- **API reference**: [robosystems.ai/docs/api](https://robosystems.ai/docs/api) · [OpenAPI specification](https://api.robosystems.ai/openapi.json)
- **Technical docs**: [robosystems.ai/docs/technical](https://robosystems.ai/docs/technical)
- **Related**: [RoboSystems](https://github.com/RoboFinSystems/robosystems) · [TypeScript client](https://github.com/RoboFinSystems/robosystems-typescript-client) · [MCP bridge](https://github.com/RoboFinSystems/robosystems-mcp-bridge)

## Support

- [Issues](https://github.com/RoboFinSystems/robosystems-python-client/issues) · [Discussions](https://github.com/orgs/RoboFinSystems/discussions) · [Projects](https://github.com/orgs/RoboFinSystems/projects)
- [CONTRIBUTING.md](.github/CONTRIBUTING.md): branch conventions, coding standards and the pull request process

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

MIT © 2026 RFS LLC
