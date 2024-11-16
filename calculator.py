class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot find modulo by zero")
        while a >= b:
            a = self.subtract(a, b)
        return a