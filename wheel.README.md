# 📦 Build Python Wheel Action (Flexible)

A GitHub Action to **build Python wheel packages** flexibly using different build systems like `setuptools`, `poetry`, `flit`, or `build`. Supports custom build commands, optional testing, and linting.

---

## 🔧 Features

- 🧩 Supports all major Python build tools
- ⚙️ Auto-detects `setup.cfg`, `setup.py`, or `pyproject.toml`
- ✅ Optional linting (`black`) and testing (`pytest`)
- 🎛️ Custom build command override
- 📤 Uploads the built `.whl` file as an artifact

---

## 📁 Supported Build Systems

| Build System | Config Files                  | Build Command                   |
|--------------|-------------------------------|----------------------------------|
| `setuptools` | `setup.py`, `setup.cfg`       | `python -m build` or `python setup.py bdist_wheel` |
| `build`      | `pyproject.toml`, `setup.cfg` | `python -m build`                |
| `poetry`     | `pyproject.toml`              | `poetry build`                   |
| `flit`       | `pyproject.toml`              | `flit build`                     |

---




| Build Tool | Main Config File(s) | Build Command | Install Command | Run Tests Command |
|:--------------:|:------------------------:|:----------------------------|:-----------------------|:----------------------| 
| setuptools | setup.cfg, pyproject.toml | python -m build or python setup.py bdist_wheel | pip install . | pytest |
| poetry | pyproject.toml | poetry build | poetry install | poetry run pytest |
| flit | pyproject.toml | flit build | pip install . or flit install | pytest (if tests present) |
| build (PEP 517)| pyproject.toml, setup.cfg | python -m build | pip install . | pytest |


## 📥 Inputs

| Name             | Description                                      | Default   |
|------------------|--------------------------------------------------|-----------|
| `python-version` | Python version to use                           | `3.10`    |
| `build-backend`  | `build`, `poetry`, `flit`, `setuptools`          | `build`   |
| `build-command`  | Custom shell command to override default build   | *(empty)* |
| `run-tests`      | Run `pytest` tests                               | `true`    |
| `run-lint`       | Run `black` linting                              | `false`   |

---

## 🚀 Example Usage in Workflow

### `.github/workflows/build.yml`

```yaml
name: Build and Package

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - uses: your-org/build-wheel-action@v1
        with:
          python-version: "3.11"
          build-backend: "poetry"
          run-tests: "true"
          run-lint: "true"
```

Or use a custom command:

```yaml
      - uses: your-org/build-wheel-action@v1
        with:
          build-command: "poetry build && cp dist/*.whl my-artifacts/"
```

---

## 📦 Sample Config Files

### `setup.cfg` (for setuptools)

```ini
[metadata]
name = my_package
version = 0.1.0
description = Example setuptools package
author = Your Name
author_email = you@example.com
license = MIT

[options]
packages = find:
install_requires =
    requests
    numpy
python_requires = >=3.7

[options.packages.find]
where = src

[options.extras_require]
testing =
    pytest

[options.entry_points]
console_scripts =
    mycli = my_package.cli:main

[classifiers]
Programming Language :: Python :: 3
License :: OSI Approved :: MIT License
Operating System :: OS Independent
```

### `pyproject.toml` (for setuptools)

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
dependencies = ["requests", "numpy"]
```

### `pyproject.toml` (for poetry)

```toml
[tool.poetry]
name = "my-package"
version = "0.1.0"
description = "A sample Python package"
authors = ["You <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "*"
numpy = "*"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### `pyproject.toml` (for flit)

```toml
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "my_package"
version = "0.1.0"
description = "Example using flit"
dependencies = ["requests", "numpy"]
```

---

## 🧪 Running Build and Tests Locally

### For setuptools:
```bash
pip install build
python -m build
```

To run tests:
```bash
pip install .[testing]
pytest
```

### For poetry:
```bash
poetry install
poetry build
poetry run pytest
```

### For flit:
```bash
pip install flit
flit build
```

---

## 🧪 Output

- A built `.whl` file is saved in `dist/`
- It is uploaded as a GitHub artifact named `built-wheel`

---

## 🧠 Best Practices

- Keep `pyproject.toml` or `setup.cfg` in project root
- Validate with `python -m build` locally before using in CI
- Use `build` for most flexible modern packaging
- Use `poetry` or `flit` for isolated builds and dependency management

---

## 🧩 Contributing

Feel free to fork, improve, or open issues. Contributions welcome! 😊
