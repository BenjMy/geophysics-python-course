# Troubleshooting Guide

## Common Issues

### Poetry Installation Issues

**Problem**: `poetry: command not found`

**Solution**:
```bash
export PATH="$HOME/.local/bin:$PATH"
# Add to ~/.bashrc or ~/.zshrc for permanent fix
```

### Conda Environment Issues

**Problem**: Environment not activating

**Solution**:
```bash
conda init bash  # or zsh, fish, etc.
# Restart terminal
conda activate geophysics-course
```

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'resipy'`

**Solution**:
```bash
# Using Poetry
poetry install

# Using Conda
conda env update -f environment.yml

# Using pip
pip install -r requirements.txt
```

### Jupyter Kernel Issues

**Problem**: Kernel not found

**Solution**:
```bash
# Poetry
poetry run python -m ipykernel install --user --name=geophysics-course

# Conda
python -m ipykernel install --user --name=geophysics-course
```

### Performance Issues

**Problem**: Slow inversion

**Solution**:
- Reduce mesh resolution
- Use parallel processing
- Check RAM usage

## Getting Help

1. Check existing [GitHub Issues](https://github.com/yourusername/geophysics-python-course/issues)
2. Search course documentation
3. Open a new issue with:
   - Python version
   - Operating system
   - Error messages
   - Steps to reproduce
