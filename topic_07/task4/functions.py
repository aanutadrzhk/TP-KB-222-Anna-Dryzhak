class Calculator:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Ділення на нуль неможливе")
            return None