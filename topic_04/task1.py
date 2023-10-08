def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    if b == 0:
        return "Ділення на 0 не можливе"
    return a / b

def value(promt:str):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("Неправильне значення (введіть число)")
        
while True:
    print("Додавання: + ")
    print("Віднімання: - ")
    print("Множення: * ")
    print("Ділення: / ")
    print("Вихід: 0 ")

    a = value("Введіть значення a: ")
    b = value("Введіть значення b: ")
    op = (input("Операція, яку треба виконати: ")) 

    if op == "0":
        break

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