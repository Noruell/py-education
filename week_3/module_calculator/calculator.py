from operations import add, subtract, multiply, divide, power, oper_list

# Check correct input
def safe_input(prompt, data_type=None):
    while True:
        user_input = input(prompt).lower().strip()
        if data_type is None:
            return user_input
        try:
            return data_type(user_input)
        except ValueError:
            print("Ошибка! Некорректный ввод!\n")

# Program restart
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

def run_calculator():
    while True:
        error_occurred = False

        a = safe_input("\nВведите первое число: ", float)
        b = safe_input("Введите второе число: ", float)

        print("=== СПИСОК ОПЕРАЦИЙ ===")
        for i, oper in enumerate(oper_list, start=1):
            print(f"{i}. {oper}")

        user_chose = safe_input("Выберите операцию: ", int)

        if user_chose == 1:
            result = add(a, b)
        elif user_chose == 2:
            result = subtract(a, b)
        elif user_chose == 3:
            result = multiply(a, b)
        elif user_chose == 4:
            try:
                result = divide(a, b)
            except ZeroDivisionError:
                print("Ошибка: деление на ноль!")
                error_occurred = True
        elif user_chose == 5:
            result = power(a, b)
        else:
            print("Ошибка: Неизвестная операция!")
            error_occurred = True
            
        if not error_occurred:
            print(f"\n{round(result, 2)}")


        if not restart_prog():
            break

if __name__ == "__main__":
    run_calculator()