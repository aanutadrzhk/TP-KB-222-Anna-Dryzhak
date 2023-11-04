import random

def get_user_choice():
    user_choice = input("Камінь (r), ножиці (s), папір (p). Оберіть: ")
    return user_choice

def get_computer_choice():
    options = ['r', 's', 'p']
    computer_choice = random.choice(options)
    return computer_choice

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Нічия!"
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
        return "Ви перемогли!"
    else:
        return "Комп'ютер переміг."

def main():
    while True:
        user_choice = get_user_choice()
        if user_choice not in ['r', 's', 'p']:
            print("Введено некоректний варіант. Спробуйте ще раз.")
            continue

        computer_choice = get_computer_choice()
        print(f"Ваш вибір: {user_choice}")
        print(f"Вибір комп'ютера: {computer_choice}")

        result = winner(user_choice, computer_choice)
        print(result)

        play_again = input("Зіграти ще раз? (y/n): ")
        if play_again.lower() == 'n':
            break

if __name__ == "__main__":
    main()
    