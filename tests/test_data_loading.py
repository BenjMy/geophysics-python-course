"""
Tests for data loading functions
"""
import pytest
from src.utils import load_resistivity_data


def test_load_resistivity_data_file_not_found():
    """Test error handling for missing files"""
    with pytest.raises(Exception):
        load_resistivity_data("nonexistent_file.dat")
