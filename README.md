# `uv` Python Template

Modern Python project template using [uv](https://docs.astral.sh/uv/) for easy dependency management.

Alternative using `poetry` found [here](https://github.com/idatsy/python-base).

## Features

* `pytest` with `pytest-asyncio` and `pytest-watcher` for TDD
* `loguru` for logging
* `ruff` and `pyright` for linting, formatting, and type checking (with strict defaults!)
* GitHub Actions CI

## Usage

- Clone the repo
- Find/replace `python-base-uv` with your project name
  - Or ask copilot to change all template references as the initial commit!

**Makefile**
- `make sync` to update dependencies.
- `make check` before committing (runs ruff and pyright)
- `make test` to run tests.
- `make watch` for TDD mode (auto-run tests on save).
- `make help` for all commands.

> Prefix files with `wip_` to skip linting.
