#!/usr/bin/env python3
"""
Generate Python SDK from OpenAPI specification with post-generation patches.

This script handles the complete SDK generation workflow:
1. Generate SDK using openapi-python-client
2. Copy generated files to robosystems_client/
3. Apply post-generation patches (NDJSON handling, etc.)
4. Format and lint the generated code
"""

import sys
import subprocess
import shutil
from pathlib import Path


def run_command(cmd: str, description: str) -> bool:
  """Run a shell command and return success status."""
  print(f"📦 {description}...")
  result = subprocess.run(cmd, shell=True, cwd=Path(__file__).parent.parent)
  return result.returncode == 0


def patch_ndjson_handling() -> bool:
  """Add NDJSON handling to execute_cypher_query._parse_response."""

  file_path = (
    Path(__file__).parent.parent
    / "robosystems_client"
    / "api"
    / "query"
    / "execute_cypher_query.py"
  )

  if not file_path.exists():
    print(f"❌ File not found: {file_path}")
    return False

  # Read the current file content
  content = file_path.read_text()

  # Check if patch is already applied
  if "application/x-ndjson" in content:
    print("✅ NDJSON patch already applied")
    return True

  # Define the patch to insert (note: using 4-space indentation to match generated code)
  ndjson_check = """        content_type = response.headers.get("content-type", "")
        if (
            "application/x-ndjson" in content_type
            or response.headers.get("x-stream-format") == "ndjson"
        ):
            return None
"""

  # Find the location to insert the patch (raw generated code uses 4 spaces)
  search_pattern = "    if response.status_code == 200:\n        response_200 = ExecuteCypherQueryResponse200.from_dict(response.json())\n\n        return response_200"

  if search_pattern not in content:
    print(f"❌ Could not find expected pattern in {file_path}")
    print("The generated code structure may have changed.")
    return False

  # Replace the pattern with the patched version
  replacement = f"    if response.status_code == 200:\n{ndjson_check}        response_200 = ExecuteCypherQueryResponse200.from_dict(response.json())\n\n        return response_200"
  patched_content = content.replace(search_pattern, replacement)

  # Write the patched content back
  _ = file_path.write_text(patched_content)

  print(f"✅ Applied NDJSON patch to {file_path.name}")
  return True


def main():
  """Main SDK generation workflow."""

  # Get OpenAPI URL from command line or use default
  url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000/openapi.json"

  print(f"🚀 Generating Python SDK from {url}...")
  print()

  # Step 1: Generate SDK
  if not run_command("rm -rf generated", "Cleaning previous generation"):
    return 1

  if not run_command(
    f"uv run openapi-python-client generate --url {url} --output-path generated --config robosystems_client/sdk-config.yaml",
    f"Generating SDK from {url}",
  ):
    return 1

  # Step 2: Copy generated files
  print("📦 Copying generated code to robosystems_client/...")

  base_path = Path(__file__).parent.parent
  generated_path = base_path / "generated" / "robo_systems_api_client"
  target_path = base_path / "robosystems_client"

  # Remove old generated files
  for item in ["api", "models", "client.py", "errors.py", "types.py", "py.typed"]:
    item_path = target_path / item
    if item_path.exists():
      if item_path.is_dir():
        shutil.rmtree(item_path)
      else:
        item_path.unlink()

  # Copy new generated files
  for item in ["api", "models", "client.py", "errors.py", "types.py", "py.typed"]:
    src = generated_path / item
    dst = target_path / item
    if src.exists():
      if src.is_dir():
        shutil.copytree(src, dst)
      else:
        shutil.copy2(src, dst)

  # Clean up generated folder
  shutil.rmtree(base_path / "generated")

  print()

  # Step 3: Apply patches
  print("🔧 Applying post-generation patches...")
  if not patch_ndjson_handling():
    print("⚠️  Warning: NDJSON patch failed, but continuing...")

  print()

  # Step 4: Format and lint
  if not run_command("uv run ruff format .", "Formatting code"):
    return 1

  if not run_command("uv run ruff check . --fix", "Fixing linting issues"):
    return 1

  if not run_command("uv run ruff check .", "Running final linting check"):
    return 1

  if not run_command("uv run ruff format --check .", "Verifying formatting"):
    return 1

  print()
  print("✅ SDK generation complete!")
  print()
  print("Changes applied:")
  print("  - Generated fresh SDK from OpenAPI spec")
  print("  - Applied NDJSON streaming support patch")
  print("  - Formatted and linted all code")
  print()

  return 0


if __name__ == "__main__":
  sys.exit(main())
