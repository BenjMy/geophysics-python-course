"""
Tests for utility functions
"""
import pytest
import numpy as np
from src.utils import calculate_apparent_resistivity


def test_calculate_apparent_resistivity():
    """Test apparent resistivity calculation"""
    voltage = np.array([1.0, 2.0, 3.0])
    current = np.array([0.1, 0.1, 0.1])
    geometry_factor = 2.0
    
    result = calculate_apparent_resistivity(voltage, current, geometry_factor)
    expected = np.array([20.0, 40.0, 60.0])
    
    np.testing.assert_array_almost_equal(result, expected)


def test_calculate_apparent_resistivity_zero_current():
    """Test that division by zero is handled"""
    voltage = np.array([1.0])
    current = np.array([0.0])
    geometry_factor = 2.0
    
    with pytest.warns(RuntimeWarning):
        result = calculate_apparent_resistivity(voltage, current, geometry_factor)
        assert np.isinf(result[0])
