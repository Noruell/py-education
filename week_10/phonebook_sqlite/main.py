from db import (init_db, add_contact, get_all_contacts, 
                find_contacts_by_name, update_phone, delete_contact)

def print_contacts(contacts):
    if not contacts:
        print("Список контактов пуст!")
        return
    print("\nID | ИМЯ | ТЕЛЕФОН | EMAIL")
    print("-" * 50)
    for contact in contacts:
        print(f"{contact[0]} | {contact[1]} | {contact[2]} | {contact[3]}")

def main():
    init_db()

    while True:
        print("\n=== ТЕЛЕФОННАЯ КНИГА ===")
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Найти контакт")
        print("4. Обновить номер")
        print("5. Удалить контакт")
        print("6. Выйти")

        try:
            choice = int(input("\nВыбор: "))
        except TypeError:
            print("Неизвестная комманда!")
            continue

        if choice == 1:
            name = input("Имя: ")
            phone = input("Номер: ")
            email = input("email (необязательно): ")
            answ, result = add_contact(name, phone, email)
            print(result)
        elif choice == 2:
            contacts = get_all_contacts()
            print_contacts(contacts)
        elif choice == 3:
            name = input("Имя для поиска: ")
            print_contacts(find_contacts_by_name(name))
        elif choice == 4:
            name = input("Имя: ")
            new_phone = input("Новый номер: ")
            update_phone(name, new_phone)
            print(f"Контакт: {name} - обновлен!")
        elif choice == 5:
            name = input("Имя: ")
            delete_contact(name)
            print(f"Контакт: {name} - удален!")
        elif choice == 6:
            print("До свидания!")
            break
        else:
            print("Неизвестная комманда")

if __name__ == "__main__":
    main()