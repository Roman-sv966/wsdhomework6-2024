"""
Calculator Module

This module provides a simple calculator with basic arithmetic functions such as addition, 
subtraction, multiplication, and division. It uses the Decimal class to ensure accurate numerical 
computations and stores each result for possible future reference.
"""

from calculator.operations import add, subtract, divide, multiply
from calculator.calculation import Calculation
from calculator.calculations import calculations
from decimal import Decimal
from typing import Callable

class Calculator:
    """
    A class for performing basic arithmetic operations.

    Methods:
        perform(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
            Executes the specified operation on two Decimal values and records the calculation.

        add(a: Decimal, b: Decimal) -> Decimal:
            Calculates the sum of two Decimal values.
        
        subtract(a: Decimal, b: Decimal) -> Decimal:
            Computes the difference between two Decimal values.
        
        multiply(a: Decimal, b: Decimal) -> Decimal:
            Determines the product of two Decimal values.
        
        divide(a: Decimal, b: Decimal) -> Decimal:
            Finds the quotient when one Decimal value is divided by another.
    """

    @staticmethod
    def perform(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """
        Perform the specified arithmetic operation and logs the result for future reference.

        Args:
            a (Decimal): The first number in the operation.
            b (Decimal): The second number in the operation.
            operation (Callable[[Decimal, Decimal], Decimal]): The function representing the arithmetic operation.

        Returns:
            Decimal: The result of the arithmetic operation.
        """
        # Create and log the calculation
        calculation = Calculation.create(a, b, operation)
        calculations.add_calculation(calculation)
        # Run the operation and return the output
        return calculation.operate()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """
        Calculate the sum of two Decimal numbers.

        Args:
            a (Decimal): The first number.
            b (Decimal): The second number.

        Returns:
            Decimal: The result of adding a and b.
        """
        return Calculator.perform(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """
        Calculate the difference between two Decimal numbers.

        Args:
            a (Decimal): The number to subtract from.
            b (Decimal): The number to be subtracted.

        Returns:
            Decimal: The result of a minus b.
        """
        return Calculator.perform(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """
        Calculate the product of two Decimal numbers.

        Args:
            a (Decimal): The first number.
            b (Decimal): The second number.

        Returns:
            Decimal: The result of a times b.
        """
        return Calculator.perform(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        Divide one Decimal number by another.

        Args:
            a (Decimal): The number to be divided.
            b (Decimal): The divisor.

        Returns:
            Decimal: The result of a divided by b.
        
        Raises:
            ZeroDivisionError: If b is zero, to prevent division by zero.
        """
        return Calculator.perform(a, b, divide)
