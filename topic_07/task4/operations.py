from functions import Calculator

class CalculatorOperations:
    @staticmethod
    def value(prompt: str):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Неправильне значення (введіть число)")

    @staticmethod
    def operation(a, b, op):
        calculator = Calculator()
        if op in ['+', '-', '*', '/']:
            if op == '+':
                print(calculator.addition(a, b))
            elif op == '-':
                print(calculator.subtraction(a, b))
            elif op == '*':
                print(calculator.multiplication(a, b))
            elif op == '/':
                print(calculator.division(a, b))
        else:
            print("Неправильно введена операція, спробуйте *, /, -, +")