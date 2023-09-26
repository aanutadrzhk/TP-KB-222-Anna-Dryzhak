a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
op = (input("Операція, яку треба виконати: "))

def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    if b == 0:
        res = "Ділення на 0 не можливе"
    else:
        res = a / b
    return res

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