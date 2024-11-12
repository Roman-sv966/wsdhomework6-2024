import sys
import os
import importlib
from decimal import Decimal, InvalidOperation
from calculator.command_registry import command_registry  # Import the registry
import multiprocessing

import logging
import logging.config
from dotenv import load_dotenv


def load_environment_variables():
    load_dotenv()
    settings = {key: value for key, value in os.environ.items()}
    logging.info("Environment variables loaded.")
    logging.debug(f"Loaded environment variables: {settings}")
    return settings


def configure_logging():
    os.makedirs("logs", exist_ok=True)
    logging_conf_path = "logging.conf"
    if os.path.exists(logging_conf_path):
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        logging.info("Logging configuration loaded from 'logging.conf'.")
    else:
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logging.info("Default logging configuration applied.")
    logging.info("Logging configured.")


def load_plugins():
    """
    Dynamically loads all command plugins from the plugins folder.
    """
    plugins_dir = os.path.join(os.path.dirname(__file__), 'calculator', 'plugins')
    logging.info(f"Loading plugins from directory: {plugins_dir}")
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"calculator.plugins.{filename[:-3]}"  # Remove .py extension
            logging.debug(f"Importing plugin: {module_name}")
            importlib.import_module(module_name)  # Dynamically import the module
    logging.info("All plugins loaded.")


def perform_calculation_and_display(value1, value2, operation_type):
    """
    Executes the specified arithmetic operation on two inputs using multiprocessing
    and displays the outcome.
    """
    try:
        logging.info(f"Performing calculation: {operation_type} with values {value1} and {value2}")
        
        # Convert inputs to Decimal
        decimal_value1 = Decimal(value1)
        decimal_value2 = Decimal(value2)
        logging.debug(f"Converted values to Decimal: {decimal_value1}, {decimal_value2}")

        # Get the command class from the registry
        command_class = command_registry.get(operation_type)
        if not command_class:
            logging.error(f"Invalid operation type: {operation_type}")
            print(f"Invalid operation type: {operation_type}")
            return

        # Create an instance of the command with the provided arguments
        command_instance = command_class(decimal_value1, decimal_value2)
        logging.debug(f"Command instance created: {command_instance}")

        # Set up multiprocessing to execute the command
        result_queue = multiprocessing.Queue()
        logging.info("Starting process to execute the command.")
        process = multiprocessing.Process(target=command_instance.execute_in_process, args=(result_queue,))
        process.start()
        process.join()

        # Get the result from the process
        result = result_queue.get()
        logging.info(f"Process completed. Result: {result}")

        # Display the result or handle any errors
        if isinstance(result, Exception):
            logging.error(f"An error occurred during the operation: {result}")
            print(f"An error occurred: {result}")
        else:
            logging.info(f"Calculation result: {value1} {operation_type} {value2} = {result}")
            print(f"The result of {value1} {operation_type} {value2} is {result}")

    except InvalidOperation:
        logging.error(f"Invalid input: {value1} or {value2} is not a valid number.")
        print(f"Invalid input: {value1} or {value2} is not a valid number.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")


def display_menu():
    """
    Displays the list of available commands.
    """
    logging.info("Displaying available commands.")
    print("Available commands:", ", ".join(command_registry.keys()))


def repl():
    """
    Interactive REPL loop for the calculator using command pattern.
    """
    print("Welcome to the Interactive Calculator. Type 'exit' to quit or 'menu' to see available commands.")
    display_menu()  # Display menu at the start

    while True:
        user_input = input("Enter command (e.g., 'add 5 3'): ").strip()
        logging.info(f"User input received: {user_input}")

        if user_input.lower() == 'exit':
            logging.info("Exiting the REPL.")
            print("Goodbye!")
            break
        elif user_input.lower() == 'menu':
            display_menu()
            continue
        parts = user_input.split()
        if len(parts) < 3:
            logging.warning(f"Invalid input format: {user_input}. Expected format: <operation> <num1> <num2>")
            print("Invalid input format. Use: <operation> <num1> <num2>")
            continue
        operation, num1, num2 = parts[0], parts[1], parts[2]
        logging.info(f"Processing command: {operation} {num1} {num2}")
        perform_calculation_and_display(num1, num2, operation)


def main():
    """
    Main function to either process command-line arguments or start the REPL loop.
    """
    # Load plugins dynamically at startup
    load_plugins()

    # If command-line arguments are provided, execute once and exit
    if len(sys.argv) == 4:
        _, value1, value2, operation_type = sys.argv
        logging.info(f"Command-line input detected: {value1}, {value2}, {operation_type}")
        perform_calculation_and_display(value1, value2, operation_type)
    else:
        # Start the REPL if no command-line arguments are provided
        logging.info("Starting REPL loop.")
        repl()


if __name__ == '__main__':
    configure_logging()
    settings = load_environment_variables()

    logging.info(f"Environment: {settings.get('ENVIRONMENT')}")
    logging.info("Application started.")
    main()
