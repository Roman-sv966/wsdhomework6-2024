import pytest
import multiprocessing
from decimal import Decimal
from calculator.command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator.command_registry import command_registry

def test_add_command():
    # Test addition operation
    add_command = AddCommand(Decimal("5"), Decimal("3"))
    assert add_command.execute() == Decimal("8")

def test_subtract_command():
    # Test subtraction operation
    subtract_command = SubtractCommand(Decimal("10"), Decimal("4"))
    assert subtract_command.execute() == Decimal("6")

def test_multiply_command():
    # Test multiplication operation
    multiply_command = MultiplyCommand(Decimal("6"), Decimal("7"))
    assert multiply_command.execute() == Decimal("42")

def test_divide_command():
    # Test division operation
    divide_command = DivideCommand(Decimal("20"), Decimal("5"))
    assert divide_command.execute() == Decimal("4")

def test_divide_by_zero():
    # Test division by zero
    divide_command = DivideCommand(Decimal("10"), Decimal("0"))
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute()

def test_execute_in_process_add_command():
    # Test executing AddCommand in a separate process
    add_command = AddCommand(Decimal("5"), Decimal("3"))
    result_queue = multiprocessing.Queue()
    add_command.execute_in_process(result_queue)
    result = result_queue.get()
    assert result == Decimal("8")

def test_execute_in_process_error_handling():
    # Test that execute_in_process catches exceptions properly
    divide_command = DivideCommand(Decimal("10"), Decimal("0"))
    result_queue = multiprocessing.Queue()
    divide_command.execute_in_process(result_queue)
    result = result_queue.get()
    assert isinstance(result, ValueError)
    assert str(result) == "Cannot divide by zero"

