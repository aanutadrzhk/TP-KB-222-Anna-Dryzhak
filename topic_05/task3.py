from operations import value, operation

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

    result = operation(a, b, op)
    if result is not None:
        print(result)
