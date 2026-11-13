#!/usr/bin/env python3
"""Fail a pull request that changes a scanned list without Survival Servers Security's OK noted in it.

The scanned lists (any SHA256SUMS.scanned) and the SOURCE_DATE_EPOCH file decide what a release may send, so each
change to them must carry Security's OK for that exact content. For every such file the pull request changes, its
description must hold one line:

    Security OK: <path> <sha256 of the file as this pull request has it>

or, for a file the pull request deletes, "Security OK: <path> deleted". A later push that changes the file changes its
hash, so the old line no longer counts. The required lines are printed, so whoever relays the OK copies them.

Environment: BASE and HEAD (commit ids), PR_BODY (the pull request's description).
Usage: python3 -I .github/scripts/check-scanned-ok.py
"""
import hashlib
import os
import re
import subprocess
import sys


def guarded(path):
    return path.endswith("SHA256SUMS.scanned") or path == "SOURCE_DATE_EPOCH"


def main():
    base, head = os.environ["BASE"], os.environ["HEAD"]
    body = os.environ.get("PR_BODY", "") or ""
    changed = subprocess.run(["git", "diff", "--name-only", "--no-renames", base, head],
                             check=True, capture_output=True, text=True).stdout.split("\n")
    changed = sorted(p for p in changed if p and guarded(p))
    if not changed:
        print("no scanned list or SOURCE_DATE_EPOCH changed")
        return 0
    lines = {re.sub(r"\s+", " ", line.strip()) for line in body.splitlines()}
    missing = []
    for path in changed:
        show = subprocess.run(["git", "show", f"{head}:{path}"], capture_output=True)
        want = (f"Security OK: {path} deleted" if show.returncode != 0
                else f"Security OK: {path} {hashlib.sha256(show.stdout).hexdigest()}")
        print(("found:    " if want in lines else "MISSING:  ") + want)
        if want not in lines:
            missing.append(want)
    if missing:
        print(f"{len(missing)} change(s) to the scanned lists without Security's OK noted in this pull request.")
        return 1
    print("OK: every changed scanned list carries Security's OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
