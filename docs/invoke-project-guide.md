# Invoke Project Guide (Folder-Based, Non-Package First)

## Purpose

This guide defines a practical layout and coding standard for an Invoke-driven automation project.

Design goals:
- Keep it simple and function-oriented (Makefile style in Python).
- Start as a normal folder, not a distributable pip package.
- Use dynamic namespace discovery from the tasks directory.
- Avoid unnecessary object-oriented abstractions unless stateful behavior is required.

## Core Decisions

- The Invoke project lives in its own folder.
- It does not need to be a pip library at the start.
- A tasks package is still used (because Python module loading requires it).
- Namespace folder names are domain-driven, not forced to be tools.
- crun is excluded from this layout.

## Recommended Layout

```text
invoke-automation/
  invoke.yaml
  main.py
  tasks/
    __init__.py
    ci/
      build.py
      release.py
    repo/
      branches.py
      pull_requests.py
    artifacts/
      publish.py
```

Notes:
- tasks is the root task package.
- Each folder under tasks becomes a namespace.
- Each Python file under those folders contributes task functions.

Examples:
- tasks/ci/build.py -> inv ci-build.compile-image
- tasks/repo/branches.py -> inv repo-branches.create-stg

(If you prefer dot-style grouping, you can change the label strategy in tasks/__init__.py.)

## Dynamic Namespace Loader (tasks/__init__.py)

Use a dynamic loader so every subfolder/file pair becomes a collection automatically.

```python
import importlib
import os
import sys
from invoke.collection import Collection


def _build_namespace() -> Collection:
    ns = Collection()
    root = os.path.dirname(os.path.abspath(__file__))

    for current_root, _, files in os.walk(root):
        rel = current_root.replace(root + "/", "")
        if current_root == root:
            continue

        for filename in files:
            if not filename.endswith(".py") or filename == "__init__.py":
                continue

            module_name = os.path.splitext(filename)[0]
            folder_name = os.path.basename(current_root)
            import_path = f"{folder_name}.{module_name}"
            namespace_label = f"{folder_name}-{module_name}"

            try:
                module = importlib.import_module(import_path)
            except ModuleNotFoundError:
                print(
                    f"Warning: failed to load task module '{import_path}'",
                    file=sys.stderr,
                )
                continue

            ns.add_collection(Collection.from_module(module), namespace_label)

    return ns


ns = _build_namespace()
```

Why this works:
- Invoke looks for ns (or namespace) in the loaded tasks module.
- Collection.from_module extracts decorated @task functions.
- add_collection attaches each module as a named command namespace.

## Task Authoring Standard

Use function-based tasks first.

```python
from invoke import task


@task
def compile_image(c, tag="latest"):
    c.run(f"echo Building image:{tag}")


@task
def run_tests(c):
    c.run("pytest -q", warn=True)
```

Guidelines:
- Keep tasks thin and composable.
- Move repeated logic into private helpers within the same file or a shared helpers module.
- Prefer explicit arguments over hidden global state.
- Introduce classes only when state and lifecycle management are genuinely needed.

## Naming and CLI Conventions

- Use snake_case for Python function names.
- Assume CLI task names are auto-dashed by Invoke.
- Keep namespace names short and domain-based (ci, repo, artifacts, deploy).
- Avoid generic buckets unless they truly represent a broad utility domain.

Example mapping:
- Python function: create_stg_branch
- CLI command: create-stg-branch

## Configuration (invoke.yaml)

Keep project defaults in invoke.yaml at repo root:

```yaml
run:
  echo: true
  pty: false

tasks:
  auto_dash_names: true
```

Recommendations:
- Put stable defaults here.
- Use environment variables for sensitive values.
- Avoid embedding secrets in invoke.yaml.

## main.py Role

main.py is optional for Invoke itself. Keep it only if you need a Python entry script for local debugging or orchestration outside inv commands.

```python
def main() -> None:
    print("Invoke automation project")


if __name__ == "__main__":
    main()
```

## Python Best Practices for Invoke Projects

- Keep task modules focused by domain.
- Validate external command assumptions (tools installed, paths exist).
- Use warn=True only where non-zero exit is acceptable.
- Fail fast for critical steps.
- Keep shell strings readable and deterministic.
- Add type hints for task arguments and helper functions.
- Write clear docstrings for non-obvious tasks.
- Prefer standard library first.

## General Engineering Best Practices

- Keep commands idempotent where practical.
- Separate read-only tasks (status, show, list) from mutating tasks (apply, release, delete).
- Provide safe preview tasks when destructive behavior is possible.
- Keep task outputs concise and actionable.
- Use consistent naming and folder taxonomy.
- Add a short README section listing the most-used inv commands.

## Testing Strategy

Suggested levels:
- Smoke tests: run core commands in a disposable environment.
- Unit tests: test helper functions without shell execution.
- Contract checks: verify expected command strings for critical flows.

For shell-heavy logic, isolate command construction in pure helper functions so they are testable.

## Migration Path to Package Later

You can convert later if needed for reuse across repos.

Potential trigger points:
- Multiple repositories need the same task library.
- You want versioned distribution.
- You need plugin-like extension points.

Until then, folder-first keeps friction low and iteration speed high.

## Summary

This layout keeps Invoke simple, dynamic, and scalable:
- folder-based project
- dynamic namespace discovery
- domain-based subfolders
- function-first tasks
- config in invoke.yaml
- no crun dependency
