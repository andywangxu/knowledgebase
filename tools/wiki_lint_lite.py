#!/usr/bin/env python3
"""Lightweight read-only checks for the Markdown knowledge base."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


CORE_DIRS = [
    Path("inbox"),
    Path("raw"),
    Path("wiki"),
    Path("wiki/assets"),
    Path("wiki/materials"),
    Path("wiki/sources"),
    Path("wiki/templates"),
    Path("wiki/scenarios"),
    Path("wiki/reports/triage"),
    Path("wiki/domains"),
]

FRONTMATTER_ROOTS = [
    Path("wiki/assets"),
    Path("wiki/materials"),
    Path("wiki/sources"),
    Path("wiki/scenarios"),
    Path("wiki/reports/triage"),
    Path("wiki/domains"),
]

INDEX_PAGES_WITHOUT_FRONTMATTER = {
    Path("wiki/index.md"),
    Path("wiki/search.md"),
    Path("wiki/principles.md"),
    Path("wiki/tags.md"),
    Path("wiki/modules.md"),
    Path("wiki/projects.md"),
    Path("wiki/vendors.md"),
    Path("wiki/assets/index.md"),
    Path("wiki/assets/troubleshooting/index.md"),
    Path("wiki/assets/architecture/index.md"),
    Path("wiki/assets/postmortems/index.md"),
    Path("wiki/assets/checklists/index.md"),
    Path("wiki/materials/index.md"),
    Path("wiki/materials/operations/index.md"),
    Path("wiki/materials/vendor-docs/index.md"),
    Path("wiki/materials/project-docs/index.md"),
    Path("wiki/materials/references/index.md"),
    Path("wiki/sources/index.md"),
    Path("wiki/domains/index.md"),
    Path("wiki/reports/index.md"),
    Path("wiki/reports/triage/index.md"),
}

ALLOWED_TYPES = {
    "asset",
    "material",
    "source",
    "scenario",
    "triage-report",
    "domain",
}

ALLOWED_STATUS = {
    "draft",
    "active",
    "pending-review",
    "accepted",
    "rejected",
    "parked",
    "watching",
    "needs-followup",
    "archived",
}

REQUIRED_FIELDS = {
    "asset": ["type", "schema_version", "asset_type", "status", "domains", "keywords", "sources"],
    "material": ["type", "schema_version", "status", "domains", "keywords", "source"],
    "source": ["type", "schema_version", "status", "source_type", "domains", "keywords", "original"],
    "scenario": ["type", "status", "modules", "keywords"],
    "triage-report": [
        "type",
        "schema_version",
        "status",
        "source_path",
        "created",
        "domains",
        "recommended_actions",
        "confidence",
    ],
    "domain": ["type", "schema_version", "status", "domain_status", "domains", "keywords"],
}

LINK_RE = re.compile(r"(?<!!)(?:\[[^\]]+\])\(([^)]+)\)")
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
UNFINISHED_MARKERS = [
    "T" + "BD",
    "TO" + "DO",
    "待" + "定",
    "PLACE" + "HOLDER",
    "FIX" + "ME",
    "待" + "补充",
    "未" + "完成",
]


@dataclass
class LintResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    files_checked: int = 0

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_warning(self, message: str, strict: bool) -> None:
        if strict:
            self.errors.append(message)
        else:
            self.warnings.append(message)


def normalize(path: Path) -> Path:
    return Path(path.as_posix())


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def read_text(path: Path, result: LintResult) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        result.add_error(f"{path}: file is not UTF-8 text")
    except OSError as exc:
        result.add_error(f"{path}: cannot read file: {exc}")
    return None


def parse_frontmatter(path: Path, text: str, result: LintResult) -> dict[str, object] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        result.add_error(f"{path}: malformed frontmatter")
        return {}

    data: dict[str, object] = {}
    for raw_line in lines[1:end_index]:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            result.add_error(f"{path}: malformed frontmatter line `{raw_line}`")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = parse_value(value.strip())
    return data


def parse_value(value: str) -> object:
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip('"\'') for item in inner.split(",") if item.strip()]
    return value.strip('"\'')


def should_require_frontmatter(path: Path) -> bool:
    path = normalize(path)
    if path in INDEX_PAGES_WITHOUT_FRONTMATTER:
        return False
    return any(is_relative_to(path, root) for root in FRONTMATTER_ROOTS)


def iter_markdown_files(paths: Iterable[Path] | None) -> list[Path]:
    if paths:
        roots = [Path(path) for path in paths]
    else:
        roots = [Path("wiki"), Path("inbox"), Path("CLAUDE.md")]

    files: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        if root.is_file() and root.suffix == ".md":
            files.append(root)
        elif root.is_dir():
            files.extend(path for path in root.rglob("*.md") if "raw" not in path.parts)
    return sorted(set(files))


def load_domain_index() -> set[str]:
    domains = set()
    index = Path("wiki/domains/index.md")
    if not index.exists():
        return domains
    text = index.read_text(encoding="utf-8")
    domains.update(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`", text))
    for page in Path("wiki/domains").glob("*.md"):
        if page.name != "index.md":
            domains.add(page.stem)
    return domains


def check_core_dirs(result: LintResult) -> None:
    for directory in CORE_DIRS:
        if not directory.is_dir():
            result.add_error(f"{directory}: required directory is missing")


def check_frontmatter(path: Path, data: dict[str, object] | None, result: LintResult, strict: bool) -> None:
    if data is None:
        if should_require_frontmatter(path):
            result.add_error(f"{path}: missing frontmatter")
        return

    page_type = data.get("type")
    if isinstance(page_type, str):
        if page_type not in ALLOWED_TYPES:
            result.add_warning(f"{path}: unknown type `{page_type}`", strict)
    elif should_require_frontmatter(path):
        result.add_warning(f"{path}: missing field `type`", strict)
        return
    else:
        return

    status = data.get("status")
    if isinstance(status, str) and status and status not in ALLOWED_STATUS:
        result.add_warning(f"{path}: unknown status `{status}`", strict)

    required = REQUIRED_FIELDS.get(page_type, []) if isinstance(page_type, str) else []
    for field_name in required:
        if field_name not in data:
            result.add_warning(f"{path}: missing suggested field `{field_name}`", strict)


def check_unfinished_markers(path: Path, text: str, data: dict[str, object] | None, result: LintResult, strict: bool) -> None:
    active = data is not None and data.get("status") == "active"
    for marker in UNFINISHED_MARKERS:
        if marker in text:
            message = f"{path}: contains unfinished marker `{marker}`"
            if active:
                result.add_error(message)
            else:
                result.add_warning(message, strict)


def check_links(path: Path, text: str, result: LintResult) -> None:
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean_target = target.split("#", 1)[0]
        if not clean_target:
            continue
        target_path = (path.parent / clean_target).resolve()
        if not target_path.exists():
            result.add_error(f"{path}: broken link `{target}`")


def check_filename(path: Path, data: dict[str, object] | None, result: LintResult, strict: bool) -> None:
    if data is None:
        return
    if path.name == "index.md":
        return
    checked_roots = [Path("wiki/assets"), Path("wiki/materials"), Path("wiki/sources"), Path("wiki/domains"), Path("wiki/reports/triage")]
    if any(is_relative_to(path, root) for root in checked_roots) and not KEBAB_RE.match(path.name):
        result.add_warning(f"{path}: filename is not kebab-case", strict)


def check_domains(path: Path, data: dict[str, object] | None, known_domains: set[str], result: LintResult, strict: bool) -> None:
    if data is None:
        return
    domains = data.get("domains")
    if not isinstance(domains, list):
        return
    for domain in domains:
        if not isinstance(domain, str) or not domain:
            continue
        domain_page = Path("wiki/domains") / f"{domain}.md"
        if domain not in known_domains and not domain_page.exists():
            result.add_warning(f"{path}: domain `{domain}` is referenced but not listed in domains index", strict)


def run_lint(paths: list[Path] | None = None, strict: bool = False) -> LintResult:
    result = LintResult()
    if paths is None:
        check_core_dirs(result)

    known_domains = load_domain_index()
    for path in iter_markdown_files(paths):
        result.files_checked += 1
        text = read_text(path, result)
        if text is None:
            continue
        data = parse_frontmatter(path, text, result)
        check_frontmatter(path, data, result, strict)
        check_unfinished_markers(path, text, data, result, strict)
        check_links(path, text, result)
        check_filename(path, data, result, strict)
        check_domains(path, data, known_domains, result, strict)
    return result


def print_result(result: LintResult) -> None:
    print("Wiki lint lite report")
    print()
    print("Errors:")
    if result.errors:
        for error in result.errors:
            print(f"- {error}")
    else:
        print("- none")
    print()
    print("Warnings:")
    if result.warnings:
        for warning in result.warnings:
            print(f"- {warning}")
    else:
        print("- none")
    print()
    print("Summary:")
    print(f"- files checked: {result.files_checked}")
    print(f"- errors: {len(result.errors)}")
    print(f"- warnings: {len(result.warnings)}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run lightweight Wiki structure checks.")
    parser.add_argument("--path", action="append", type=Path, help="Limit checks to a file or directory. Can be used multiple times.")
    parser.add_argument("--strict", action="store_true", help="Promote warnings to errors.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    result = run_lint(paths=args.path, strict=args.strict)
    print_result(result)
    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
