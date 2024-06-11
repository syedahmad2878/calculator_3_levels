"""
Initialization module for the tests package.

This module can contain setup code for the tests package if needed.
"""

# Add any initialization code if needed

# Ensure there is a newline at the end of the file



from calculator import Calculator


def test_addition():
    """Test that the addition function works."""
    assert Calculator.add(2, 2) == 4

def test_subtraction():
    """Test that the subtraction function works."""
    assert Calculator.subtract(2, 2) == 0

def test_multiply():
    """Test that the multiply function works."""
    assert Calculator.multiply(2, 2) == 4

def test_divide():
    """Test that the divide function works."""
    assert Calculator.divide(2, 2) == 1
