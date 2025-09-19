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

# Generate SDK from localhost API
generate-sdk url="http://localhost:8000/openapi.json":
    @echo "🚀 Generating Client from {{url}}..."
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
    @echo "✅ Client generation complete!"

# Build python package locally (for testing)
build-package:
    python -m build

# Create a feature branch
create-feature branch_type="feature" branch_name="" base_branch="main":
    bin/create-feature {{branch_type}} {{branch_name}} {{base_branch}}

# Version management
create-release type="patch":
    bin/create-release {{type}}

# Create PR
create-pr target_branch="main" claude_review="true":
    bin/create-pr {{target_branch}} {{claude_review}}

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