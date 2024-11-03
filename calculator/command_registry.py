# calculator/command_registry.py

command_registry = {}

def register_command(name, command_class):
    """Registers a command in the global command registry."""
    command_registry[name] = command_class
