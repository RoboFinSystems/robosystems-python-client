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
generate-sdk url="http://localhost:8000/openapi.json":
    bin/generate-sdk.sh {{url}}

# Refresh the checked-in GraphQL schema snapshot. tests/test_graphql_queries.py
# validates every hand-written query document against it, so refresh this
# whenever the backend schema changes. A stale snapshot can only cause a false
# failure here, never a false pass.
refresh-schema backend="../robosystems":
    cd {{backend}} && uv run python -c "from robosystems.graphql.schema import schema; from pathlib import Path; sdl = schema.as_str() if hasattr(schema, 'as_str') else str(schema); Path('{{justfile_directory()}}/robosystems_client/graphql/schema.graphql').write_text(sdl)"
    @echo "schema.graphql refreshed - re-run 'just test-all'"

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