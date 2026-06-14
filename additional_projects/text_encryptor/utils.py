from Education.additional_projects.text_encryptor.alphabets import ALPHABETS_DICT
from Education.additional_projects.text_encryptor.chipher_methods import CHIPHER_METHODS
import os
from datetime import datetime as dt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def safe_input(prompt, options, data_type=str):
    """Универсальный безопасный ввод"""
    while True:
        user_input = input(prompt).strip()
        if data_type == int:
            try:
                user_input = int(user_input)
            except ValueError:
                print(f"Ошибка! введите число из {options}\n")
                continue
        elif data_type == str:
            user_input = user_input.lower()

        if user_input in options:
            return user_input
        print(f"Ошибка! Введите {options}\n")

def choose_language(alphabets):
    """Динамическое построение меню выбора языка"""
    print("\nВыберите язык:")
    keys = list(alphabets)
    for i, lang in enumerate(alphabets, start=1):
        print(f"{i}. {lang.title()}")
    choice = safe_input("Ваш выбор: ", range(1, len(keys) + 1), int)
    return keys[choice - 1]

def choose_action():
    """Выбор действия"""
    print("\nВыбор действия:")
    print("1. Зашифровать")
    print("2. Расшифровать")
    choice = safe_input("Ваш выбор: ", {1, 2}, int)
    return "encrypt" if choice == 1 else "decrypt"

def choose_chipher(chiphers_list):
    """Динамическое построение способов шифрования"""
    print("\nВыберите метод:")
    for key, value in chiphers_list.items():
        print(f"{key}. {value}")
    choice = safe_input("Ваш выбор: ", range(1, len(chiphers_list.keys()) + 1), int)
    return chiphers_list.get(choice).lower()

def get_text():
    """Получает текст (ввод или из файла)"""
    choice = safe_input("\n1. Ввести с клавиатуры\n2. Загрузить из файла\nВаш выбор: ", {1, 2}, int)
    if choice == 1:
        return input("Введите текст: ").lower()
    else:
        filename = input("Имя файла: ")
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print("Ошибка! Файл не найден!")
            return get_text()

def get_shift():
    """Получение сдвига для цезаря"""
    return safe_input("Введите сдвиг: ", range(-100, 101), int)

def get_xor_key():
    """Получение ключа для XOR"""
    allowed = set(
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "123456789!@#$%^*()_+-=/"
    )
    return safe_input("Введите ключ (один символ): ", allowed, str)

def format_result(result):
    if isinstance(result, list):
        result = " ".join(map(str, result))
        return result
    return result

def save_result(chipher, text, result, key=None):
    """Сохранение в history.txt"""
    result = format_result(result)
    with open("history.txt", "a", encoding="utf-8") as f:
        if key is not None:
            f.write(f"{chipher} ({key}): {text} -> {result}\n")
        else:
            f.write(f"{chipher}: {text} -> {result}\n")

def auto_log(timestamp, chipher, text, result, key=None):
    """Автосохранение в log.txt"""
    result = format_result(result)
    with open("log.txt", "a", encoding="utf-8") as f:
        if key is not None:
            f.write(f"[{timestamp}] Метод: {chipher.title()} | Ключ: {key} | Исходное: {text} | Результат: {result}\n")
        else:
            f.write(f"[{timestamp}] Метод: {chipher.title()} | Исходное: {text} | Результат: {result}\n")



if __name__ == "__main__":
    timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    KEY = choose_language(ALPHABETS_DICT)
    print(KEY)
    kk = choose_chipher(CHIPHER_METHODS)
    print(kk)
    k = get_text()
    print(k)
    get_xor_key()
    save_result("XOR", "привет, Андрей", [15, 112, 8, 2, 5, 114, 1052, 1040, 32, 13, 4, 112, 5, 9], key="а")
    save_result("Переворот", "привет", "тевирп")
    auto_log(timestamp, "Переворот", "привет", "тевирп")
    auto_log(timestamp, "XOR", "привет, Андрей", [15, 112, 8, 2, 5, 114, 1052, 1040, 32, 13, 4, 112, 5, 9], key="а")