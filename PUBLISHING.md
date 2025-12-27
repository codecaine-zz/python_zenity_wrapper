# Building and Publishing Guide

## Building the Package

### 1. Install Build Tools

```bash
pip3 install --upgrade build twine
```

### 2. Build the Package

```bash
# Build both source distribution and wheel
python3 -m build

# This creates:
# - dist/python-zenity-wrapper-0.1.0.tar.gz (source distribution)
# - dist/python_zenity_wrapper-0.1.0-py3-none-any.whl (wheel)
```

### 3. Test the Package Locally

```bash
# Install in development mode
pip3 install -e .

# Or install from the built wheel
pip3 install dist/python_zenity_wrapper-0.1.0-py3-none-any.whl

# Test import
python3 -c "from zenity_wrapper import Zenity; print('Success!')"
```

## Publishing to PyPI

### 1. Create PyPI Account

- Go to https://pypi.org/account/register/
- Verify your email address
- Set up 2FA (required for publishing)

### 2. Create API Token

- Go to https://pypi.org/manage/account/token/
- Create a new API token with appropriate scope
- Save the token securely (you'll need it only once)

### 3. Configure Authentication

```bash
# Option 1: Using environment variables
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=<your-api-token>

# Option 2: Create ~/.pypirc file
cat > ~/.pypirc <<EOF
[pypi]
username = __token__
password = <your-api-token>
EOF
chmod 600 ~/.pypirc
```

### 4. Upload to PyPI

```bash
# Check the package first
twine check dist/*

# Upload to Test PyPI first (recommended)
twine upload --repository testpypi dist/*

# Test installation from Test PyPI
pip3 install --index-url https://test.pypi.org/simple/ python-zenity-wrapper

# If everything works, upload to production PyPI
twine upload dist/*
```

## Version Management

When releasing a new version:

1. Update version in `setup.py` (line 13)
2. Update version in `pyproject.toml` (line 6)
3. Update version in `__init__.py` (line 24)
4. Create a git tag:
   ```bash
   git tag -a v0.1.0 -m "Release version 0.1.0"
   git push origin v0.1.0
   ```
5. Rebuild and republish:
   ```bash
   rm -rf dist/ build/ *.egg-info
   python3 -m build
   twine upload dist/*
   ```

## Cleanup

```bash
# Remove build artifacts
rm -rf build/ dist/ *.egg-info __pycache__

# Remove installed development package
pip3 uninstall python-zenity-wrapper
```

## Quick Commands Reference

```bash
# Development workflow
pip3 install -e .                    # Install in editable mode
python3 demo.py                      # Run demo

# Build and test
python3 -m build                     # Build package
twine check dist/*                   # Validate package
pip3 install dist/*.whl              # Test installation

# Publish
twine upload --repository testpypi dist/*  # Test upload
twine upload dist/*                        # Production upload
```
