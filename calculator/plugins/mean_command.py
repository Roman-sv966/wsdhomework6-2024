# calculator/plugins/add_command.py
from decimal import Decimal
from calculator.command import Command
from calculator.command_registry import register_command

class MeanCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        return (self.a + self.b)/2

register_command("mean", MeanCommand)
