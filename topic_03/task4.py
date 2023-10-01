numbers = [1, 3, 5,]

while True:
    print("Список:", numbers)
    new_number = input("Введіть нове число, чи введіть 'вихід', якщо хочете вийти: ")

    if new_number == 'вихід':
        break

    new_number = int(new_number) 

    insert_index = 0

    for num in numbers:
        if new_number > num:
            insert_index += 1

    numbers.insert(insert_index, new_number)