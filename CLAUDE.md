# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository currently contains a single static HTML document, `llm-wiki.html`, written in Chinese. It is a self-contained guide for the LLM-Wiki personal knowledge base workflow.

The file includes:

- Inline CSS in the `<style>` block.
- Static article content in the `<body>`.
- No external JavaScript, CSS, assets, package manifest, or build system.

There is no detected README, package manager config, test framework, Cursor rules, or Copilot instructions in this repository.

## Common Commands

Because this is currently a static HTML-only repository, there are no project-specific build, lint, or test commands.

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

The document content describes the LLM-Wiki concept and workflow rather than implementing the workflow itself. The guide references a possible LLM-Wiki project layout (`raw/`, `wiki/`, `graph/`, `tools/`, `data/`, `.claude/commands/`), but those directories are not present in this repository at the time this file was created.

## Editing Guidance

When modifying the page:

- Keep the file self-contained unless the repository is intentionally converted to a multi-file site.
- Preserve the Chinese article structure and section numbering unless the content itself is being reorganized.
- Reuse existing CSS component classes before adding new styles.
- Do not add build/test commands to this file unless corresponding tooling is actually added to the repository.
