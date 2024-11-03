'''
This module contains tests for the `perform_calculation_and_display` function
from the main application. It uses pytest to verify correct behavior across
different arithmetic operations, including edge cases such as invalid inputs
and unknown operations.
'''
import pytest
from main import perform_calculation_and_display

@pytest.mark.parametrize("value1, value2, operation_type, expected_output", [
    ("5", "3", 'add', "The result of 5 add 3 is 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is 5"),
    ("1", "0", 'divide', "Error: Cannot divide by zero"),  # Test division by zero
    ("9", "3", 'unknown', "Invalid operation type: unknown"),  # Test for unknown operation
    ("a", "3", 'add', "Invalid input: a or 3 is not a valid number."),  # Invalid input test
    ("5", "b", 'subtract', "Invalid input: 5 or b is not a valid number.")  # Another invalid input test
])
def test_perform_calculation_and_display(value1, value2, operation_type, expected_output, capsys):
    '''
    Tests perform_calculation_and_display for various input scenarios.
    '''
    perform_calculation_and_display(value1, value2, operation_type)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
