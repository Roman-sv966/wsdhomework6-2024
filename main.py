import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def perform_calculation_and_display(value1, value2, operation_type):
    """
    Executes the specified arithmetic operation on two inputs and displays the outcome.
    """
    operation_map = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }
    try:
        decimal_value1, decimal_value2 = map(Decimal, [value1, value2])
        operation_func = operation_map.get(operation_type)
        if operation_func:
            result = operation_func(decimal_value1, decimal_value2)
            print(f"The result of {value1} {operation_type} {value2} is {result}")
        else:
            print(f"Invalid operation type: {operation_type}")
    except InvalidOperation:
        print(f"Invalid input: {value1} or {value2} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to process command-line arguments and start the calculation.
    """
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, value1, value2, operation_type = sys.argv
    perform_calculation_and_display(value1, value2, operation_type)

if __name__ == '__main__':
    main()
