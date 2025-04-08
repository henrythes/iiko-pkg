# Contributing to iiko-pkg

Thank you for considering contributing to iiko-pkg! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project.

## How to Contribute

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes
4. Run tests to ensure your changes don't break existing functionality
5. Submit a pull request

## Development Setup

1. Clone the repository
2. Create a virtual environment
3. Install development dependencies

```bash
git clone https://github.com/yourusername/iiko-pkg.git
cd iiko-pkg
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Running Tests

```bash
python run_tests.py
```

Or using tox:

```bash
tox
```

## Code Style

This project uses:
- Black for code formatting
- isort for import sorting
- flake8 for linting
- mypy for type checking

You can run all of these with:

```bash
tox -e lint
tox -e type
```

## Pull Request Process

1. Ensure your code follows the style guidelines
2. Update the README.md with details of changes if appropriate
3. Update the examples if appropriate
4. The pull request will be merged once it has been reviewed and approved

## Adding New Features

If you're adding a new feature, please also add:
1. Tests for the feature
2. Documentation for the feature
3. Example usage in the examples directory

## Reporting Bugs

Please report bugs by opening an issue on the GitHub repository. Include:
1. A clear description of the bug
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Environment information (OS, Python version, iiko-pkg version)

## Feature Requests

Feature requests are welcome. Please open an issue on the GitHub repository and describe the feature you'd like to see, why you need it, and how it should work.

## Questions

If you have any questions, please open an issue on the GitHub repository.
