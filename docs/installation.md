# Installation Guide

## System Requirements

- Python 3.9 or higher
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space

## Installation Methods

### Method 1: Poetry (Recommended)

Poetry is a modern dependency management tool for Python.

1. **Install Poetry**:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone and Install**:
   ```bash
   git clone https://github.com/yourusername/geophysics-python-course.git
   cd geophysics-python-course
   poetry install
   poetry shell
   ```

### Method 2: Conda

1. **Install Conda/Miniconda**:
   - Download from https://docs.conda.io/en/latest/miniconda.html

2. **Create Environment**:
   ```bash
   conda env create -f environment.yml
   conda activate geophysics-course
   ```

### Method 3: pip + venv

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Verifying Installation

```python
import resipy
import emagpy
import numpy as np
import matplotlib.pyplot as plt

print("All packages imported successfully!")
```

## Troubleshooting

See [troubleshooting.md](troubleshooting.md) for common issues.
