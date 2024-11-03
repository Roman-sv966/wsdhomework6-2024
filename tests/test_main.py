import pytest
from decimal import Decimal
from calculator.command_registry import command_registry
from main import perform_calculation_and_display, load_plugins

# Load plugins once before running tests
load_plugins()

def test_add_command(capsys):
    # Test addition
    perform_calculation_and_display("5", "3", "add")
    captured = capsys.readouterr()
    assert "The result of 5 add 3 is 8" in captured.out

def test_subtract_command(capsys):
    # Test subtraction
    perform_calculation_and_display("10", "4", "subtract")
    captured = capsys.readouterr()
    assert "The result of 10 subtract 4 is 6" in captured.out

def test_multiply_command(capsys):
    # Test multiplication
    perform_calculation_and_display("6", "7", "multiply")
    captured = capsys.readouterr()
    assert "The result of 6 multiply 7 is 42" in captured.out

def test_divide_command(capsys):
    # Test division
    perform_calculation_and_display("20", "5", "divide")
    captured = capsys.readouterr()
    assert "The result of 20 divide 5 is 4" in captured.out

def test_divide_by_zero(capsys):
    # Test division by zero
    perform_calculation_and_display("10", "0", "divide")
    captured = capsys.readouterr()
    assert "An error occurred: Cannot divide by zero" in captured.out

def test_invalid_command(capsys):
    # Test invalid command
    perform_calculation_and_display("5", "3", "unknown")
    captured = capsys.readouterr()
    assert "Invalid operation type: unknown" in captured.out

def test_invalid_number_input(capsys):
    # Test invalid numeric input
    perform_calculation_and_display("a", "3", "add")
    captured = capsys.readouterr()
    assert "Invalid input: a or 3 is not a valid number." in captured.out

    perform_calculation_and_display("5", "b", "subtract")
    captured = capsys.readouterr()
    assert "Invalid input: 5 or b is not a valid number." in captured.out

def test_menu_display(capsys):
    # Test if menu displays correct commands
    from main import display_menu
    display_menu()
    captured = capsys.readouterr()
    assert "Available commands: add, subtract, multiply, divide" in captured.out
