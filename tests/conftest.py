'''
This module configures test settings and generates data for arithmetic operation testing
using the pytest framework. It leverages the Faker library to produce random data for
operations like addition, subtraction, multiplication, and division. The generated
data is used to create dynamic tests that validate the functionality of arithmetic operations.
'''

from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

# Instantiate a Faker object for generating random data
fake = Faker()

def generate_test_data(record_count):
    """
    Create test data for arithmetic operations.
    """
    # Define mappings for available operations
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    # Generate the specified number of test cases
    for idx in range(record_count):
        num1 = Decimal(fake.random_number(digits=2))
        num2 = Decimal(fake.random_number(digits=2)) if idx % 4 != 3 else Decimal(fake.random_number(digits=1))
        op_name = fake.random_element(elements=list(operations.keys()))
        op_func = operations[op_name]

        # Adjust for division by zero in test data
        if op_func == divide:
            num2 = Decimal('1') if num2 == Decimal('0') else num2

        try:
            if op_func == divide and num2 == Decimal('0'):
                result = "ZeroDivisionError"
            else:
                result = op_func(num1, num2)
        except ZeroDivisionError:
            result = "ZeroDivisionError"

        # Yield each set of test data
        yield num1, num2, op_name, op_func, result

def pytest_addoption(parser):
    """
    Add command-line options for pytest.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Specify the number of test records to generate")

def pytest_generate_tests(metafunc):
    """
    Generate dynamic tests based on the required test parameters.
    """
    if {"operand1", "operand2", "expected_result"}.intersection(set(metafunc.fixturenames)):
        record_count = metafunc.config.getoption("num_records")
        test_data = list(generate_test_data(record_count))

        # Customize parameters based on available fixtures
        customized_params = [
            (n1, n2, op_name if 'operation_name' in metafunc.fixturenames else op_func, result)
            for n1, n2, op_name, op_func, result in test_data
        ]

        # Parameterize tests with the generated data
        metafunc.parametrize("operand1,operand2,operation,expected_result", customized_params)
