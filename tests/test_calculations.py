"""
This module contains tests for the Calculations class.
"""

from decimal import Decimal
#import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

def test_add_calculation():
    """Test adding a calculation to the history."""
    Calculations.clear_history()
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    assert Calculations.get_history()[0] == calc

def test_clear_history():
    """Test clearing the calculation history."""
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    Calculations.add_calculation(calc)
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

def test_get_latest():
    """Test retrieving the latest calculation."""
    Calculations.clear_history()
    calc1 = Calculation(Decimal('10'), Decimal('5'), add)
    calc2 = Calculation(Decimal('20'), Decimal('10'), subtract)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    latest_calc = Calculations.get_latest()
    assert latest_calc == calc2

def test_find_by_operation():
    """Test finding calculations by operation name."""
    Calculations.clear_history()
    calc1 = Calculation(Decimal('10'), Decimal('5'), add)
    calc2 = Calculation(Decimal('20'), Decimal('10'), subtract)
    calc3 = Calculation(Decimal('2'), Decimal('3'), multiply)
    calc4 = Calculation(Decimal('10'), Decimal('2'), divide)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    Calculations.add_calculation(calc3)
    Calculations.add_calculation(calc4)

    add_calculations = Calculations.find_by_operation('add')
    subtract_calculations = Calculations.find_by_operation('subtract')
    multiply_calculations = Calculations.find_by_operation('multiply')
    divide_calculations = Calculations.find_by_operation('divide')

    assert len(add_calculations) == 1
    assert add_calculations[0] == calc1
    assert len(subtract_calculations) == 1
    assert subtract_calculations[0] == calc2
    assert len(multiply_calculations) == 1
    assert multiply_calculations[0] == calc3
    assert len(divide_calculations) == 1
    assert divide_calculations[0] == calc4

def test_get_history():
    """Test retrieving the entire calculation history."""
    Calculations.clear_history()
    calc1 = Calculation(Decimal('10'), Decimal('5'), add)
    calc2 = Calculation(Decimal('20'), Decimal('10'), subtract)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    history = Calculations.get_history()
    assert len(history) == 2
    assert history[0] == calc1
    assert history[1] == calc2
