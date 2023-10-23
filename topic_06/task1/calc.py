import logging
import os
from operations import value, operation

current_directory = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_directory, 'calculator.log')

logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


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

logging.shutdown()
