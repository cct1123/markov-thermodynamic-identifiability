"""Create the self-contained manuscript/research reproduction archive.

Run from repository root after the final build and audits:
    python -B manuscript/scripts/package.py
Inspect the exact file list without writing with --list. The archive preserves
root-relative paths so the documented reproduction commands work after extraction.
This script packages files; it does not compile or certify the manuscript.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[2]
ROOT_FILES = {"AGENTS.md", "ARCHITECTURE.md", "PROJECT.md", "README.md", "STATE.md",
              ".gitattributes", ".gitignore", "reproduce_all.py", "REVISION_NOTES.md"}
TREES = {"analysis", "docs", "evidence", "formal", "knowledge", "manuscript", "outputs"}
SKIP_DIRS = {".git", ".venv", "venv", ".cache", ".browser-qa", "__pycache__", ".pytest_cache",
             ".mypy_cache", ".ruff_cache", ".lake", "node_modules", "tmp", "temp",
             "compiler", "compilers", "qa", "rendered", "page-renders", "build-temp"}
SKIP_SUFFIXES = {".pyc", ".pyo", ".aux", ".log", ".out", ".toc", ".blg", ".fls",
                 ".fdb_latexmk", ".synctex", ".gz", ".dvi", ".xdv", ".exe", ".dll",
                 ".zip", ".tar", ".7z", ".tmp"}
REQUIRED = {
    "PROJECT.md", "analysis/requirements-research.txt",
    "analysis/requirements-lock-py39-windows.txt", "outputs/balanced-fold-checks.json",
    "analysis/publication-endpoint-audit.md", "manuscript/main.tex", "manuscript/main.pdf",
    "manuscript/references.bib", "manuscript/README.md", "manuscript/supplementary/proofs.tex",
    "manuscript/scripts/reproduce.py", "manuscript/scripts/check_table_bounds.py",
    "manuscript/scripts/package.py", "manuscript/supplementary/computational-results.json",
    "manuscript/supplementary/table-bound-checks.json", "manuscript/figures/balanced-fiber.pdf",
    "manuscript/figures/three-state-instability.pdf", "reproduce_all.py", "REVISION_NOTES.md",
    "analysis/revision/inference.py", "analysis/revision/continuation.py",
    "analysis/revision/rare_event.py", "outputs/revision/statistics.json",
    "outputs/revision/continuation.json", "outputs/revision/rare-event.json",
    "analysis/correctness/global_independent.py", "analysis/correctness/laplace_two.py",
    "analysis/correctness/test_laplace_two.py", "analysis/correctness/mechanism.py",
    "manuscript/supplementary/laplace-two.tex", "manuscript/supplementary/compact-priors.tex",
    "manuscript/supplementary/moment-confidence.tex",
    "outputs/correctness-2026-09-15/reproduction.json",
}


def selected_files():
    paths = [ROOT / p for p in ROOT_FILES if (ROOT / p).is_file()]
    for name in TREES:
        for path in (ROOT / name).rglob("*"):
            if not path.is_file() or path.is_symlink():
                continue
            relative = path.relative_to(ROOT)
            if any(part.lower() in SKIP_DIRS for part in relative.parts[:-1]):
                continue
            if path.suffix.lower() in SKIP_SUFFIXES:
                continue
            if path.name.startswith(".env") or path.name.endswith("Notes.bib"):
                continue
            # Vector publication figures are sufficient; omit duplicate raster
            # figure exports and all manuscript page/QA snapshots.
            if relative.parts[0] == "manuscript" and path.suffix.lower() == ".png":
                continue
            if path.suffix.lower() == ".png" and path.name.startswith("atlas-"):
                continue
            if path.name.startswith("~") or path.name.endswith("~"):
                continue
            paths.append(path)
    return sorted(paths, key=lambda p: p.relative_to(ROOT).as_posix())


def byte_hash(data):
    return hashlib.sha256(data).hexdigest()


def write_entry(archive, name, content):
    # Fixed ZIP metadata makes identical input bytes give an identical archive.
    info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    archive.writestr(info, content, compress_type=ZIP_DEFLATED, compresslevel=9)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List archive paths; do not write")
    parser.add_argument("--output", default="outputs/manuscript-package.zip")
    args = parser.parse_args()
    paths = selected_files()
    names = {p.relative_to(ROOT).as_posix() for p in paths}
    missing = sorted(REQUIRED - names)
    if args.list:
        print("\n".join(sorted(names)))
        print(json.dumps({"files": len(paths), "uncompressed_bytes": sum(p.stat().st_size for p in paths),
                          "missing_required_final_files": missing}, indent=2))
        return
    if missing:
        raise SystemExit("Build/finish the package before archiving; missing: " + ", ".join(missing))
    destination = (ROOT / args.output).resolve()
    if not destination.is_relative_to(ROOT) or destination.suffix.lower() != ".zip":
        raise SystemExit("Archive destination must be a .zip inside the repository")
    records = []
    payload = []
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        data = path.read_bytes()
        payload.append((relative, data))
        records.append({"path": relative, "bytes": len(data), "sha256": byte_hash(data)})
    manifest = {"format": "manuscript-reproduction-package-v1", "files": records,
                "preserves_root_relative_paths": True,
                "excluded": "Git metadata, environments, credentials/prompt history, caches, temporary/compiler binaries, auxiliary build files, duplicate manuscript PNG exports and QA page images",
                "reproduction": ["python -m venv .venv", "python -m pip install -r analysis/requirements-research.txt",
                                 "python -B reproduce_all.py"],
                "note": "Use the virtual environment's Python for package installation and reproduction; build instructions are in manuscript/README.md. Proof status is conventional plus exact computational support, not formal verification."}
    manifest_bytes = (json.dumps(manifest, indent=2)+"\n").encode("utf-8")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "w") as archive:
        for name, data in payload:
            write_entry(archive, name, data)
        write_entry(archive, "PACKAGE-MANIFEST.json", manifest_bytes)
    with ZipFile(destination) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == names | {"PACKAGE-MANIFEST.json"}
        for record in records:
            assert byte_hash(archive.read(record["path"])) == record["sha256"]
    print(json.dumps({"archive": str(destination), "file_count_including_manifest": len(records)+1,
                      "archive_bytes": destination.stat().st_size, "sha256": byte_hash(destination.read_bytes()),
                      "integrity_verified": True}, indent=2))


if __name__ == "__main__":
    main()
