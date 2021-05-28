"""
Tests for the measure module.
"""

import numpy as np
import molecool
import pytest

def test_calculate_distance():
    """Test that calclulate_distance calculates what we expect"""

    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

@pytest.mark.skip
def test_molecular_mass(symbols):
    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

def test_build_bond_list():
    coordinates = np.array([
                    [1,1,1],
                    [2.4,1,1],
                    [-0.4,1,1],
                    [1,1,2.4],
                    [1,1,-0.4]])
    
    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4

@pytest.mark.xfail
def test_calculate_angle():
    """Test the calculate_angle function"""

    r1 = np.array([0,0,-1])
    r2 = np.array([0,1,0])
    r3 = np.array([1,0,0])

    expected_value = 120
    calculated_value = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert pytest.approx(expected_value) == calculated_value

@pytest.mark.parametrize("r1, r2, r3, expected_angle", [
    (np.array([1,0,0]), np.array([0,0,0]), np.array([0,1,0]), 90),
    (np.array([0,0,-1]), np.array([0,1,0]), np.array([1,0,0]), 60)
])
def test_calculate_angle_many(r1, r2, r3, expected_angle):
    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)
    assert pytest.approx(calculated_angle) == expected_angle