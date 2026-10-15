---
description: Monitor a release/publish run — diagnose failures, verify the package actually landed on PyPI.
argument-hint: '[run-id]'
---

Monitor a release and publish run — pinpoint why it failed, and confirm the version actually landed on PyPI. Releases go through GitHub Actions; this command is about watching and diagnosing them, not replacing the pipeline.

## How a release actually happens here

One workflow, `create-release.yml` (`workflow_dispatch`, or `bin/create-release.sh`), with three jobs in sequence:

1. **`create-release`** — reads the current version from `pyproject.toml`, computes the next one from the requested bump, commits the bump **to `main`**, and cuts `release/<version>` from that commit.
2. **`create-tag`** — `tag-release.yml` tags that branch and cuts the GitHub Release.
3. **`publish`** — runs once the tag exists, under the `production` environment, so its required-reviewer prompt lands on this same run. It checks out the tag, verifies the version is the one just cut, builds the distribution, checks the PyPI JSON API for that version, and if it isn't there, publishes over OIDC trusted publishing. PyPI's trusted publisher is registered against `create-release.yml` and the `production` environment.

So: **merging a PR to `main` publishes nothing.** Dispatching the workflow is the publishing event, and nothing uploads until the deployment is approved on the run page. A failed publish is retried with **Re-run failed jobs** on that run — the version and tag are already cut, and a new release is warranted only when the code itself is at fault. The job refuses a version that already exists on PyPI, so a re-run after a successful upload fails at the existence check rather than uploading twice. Note the build step runs *before* that check, so a green build tells you nothing about whether a publish happened.

`tag-release.yml` writes the GitHub release body separately; see `/release-notes` for the curated-notes override.

## Scope & guardrails

- **`gh` reads are free; triggering a release is not.** Reading runs, jobs, and logs (`gh run list/view/watch`) needs no confirmation. **Dispatching `create-release.yml`** is an outward-facing and effectively irreversible action — a PyPI version can be yanked but **never** re-uploaded, so a bad publish burns that version number permanently. Confirm the bump type and the ref with the user, and default to watching a run they already started.
- **Never bump the version in `pyproject.toml` by hand.** The workflow owns the bump; a hand-bump collides with it and can produce a version that's tagged but never published.
- **Never push `main` or `release/*`.** Those are the user's. The pre-push hook blocks them.
- **The user owns the decision to publish a major.** A major reaches every consuming app and every external integrator. If the change set implies one, say so and stop — don't dispatch.

## 1. Find the run

```bash
gh run list --workflow=create-release.yml --limit 5
gh run view <run-id>
gh run watch <run-id>            # live, if it's in flight
```

## 2. Pinpoint the failure

```bash
gh run view <run-id> --log-failed
```

Classify by stage:

- **`create-release.yml` — branch already exists.** The workflow checks for `release/<version>` before creating it. A failure here usually means a previous run got partway, and the fix is to resolve the leftover branch, not to re-dispatch blindly.
- **`create-release.yml` — push to `main` rejected.** The version bump commits directly to a protected branch and needs `ACTIONS_TOKEN`; a permissions failure here looks like an auth error at the push step.
- **`publish` — waiting.** The job is paused on the `production` environment's required reviewer. Nothing is wrong; approve it from the run page (_Review deployments_).
- **`publish` — "checked out version X, expected Y".** The tag the job checked out does not carry the version this run cut. Nothing was uploaded; look at what `create-tag` tagged.
- **`publish` — "version exists on PyPI".** The job fails at the existence check and uploads nothing. After a successful publish this is the expected result of a re-run; otherwise the version wasn't bumped.
- **`publish` — build.** `pip install build twine` then `python -m build`. A build failure here is a packaging problem — usually `pyproject.toml` metadata or a missing file — that the test suite does not cover, since `just test-all` never builds a distribution.
- **`publish` — the upload.** OIDC trusted publishing. Failures are usually the PyPI-side trusted-publisher configuration (the publisher must name `create-release.yml` and the `production` environment) rather than anything in the code.

## 3. Verify it actually landed

A green workflow is not proof. Check PyPI directly:

```bash
curl -s https://pypi.org/pypi/robosystems-client/json | jq -r '.info.version'          # latest
curl -s https://pypi.org/pypi/robosystems-client/json | jq -r '.releases | keys[]'     # history
```

Then confirm the published artifact is usable, since packaging problems don't fail the upload:

```bash
pip download robosystems-client==<version> --no-deps -d /tmp/verify   # fetch the wheel
unzip -l /tmp/verify/robosystems_client-<version>-*.whl | head -30    # what actually ships
```

Check `py.typed` is present in that listing — its absence turns the SDK untyped for every consumer and nothing in CI catches it.

If the version is a major, downstream consumers need coordinated adoption — say so rather than treating the publish as the end of the task. External integrators pin against this package, so a major is a support event, not just a release.

## Output

A short status: which job, what failed and at which step, the root cause, the re-run link if any, and the verified published version from PyPI. If nothing failed, say so — don't manufacture work.

$ARGUMENTS
