#!/usr/bin/env python3
"""Refuse any file that is not, byte for byte, a file that was scanned before it went out.

Every file a release publishes or uploads must have its name and SHA-256 on one of the scanned lists: the files named
SHA256SUMS.scanned in this repository (sha256sum's own format, "<64 lowercase hex>  <name>"). Each list is written from
a rehearsal build of the same source with the same SOURCE_DATE_EPOCH, after that build's files were scanned, and it is
committed only after the scan was read. A hash that differs refuses. A file on no list refuses in --release mode and is
only reported in --check mode (a pull request may add files before their list). A release never rebuilds to get past
this check.

Usage: python3 -I .github/scripts/match-scanned.py --release|--check DIR [DIR ...]
Every regular file in each DIR is checked, except SHA256SUMS (the release's own list, written after this check).
"""
import hashlib
import pathlib
import re
import subprocess
import sys

LINE = re.compile(r"^([0-9a-f]{64})  ([^/\s][^/]*)$")


def load_lists():
    names = subprocess.run(["git", "ls-files", "-z", "*SHA256SUMS.scanned", "**/SHA256SUMS.scanned"],
                           check=True, capture_output=True, text=True).stdout.split("\0")
    scanned, problems = {}, []
    for name in sorted({n for n in names if n}):
        for number, line in enumerate(pathlib.Path(name).read_text().splitlines(), 1):
            m = LINE.match(line)
            if not m:
                problems.append(f"{name}:{number}: not in sha256sum's format")
                continue
            digest, file = m.groups()
            if file in scanned and scanned[file][0] != digest:
                problems.append(f"{file}: two different hashes on the scanned lists ({scanned[file][1]}, {name})")
            scanned[file] = (digest, name)
    return scanned, problems


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("--release", "--check"):
        print(__doc__.strip().splitlines()[-2])
        return 2
    release = sys.argv[1] == "--release"
    scanned, problems = load_lists()
    checked = 0
    for d in sys.argv[2:]:
        folder = pathlib.Path(d)
        if not folder.is_dir():
            continue
        for path in sorted(folder.iterdir()):
            if path.name == "SHA256SUMS":
                continue
            if path.is_symlink() or not path.is_file():
                problems.append(f"{path}: not a regular file")
                continue
            checked += 1
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if path.name not in scanned:
                if release:
                    problems.append(f"{path.name}: on no scanned list")
                else:
                    print(f"{path.name}: {digest}  (on no scanned list yet)")
                continue
            want, listed_in = scanned[path.name]
            if digest != want:
                problems.append(f"{path.name}: built {digest}, scanned {want} ({listed_in})")
            else:
                print(f"{path.name}: matches the scanned file ({listed_in})")
    if problems:
        print("REFUSED: what would go out is not what was scanned:")
        for p in problems:
            print(" -", p)
        return 1
    print(f"OK: {checked} file(s) checked against {len(scanned)} scanned file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
