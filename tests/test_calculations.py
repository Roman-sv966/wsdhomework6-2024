'''
Calculations Test Module

This module contains unit tests for managing the history of calculations.
It ensures that calculations can be added, retrieved, cleared, and filtered
accurately using pytest.
'''

from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def sample_operations():
    '''
    Fixture to populate history with sample calculations for testing.

    This function clears any existing history and adds four sample
    calculations for testing purposes.
    '''
    calculations.delete_calculation()

    calculations.add_calculation(Calculation(Decimal('7'), Decimal('2'), add))
    calculations.add_calculation(Calculation(Decimal('5'), Decimal('3'), subtract))
    calculations.add_calculation(Calculation(Decimal('6'), Decimal('4'), multiply))
    calculations.add_calculation(Calculation(Decimal('8'), Decimal('2'), divide))

def test_add_calculation():
    '''
    Test adding a calculation to the history.

    This test creates a Calculation instance and verifies that it
    is successfully stored in the calculations history.
    '''
    add_obj = Calculation(Decimal('3'), Decimal('9'), add)
    calculations.add_calculation(add_obj)
    assert calculations.get_latest() == add_obj, "Failed to add calculation to history."

def test_get_all_history(sample_operations):
    '''
    Test retrieving all calculations from history.

    This test checks that the number of entries in the history
    matches the expected count after adding sample calculations.
    '''
    history = calculations.print_all_calculation()
    assert len(history) == 4, "Incorrect number of entries in history."

def test_delete_history():
    '''
    Test clearing the calculation history.

    This test verifies that the delete_calculation method removes
    all entries from the history.
    '''
    calculations.delete_calculation()
    assert len(calculations.print_all_calculation()) == 0, "Failed to clear calculation history."

def test_get_latest_calculation(sample_operations):
    '''
    Test retrieving the most recent calculation from history.

    This test checks that the latest calculation is accurate
    based on the sample operations added earlier.
    '''
    latest = calculations.get_latest()
    assert latest.a == Decimal('8') and latest.b == Decimal('2'), "Incorrect latest calculation."

def test_get_latest_after_clear():
    '''
    Test retrieving the latest calculation after clearing history.

    This test confirms that get_latest returns None after history
    has been cleared.
    '''
    calculations.delete_calculation()
    assert calculations.get_latest() is None, "History should be empty but get_latest is not None."

def test_find_by_operation(sample_operations):
    '''
    Test filtering calculations by specific operation type.

    This test verifies that the filter_with_operation method correctly
    returns the expected number of operations for specified types (add, divide).
    '''
    add_results = calculations.filter_with_operation("add")
    assert len(add_results) == 1, "Incorrect count of 'add' operations."
    divide_results = calculations.filter_with_operation("divide")
    assert len(divide_results) == 1, "Incorrect count of 'divide' operations."
