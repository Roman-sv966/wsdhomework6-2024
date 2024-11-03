# calculator/command.py
from abc import ABC, abstractmethod
from decimal import Decimal
from calculator.command_registry import register_command

class Command(ABC):
    @abstractmethod
    def execute(self) -> Decimal:
        raise NotImplementedError("Each command must implement the execute method.")

    def execute_in_process(self, result_queue):
        try:
            result = self.execute()
            result_queue.put(result)
        except Exception as e:
            result_queue.put(e)

class AddCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        return self.a + self.b

register_command("add", AddCommand)

class SubtractCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        return self.a - self.b

register_command("subtract", SubtractCommand)

class MultiplyCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        return self.a * self.b

register_command("multiply", MultiplyCommand)

class DivideCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

register_command("divide", DivideCommand)
