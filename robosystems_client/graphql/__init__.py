"""Extensions GraphQL transport for the Python client.

Thin wrapper around httpx that lets facade clients (e.g. LedgerClient)
execute queries against the /extensions/graphql endpoint without pulling
in a dedicated GraphQL library. Response parsing reuses the existing
generated Pydantic response models from `robosystems_client.models`, so
facade return types are unchanged regardless of transport.

This is an implementation detail — consumers only interact with the
facade clients, which hide the transport entirely.
"""

from robosystems_client.graphql.client import GraphQLClient, GraphQLError

__all__ = ["GraphQLClient", "GraphQLError"]
