"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import numpy as np
import molecool
import pytest
import sys

def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules



def test_calculate_angle():
    """Test the calculate_angle function"""

    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])

    expected_value = 90
    calculated_value = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert expected_value == calculated_value



