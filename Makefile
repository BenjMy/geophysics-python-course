.PHONY: install test lint format clean help notebook

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies using Poetry"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linters"
	@echo "  make format     - Format code with black"
	@echo "  make clean      - Remove generated files"
	@echo "  make notebook   - Launch Jupyter Lab"

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 src tests
	poetry run mypy src

format:
	poetry run black src tests
	poetry run isort src tests

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf dist/ build/ *.egg-info

notebook:
	poetry run jupyter lab
