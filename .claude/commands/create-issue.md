---
description: Create a GitHub issue from the repo's templates, with the right type and labels.
argument-hint: '[what the issue is about]'
---

Create a GitHub issue for the current repository based on the user's input.

## Instructions

1. **Check you're in the right repo first** - This is a **generated** SDK. `robosystems_client/api/` and `robosystems_client/models/` come from the RoboSystems API's OpenAPI document via `openapi-python-client`, and `robosystems_client/graphql/generated/` comes from `ariadne-codegen` over the checked-in `schema.graphql` plus the operation documents. A large share of apparent SDK bugs are really API bugs. Before filing here, work out which:
   - A wrong or missing **type, field, or endpoint** almost always originates in the API's OpenAPI schema — file it in `RoboFinSystems/robosystems`. Regenerating here would only reproduce the same output.
   - A bug in the **generation pipeline** — `bin/generate-sdk.sh` and its post-generation patches, `bin/generate-graphql.sh`, `bin/refresh-schema.py`, the `[tool.ariadne-codegen]` config in `pyproject.toml` — belongs here.
   - A bug in **hand-written surface** — the typed facades under `robosystems_client/clients/`, `client.py`, `errors.py`, auth and token handling, the dataframe helpers — belongs here.
   - A stale **GraphQL schema snapshot** is its own class: `schema.graphql` is checked in, so a drifted snapshot is a repo problem even though the schema itself lives in the API.

   When it's ambiguous, say which layer you think it is and why; a misfiled SDK issue costs a full round trip.

2. **Determine Issue Type** - Based on the user's description, pick one:
   - **Bug**: Defects or unexpected behavior
   - **Task**: Specific, bounded work items that can be completed in one PR
   - **Feature**: Request a new capability (no design required)
   - **RFC**: Propose a design for discussion before implementation
   - **Spec**: Approved implementation plan ready for execution

   Confirm what this repo actually offers before assuming — `ls .github/ISSUE_TEMPLATE/` for the templates and `gh issue create --help` for whether `--type` is supported.

3. **Gather Context** - If the user provides a file path or references existing code:
   - Read the relevant files to understand the current implementation
   - Check whether the file is generated (`robosystems_client/api/`, `robosystems_client/models/`, `robosystems_client/graphql/generated/`) before proposing a fix in it
   - Review any referenced documentation

4. **Draft the Issue** - Read the matching YAML template in `.github/ISSUE_TEMPLATE/` and mirror its structure. Each template declares its own `type:` in frontmatter and marks which fields are required — read the file rather than guessing the sections. Fill the optional fields too where you have the information; they're the ones that make an issue actionable later.

   Note `gh issue create --title/--body` **bypasses templates entirely** — nothing prefills and nothing validates. That's exactly why the body has to be hand-matched to the template structure.

   For an SDK bug, the reproduction needs what a consumer report usually omits: the **installed version** (`pip show robosystems-client`), the **Python version** (the package supports 3.11–3.13), a **minimal call** showing the arguments passed, and the **actual vs expected** result. Include tracebacks verbatim, and say whether the sync or async path was used — they're separate code paths and a bug in one often isn't in the other.

5. **Say whether it's a compatibility break** - This package is **post-1.0 and published on PyPI**, so external integrators pin against it. If the issue implies changing an existing signature, model field, or exported name, say so explicitly — that turns the fix into a **major** and forces coordination with the API and every consumer. Issues that quietly imply a break are the expensive ones.

6. **Sanitize for Public Visibility** - This repo is public and the issue is world-readable immediately. Before creating:
   - Remove API keys and JWTs — SDK repro snippets carry credentials more often than any other kind of issue. Check pasted tracebacks and request/response dumps line by line; an httpx traceback can include headers.
   - Remove customer names, graph IDs, and real financial payloads; reconstruct with dummy values.
   - Remove internal pricing, margins, or cost details.
   - For anything security-adjacent, keep the text terse and non-actionable — no exploit mechanics, no endpoint enumerations, no payloads. For coordinated disclosure use a private GitHub Security Advisory, never a public issue.
   - Keep ordinary technical implementation details (these are fine to share)

7. **Create the Issue** - One command, with the type set inline:

   ```bash
   gh issue create \
     --type <Bug|Task|Feature|RFC|Spec> \
     --title "<clear, concise title>" \
     --body-file /tmp/issue-body.md \
     --label "<labels>"
   ```

   No prefixes like `[SPEC]` in the title — the type handles categorization. Write the body to a file rather than inlining it, to avoid shell-escaping problems.

   To change the type on an **existing** issue: `gh issue edit <n> --type <Type>` (or `--remove-type`).

## Labels

Issue types handle primary categorization; labels carry the metadata. Always enumerate what actually exists rather than working from memory — and raise the limit, since the default truncates at 30:

```bash
gh label list --limit 100
```

The families to expect in this repo:

- **`area:*`** — the primary routing dimension: `client` (the hand-written facades), `api` (the generated endpoint surface), `types`, `auth`, `errors`, `packaging` (build, wheel contents, dependency pins), `docs`, `testing`, `ci-cd`. **Always apply one.**
- **`priority:*`** — when to do it. Note the ladder is `critical` / `high` / `low` — there is **no `priority:medium`**.
- **`size:*`** — rough effort: `small` (< 1 day), `medium` (1–3 days), `large` (> 3 days).
- **Status** — `blocked`, `needs-review`.

## Questions vs issues

`.github/ISSUE_TEMPLATE/config.yml` disables blank issues and routes open-ended questions to the org's GitHub Discussions. `gh issue create` bypasses that chooser entirely, so apply the intent yourself: if the user's input is a question ("how do I authenticate?") rather than actionable work, say so and suggest a Discussion instead of filing it.

## Example Usage

User: "The graph query response model is missing the row count field"

Response: Let me check whether that model is generated...

[Read the model — if it's under `robosystems_client/models/`, it comes from the API's OpenAPI schema, so the fix belongs in robosystems unless the post-generation patches are dropping it]
[Read bug.yml and draft a body matching its structure, with version, Python version, minimal call, and the traceback]
[Create with `gh issue create --type Bug --label area:api,size:small`]

## Output Format

After creating the issue, provide:

1. The issue URL
2. Brief summary of what was created
3. Issue type and labels applied
4. Whether the fix implies a semver break, and any companion issue that should be filed against the API

$ARGUMENTS
