from random import choices, shuffle
# Генерация данных для пароля
list1 = [chr(i) for i in range(ord('a'), ord('z') + 1)]
list2 = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
numbers = [str(i) for i in range(0, 10)]
characters = list("!@#$%^&*()_+-=[]{};':\\|,.<>/?")



def password_generator(length, use_digits, use_symbols):
    if length <= 0:
        return "Длина пароля не может быть 0 или меньше"
    pool = [*list1, *list2]

    if use_digits:
        pool = [*pool, *numbers]
    if use_symbols:
        pool = [*pool, *characters]
    password = choices(pool, k=length)
    shuffle(password)

    return "".join(password)

def main():
    print("===== ГЕНЕРАТОР ПАРОЛЕЙ v2 =====")
    lenght = int(input("Длина пароля: "))
    use_digits = input("Использовать цифры? (да/нет): ").lower().strip() == "да"
    use_symbols = input("Использовать спец. символы? (да/нет): ").lower().strip() == "да"

    password = password_generator(lenght, use_digits, use_symbols)
    print(f"\nВаш пароль: {password}")


if __name__ == "__main__":
    main()
