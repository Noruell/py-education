import os

# Переменные
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTACTS_PATH = os.path.join(BASE_DIR, "contacts.txt")

command_list = {1: "Добавить контакт",
                2: "Найти контакт",
                3: "Удалить контакт",
                4: "Показать все контакты",
                5: "Выйти"}

contacts = {}

# Загрузка контактов из файла
def load_contacts():
    global contacts
    contacts = {}
    if not os.path.exists(CONTACTS_PATH):
        return contacts
    with open(CONTACTS_PATH, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                name, phone = line.split("|")
                contacts[name] = phone
    return contacts

# Сохранение контактов в файл
def save_contacts():
    with open(CONTACTS_PATH, "w", encoding="utf-8") as file:
        for name, phone in contacts.items():
            file.write(f"{name}|{phone}\n")

    
# Корректный ввод
def safe_name(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Ошибка: имя не может быть пустым!")
        else:
            return user_input.title()

def safe_phone(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Ошибка: номер не может быть пустым!")
        else:
            return user_input

# Добавить контакт
def contact_add():
    name = safe_name("Имя: ")
    phone = safe_phone("Номер: ")
    contacts[name] = phone
    print(f"Контакт '{name}' добавлен!")

# Найти контакт
def contact_find():
    name = safe_name("Имя: ")
    if name in contacts:
        print(f"Номер: {contacts[name]}")
    else:
        print(f"{name} - не найдено в списке контактов!")

# Удаление контакта
def contact_delete():
    name = safe_name("Имя: ")
    if name in contacts:
        del contacts[name]
        print(f"Контакт '{name}' удален!")
    else:
        print(f"{name} - не найдено в списке контактов!")

# Просмотр всех контактов
def contact_list():
    if not contacts:
        print("Список контактов пуст.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

# Закрыть программу
def program_close():
    print("До свидания!")
    return False

# Вывод списка команд
def commands():
    print("\n=== ТЕЛЕФОННАЯ КНИГА ===")
    for num, command in command_list.items():
        print(f"{num}. {command}")

# Тест
if __name__ == "__main__":
    contacts = load_contacts()
    while True:
        commands()
        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            contact_add()
        elif choice == "2":
            contact_find()
        elif choice == "3":
            contact_delete()
        elif choice == "4":
            contact_list()
        elif choice == "5":
            if not program_close():
                break
        else:
            print("Неизвестная команда! Выберите из списка команд (1-5).\n")

