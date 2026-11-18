#!/usr/bin/env python3
"""Tests for mcp-registry-gate.py and the publish workflow's two MCP Registry jobs. Nothing is sent anywhere.

    python3 -I .github/scripts/mcp-registry-gate_test.py
"""
import hashlib
import importlib.util
import json
import os
import re
import shutil
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
spec = importlib.util.spec_from_file_location("gate", os.path.join(HERE, "mcp-registry-gate.py"))
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

fails = []


def check(ok, what):
    print(("ok   " if ok else "FAIL ") + what)
    if not ok:
        fails.append(what)


def tree(entry=None, approval="same", go=None, workflow=None):
    """A copy of this repository's entry and gate files in a fresh folder, with changes: entry (bytes), approval
    ("same", None for no file, or a text), go (None for no file, or a text with {sha} and {version})."""
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "go", "mcp"))
    os.makedirs(os.path.join(d, "mcp-registry"))
    raw = entry if entry is not None else open(os.path.join(ROOT, "go", "mcp", "server.json"), "rb").read()
    with open(os.path.join(d, "go", "mcp", "server.json"), "wb") as f:
        f.write(raw)
    os.makedirs(os.path.join(d, ".github", "workflows"))
    if workflow is None:
        shutil.copy(os.path.join(ROOT, ".github", "workflows", "publish.yml"), os.path.join(d, ".github", "workflows", "publish.yml"))
    else:
        with open(os.path.join(d, ".github", "workflows", "publish.yml"), "w") as f:
            f.write(workflow)
    if approval == "same":
        shutil.copy(os.path.join(ROOT, "mcp-registry", "approved.sha256"), os.path.join(d, "mcp-registry", "approved.sha256"))
    elif approval is not None:
        with open(os.path.join(d, "mcp-registry", "approved.sha256"), "w") as f:
            f.write(approval)
    if go is not None:
        sha = hashlib.sha256(raw).hexdigest()
        try:
            version = json.loads(raw)["version"]
        except Exception:
            version = "?"
        with open(os.path.join(d, "mcp-registry", "publish-go"), "w") as f:
            f.write(go.format(sha=sha, version=version))
    return d


def run(d, *args):
    out = os.path.join(d, "out")
    rc = gate.main(["--root", d, "--github-output", out, *args])
    got = open(out).read() if os.path.exists(out) else ""
    return rc, got


GOOD_GO = "# the lead's go\nversion: {version}\nserver.json sha256: {sha}\nhosted server live since: 2026-11-18\nevery tool connected once by: 2026-11-19\n"
entry = open(os.path.join(ROOT, "go", "mcp", "server.json"), "rb").read()
doc = json.loads(entry)


def changed(change):
    d = json.loads(entry)
    change(d)
    return (json.dumps(d, indent=2) + "\n").encode()


# The repository as committed: the entry passes the rules, the owner's approval names its bytes, no go yet.
check(gate.entry_problems(entry) == [], f"the committed go/mcp/server.json passes the rules: {gate.entry_problems(entry)}")
check(doc["remotes"] == [{"type": "streamable-http", "url": gate.URL}] and doc["name"] == gate.NAME,
      "the committed entry names our name and the one hosted address")
check(len(doc["description"]) <= 100, f"the committed description is at most 100 characters ({len(doc['description'])})")
check(not os.path.exists(os.path.join(ROOT, "mcp-registry", "publish-go")), "no go is committed with the job: it is the lead's, at publish time")
check(gate.entry_state(ROOT)[2] == [], f"the committed entry is the bytes the owner approved: {gate.entry_state(ROOT)[2]}")
rc, got = run(tree())
check(rc == 0 and "go=false" in got and f"sha256={hashlib.sha256(entry).hexdigest()}" in got,
      f"today: approved, no go: go=false, exit 0 ({rc}, {got!r})")
check(gate.main(["--root", tree(), "--require-go"]) == 1, "today with --require-go: refused")

rc, got = run(tree(go=GOOD_GO))
check(rc == 0 and "go=true" in got, f"with the approval and a go naming these bytes: go=true ({rc}, {got!r})")
check(gate.main(["--root", tree(go=GOOD_GO), "--require-go"]) == 0, "and --require-go passes")

# Beside its go the gate prints the mcp-publisher the registry job runs, with its release date, from that job's env.
wf_text = open(os.path.join(ROOT, ".github", "workflows", "publish.yml")).read()
go_line = gate.decide(tree(go=GOOD_GO))[2][-1]
check("mcp-publisher 1.8.7, released 2026-10-30, archive sha256 00b21004149a4ce66f0782508ae4a2bce67d1bea395a8da0bd8028159fb59579" in go_line,
      f"the go names mcp-publisher 1.8.7 and its release date 2026-10-30: {go_line!r}")
check("released 2026-10-30" in gate.decide(tree())[2][-1], "the no-go line names it too")
for what, wf in [
    ("no release date", re.sub(r'\n\s+MCP_PUBLISHER_RELEASED:.*', "", wf_text)),
    ("a release date that is not a date", wf_text.replace('MCP_PUBLISHER_RELEASED: "2026-10-30"', 'MCP_PUBLISHER_RELEASED: "late October"')),
    ("a second version line", wf_text.replace('MCP_PUBLISHER_VERSION: "1.8.7"', 'MCP_PUBLISHER_VERSION: "1.8.7"\n      MCP_PUBLISHER_VERSION: "1.8.9"')),
    ("no checksum", re.sub(r'\n\s+MCP_PUBLISHER_SHA256:.*', "", wf_text)),
]:
    check(run(tree(go=GOOD_GO, workflow=wf))[0] == 1, f"a go with {what} in the publisher's pin: refused")
    check(run(tree(workflow=wf))[0] == 0, f"no go with {what} in the pin: go=false, a NOTE only")

# The words changed after the yes: one character of the description. Without a go it is a NOTE (nothing is sent);
# with a go, even one naming the new bytes, a red run.
one = entry.replace(b"rollouts.", b"rollouts!")
check(one != entry, "the test's changed entry differs from the committed one")
rc, got = run(tree(entry=one))
check(rc == 0 and "go=false" in got, "one character changed after the yes, no go: go=false, nothing sent")
check(run(tree(entry=one, go=GOOD_GO))[0] == 1, "one character changed after the yes, with a go naming the new bytes: refused")
check(run(tree(entry=entry + b" ", go=GOOD_GO))[0] == 1, "a byte added after the final newline, with a go: refused")
check(run(tree(entry=entry.replace(b"https://studio.survivalservers.com/mcp", b"https://mcp.example.com/mcp"), go=GOOD_GO))[0] == 1,
      "the stand-in address back (a copy from before the rename), with a go: refused")

rc, got = run(tree(approval=None))
check(rc == 0 and "go=false" in got, "no approval file, no go: go=false, exit 0 (the release goes on, nothing is sent)")
check(run(tree(approval=None, go=GOOD_GO))[0] == 1, "a go without the owner's approval: refused")
check(run(tree(approval="# x\n" + "0" * 64 + "  go/mcp/server.json\n", go=GOOD_GO))[0] == 1, "an approval of other bytes, with a go: refused")
two = hashlib.sha256(entry).hexdigest() + "  go/mcp/server.json\n"
check(run(tree(approval=two + two, go=GOOD_GO))[0] == 1, "an approval file with two lines, with a go: refused")
check(run(tree(approval=hashlib.sha256(entry).hexdigest() + " go/mcp/server.json\n", go=GOOD_GO))[0] == 1,
      "an approval line not in sha256sum's form, with a go: refused")
check(run(tree(approval=hashlib.sha256(entry).hexdigest() + "  mcp/server.json\n", go=GOOD_GO))[0] == 1,
      "an approval naming another file, with a go: refused")

for what, go in [
    ("names other bytes", GOOD_GO.replace("{sha}", "1" * 64)),
    ("names another version", GOOD_GO.replace("{version}", "9.9.9")),
    ("misses the line that every tool has connected", GOOD_GO.replace("every tool connected once by: 2026-11-19\n", "")),
    ("misses the line that the hosted server is live", GOOD_GO.replace("hosted server live since: 2026-11-18\n", "")),
    ("has a line that is not a date", GOOD_GO.replace("2026-11-19", "soon")),
    ("has a line it does not know", GOOD_GO + "publish anyway: yes\n"),
    ("names a key twice", GOOD_GO + "version: {version}\n"),
]:
    rc, _ = run(tree(go=go))
    check(rc == 1, f"a go that {what}: refused")

# The entry's rules.
for what, bad in [
    ("two remotes", changed(lambda d: d["remotes"].append({"type": "streamable-http", "url": "https://x.example.org/mcp"}))),
    ("a header on the remote", changed(lambda d: d["remotes"][0].update({"headers": [{"name": "Authorization"}]}))),
    ("another address", changed(lambda d: d["remotes"][0].update({"url": "https://mcp.example.com/mcp"}))),
    ("packages", changed(lambda d: d.update({"packages": []}))),
    ("another name", changed(lambda d: d.update({"name": "io.github.someone/survival-servers"}))),
    ("a description of 101 characters", changed(lambda d: d.update({"description": "x" * 101}))),
    ("a description on two lines", changed(lambda d: d.update({"description": "a\nb"}))),
    ("a version range", changed(lambda d: d.update({"version": "^0.1.1"}))),
    ("another schema", changed(lambda d: d.update({"$schema": "https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json"}))),
    ("another repository", changed(lambda d: d.update({"repository": {"url": "https://github.com/x/y", "source": "github"}}))),
]:
    check(gate.entry_problems(bad) != [], f"the rules refuse {what}")
twice = entry.replace(b'  "title"', b'  "name": "io.github.survivalservers/other",\n  "title"', 1)
check(gate.entry_problems(twice) != [], "the rules refuse a key written twice")
check(gate.entry_problems(entry.rstrip(b"\n")) != [], "the rules refuse an entry with no final newline")
check(gate.entry_problems(b"\xff" + entry) != [], "the rules refuse bytes that are not UTF-8")

# The words live in one file: nothing else in the repository repeats the description.
words = doc["description"]
elsewhere = []
for base, dirs, names in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in (".git", "node_modules", "dist", "target")]
    for n in names:
        p = os.path.join(base, n)
        if os.path.relpath(p, ROOT) == os.path.join("go", "mcp", "server.json"):
            continue
        try:
            if words in open(p, encoding="utf-8", errors="ignore").read():
                elsewhere.append(os.path.relpath(p, ROOT))
        except OSError:
            pass
check(elsewhere == [], f"the description is written only in go/mcp/server.json: {elsewhere}")

# The workflow, against Survival Servers Security's terms for this job.
wf = yaml.safe_load(open(os.path.join(ROOT, ".github", "workflows", "publish.yml")))
on = wf.get("on", wf.get(True))
check(on == {"push": {"tags": ["v*"]}}, f"the workflow runs only on a pushed v* tag: {on}")
check(wf.get("permissions") == {}, "the workflow gives nothing by default")
jobs = wf["jobs"]
g, p = jobs.get("mcp-registry-gate", {}), jobs.get("mcp-registry", {})
check(g.get("permissions") == {"contents": "read"}, f"the gate job: contents: read only ({g.get('permissions')})")
check("environment" not in g, "the gate job waits for no approval and holds no publishing identity")
check(p.get("permissions") == {"contents": "read", "id-token": "write"}, f"the registry job: id-token: write and contents: read, nothing else ({p.get('permissions')})")
others = [n for n, j in jobs.items() if n not in ("pypi", "npm", "mcp-registry") and "id-token" in (j.get("permissions") or {})]
check(others == [], f"no other job gained the id-token: {others}")
check(p.get("needs") == ["check", "mcp-registry-gate"] and "needs.mcp-registry-gate.outputs.go == 'true'" in p.get("if", ""),
      "the registry job runs only after the check job and only when the gate says go")
check("startsWith(github.ref, 'refs/tags/v')" in p.get("if", "") and "github.ref_type == 'tag'" in p.get("if", ""),
      "the registry job runs only for a v tag")
check(g.get("needs") == "check", "the gate runs after the check job (the tag is on main, the actions allowed)")
check((p.get("environment") or {}).get("name") == "publish", "the registry job waits in the publish environment for its reviewer")
check(p.get("runs-on") == "ubuntu-24.04" and g.get("runs-on") == "ubuntu-24.04", "both run on GitHub's hosted runner")
steps = p.get("steps") or []
runs = "\n".join(s.get("run", "") for s in steps)
for want in ['git merge-base --is-ancestor "$GITHUB_SHA" origin/main', "mcp-registry-gate.py --require-go",
             'login github-oidc', 'publish server.json', 'sha256sum -c --strict', "oauth-protected-resource"]:
    check(want in runs, f"the registry job's steps hold: {want}")
check(runs.index("mcp-registry-gate.py --require-go") < runs.index("login github-oidc") < runs.rindex("--require-go") < runs.index("publish server.json"),
      "the gate is read again after the sign-in, right before the publish")
gsteps = "\n".join(s.get("run", "") for s in g.get("steps") or [])
check('git merge-base --is-ancestor "$GITHUB_SHA" origin/main' in gsteps and "--github-output" in gsteps, "the gate job checks the tag is on main and writes its answer")
envs = p.get("env") or {}
check(envs.get("MCP_PUBLISHER_VERSION") == "1.8.7" and envs.get("MCP_PUBLISHER_SHA256") == "00b21004149a4ce66f0782508ae4a2bce67d1bea395a8da0bd8028159fb59579"
      and envs.get("MCP_PUBLISHER_RELEASED") == "2026-10-30", "the registry job pins mcp-publisher 1.8.7, its archive's SHA-256 and its release date (Security's YH)")
check(re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", str(envs.get("MCP_PUBLISHER_VERSION", ""))) is not None, "mcp-publisher is pinned to one version")
check(re.fullmatch(r"[0-9a-f]{64}", str(envs.get("MCP_PUBLISHER_SHA256", ""))) is not None, "and to one SHA-256")
check("cd go/mcp" in runs and "--root ../.. --require-go" in runs and "go/mcp/server.json" in runs,
      "the job validates and publishes the entry file itself, from its own folder")
check("releases/download/v${MCP_PUBLISHER_VERSION}/mcp-publisher_linux_amd64.tar.gz" in runs and "latest" not in runs,
      "it is fetched by that version, never 'latest'")
uses = [s["uses"] for j in (g, p) for s in j.get("steps") or [] if "uses" in s]
check(uses and all(re.fullmatch(r"[\w.-]+/[\w.-]+@[0-9a-f]{40}", u) for u in uses), f"every action of both jobs is pinned by commit: {uses}")
check(all(s.get("with", {}).get("persist-credentials") is False for j in (g, p) for s in j.get("steps") or [] if "uses" in s),
      "no checkout keeps a token")
check("secrets." not in open(os.path.join(ROOT, ".github", "workflows", "publish.yml")).read(), "the workflow names no secret")

if fails:
    print(f"FAIL: {len(fails)}")
    sys.exit(1)
print("mcp-registry-gate_test: passed")
