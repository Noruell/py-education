def safe_input(prompt, data_type=None):
    while True:
        user_input = input(prompt).lower().strip()
        if data_type is None:
            return user_input
        try:
            return data_type(user_input)
        except ValueError:
            print("Ошибка! Некорректный ввод!\n")

def restart_prog():
    while True:
        user_choose = input("\nПродолжить? (да/нет): ").lower().strip()
        
        if user_choose == "да":
            return True
        
        elif user_choose == "нет":
            print("Выход...")
            return False
        
        else:
            print("Введите (да/нет)!")
        


while True:
    result = 0

    first_num = safe_input("\nВведите первое число: ", float)
    second_num = safe_input("Введите второе число: ", float)

    operation = safe_input("Выберите операцию (+, -, *, /): ", str)

    if operation == "+":
        result = first_num + second_num
        print(f"\n{round(result, 2)}")
    elif operation == "-":
        result = first_num - second_num
        print(f"\n{round(result, 2)}")
    elif operation == "*":
        result = first_num * second_num
        print(f"\n{round(result, 2)}")
    elif operation == "/":
        try:
            result = first_num / second_num
            print(f"\n{round(result, 2)}")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль!")
    else:
        print("Ошибка: Неизвестная операция!")
        

    if not restart_prog():
        break


