#!/usr/bin/env python3
"""Tests for check-scanned-ok.py's rules, on made-up file lists and descriptions (no network).

Usage: python3 -I .github/scripts/check-scanned-ok_test.py
"""
import importlib.util
import pathlib
import sys

sys.dont_write_bytecode = True  # leave no __pycache__ beside the script
spec = importlib.util.spec_from_file_location("check", pathlib.Path(__file__).resolve().parent / "check-scanned-ok.py")
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

A = "a" * 40
B = "b" * 40
T = "at 2026-11-13 05:40 UTC"


def main():
    failures = []

    def case(name, files, body, want_missing):
        got = len(check.missing(files, body))
        ok = got == want_missing
        print(f"{'PASS' if ok else 'FAIL'}: {name} (missing {got}, want {want_missing})")
        if not ok:
            failures.append(name)

    lst = {"filename": "go/cli/SHA256SUMS.scanned", "status": "added", "sha": A}
    wf = {"filename": ".github/workflows/publish.yml", "status": "modified", "sha": B}
    readme = {"filename": "README.md", "status": "modified", "sha": A}
    case("an unguarded file needs nothing", [readme], "", 0)
    case("a scanned list with no line is missing", [lst], "", 1)
    case("a scanned list with its line passes", [lst], f"Security OK: go/cli/SHA256SUMS.scanned {A} {T}", 0)
    case("a line without the quoted time does not count", [lst], f"Security OK: go/cli/SHA256SUMS.scanned {A}", 1)
    case("a line with another hash does not count", [lst], f"Security OK: go/cli/SHA256SUMS.scanned {B} {T}", 1)
    case("anything under .github/ needs a line", [wf], "", 1)
    case(".github/ with its line passes", [wf], f"Security OK: .github/workflows/publish.yml {B} {T}", 0)
    case("SOURCE_DATE_EPOCH needs a line", [{"filename": "SOURCE_DATE_EPOCH", "status": "added", "sha": A}], "", 1)
    case("a deleted list needs a deleted line", [{"filename": "npm/studio/SHA256SUMS.scanned", "status": "removed", "sha": A}],
         f"Security OK: npm/studio/SHA256SUMS.scanned deleted {T}", 0)
    case("a deleted list with a hash line does not count",
         [{"filename": "npm/studio/SHA256SUMS.scanned", "status": "removed", "sha": A}],
         f"Security OK: npm/studio/SHA256SUMS.scanned {A} {T}", 1)
    case("a rename out of .github/ needs the old path deleted",
         [{"filename": "tools/x.py", "status": "renamed", "previous_filename": ".github/scripts/x.py", "sha": A}], "", 1)
    case("two guarded files with one line: one missing", [lst, wf], f"Security OK: go/cli/SHA256SUMS.scanned {A} {T}", 1)
    case("extra spaces and other text around the lines are fine", [lst, wf],
         f"intro\n  Security OK:  go/cli/SHA256SUMS.scanned {A} {T}  \nSecurity OK: .github/workflows/publish.yml {B} {T}\n", 0)

    if failures:
        print(f"{len(failures)} case(s) failed")
        return 1
    print("all cases passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
