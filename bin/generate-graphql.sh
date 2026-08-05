#!/usr/bin/env bash
#
# Regenerate typed GraphQL models from the checked-in schema snapshot
# (robosystems_client/graphql/schema.graphql) and the .graphql operation
# documents under robosystems_client/graphql/operations/.
#
# Hermetic: reads only checked-in files, no running backend required.
# If the backend schema changed, run `just refresh-schema` first.
# Config lives in [tool.ariadne-codegen] in pyproject.toml.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "📦 Generating typed GraphQL models (ariadne-codegen)..."
uv run ariadne-codegen

echo "🎨 Formatting generated code..."
uv run ruff format robosystems_client/graphql/generated/
uv run ruff check --fix robosystems_client/graphql/generated/

echo "✅ GraphQL codegen complete: robosystems_client/graphql/generated/"
