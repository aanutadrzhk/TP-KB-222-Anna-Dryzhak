import logging

def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ділення на нуль неможливе")
        return None
    