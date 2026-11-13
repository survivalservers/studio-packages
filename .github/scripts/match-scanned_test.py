#!/usr/bin/env python3
"""Tests for match-scanned.py: each case builds a throwaway repository with a scanned list and runs the script on it.

Usage: python3 -I .github/scripts/match-scanned_test.py
"""
import hashlib
import os
import pathlib
import subprocess
import sys
import tempfile

SCRIPT = pathlib.Path(__file__).resolve().parent / "match-scanned.py"
GOOD = b"the scanned bytes\n"


def repo_with_list(root):
    """A git repository whose pkg/SHA256SUMS.scanned lists good.tgz with GOOD's hash."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    subprocess.run(["git", "init", "-q", str(root)], check=True, env=env)
    (root / "pkg").mkdir()
    digest = hashlib.sha256(GOOD).hexdigest()
    (root / "pkg" / "SHA256SUMS.scanned").write_text(f"{digest}  good.tgz\n")
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=True, env=env)
    return env


def run(root, env, *args):
    return subprocess.run([sys.executable, "-I", str(SCRIPT), *args], cwd=root, env=env, capture_output=True, text=True)


def main():
    failures = []

    def case(name, want, root, env, *args):
        r = run(root, env, *args)
        ok = (r.returncode == 0) == want
        print(f"{'PASS' if ok else 'FAIL'}: {name} (exit {r.returncode})")
        if not ok:
            failures.append(name)
            print(r.stdout)

    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t)
        env = repo_with_list(root)
        out = root / "out"
        out.mkdir()
        empty = root / "empty"
        empty.mkdir()

        case("--release: a folder that does not exist refuses", False, root, env, "--release", "missing")
        case("--release: a missing folder beside a good one still refuses", False, root, env, "--release", "out", "missing")
        case("--release: no file checked refuses", False, root, env, "--release", "empty")
        case("--check: a missing folder is only skipped", True, root, env, "--check", "missing")

        (out / "good.tgz").write_bytes(GOOD)
        case("--release: the scanned file passes", True, root, env, "--release", "out")
        (out / "SHA256SUMS").write_text("the release's own list is not checked\n")
        case("--release: SHA256SUMS beside it is left out", True, root, env, "--release", "out")

        (out / "other.whl").write_bytes(b"never scanned\n")
        case("--release: a file on no list refuses", False, root, env, "--release", "out")
        case("--check: a file on no list is only reported", True, root, env, "--check", "out")
        (out / "other.whl").unlink()

        (out / "good.tgz").write_bytes(b"different bytes\n")
        case("--release: a different hash refuses", False, root, env, "--release", "out")
        case("--check: a different hash refuses too", False, root, env, "--check", "out")
        (out / "good.tgz").write_bytes(GOOD)

        (out / "link.tgz").symlink_to(out / "good.tgz")
        case("--release: a link refuses", False, root, env, "--release", "out")

    if failures:
        print(f"{len(failures)} case(s) failed")
        return 1
    print("all cases passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
