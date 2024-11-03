"""
Calculations Class

This module defines a class to manage a record of multiple calculations.
It supports adding, clearing, retrieving, and filtering calculations based on
the type of operation performed.
"""

from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable, List

class calculations:
    """
    A class to keep track of a history of calculation instances.

    Attributes:
        history (List[Calculation]): A list that stores individual Calculation instances.

    Methods:
        add_calculation(calculation: Calculation):
            Appends a new Calculation instance to the history list.

        delete_calculation():
            Empties the history list, removing all stored calculations.

        get_latest() -> Calculation:
            Retrieves the most recent Calculation instance from the history, or None if history is empty.

        print_all_calculation() -> List[Calculation]:
            Returns the complete list of Calculation instances in the history.

        filter_with_operation(operation: str) -> List[Calculation]:
            Filters the history to return Calculation instances with a specified operation.
    """

    history = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """
        Append a Calculation instance to the history list.

        Args:
            calculation (Calculation): The Calculation instance to be added to history.
        """
        cls.history.append(calculation)

    @classmethod
    def delete_calculation(cls):
        """
        Clear all Calculation instances from the history list.
        """
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """
        Get the most recently added Calculation instance.

        Returns:
            Calculation: The latest Calculation in history, or None if no calculations exist.
        """
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def print_all_calculation(cls) -> List[Calculation]:
        """
        Retrieve the entire history of Calculation instances.

        Returns:
            List[Calculation]: The list of all calculations stored in history.
        """
        return cls.history

    @classmethod
    def filter_with_operation(cls, operation: str) -> List[Calculation]:
        """
        Retrieve Calculation instances that match a given operation.

        Args:
            operation (str): The name of the operation to filter by (e.g., 'add', 'subtract').

        Returns:
            List[Calculation]: A list of calculations that use the specified operation.
        """
        return [calc for calc in cls.history if calc.operation.__name__ == operation]
