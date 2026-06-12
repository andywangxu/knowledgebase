# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains an Android Framework knowledge base scaffold plus `llm-wiki.html`, a self-contained Chinese reference page for the LLM-Wiki personal knowledge base workflow.

The file includes:

- Inline CSS in the `<style>` block.
- Static article content in the `<body>`.
- No external JavaScript, CSS, assets, package manifest, or build system.

There is no top-level README, package manager config, test framework, Cursor rules, or Copilot instructions in this repository; `inbox/README.md` exists for inbox-specific guidance.

## Common Commands

Because this repository currently has no package manifest, build system, or test framework, there are no project-specific build, lint, or test commands.

Useful local commands:

```bash
# Open the document in a browser from the repository root
xdg-open llm-wiki.html

# Serve the directory locally for browser testing
python3 -m http.server 8000
# then open http://localhost:8000/llm-wiki.html
```

## Architecture and Structure

`llm-wiki.html` is organized as a single-page article:

- `<head>` defines metadata and all presentation styles.
- CSS custom properties under `:root` define the color palette, spacing, and reusable theme values.
- The body is wrapped in `.wrapper`, with repeated `.section` blocks for each major chapter.
- Reusable visual components include:
  - `.highlight-block` for emphasized callouts.
  - `.demo-box` for command/output examples.
  - `.compare-box` for before/after or old/new comparisons.
  - `.table-wrapper` and table styles for comparison tables.
  - `.numbered-list`, `.no-bullet-list`, and `.flow-steps` for structured content.
- Responsive behavior is handled by a small media query for screens under 480px.

The document content describes the LLM-Wiki concept and workflow as a reference page, while the repository scaffold now provides starting knowledge-base directories such as `inbox/`, `raw/`, and `wiki/`.

## Editing Guidance

When modifying the page:

- Keep the file self-contained unless the repository is intentionally converted to a multi-file site.
- Preserve the Chinese article structure and section numbering unless the content itself is being reorganized.
- Reuse existing CSS component classes before adding new styles.
- Do not add build/test commands to this file unless corresponding tooling is actually added to the repository.

## Knowledge Base Operating Model

This repository is evolving into an Android Framework knowledge base.

Primary layers:

- `inbox/` — low-friction team submissions; content here is not formal Wiki knowledge yet.
- `raw/` — original files and source material; preserve context and avoid rewriting originals.
- `wiki/scenarios/` — scenario entry pages for common Android Framework work contexts.
- `wiki/assets/` — curated reusable knowledge: troubleshooting, architecture, postmortems, checklists.
- `wiki/materials/` — controlled reference materials: operations docs, vendor docs, project docs, references.
- `wiki/sources/` — structured summaries of original material.
- `wiki/templates/` — templates for creating new assets, materials, and source summaries.

Content rules:

- Do not move rough team submissions directly into `wiki/assets/`.
- Assets must include at least: one-line conclusion, applicability, and source.
- Materials must include searchable metadata in frontmatter.
- Prefer linking to `raw/` or `wiki/sources/` instead of copying large original documents into Wiki pages.
- Keep the first phase small: prioritize high-frequency, high-impact, reusable content.

Useful commands:

```bash
# Search all wiki content
rg "keyword" wiki/

# Find materials
rg "type: material" wiki/

# Find assets
rg "type: asset" wiki/

# Find pages for a module or vendor
rg "Display|VendorName" wiki/
```

## Semi-Automatic LLM-Wiki Enhancement

This repository includes a first-version semi-automatic LLM-Wiki workflow.

Key files:

- `.claude/commands/wiki-triage.md` — Claude command guidance for triaging `inbox/*.md` inputs.
- `wiki/workflows/triage.md` — human-readable triage process and safety boundaries.
- `wiki/reports/triage/` — generated triage reports awaiting human review.
- `wiki/domains/` — technology domain index for Android/System-adjacent and frontier topics.
- `tools/wiki_lint_lite.py` — read-only structure and metadata checks.

Important boundaries:

- `/wiki-triage` supports `inbox/*.md` as the first-version formal input.
- `raw/` remains the original-material directory, but raw files should be summarized into `inbox/*.md` before triage.
- Triage reports are process records, not formal knowledge assets.
- Do not automatically promote triage output into `wiki/assets/`, `wiki/materials/`, `wiki/sources/`, or `wiki/domains/`.
- Do not automatically move `inbox/` or `raw/` files.
- Do not automatically change any page to `status: active`.

Useful commands:

```bash
# Run all lightweight Wiki checks
python3 tools/wiki_lint_lite.py

# Check only triage reports
python3 tools/wiki_lint_lite.py --path wiki/reports/triage

# Run lint tool tests
PYTHONPATH=tools python3 -m unittest tools/test_wiki_lint_lite.py -v
```

## MkDocs Material Wiki UI

This repository can be viewed through a local MkDocs Material browser UI.

Key files:

- `mkdocs.yml` — MkDocs site configuration using `docs_dir: wiki`.
- `requirements.txt` — Python dependencies for the local documentation site.
- `wiki/index.md` — browser-facing knowledge base homepage.
- `wiki/search.md` — browser, AI, and manual search guidance.

Useful commands:

```bash
# Install UI dependencies
pip install -r requirements.txt

# Start the local browser UI
mkdocs serve
# then open http://127.0.0.1:8000

# Build the static site locally
mkdocs build

# Run UI smoke tests
python3 -m unittest tools/test_mkdocs_wiki_ui.py -v
```

Important boundaries:

- The MkDocs UI is read-only.
- Do not move `inbox/` or `raw/` files as part of UI work.
- Do not automatically change any page to `status: active`.
- Do not publish the site externally without reviewing sensitive materials.
- `raw/` and `inbox/` are not part of the MkDocs `docs_dir`; team-facing pages should live under `wiki/`.
