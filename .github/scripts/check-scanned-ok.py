#!/usr/bin/env python3
"""Refuse a pull request that changes a guarded file without Survival Servers Security's OK noted in it.

Guarded: the scanned lists (any SHA256SUMS.scanned), the SOURCE_DATE_EPOCH file, and everything under .github/
(workflows, scripts, CODEOWNERS). They decide what a release may send and how it is checked, so each change must carry
Security's OK for that exact content. Security sends its OK to the Studio Launch tab with the file's git blob id
(`git hash-object FILE`); whoever writes the line into the pull request's description quotes that message's time:

    Security OK: <path> <git blob id of the file as the pull request has it> at <time of Security's message, UTC>
    Security OK: <path> deleted at <time of Security's message, UTC>          (a file the pull request deletes)

for example "Security OK: go/cli/SHA256SUMS.scanned 3b18e512dba79e4c8300dd08aeb37f8e728b8dad at 2026-11-13 05:40 UTC".
A later push that changes the file changes its blob id, so the old line no longer counts. A renamed file needs a
"deleted" line for its old path and a line for its new one.

This runs from main's copy (the pull_request_target workflow "scanned"): it reads only the pull request's file list and
description through the API, never checks out or runs the pull request's code, and posts its answer as the commit
status "Scanned lists change only with Security's OK" on the pull request's head commit (the one main's ruleset
requires). The required lines are printed, so the OK can be asked for exactly.

Environment: GITHUB_REPOSITORY, PR_NUMBER, GITHUB_TOKEN, optional GITHUB_API_URL; POST_STATUS=0 only prints.
Usage: python3 -I .github/scripts/check-scanned-ok.py
"""
import json
import os
import re
import sys
import urllib.request

CONTEXT = "Scanned lists change only with Security's OK"
OK_LINE = re.compile(r"^Security OK: (\S+) ([0-9a-f]{40}|deleted) at (\d{4}-\d{2}-\d{2} \d{2}:\d{2}(?::\d{2})? UTC)$")
MAX_FILES = 3000  # the most files GitHub lists for one pull request


def guarded(path):
    return path.endswith("SHA256SUMS.scanned") or path == "SOURCE_DATE_EPOCH" or path.startswith(".github/")


def required(files):
    """(path, blob id or "deleted") for every guarded file the pull request changes, from GitHub's file list."""
    want = {}
    for f in files:
        status, path = f.get("status"), f["filename"]
        if status == "renamed" and f.get("previous_filename") and guarded(f["previous_filename"]):
            want[f["previous_filename"]] = "deleted"
        if guarded(path):
            want[path] = "deleted" if status == "removed" else f["sha"]
    return sorted(want.items())


def missing(files, body):
    """The lines a description must hold and does not, given GitHub's file list and the description."""
    given = set()
    for line in (body or "").splitlines():
        m = OK_LINE.match(re.sub(r"[ \t]+", " ", line.strip()))
        if m:
            given.add((m.group(1), m.group(2)))
    return [(path, digest) for path, digest in required(files) if (path, digest) not in given]


def api(method, url, token, data=None):
    req = urllib.request.Request(url, method=method, data=None if data is None else json.dumps(data).encode(),
                                 headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                                          "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "studio-packages-check"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read() or b"null")


def main():
    repo, number, token = os.environ["GITHUB_REPOSITORY"], int(os.environ["PR_NUMBER"]), os.environ["GITHUB_TOKEN"]
    base = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
    pr = api("GET", f"{base}/repos/{repo}/pulls/{number}", token)
    head = pr["head"]["sha"]
    files, page = [], 1
    while True:
        batch = api("GET", f"{base}/repos/{repo}/pulls/{number}/files?per_page=100&page={page}", token)
        files += batch
        if len(batch) < 100:
            break
        page += 1
    problems = []
    if len(files) >= MAX_FILES or pr.get("changed_files", 0) > len(files):
        problems.append(f"GitHub listed {len(files)} of {pr.get('changed_files')} changed files; split the pull request")
    gaps = missing(files, pr.get("body"))
    for path, digest in required(files):
        line = f"Security OK: {path} {digest} at <time of Security's message, UTC>"
        print(("MISSING:  " if (path, digest) in gaps else "found:    ") + line)
    if not required(files):
        print("no guarded file changed (scanned lists, SOURCE_DATE_EPOCH, .github/)")
    problems += [f"{p} has no Security OK line for {d}" for p, d in gaps]
    state = "failure" if problems else "success"
    text = (f"{len(problems)} guarded change(s) without Security's OK" if problems
            else "every guarded change carries Security's OK" if required(files) else "no guarded file changed")
    for p in problems:
        print(" -", p)
    if os.environ.get("POST_STATUS", "1") != "0":
        api("POST", f"{base}/repos/{repo}/statuses/{head}", token,
            {"state": state, "context": CONTEXT, "description": text[:140]})
        print(f"status {state} posted on {head[:12]}: {text}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
