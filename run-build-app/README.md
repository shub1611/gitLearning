# Simple Python Package Example

## How to Build and Install

1. **Build the wheel package:**

```bash
cd src
python -m pip install --upgrade build
python -m build
```

2. **Install the package in another app:**

```bash
pip install src/dist/my_simple_lib-0.1.0-py3-none-any.whl
```

3. **Run the example app:**

```bash
python run-build-app/main.py
```

## How to Use in a GitHub Workflow

Add these steps to your workflow:

```yaml
- name: Build wheel
  run: |
    cd src
    python -m pip install --upgrade build
    python -m build

- name: Install wheel
  run: |
    pip install src/dist/my_simple_lib-0.1.0-py3-none-any.whl

- name: Run app
  run: |
    python run-build-app/main.py
```
