#!/usr/bin/env bash
# Writes DIR/SHA256SUMS for a release: one line per file in DIR ("<lowercase hex>  <name>", sha256sum's own format),
# sorted by name, every regular file but SHA256SUMS itself, then checks it with `sha256sum -c` inside DIR.
#
#   ops/publish/checksums.sh DIR
#
# It refuses (exit 1) a missing or empty folder, and anything in DIR that is not a regular file (a folder, a link):
# every file a release ships must have its line, so nothing may sit beside them unchecked. Names with a newline or a
# backslash are refused too (sha256sum would escape them). Plain bash and coreutils (or macOS's shasum) only: the
# public packages repository carries a copy of this file as it is. Security, 11/12: release files with checksums.
set -euo pipefail
export LC_ALL=C
dir=${1:?usage: checksums.sh DIR}
[ -d "$dir" ] || { echo "checksums: $dir is not a folder" >&2; exit 1; }
cd "$dir"

if command -v sha256sum >/dev/null; then
	sum() { sha256sum -- "$@"; }
	check() { sha256sum -c --quiet --strict SHA256SUMS; }
elif command -v shasum >/dev/null; then
	sum() { shasum -a 256 -- "$@"; }
	check() { shasum -a 256 -c --quiet SHA256SUMS; }
else
	echo "checksums: neither sha256sum nor shasum is installed" >&2
	exit 1
fi

files=()
while IFS= read -r -d '' f; do
	f=${f#./}
	[ "$f" = SHA256SUMS ] && continue
	case $f in
	*$'\n'* | *\\*) echo "checksums: a file name with a newline or a backslash: $(printf %q "$f")" >&2; exit 1 ;;
	esac
	if [ -L "$f" ] || [ ! -f "$f" ]; then
		echo "checksums: $f is not a regular file; a release folder holds only the files it ships" >&2
		exit 1
	fi
	files+=("$f")
done < <(find . -mindepth 1 -maxdepth 1 -print0 | sort -z)
[ "${#files[@]}" -gt 0 ] || { echo "checksums: $dir has no files" >&2; exit 1; }

tmp=$(mktemp "${TMPDIR:-/tmp}/sha256sums.XXXXXX")
trap 'rm -f -- "$tmp"' EXIT
sum "${files[@]}" > "$tmp"
# One line per file, each "<64 lowercase hex>  <name>", in the order given (sorted above).
[ "$(wc -l < "$tmp")" -eq "${#files[@]}" ] || { echo "checksums: expected ${#files[@]} lines" >&2; exit 1; }
if grep -vqE '^[0-9a-f]{64}  [^/]+$' "$tmp"; then echo "checksums: a line is not in sha256sum's format" >&2; exit 1; fi
cat "$tmp" > SHA256SUMS
check
echo "SHA256SUMS: ${#files[@]} files"
