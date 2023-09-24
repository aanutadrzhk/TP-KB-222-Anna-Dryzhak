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
    return a / b

if op == "+":
    result = addition(a,b)
elif op == "-":
    result = subtraction(a,b)
elif op == "*":
    result = multiplication(a,b)  
elif op == "/":
    result = division(a,b)
else: 
    result = "Неправильно введена операція, спробуйте *,/,-,+"

print(result)