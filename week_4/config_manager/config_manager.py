import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.txt")

commands_list = {1: "Просмотреть все настройки",
                 2: "Изменить настройку",
                 3: "Добавить настройку",
                 4: "Удалить настройку",
                 5: "Выйти"}

# Получение настроек из файла config.txt
def config_read():
    global config
    config = {}

    if not os.path.exists(CONFIG_PATH):
        return config

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                setting, value = line.split(" = ")
                config[setting] = value
#                config = {setting.strip(): value.strip() for setting, value in config.items()}
#                Альтернативный вариант очистки словаря от пробелов, более надежный
    return config

# Запись настроек в config.txt
def config_save():
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as file:
            for setting, value in config.items():
                file.write(f"{setting} = {value}\n")
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False
            

# Просмотр списка команд
def commands_list_view():
    print("\n=== КОНФИГ-МЕНЕДЖЕР ===")
    for num, command in commands_list.items():
        print(f"{num}. {command}")

# 1. Просмотр настроек 
def setting_view():
    for setting, value in config.items():
        print(f"{setting} = {value}")

# 2. Изменить настроку
def setting_change():
    setting_key = input("Ключ: ").strip()

    if not setting_key:
        print("Ошибка: не указан 'ключ' настройки!")
    elif setting_key in config:
        config[setting_key] = input("Новое значение: ")
        print("Сохранено!")
    else:
        print("Настройка не найдена!")
    
# 3. Добавить настройку
def setting_add():
    setting_key = input("Ключ настройки: ").strip()
    setting_value = input("Значение настройки: ").strip()

    if not setting_value or not setting_key:
        print("Ключ/Значение не могут быть пустыми!")
    elif setting_key in config:
        print(f"{setting_key} уже существует.")
    else:
        config[setting_key] = setting_value
        print("Сохранено!")

# 4. Удалить настройку
def setting_remove():
    setting_key = input("Ключ: ").strip()

    if not setting_key:
        print("Ошибка: не указан 'ключ' настройки!")
    elif setting_key in config:
        del config[setting_key]
        print(f"Настройка '{setting_key}' удалена!")
    else:
        print("Настройка не найдена!")

# 5. Закрыть программу
def programm_close():
    if config_save():
        print("Настройки сохранены. До свидания!")
    else:
        print("Настройки не сохранились.. До свидания!")
    return False

# main
def run_config_manager():
    config_read()
    while True:
        commands_list_view()
        user_chose = input("\nВыбор: ")

        if user_chose == "1": setting_view()
        elif user_chose == "2": setting_change()
        elif user_chose == "3": setting_add()
        elif user_chose == "4": setting_remove()
        elif user_chose == "5": 
            if not programm_close(): break
        else: print("Неизвестная команда. Введите команду из списка (1-5)")

