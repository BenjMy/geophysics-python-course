#!/bin/bash

echo "🚀 Setting up Geophysics Python Course environment..."

# Check if Poetry is installed
if ! command -v poetry &> /dev/null
then
    echo "📦 Poetry not found. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
fi

# Install dependencies
echo "📥 Installing dependencies with Poetry..."
poetry install

echo "✅ Setup complete! Activate the environment with: poetry shell"
echo "📓 Then launch Jupyter with: jupyter lab"
