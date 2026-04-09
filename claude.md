# CLAUDE.md – Global Configuration

**PRIORITY: Be extremely concise in all interactions and commit messages. Sacrifice grammar for concision.**

## General
- Critical trading systems → code must be deterministic
- Most projects run in dev containers
- Explicit > implicit, KISS always

## Architecture
- Organize code in folders early
- Main file at root, minimal (40–60 lines max), high-level ops only
- No other files at root level besides main

## Code

### Naming
- Explicit > implicit always
- Wrong: summarize code behind boilerplate naming
- Correct: name must be self-sufficient to understand code
- Can’t find good name? Function/class doing too much → split it

### Fail Fast
- Validate env vars early (is _not_ none at program start)
- Test connections early (API smoke test like balance check, DB dummy select)
- `else` blocks must always raise, no defaults
- No fallback values for API, env vars
- Use `continue` / `pass` with extreme caution

### Python Specifics
- Full type hints, mypy + ruff compliant
- All imports at top, never nested
- Max 3 nesting levels in functions, 4 in classes
- Always use f-strings
- No default arguments in functions
- Max 5 params per function → split or use model/dataclass
- Prefer composition over inheritance
- Prefer functional for stateless logic (easier testing)
- Models for everything

### Principles
- Single responsibility for classes, functions, modules, models
- No comments (except non-trivial business rules / workarounds that naming alone can’t explain)
- No docs in code

### Logging
- Log once at important app boundaries
- Add context whenever possible
- Avoid duplicate logs
- Don’t log and re-raise exceptions
