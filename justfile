# Default recipe to run when just is called without arguments
default:
    @just --list

# Create virtual environment and install dependencies
venv:
    pip install uv
    uv venv
    source .venv/bin/activate
    @just install-hooks
    @just install

# Install git hooks (points core.hooksPath at .githooks; idempotent, safe to re-run)
install-hooks:
    git config core.hooksPath .githooks

# Install dependencies
install:
    uv pip install -e ".[dev]"
    uv sync --all-extras

# Update dependencies
update:
    uv pip install -e ".[dev]"
    uv lock --upgrade

# Run tests
test:
    uv run pytest

# Run all tests
test-all:
    @just test
    @just format
    @just lint
    @just typecheck

# Run linting
lint:
    uv run ruff check .
    uv run ruff format --check .

# Format code
format:
    uv run ruff format .

# Run type checking
typecheck:
    uv run basedpyright

# Generate SDK from localhost API
generate-sdk url="http://localhost:8000/openapi.json" graphql_url="http://localhost:8000/extensions/kg00000000000000000000/graphql":
    bin/generate-sdk.sh {{url}}
    @just refresh-schema {{graphql_url}}

# Refresh the checked-in GraphQL SDL snapshot by introspecting a running backend.
# tests/test_graphql_queries.py validates the operations/*.graphql documents
# against it. generate-sdk runs this too, so the snapshot can't silently drift.
refresh-schema url="http://localhost:8000/extensions/kg00000000000000000000/graphql":
    uv run bin/refresh-schema.py {{url}}

# Regenerate typed GraphQL models (ariadne-codegen) from the checked-in schema
# + operations/*.graphql. Hermetic — no running backend; refresh-schema first
# if the backend schema changed.
generate-graphql:
    bin/generate-graphql.sh

# Build python package locally (for testing)
build-package:
    python -m build

# Create a feature branch
create-feature branch_type="feature" branch_name="" base_branch="main" update="no":
    bin/create-feature.sh {{branch_type}} {{branch_name}} {{base_branch}} {{update}}

# Version management
create-release type="patch":
    bin/create-release.sh {{type}}

# Clean up development artifacts
clean:
    rm -rf .pytest_cache
    rm -rf .ruff_cache
    rm -rf __pycache__
    rm -rf robosystems_client.egg-info
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete

# Show help
help:
    @just --list