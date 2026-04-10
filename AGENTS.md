# Repository Agent Instructions

After making any coding changes in this repository, run the following checks in order:

1. `uv run ruff format`
2. `uv run ruff check .`
3. `uv run ty check`
4. `uv run pytest -q`

If any command fails, report the failure and fix it before considering the task complete.
