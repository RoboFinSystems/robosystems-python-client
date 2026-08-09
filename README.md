# RoboSystems Python Client

[![PyPI version](https://badge.fury.io/py/robosystems-client.svg)](https://pypi.org/project/robosystems-client/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python Client for the RoboSystems Financial Knowledge Graph API. Access comprehensive financial data including accounting transactions, financial reports, and advanced graph analytics through a type-safe, async-ready Python interface.

## Features

- **Type-safe API client** with full type hints and typed models
- **Async/await support** for high-performance applications
- **Parquet file uploads** for table ingestion
- **Streaming support** for memory-efficient processing of large result sets
- **Financial AI Agent** integration for natural language queries
- **Comprehensive error handling** with typed exceptions

## Installation

```bash
pip install robosystems-client
```

## Versioning

This client is `1.x` and follows semantic versioning, with one distinction worth knowing before you pin.

The **stable surface** is the facades (`robosystems_client.clients`), the root exports, the error classes, the auth configuration, and every symbol used by [`robosystems-integration-template`](https://github.com/RoboFinSystems/robosystems-integration-template) — the emit path most integrations are built on. It is frozen for the life of `1.x`; breaking any of it costs a major version.

The **generated surface** — the rest of `robosystems_client.api.*` and `models.*` — is regenerated from the platform's OpenAPI spec and tracks it. Operations there can be added, renamed, or removed on a minor release, and every such removal is named in that release's notes.

So `robosystems-client>=1,<2` is the right pin if you build on the stable surface. If you depend on a generated operation outside it, either pin a minor range (`>=1.7,<1.8`) and read the release notes when you widen, or open an issue to have it promoted — the way something joins the stable surface is by being used in the integration template.

## Resources

- [RoboSystems Platform](https://robosystems.ai)
- [GitHub Repository](https://github.com/RoboFinSystems/robosystems)
- [API Documentation](https://api.robosystems.ai/docs)
- [OpenAPI Specification](https://api.robosystems.ai/openapi.json)

## Support

- [Issues](https://github.com/RoboFinSystems/robosystems-python-client/issues)
- [Wiki](https://github.com/RoboFinSystems/robosystems/wiki)
- [Projects](https://github.com/orgs/RoboFinSystems/projects)
- [Discussions](https://github.com/orgs/RoboFinSystems/discussions)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

MIT © 2026 RFS LLC
