import logging

from functions import addition, subtraction, multiplication, division

def value(promt:str):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("Неправильне значення (введіть число)")
        

def operation(a, b, op):
    result = None
    if op == "+":
        result = addition(a, b)
    elif op == "-":
        result = subtraction(a, b)
    elif op == "*":
        result = multiplication(a, b)
    elif op == "/":
        result = division(a, b)

    if result is not None:
        logging.info(f"entered: a={a}, b={b}, operation={op}, result={result}")
    return result
