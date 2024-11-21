
# Device Management System

A prototype tracking solution for managing smart IoT devices, enabling users to create, pair, modify, and track devices within a living space.


## Installation

To install uv (Unified Python packaging) choose your prefered way based on you OS.

```bash
# On macOS and Linux.
$ curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
$ powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip.
$ pip install uv
```

After installing uv sync the project

```bash
uv sync
```

To run test suite and check coverage

```bash
uv run pytest
uv run pytest --cov
```

To run the driver code

```bash
uv run main.py
```