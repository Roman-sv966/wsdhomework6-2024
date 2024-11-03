"""
Calculation Test Module

This module provides unit tests for the Calculation class, focusing on
verifying the accuracy of arithmetic operations (addition, subtraction,
multiplication, and division) using pytest. The tests validate that the
operate method correctly handles Decimal inputs and that the string
representation of Calculation instances is accurate.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("n1, n2, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('7'), Decimal('4'), subtract, Decimal('3')),
    (Decimal('15'), Decimal('3'), divide, Decimal('5')),
    (Decimal('6'), Decimal('4'), multiply, Decimal('24')),
    (Decimal('5.0'), Decimal('2.0'), add, Decimal('7.0'))
])
def test_operate(n1, n2, operation, expected):
    """
    Test the operate method of the Calculation class.

    This test initializes a Calculation instance with the provided
    parameters and verifies that the operate method's result matches
    the expected outcome.

    Args:
        n1 (Decimal): The first operand.
        n2 (Decimal): The second operand.
        operation (Callable): The arithmetic function to apply.
        expected (Decimal): The anticipated result of the operation.
    """
    calc = Calculation(n1, n2, operation)
    assert calc.operate() == expected, "Operation result does not match the expected value!"

def test_strrepr():
    """
    Test the string output of the Calculation class.

    This test initializes a Calculation instance and checks if its
    string representation matches the expected format.

    Args:
        None
    """
    calc = Calculation(Decimal('3'), Decimal('3'), add)
    str_match = "Calculation(3, 3, add)"
    assert calc.__strrepr__() == str_match, f"Expected '{str_match}' but got '{calc.__strrepr__()}'"

def test_divide_by_zero():
    """
    Verify the division by zero error handling.

    This test creates a Calculation instance with a zero divisor and
    confirms that a ValueError is raised with an appropriate message.

    Args:
        None
    """
    calc = Calculation(Decimal('8'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Error: Cannot divide by zero!"):
        calc.operate()
