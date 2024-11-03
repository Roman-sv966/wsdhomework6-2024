# calculator/plugins/divide_command.py
from decimal import Decimal
from calculator.command import Command
from calculator.command_registry import register_command

class DivideCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

register_command("divide", DivideCommand)
