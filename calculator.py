class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        negative = False
        if b < 0:  # Handle negative multiplier
            b = -b
            negative = True
        for _ in range(b):
            result = self.add(result, a)
        return -result if negative else result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = 0
        negative = (a < 0) ^ (b < 0)  # Determine sign of result
        a, b = abs(a), abs(b)
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return -result if negative else result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        while a >= b:
            a = self.subtract(a, b)
        return a