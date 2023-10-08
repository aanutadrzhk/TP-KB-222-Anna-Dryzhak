def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    try:
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе")
        return a / b
    except ZeroDivisionError as e:
        return str(e)

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
        print(f"{result}\n")
    else:
        print("Неправильно введена операція, спробуйте *, /, -, +")
