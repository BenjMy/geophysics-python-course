# Contributing to Geophysics Python Course

Thank you for your interest in contributing! Here's how you can help.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/geophysics-python-course.git`
3. Create a branch: `git checkout -b feature/your-feature-name`

## Development Setup

### Using Poetry
```bash
poetry install
poetry shell
```

### Using Conda
```bash
conda env create -f environment.yml
conda activate geophysics-course
```

## Making Changes

1. Make your changes in your feature branch
2. Add tests if applicable
3. Run tests: `pytest`
4. Format code: `poetry run black src tests`
5. Check linting: `poetry run flake8 src tests`
6. Commit changes: `git commit -m "Description of changes"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Ensure all tests pass
- Follow the existing code style
- Update documentation if needed

## Reporting Issues

Use GitHub Issues to report bugs or suggest features. Include:
- Clear description
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Python version and OS

## Questions?

Open an issue or contact the maintainers.

Thank you for contributing! 🎉
