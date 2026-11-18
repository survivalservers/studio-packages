#!/usr/bin/env python3
"""Decide whether a release run may publish the MCP Registry entry, and refuse a wrong one.

The entry's words live in one file, go/mcp/server.json (the AI tool's own entry, copied with its source), and the
publish job sends exactly those bytes. Two more files gate it, in mcp-registry/:

  approved.sha256   the owner's yes on those exact bytes: one line "<sha256>  go/mcp/server.json" (comments start
                    with #). Added only on the owner's yes. Other bytes are refused.
  publish-go        the lead's go for one publication, added in the commit the release tag names, only once the hosted
                    AI tool server is live at the entry's address and each AI tool has connected to it once (Survival
                    Servers Security's terms for this job). "key: value" lines:
                        version: <the version in server.json>
                        server.json sha256: <the same sha256>
                        hosted server live since: YYYY-MM-DD
                        every tool connected once by: YYYY-MM-DD
                    Taken out again after the publication: a version is published once.

Decisions (printed, and written as go=true|false and sha256=... to --github-output):
  - no go file: go=false, exit 0. Nothing is sent and the release goes on; anything wrong with the entry or its
    approval is printed as NOTE lines.
  - a go file: the entry must pass every rule below, the approval must name its bytes, and the go must be whole and
    name the same bytes and version: then go=true, exit 0; otherwise exit 1 (a red run).
  - --require-go: anything but go=true is exit 1.

The rules for the entry (the registry's published rules and ours, as ops/publish/mcpregistry in the main repository
checks the copy it writes): one JSON object, no key twice, exactly the keys $schema, name, title, description,
repository, version and remotes, in that order; our name; the 2025-12-11 schema; a description of 1 to 100 characters
on one line; a plain semantic version; exactly one remote, streamable-http at the hosted address, and nothing else
(no headers); the AI tool's repository; UTF-8 ending in one newline.

Beside its go it prints the mcp-publisher the registry job runs: the version, SHA-256 and release date pinned in that
job's env in .github/workflows/publish.yml (MCP_PUBLISHER_VERSION, MCP_PUBLISHER_SHA256, MCP_PUBLISHER_RELEASED). With a
go file, a pin that is missing or not in that form is refused too.

Usage: python3 -I .github/scripts/mcp-registry-gate.py [--root DIR] [--github-output FILE] [--require-go]
"""
import hashlib
import json
import os
import re
import sys

NAME = "io.github.survivalservers/survival-servers"
URL = "https://studio.survivalservers.com/mcp"  # the hosted AI tool server, a path on the Studio's own address
SCHEMA = "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"
KEYS = ["$schema", "name", "title", "description", "repository", "version", "remotes"]
VERSION = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z][0-9A-Za-z.-]*)?$")
ENTRY = os.path.join("go", "mcp", "server.json")
GATE_DIR = "mcp-registry"
APPROVAL = re.compile(r"^([0-9a-f]{64})  go/mcp/server\.json$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
GO_KEYS = ["version", "server.json sha256", "hosted server live since", "every tool connected once by"]
WORKFLOW = os.path.join(".github", "workflows", "publish.yml")
PIN = re.compile(r'^\s+MCP_PUBLISHER_(VERSION|SHA256|RELEASED):\s*"([^"]*)"\s*$', re.M)


class Refused(Exception):
    pass


def no_twice(pairs):
    seen = {}
    for k, v in pairs:
        if k in seen:
            raise Refused(f"server.json: the key {k!r} is written twice")
        seen[k] = v
    return seen


def entry_problems(raw):
    """What is wrong with server.json's bytes, as a list of lines (empty: it may be sent)."""
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return ["server.json: not UTF-8"]
    if not text.endswith("\n") or text.endswith("\n\n"):
        return ["server.json: must end in exactly one newline"]
    try:
        doc = json.loads(text, object_pairs_hook=no_twice)
    except Refused as e:
        return [str(e)]
    except ValueError as e:
        return [f"server.json: not JSON ({e})"]
    if not isinstance(doc, dict):
        return ["server.json: not a JSON object"]
    out = []
    if list(doc) != KEYS:
        out.append(f"server.json: the keys must be exactly {KEYS}, in that order; it has {list(doc)}")
    if doc.get("$schema") != SCHEMA:
        out.append(f"server.json: $schema must be {SCHEMA}")
    if doc.get("name") != NAME:
        out.append(f"server.json: name must be {NAME}")
    d = doc.get("description")
    if not isinstance(d, str) or not d or len(d) > 100 or "\n" in d or d != d.strip():
        out.append("server.json: the description must be one line of 1 to 100 characters")
    if not isinstance(doc.get("title"), str) or not doc.get("title"):
        out.append("server.json: a title")
    v = doc.get("version")
    if not isinstance(v, str) or not VERSION.match(v):
        out.append("server.json: version must be a plain semantic version such as 0.1.1")
    r = doc.get("remotes")
    if not (isinstance(r, list) and len(r) == 1 and isinstance(r[0], dict)):
        out.append("server.json: exactly one remote, the hosted AI tool server")
    elif r[0] != {"type": "streamable-http", "url": URL}:
        out.append(f"server.json: the one remote is {{\"type\": \"streamable-http\", \"url\": \"{URL}\"}} and nothing else")
    repo = doc.get("repository")
    if not (isinstance(repo, dict) and repo.get("source") == "github" and repo.get("url") == "https://github.com/survivalservers/studio-go"):
        out.append("server.json: the repository is survivalservers/studio-go on GitHub")
    return out


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.rstrip("\n") for ln in f if ln.strip() and not ln.lstrip().startswith("#")]


def entry_state(root):
    """(sha256 or None, version or None, problems): the entry against the rules and the owner's approval."""
    entry = os.path.join(root, ENTRY)
    if not os.path.isfile(entry):
        return None, None, [f"{ENTRY} is missing"]
    with open(entry, "rb") as f:
        raw = f.read()
    sha = hashlib.sha256(raw).hexdigest()
    problems = entry_problems(raw)
    version = None if problems else json.loads(raw)["version"]
    approval = os.path.join(root, GATE_DIR, "approved.sha256")
    if not os.path.isfile(approval):
        problems.append(f"no {GATE_DIR}/approved.sha256: the owner has not said yes to these bytes")
    else:
        lines = read_lines(approval)
        m = APPROVAL.match(lines[0]) if len(lines) == 1 else None
        if not m:
            problems.append(f"{GATE_DIR}/approved.sha256: exactly one line \"<sha256>  {ENTRY}\" besides comments")
        elif m.group(1) != sha:
            problems.append(f"{ENTRY} is {sha}, but the owner approved {m.group(1)}: the bytes changed after the yes")
    return sha, version, problems


def go_problems(path, sha, version):
    """What is wrong with the lead's go file (empty: it names these bytes and this version, whole)."""
    fields, out = {}, []
    for ln in read_lines(path):
        key, sep, value = ln.partition(":")
        key, value = key.strip(), value.strip()
        if not sep or key not in GO_KEYS or key in fields:
            out.append(f"{GATE_DIR}/publish-go: the line {ln!r} is not one of {GO_KEYS}, once each")
            continue
        fields[key] = value
    missing = [k for k in GO_KEYS if k not in fields]
    if missing:
        out.append(f"{GATE_DIR}/publish-go: missing {missing}")
    if "server.json sha256" in fields and fields["server.json sha256"] != sha:
        out.append(f"{GATE_DIR}/publish-go names {fields['server.json sha256']}, not this entry ({sha})")
    if "version" in fields and fields["version"] != version:
        out.append(f"{GATE_DIR}/publish-go names version {fields['version']}, the entry has {version}")
    for k in ("hosted server live since", "every tool connected once by"):
        if k in fields and not DATE.match(fields[k]):
            out.append(f"{GATE_DIR}/publish-go: {k}: a date, YYYY-MM-DD")
    return out


def publisher_pin(root):
    """(the line naming the pinned mcp-publisher, problems), from the registry job's env in the publish workflow."""
    path = os.path.join(root, WORKFLOW)
    found = {}
    if os.path.isfile(path):
        for key, value in PIN.findall(open(path, encoding="utf-8").read()):
            found.setdefault(key, []).append(value)
    v, s, d = (found.get(k, [""]) for k in ("VERSION", "SHA256", "RELEASED"))
    problems = []
    if len(v) != 1 or not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", v[0]):
        problems.append(f"{WORKFLOW}: MCP_PUBLISHER_VERSION, once, a plain version")
    if len(s) != 1 or not re.fullmatch(r"[0-9a-f]{64}", s[0]):
        problems.append(f"{WORKFLOW}: MCP_PUBLISHER_SHA256, once, 64 hex digits")
    if len(d) != 1 or not DATE.match(d[0]):
        problems.append(f"{WORKFLOW}: MCP_PUBLISHER_RELEASED, once, YYYY-MM-DD")
    return f"mcp-publisher {v[0] or '?'}, released {d[0] or '?'}, archive sha256 {s[0] or '?'}", problems


def decide(root):
    """(go, sha256, lines to print). Raises Refused for a red run."""
    sha, version, problems = entry_state(root)
    pin, pin_problems = publisher_pin(root)
    go = os.path.join(root, GATE_DIR, "publish-go")
    if not os.path.isfile(go):
        notes = [f"NOTE: {p}" for p in problems + pin_problems]
        return False, sha, notes + [f"no go from the lead ({GATE_DIR}/publish-go): nothing is published; {pin}"]
    problems += go_problems(go, sha, version) + pin_problems
    if problems:
        raise Refused("\n".join(problems))
    return True, sha, [f"go: version {version}, the approved bytes, named by the lead's go; {pin}"]


def main(argv):
    root, out, require = ".", None, False
    args = list(argv)
    while args:
        a = args.pop(0)
        if a == "--root" and args:
            root = args.pop(0)
        elif a == "--github-output" and args:
            out = args.pop(0)
        elif a == "--require-go":
            require = True
        else:
            print(__doc__)
            return 2
    try:
        go, sha, lines = decide(root)
    except Refused as e:
        print(f"REFUSED: {e}")
        return 1
    print(f"{ENTRY} sha256 {sha}")
    print("\n".join(lines))
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(f"go={'true' if go else 'false'}\nsha256={sha or ''}\n")
    if require and not go:
        print("REFUSED: this job publishes only with the approval and the lead's go in place")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
