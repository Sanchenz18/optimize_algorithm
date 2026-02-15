# LEARN ALGORITHM OF OPTIMIZATION

## Create uv vitrual environment
### Start for a project
```bash
uv venv
.venv/Scripts/activate
```
### Python project configuration
1. Configuration file (pyproject.toml)
```toml
[project]
name = "optimize_algorithm"
version = "0.1"
requires-python = ">=3.13"
dependencies = [
    "numpy>=1.24.0",
    "matplotlib>=3.7.0",
]
```
2. Rebuild dependence
```bash
uv sync
```
3. Run
```bash
uv run python 'example.py'
```
## 

