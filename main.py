# main.py
import sys
from decimal import Decimal, InvalidOperation
from calculator.command_registry import command_registry  # Import the registry
import calculator.command  # Import command to ensure commands are registered
import multiprocessing


def perform_calculation_and_display(value1, value2, operation_type):
    """
    Executes the specified arithmetic operation on two inputs using multiprocessing
    and displays the outcome.
    """
    try:
        # Convert inputs to Decimal
        decimal_value1 = Decimal(value1)
        decimal_value2 = Decimal(value2)

        # Get the command class from the registry
        command_class = command_registry.get(operation_type)
        if not command_class:
            print(f"Invalid operation type: {operation_type}")
            return

        # Create an instance of the command with the provided arguments
        command_instance = command_class(decimal_value1, decimal_value2)

        # Set up multiprocessing to execute the command
        result_queue = multiprocessing.Queue()
        process = multiprocessing.Process(target=command_instance.execute_in_process, args=(result_queue,))
        process.start()
        process.join()

        # Get the result from the process
        result = result_queue.get()

        # Display the result or handle any errors
        if isinstance(result, Exception):
            print(f"An error occurred: {result}")
        else:
            print(f"The result of {value1} {operation_type} {value2} is {result}")

    except InvalidOperation:
        print(f"Invalid input: {value1} or {value2} is not a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def repl():
    """
    Interactive REPL loop for the calculator using command pattern.
    """
    print("Welcome to the Interactive Calculator. Type 'exit' to quit.")

    # Print command names only
    print("Available commands:", ", ".join(command_registry.keys()))

    while True:
        user_input = input("Enter command (e.g., 'add 5 3'): ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        parts = user_input.split()
        if len(parts) < 3:
            print("Invalid input format. Use: <operation> <num1> <num2>")
            continue
        operation, num1, num2 = parts[0], parts[1], parts[2]
        perform_calculation_and_display(num1, num2, operation)


def main():
    """
    Main function to either process command-line arguments or start the REPL loop.
    """
    # If command-line arguments are provided, execute once and exit
    if len(sys.argv) == 4:
        _, value1, value2, operation_type = sys.argv
        perform_calculation_and_display(value1, value2, operation_type)
    else:
        # Start the REPL if no command-line arguments are provided
        repl()

if __name__ == '__main__':
    main()
