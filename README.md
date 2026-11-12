# Survival Servers Studio packages

This repository publishes Survival Servers Studio's packages and the command-line tool's downloads: the API clients
for npm and PyPI, and the release files of `survivalservers`, the command-line tool. It holds their source and no
secrets.

- Publishing runs only when a version tag is pushed for a commit on main, and only after a named person approves it.
  Every registry's publish job waits for that one approval at the same moment.
- It never runs for pull requests.
- The package registries trust this repository's publish workflow directly, so no publishing keys are stored here.
- Nothing runs when a package is installed: no install scripts, no `setup.py`, no `build.rs`. Python packages are
  wheels only. npm packages are packed and published with scripts off, and the packed `package.json` carries no
  scripts at all.
- After the packages are published, the run makes a GitHub release for the tag with every file it built (the
  command-line tool for Linux, macOS and Windows, and the package files) and `SHA256SUMS` for them, written by
  `ops/publish/checksums.sh` and checked with `sha256sum -c`. That job runs outside the approval environment, with no
  publishing identity and no secrets.

Check a download: `sha256sum -c --ignore-missing SHA256SUMS` in the folder that holds it.

## Commits, merges and tags

- Every commit, merge and tag uses GitHub's no-reply address, never a personal one. The `emails` check refuses
  anything else, and it also refuses a personal address in a package's author or maintainer fields (a role address
  or none).
- Pull requests are merged as a squash with the no-reply author:
  `gh pr merge <number> --squash --author-email 2354446+humangenome@users.noreply.github.com`.
- Tags: `git -c user.name="Survival Servers" -c user.email=2354446+humangenome@users.noreply.github.com tag -a <tag> -m <message>`.

## Before a release

1. `.github/allowed-actions.txt` matches the repository's allowed actions:
   `gh api repos/survivalservers/studio-packages/actions/permissions/selected-actions --jq '.patterns_allowed[]' | sort`
   lists the same lines as the file (comments aside).
2. `python3 .github/scripts/check-actions.py` passes: every action the workflows use, and every action those actions
   call inside themselves, is pinned to a full commit and on the list. The `actions` check and the publish run's
   first job run it too, so a release stops before any approval instead of failing halfway.
3. The `build` check passed on main's last commit: it builds every package and download the way a release run
   does (`.github/scripts/build.sh`), so a release never meets a build problem after the approval.
4. Each package meant to go out has a new version; versions already on a registry are skipped. A name that is
   new on npm is packed but never published by the run: npm can only trust this workflow for a package that
   already exists, so its first version is published by hand from the run's `npm-first-by-hand` file.
   The command-line tool's downloads take the tag's version (tag `v0.1.0` makes `survivalservers_0.1.0_...`).
5. Tag on main with the no-reply tagger (above), then a reviewer approves the run in the `publish` environment.

Survival Servers Studio: https://studio.survivalservers.com/
