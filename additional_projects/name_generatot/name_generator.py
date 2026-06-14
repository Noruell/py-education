import os
from random import choice, randint

# 1. Получение параметров генерации - готово 
# 2. Генерация по правилу: prefix + root + suffix - готово
# 3. Вывод сгенерированных имен - готово
# 4. Возможность сохранения в фалй - пока не стал делать

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

# Словарь для разных рас
names_parts = {
    "человек": {
        "prefixes": ["Ар", "Бел", "Грим", "Род", "Яр"],
        "roots":    ["мир", "слав", "град", "полк", "вед"],
        "suffixes": ["ус", "а", "ий", "ер", "ин"]
    },
    "эльф": {
        "prefixes": ["Эль", "Ле", "Фин", "Гил", "Аэ"],
        "roots":    ["ронд", "нар", "ви", "тир", "лаур"],
        "suffixes": ["ир", "эль", "он", "аэль", "дуин"]
    },
    "орк": {
        "prefixes": ["Гор", "Мор", "Тор", "Аз", "Дур"],
        "roots":    ["баш", "рок", "зуг", "гош", "хаг"],
        "suffixes": ["ул", "ар", "ор", "ок", "ран"]
    },
}

# Обработка ввода
def safe_input(prompt, options, data_type):
    while True:
        user_input = input(prompt).strip()
        if data_type == int:
            user_input = int(user_input)
        if isinstance(user_input, data_type) and user_input in options:
            return user_input
        print(f"Ошибка! Введите {options}")

# Получение параметров
def parametr_chose():
    gender = safe_input("Укажите пол (м/ж): ", {"м", "ж"}, str)
    race = safe_input("Выберите расу (человек/эльф/орк): ", {"человек", "эльф", "орк"}, str)
    quantity = safe_input("Количество генерируемых имен: ", range(1, 11), int)
    return gender, race, quantity

# Генератор имени
def name_generator(race, quantity, gender):
    names = []
    for i in range(quantity):
        pref = choice(names_parts[race]["prefixes"])
        root = choice(names_parts[race]["roots"])
        if gender == "ж":
            suff = "a"
        else:
            suff = choice(names_parts[race]["suffixes"])
        name = pref + root + suff
        names.append(name)
        i += 1
    return names

# Вывод
def names_print(names):
    print("\n=== СПИСОК ИМЁН ===")
    for i, name in enumerate(names, start=1):
        print(f"{i}. {name}")

def main():
    gender, race, quantity = parametr_chose()
    names = name_generator(race, quantity, gender)
    names_print(names)


if __name__ == "__main__":
    main()
