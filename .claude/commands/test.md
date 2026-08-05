---
description: Run the full test and code-quality gate, fixing failures to green.
argument-hint: '[test-file-or-path]'
---

Run `just test-all` and systematically fix all failures to achieve 100% completion.

## Timeouts

Always use `timeout: 600000` (10 minutes) on Bash calls for `just test-all`. The default 2-minute Bash timeout is too short for the full suite.

## Strategy

1. **Run full suite first**: use the grep pattern below to extract the signal — pytest prints per-test output that can bury the summary.
2. **Fix in the order `test-all` runs**: pytest → format → lint → typecheck. The script short-circuits on the first failure, so fix that layer before re-running.
3. **Iterate on the failing layer only** before re-running the full suite (see Key Commands below).
4. **Stop when done**: once `just test-all` passes, stop immediately. Do NOT re-run to "confirm."

## Output Handling

**`just test-all` runs pytest FIRST, then format, lint, typecheck.** With `| tail -N`, you only see the end (typecheck output) — the pytest summary scrolls away. Always filter:

```
just test-all 2>&1 | grep -E "passed|failed|error:|FAILED|warnings summary|^= " | tail -20
```

This captures: pytest result line ("X passed, Y failed"), any FAILED test names, ruff errors, and basedpyright errors. Absence of "failed" or "FAILED" AND presence of "passed" means success — stop there.

For single-layer commands (below), output is short enough that `| tail -20` alone works.

## Key Commands

**Full suite:**

- `just test-all` — pytest + format + lint + typecheck

**Iteration (one layer at a time):**

- `uv run pytest path/to/test.py` — run a single test file (fastest feedback)
- `just test` — pytest only
- `just lint` — ruff check + ruff format --check (no auto-fix)
- `uv run ruff check . --fix` — ruff auto-fix
- `just format` — ruff format (auto-write)
- `just typecheck` — basedpyright

## Notes

- **`just test-all` mutates the working tree.** It runs `just format` (`ruff format .`, auto-write) between pytest and the lint check, so a green run can still leave modified files. Check `git status` afterwards and stage what it rewrote — the pre-commit hook runs check-only commands (`ruff check`, `ruff format --check`, `basedpyright`, `pytest`) and fails on exactly those files.
- **Never hand-fix a failure inside generated code.** `robosystems_client/api/`, `robosystems_client/models/`, and `robosystems_client/graphql/generated/` are generation output; an edit there is erased by the next `just generate-sdk` / `just generate-graphql`. The fix belongs in `bin/generate-sdk.sh`'s post-generation patches, in the `[tool.ariadne-codegen]` config in `pyproject.toml`, or in the API's schema.
- **Regeneration needs a reachable API; the GraphQL half doesn't.** `just generate-sdk` fetches the OpenAPI document from a running backend and also refreshes the checked-in `schema.graphql` snapshot. `just generate-graphql` is hermetic — it runs `ariadne-codegen` against that checked-in snapshot plus the operation documents, so it works offline but only reflects the API as of the last `just refresh-schema`. A GraphQL operation test failing after an API change usually means the snapshot is stale, not that the operation is wrong.
- **`just test-all` never builds a distribution.** Packaging problems (`pyproject.toml` metadata, missing `py.typed`, a wrong `requires-python`) pass the whole gate and fail at publish time. Use `just build-package` when the change touches packaging.

## Goal

100% pass on `just test-all` with no errors of any kind. Efficiency matters — don't re-run the full suite until you've fixed all known issues in the current layer.
