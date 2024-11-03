''' Unit tests for Calculator operations '''
import pytest
from calculator import Calculator

def test_add():
    '''Test addition operation with two integers using the Calculator object'''
    result = Calculator.add(10, 15)
    assert result == 25

def test_subtract():
    '''Test subtraction operation with two integers using the Calculator object'''
    assert Calculator.subtract(20, 5) == 15

def test_multiply():
    '''Test multiplication operation with two integers using the Calculator object'''
    assert Calculator.multiply(6, 7) == 42

def test_divide():
    '''Test division operation with two integers using the Calculator object'''
    assert Calculator.divide(100, 4) == 25

def test_divide_by_zero():
    '''Test if division operation raises an error when dividing by zero'''
    with pytest.raises(ValueError):
        Calculator.divide(50, 0)
