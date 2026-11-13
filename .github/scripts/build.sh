#!/usr/bin/env bash
# Builds every package in this repository and the command-line tool's downloads into dist/. It never publishes.
#
#   .github/scripts/build.sh --release VERSION   what a release run publishes: only versions not on npm or PyPI yet
#   .github/scripts/build.sh --check VERSION     every package, published or not (pull requests and main)
#
# VERSION is the command-line tool's version (a release run passes the tag's, v0.1.0 -> 0.1.0).
# It writes:
#   dist/npm/               npm packages for names that are already on npm (the release run publishes these)
#   dist/npm-first-by-hand/ npm packages for names new on npm: trusted publishing can only be set on a package that
#                           already exists, so a new name's first version is published by hand from this file
#   dist/pypi/              wheels (no source packages: installing a wheel runs nothing)
#   dist/cli/               the command-line tool for Linux, macOS and Windows, when its source is here (go/cli)
# and, on GitHub, the counts npm=N and pypi=N to $GITHUB_OUTPUT.
#
# Same files every time: the file SOURCE_DATE_EPOCH at the top of this repository, when present, sets every file time
# (the rehearsal build that was scanned used the same value). Then every file built is checked against the scanned
# lists (SHA256SUMS.scanned, match-scanned.py): with --release a file that differs or is on no list stops the run
# before any approval; with --check a file that differs fails and one on no list is reported.
#
# Nothing a package runs when installed: no setup.py, setup.cfg, build.rs, binding.gyp, install.ps1, .targets or
# .props anywhere; no npm script that runs at install; npm builds and packs with scripts off and the packed
# package.json carries no scripts at all (read back from each packed file).
set -euo pipefail
mode=${1:-}
version=${2:-}
case $mode in --release | --check) ;; *) echo "usage: build.sh --release|--check VERSION" >&2; exit 2 ;; esac
[ -n "$version" ] || { echo "usage: build.sh --release|--check VERSION" >&2; exit 2; }
root=$(cd "$(dirname "$0")/../.." && pwd)
cd "$root"
if [ -f SOURCE_DATE_EPOCH ]; then
  SOURCE_DATE_EPOCH=$(tr -d '[:space:]' < SOURCE_DATE_EPOCH)
  case $SOURCE_DATE_EPOCH in '' | *[!0-9]*) echo "SOURCE_DATE_EPOCH: a whole number of seconds" >&2; exit 1 ;; esac
  export SOURCE_DATE_EPOCH
  echo "SOURCE_DATE_EPOCH=$SOURCE_DATE_EPOCH"
fi
tmp=${RUNNER_TEMP:-$(mktemp -d)}
rm -rf dist && mkdir -p dist/npm dist/npm-first-by-hand dist/pypi dist/cli

echo "== No install-time code in any package"
bad=$(git ls-files | grep -E '(^|/)(setup\.py|setup\.cfg|build\.rs|binding\.gyp|install\.ps1)$|\.(targets|props)$' || true)
if [ -n "$bad" ]; then echo "Not allowed in this repository: $bad"; exit 1; fi
# npm runs these when a package is installed (prepare also for git and folder installs): never allowed.
for f in npm/*/package.json; do
  node -e '
    const p = require(process.argv[1]);
    const banned = ["preinstall", "install", "postinstall", "prepare", "preprepare", "postprepare", "prepublish"];
    const found = Object.keys(p.scripts || {}).filter(s => banned.includes(s));
    if (found.length) { console.log(process.argv[1] + " has install-time scripts: " + found.join(", ")); process.exit(1); }
  ' "$root/$f"
done

echo "== npm packages"
for d in npm/*/; do
  d=${d%/}
  name=$(node -p 'require(process.argv[1]).name' "$root/$d/package.json")
  pkgversion=$(node -p 'require(process.argv[1]).version' "$root/$d/package.json")
  if [ "$mode" = --release ] && npm view "$name@$pkgversion" version >/dev/null 2>&1; then
    echo "$name@$pkgversion is already on npm; skipped"; continue
  fi
  out=dist/npm
  if ! npm view "$name" name >/dev/null 2>&1; then echo "$name is a new name on npm: packed for a first publish by hand"; out=dist/npm-first-by-hand; fi
  work=$(mktemp -d "$tmp/npm.XXXXXX")
  cp -R "$d/." "$work/"
  if [ -f "$work/tsconfig.json" ]; then
    (cd "$work" && npm ci --ignore-scripts --no-audit --no-fund && ./node_modules/.bin/tsc -p tsconfig.json)
  fi
  # The published package.json carries no scripts and no development packages.
  (cd "$work" && npm pkg delete scripts devDependencies && npm pack --ignore-scripts --pack-destination "$root/$out")
  rm -rf "$work"
done
for t in dist/npm/*.tgz dist/npm-first-by-hand/*.tgz; do
  [ -e "$t" ] || continue
  tar -xzOf "$t" package/package.json | node -e '
    let s = ""; process.stdin.on("data", c => s += c).on("end", () => {
      const p = JSON.parse(s);
      if (p.scripts && Object.keys(p.scripts).length) { console.log(process.argv[1] + ": packed with scripts"); process.exit(1); }
      if (p.gypfile) { console.log(process.argv[1] + ": gypfile set"); process.exit(1); }
    });' "$t"
  if tar -tzf "$t" | grep -qE '(^|/)binding\.gyp$'; then echo "$t: binding.gyp packed"; exit 1; fi
  echo "$t:"; tar -tzf "$t" | sed 's/^/  /'
done

echo "== Python packages (wheels only, build tools pinned by hash)"
cat > "$tmp/build-requirements.txt" <<'REQ'
build==1.6.1 --hash=sha256:ecd351a4be9d35a9eaaba244a7687143c9c7d4aea6ac964e7e7ddab20cbcf4e7
packaging==26.3 --hash=sha256:d7193f7c8e4e93f444fde0262bf90af30e16fa0ad0ad44cb553c87339b23cd1c
pyproject_hooks==1.3.3 --hash=sha256:5fc53fdac9f7bd63fbcdc868fb5f90b4784d78a53a3d3388cd738b807441a20b
flit_core==4.2.0 --hash=sha256:2bee22dc8ba89c2e35b4e1ad575e596aac945c85672dd8f3cad21b629036e044
uv_build==0.12.24 --hash=sha256:57025a08ad963c5f3f0a573d848a39b6adf9d6095b47b87abbad68af07e9699e
REQ
rm -rf "$tmp/build"
python3 -m venv "$tmp/build"
"$tmp/build/bin/pip" install --quiet --require-hashes --only-binary=:all: -r "$tmp/build-requirements.txt"
for d in pypi/*/; do
  spec=$(python3 -c 'import sys, tomllib; p = tomllib.load(open(sys.argv[1], "rb"))["project"]; print(p["name"] + "/" + p["version"])' "$d/pyproject.toml")
  if [ "$mode" = --release ]; then
    code=$(curl -s -o /dev/null -w '%{http_code}' "https://pypi.org/pypi/$spec/json")
    if [ "$code" = 200 ]; then echo "$spec is already on PyPI; skipped"; continue; fi
    if [ "$code" != 404 ]; then echo "PyPI answered $code for $spec; stopping"; exit 1; fi
  fi
  # uv_build's backend finds its own program on PATH, so the build tools' folder goes first.
  PATH="$tmp/build/bin:$PATH" "$tmp/build/bin/python" -m build --wheel --no-isolation --outdir dist/pypi "$d"
done
echo "== Install each wheel and import it (wheels only, nothing built at install)"
for w in dist/pypi/*.whl; do
  [ -e "$w" ] || continue
  rm -rf "$tmp/try"
  python3 -m venv "$tmp/try"
  "$tmp/try/bin/pip" install --quiet --only-binary=:all: "$w"
  mods=$(python3 -c 'import sys, zipfile; print(" ".join(sorted({n.split("/")[0] for n in zipfile.ZipFile(sys.argv[1]).namelist() if "/" in n and not n.split("/")[0].endswith((".dist-info", ".data"))})))' "$w")
  # A placeholder (a near miss of one of our names) installs nothing and its import only says where the real package
  # is: that ImportError is its whole job. Any other failure fails the build.
  for m in $mods; do
    "$tmp/try/bin/python" -c '
import importlib, sys
m = sys.argv[1]
try:
    importlib.import_module(m)
    print("imported", m)
except ImportError as e:
    if "is a placeholder" in str(e) and "pip install survivalservers-studio" in str(e):
        print("placeholder", m, "points to survivalservers-studio")
    else:
        raise
' "$m"
  done
done
rm -rf "$tmp/try"

echo "== The command-line tool's downloads"
# They are built only at the version on go/cli's scanned list: a tag for something else (a placeholder package, say)
# rebuilds no downloads, so no file can go out that was never scanned and the latest downloads stay where they are.
scanned_cli=""
if [ -f go/cli/SHA256SUMS.scanned ]; then
  scanned_cli=$(sed -n 's/^[0-9a-f]\{64\}  survivalservers_\([^_]*\)_linux_amd64\.tar\.gz$/\1/p' go/cli/SHA256SUMS.scanned | head -n1)
fi
if [ -x go/cli/release.sh ] && [ -n "$scanned_cli" ] && [ "$version" != "$scanned_cli" ]; then
  echo "not rebuilt: this run's version $version is not the scanned version $scanned_cli"
elif [ -x go/cli/release.sh ]; then
  go version
  (cd go/cli && ./release.sh "$version")
  # The release writes one SHA256SUMS for every file it carries, so the tool's own list is not copied.
  find go/cli/dist -maxdepth 1 -type f \( -name '*.tar.gz' -o -name '*.zip' \) -exec cp {} dist/cli/ \;
  rm -rf go/cli/dist
  ls -l dist/cli
else
  echo "no command-line tool in this repository yet; nothing to build"
fi

echo "== What was built (SHA-256)"
find dist -type f -exec sha256sum {} + | sed 's#  dist/[^/]*/#  #' | sort -k2
echo "== Against the scanned lists"
python3 -I .github/scripts/match-scanned.py "$mode" dist/npm dist/npm-first-by-hand dist/pypi dist/cli

npm_count=$(find dist/npm -name '*.tgz' | wc -l)
pypi_count=$(find dist/pypi -name '*.whl' | wc -l)
echo "npm: $npm_count new, first by hand: $(find dist/npm-first-by-hand -name '*.tgz' | wc -l), PyPI: $pypi_count, downloads: $(find dist/cli -type f | wc -l)"
if [ -n "${GITHUB_OUTPUT:-}" ]; then
  { echo "npm=$npm_count"; echo "pypi=$pypi_count"; } >> "$GITHUB_OUTPUT"
fi
