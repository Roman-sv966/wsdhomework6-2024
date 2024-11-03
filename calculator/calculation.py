class Calculation:
    def __init__(self, operation, x, y):
        self.operation = operation
        self.x = x
        self.y = y

    def get_output(self):
        return self.operation(self.x, self.y)