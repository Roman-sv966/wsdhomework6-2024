from calculator.operations import add, subtract, divide, multiply
from calculator.calculation import Calculation

class Calculator:
    @staticmethod
    def add(a, b):
        calculation = Calculation(add, a ,b)
        return calculation.get_output()

    @staticmethod
    def subtract(a, b):
        calculation = Calculation(subtract, a ,b)
        return calculation.get_output()

    @staticmethod
    def multiply(a, b):
        calculation = Calculation(multiply, a ,b)
        return calculation.get_output()

    @staticmethod
    def divide(a, b):
        calculation = Calculation(divide, a, b)
        return calculation.get_output()