# Default recipe to run when just is called without arguments
default:
    @just --list

# Create virtual environment and install dependencies
venv:
    pip install uv
    uv venv 
    source .venv/bin/activate 
    @just install

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
    @just lint
    @just format

# Run tests with coverage
test-cov:
    uv run pytest --cov=robosystems_client tests/

# Run linting
lint:
    uv run ruff check .
    uv run ruff format --check .

# Format code
format:
    uv run ruff format .

# Run type checking
typecheck:
    uv run pyright

# Version management
create-release type="patch":
    bin/create-release {{type}}

# Create PR
create-pr target-branch="main" pr-type="release" claude-review="true":
    bin/create-pr {{target-branch}} {{pr-type}} {{claude-review}}

# Build python package locally (for testing)
build-package:
    python -m build

# Publish to PyPI via GitHub Actions
publish-pypi type="patch":
    ./scripts/publish-pypi.sh {{type}}

# Clean up development artifacts
clean:
    rm -rf .pytest_cache
    rm -rf .ruff_cache
    rm -rf __pycache__
    rm -rf robosystems_client.egg-info
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete

# Generate SDK from localhost API
generate-sdk url="http://localhost:8000/openapi.json":
    @echo "🚀 Generating SDK from {{url}}..."
    rm -rf generated
    openapi-python-client generate --url {{url}} --output-path generated --config robosystems_client/sdk-config.yaml
    @echo "📦 Copying generated code to robosystems_client..."
    rm -rf robosystems_client/api robosystems_client/models robosystems_client/client.py robosystems_client/errors.py robosystems_client/types.py robosystems_client/py.typed
    cp -r generated/robo_systems_api_client/api robosystems_client/
    cp -r generated/robo_systems_api_client/models robosystems_client/
    cp generated/robo_systems_api_client/client.py robosystems_client/
    cp generated/robo_systems_api_client/errors.py robosystems_client/
    cp generated/robo_systems_api_client/types.py robosystems_client/
    cp generated/robo_systems_api_client/py.typed robosystems_client/
    rm -rf generated
    @just format
    uv run ruff check . --fix
    @just lint
    @echo "✅ SDK generation complete!"

# Show help
help:
    @just --list