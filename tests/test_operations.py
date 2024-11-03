'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''
    assert add(2,3) == 5

def test_subtraction():
    '''Test that addition function works '''
    assert subtract(3,3) == 0

def test_multiplication():
    '''Test that multiplication function works '''
    assert multiply(2,4) == 8

def test_division():
    '''Test that multiplication function works '''
    assert divide(2,2) == 1