"""
Operations Module

This module offers fundamental arithmetic functions, including addition, 
subtraction, multiplication, and division. Each function accepts two inputs 
and returns the resulting value. The division function will raise an error 
if division by zero is attempted.
"""

def add(a, b):
    """
    Calculate the sum of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The total of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Calculate the difference between two numbers.

    Args:
        a: The number to be reduced.
        b: The amount to subtract from a.

    Returns:
        The difference obtained from a - b.
    """
    return a - b

def multiply(a, b):
    """
    Calculate the product of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The multiplication result of a and b.
    """
    return a * b

def divide(a, b):
    """
    Perform division of one number by another.

    Args:
        a: The number to be divided (dividend).
        b: The number by which to divide (divisor).

    Returns:
        The quotient resulting from a / b.

    Raises:
        ValueError: If b is zero, to prevent division by zero.
    """
    if b != 0:
        return a / b
    else:
        raise ValueError("Error: Cannot divide by zero!")
