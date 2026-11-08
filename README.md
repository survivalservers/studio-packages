# Survival Servers Studio packages

This repository publishes the first versions of Survival Servers Studio's package names. It holds no product code
and no secrets.

- Publishing runs only when a version tag is pushed for a commit on main, and only after a named person approves it.
- It never runs for pull requests.
- The package registries trust this repository's publish workflow directly, so no publishing keys are stored here.
- Packages published from here have no dependencies and run nothing when installed.

## Commits, merges and tags

- Every commit, merge and tag uses GitHub's no-reply address, never a personal one. The `emails` check refuses
  anything else, and it also refuses a personal address in a package's author or maintainer fields (a role address
  or none).
- Pull requests are merged as a squash with the no-reply author:
  `gh pr merge <number> --squash --author-email 2354446+humangenome@users.noreply.github.com`.
- Tags: `git -c user.name="Survival Servers" -c user.email=2354446+humangenome@users.noreply.github.com tag -a <tag> -m <message>`.

Survival Servers Studio: https://studio.survivalservers.com/
