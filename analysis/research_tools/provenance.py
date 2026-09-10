"""Write small reproducible run manifests without capturing environment secrets."""

from datetime import datetime, timezone
import hashlib
from importlib import metadata
import json
from pathlib import Path
import platform
import subprocess
import sys


def write_manifest(path, *, sources, settings, results, artifacts=(), root=None,
                   kind="computational-run"):
    """Caller lists all local helper/input sources and consequential settings.

    Relative paths resolve against root (default cwd). No automatic evidence
    promotion, stdout scraping, environment-variable capture or scientific IDs.
    """
    root = Path(root or Path.cwd()).resolve()

    def hashes(paths):
        result = {}
        for item in paths:
            p = Path(item)
            p = (root / p).resolve() if not p.is_absolute() else p.resolve()
            result[p.relative_to(root).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
        return result

    versions = {}
    for name in ("numpy", "scipy", "mpmath", "sympy", "networkx", "matplotlib", "z3-solver"):
        try:
            versions[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            versions[name] = None
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, stderr=subprocess.DEVNULL, text=True).strip()
        dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=root, text=True))
    except (OSError, subprocess.CalledProcessError):
        commit, dirty = None, None
    if hasattr(sys, "orig_argv"):
        command, command_note = sys.orig_argv, "original interpreter arguments"
    else:
        spec = getattr(sys.modules.get("__main__"), "__spec__", None)
        command = ([sys.executable, "-m", spec.name] + sys.argv[1:] if spec is not None
                   else [sys.executable] + sys.argv)
        command_note = "replay invocation; Python 3.9 does not retain original interpreter flags"
    report = {"kind": kind, "automatically_promotes_evidence": False,
              "executed_at_utc": datetime.now(timezone.utc).isoformat(),
              "command_argv": command, "command_note": command_note,
              "working_directory": str(root), "python": sys.version,
              "platform": platform.platform(), "packages": versions,
              "git_commit": commit, "git_dirty": dirty,
              "source_sha256": hashes(sources), "artifact_sha256": hashes(artifacts),
              "settings": settings, "results": results}
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return report
