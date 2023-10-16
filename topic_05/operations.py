from functions import addition, subtraction, multiplication, division

def value(promt:str):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("Неправильне значення (введіть число)")
        

def operation(a, b, op):
    match op:
        case "+":
            print(addition(a,b))
        case "-":
            print(subtraction(a,b))
        case "*":
            print(multiplication(a,b))  
        case "/":
            print(division(a,b))
        case _: 
            print("Неправильно введена операція, спробуйте *,/,-,+")