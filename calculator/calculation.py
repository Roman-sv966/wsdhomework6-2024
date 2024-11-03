"""
Calculation Class

The Calculation class encapsulates a mathematical operation between two Decimal numbers 
using a specified arithmetic function. It provides methods to execute the calculation 
and to create instances of Calculation.
"""

from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    """
    A class that represents a single mathematical calculation.

    Attributes:
        a (Decimal): The first value in the calculation.
        b (Decimal): The second value in the calculation.
        operation (Callable[[Decimal, Decimal], Decimal]): The mathematical function to execute.

    Methods:
        operate() -> Decimal:
            Executes the chosen operation on the operands and returns the outcome.
        
        create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> 'Calculation':
            Static method that initializes a new Calculation instance.
        
        __strrepr__() -> str:
            Provides a string representation of the Calculation instance for easy readability.
    """

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Set up a Calculation instance with two values and a specified operation.

        Args:
            a (Decimal): The first number.
            b (Decimal): The second number.
            operation (Callable[[Decimal, Decimal], Decimal]): The arithmetic function to apply.
        """
        self.a = a
        self.b = b
        self.operation = operation

    def operate(self) -> Decimal:
        """
        Execute the assigned arithmetic function on the two values.

        Returns:
            Decimal: The result produced by the operation.
        """
        return self.operation(self.a, self.b)

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> 'Calculation':
        """
        Initialize a new Calculation object.

        Args:
            a (Decimal): The first number.
            b (Decimal): The second number.
            operation (Callable[[Decimal, Decimal], Decimal]): The arithmetic function to apply.

        Returns:
            Calculation: A newly created Calculation instance.
        """
        return Calculation(a, b, operation)

    def __strrepr__(self) -> str:
        """
        Return a detailed string representation of this Calculation instance.

        Returns:
            str: A descriptive string of the Calculation instance.
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
