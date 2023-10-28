from operations import CalculatorOperations

while True:
    print("Додавання: + ")
    print("Віднімання: - ")
    print("Множення: * ")
    print("Ділення: / ")
    print("Вихід: 0 ")

    calc_op = CalculatorOperations()
    
    a = calc_op.value("Введіть значення a: ")
    b = calc_op.value("Введіть значення b: ")
    op = (input("Операція, яку треба виконати: "))

    if op == "0":
        break

    result = calc_op.operation(a, b, op)
    if result is not None:
        print(result)