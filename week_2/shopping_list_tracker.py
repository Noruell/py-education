command_list = ["Добавить товар", "Удалить товар", "Показать список", "Итоговая сумма", "Выйти"]

shop_list = []

def safe_input(prompt, data_type):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return data_type(user_input)
        print("Некорректный ввод!")


# Отображение всех команд
print("=== СПИСОК ПОКУПОК ===")
for a, command in enumerate(command_list, start = 1):
    print(f"{a}. {command}")

while True:
    command_choose = safe_input("\nВыбор: ", int)

    # Добавление в список
    if command_choose == 1:
        entity = input("Название: ").strip()
        cost = safe_input("Стоимость: ", float)
        
        shop_list.append((entity, cost))

        print("Добавлено!")
        
    # Удаление последнего добавленного элемента
    elif command_choose == 2:
        if not shop_list:
            print("Список пуст!")
            continue

        idx = safe_input("Номер для удаления: ", int) - 1
        if 0 <= idx < len(shop_list):
            removed = shop_list[idx]
            del shop_list[idx]
            print(f"Удалено: {removed[0]} - {removed[1]} руб.")
        else:
            print("Неверный номер!")

    # Просмотр списка
    elif command_choose == 3:
        for  i, item in enumerate(shop_list, start = 1):
            first, second = item[0], item[1]
            print(f"{i}. {first} - {second} руб.")
    
    # Просмотр общей суммы списка
    elif command_choose == 4:
        result = sum(float(item[1]) for item in shop_list)
        print(f"Итого: {result} руб.")    

    # Выход из программы
    elif command_choose == 5:
        print("Выход...")
        break

