from phone_book_commands import (commands, contact_add, contact_delete, 
                                 contact_find, contact_list, program_close,
                                 load_contacts, save_contacts)

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
                save_contacts()
                break
        else:
            print("Неизвестная команда! Выберите из списка команд (1-5).\n")
