import os
import shutil
import fnmatch as fnm
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "data", "state.json")

actions = ["Перейти в папку", "Создать папку", "Удалить файл/папку", "Копировать файл", 
           "Переместить файл", "Поиск по маске", "Выйти"]
clear = lambda: os.system("cls")

def list_directory(path):
    """ Принимает путь к папке\n
    Выводит все папки с эмодзи 📁\n
    Выводит все файлы с эмодзи 📄\n
    Выводит общее количество папок и файлов"""
    if not os.path.exists(path):
        print(f"Путь '{path}' не существует!")
        return
    
    items = os.listdir(path)

    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]

    for d in sorted(dirs):
        print(f"📁 {d}")
    for f in sorted(files):
        print(f"📄 {f}")


def create_folder(path, folder_name):
    """Принимает путь и имя новой папки\n
    Создаёт папку\n
    Если папка уже существует — выводит сообщение\n
    Если путь не существует — выводит сообщение"""

    new_folder = os.path.join(path, folder_name)
    
    if not os.path.exists(path):
        print(f"Пути '{path}' не существует.")
    elif os.path.exists(new_folder):
        print(f"Папка с именем '{folder_name}' уже существует.")
    else:
        os.makedirs(new_folder)

def delete_item(path, item_name):
    """Принимает путь и имя файла/папки\n 
    Удаляет файл или пустую папку\n 
    Если это папка с содержимым — выводит сообщение 'Папка не пуста'\n 
    Если файла/папки не существует — выводит сообщение"""

    item = os.path.join(path, item_name)

    if os.path.isdir(item):
        if len(os.listdir(item)) > 0:
            print("Папка не пуста")
        else:
            os.rmdir(item)
            print(f"Папка '{item}' удалена")
    elif os.path.isfile(item):
        try:
            os.remove(item)
            print(f"Файл '{item}' удален")
        except FileNotFoundError:
            print(f"Ошибка: файла {item_name} не существует")
    else:
        print(f"Элемент '{item_name}' не найден")

def copy_file(source_path, dest_path):
    """Принимает путь к исходному файлу и путь для копирования\n
    Проверяет, существует ли исходный файл\n
    Создаёт папку назначения, если её нет\n
    Копирует файл"""
    if not os.path.exists(source_path):
        print("Исходный файл не существует")
        return
    
    dest_dir = os.path.dirname(dest_path)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)
    
    shutil.copy2(source_path, dest_path)

def move_file(source_path, dest_path):
    if not os.path.exists(source_path):
        print("Исходный файл не существует")
        return
    
    dest_dir = os.path.dirname(dest_path)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)
    try:
        shutil.move(source_path, dest_path)
    except shutil.Error as e:
        print(f"Ошибка {e}")
        return

def search_file(path, mask):
    result = []
    if not os.path.exists(path):
        print("Путь не существует")
        return []
    for item in os.listdir(path):
        FULL_PATH = os.path.join(path, item)
        if os.path.isdir(FULL_PATH):
            result.extend(search_file(FULL_PATH, mask))
        else:
            if fnm.fnmatch(item, mask):
                    result.append(FULL_PATH)
    return result

def save_current_path(path):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump({"current_path": path}, f, ensure_ascii=False, indent=2)

def load_current_path():
    if not os.path.exists(JSON_PATH):
        return os.getcwd()
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("current_path", os.getcwd())
    except (json.JSONDecodeError, FileNotFoundError):
        return os.getcwd()

def print_menu(current_path):
    print(f"Текущая папка: {current_path}\n")
    print("Содержимое:")
    list_directory(current_path)
    print("\nДействия:")
    for i, action in enumerate(actions, start=1):
        print(f"{i}. {action}")

def safe_input(prompt, options):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit() and int(user_input) in options:
            return int(user_input)
        print(f"Ошибка! Введите число от {min(options)} до {max(options)}")

def main():
    current_path = load_current_path()
    print("=== КОНСОЛЬНЫЙ ФАЙЛОВЫЙ МЕНЕДЖЕР ===")
    while True:
        print_menu(current_path)

        choice = safe_input("\nВыбор: ", range(1, len(actions) + 1))

        if choice == 1:
            dir_to_move = input("Имя папки: ")
            new_path = os.path.join(current_path, dir_to_move)
            if os.path.isdir(new_path):
                current_path = new_path
            else:
                print("Папка не существует!")
        elif choice == 2:
            dir_name = input("Имя новой папки: ")
            create_folder(current_path, dir_name)
        elif choice == 3:
            item_name = input("Имя папки/файла: ")
            delete_item(current_path, item_name)
        elif choice == 4:
            source_path = input("Какой файл копировать? (полный путь): ")
            dest_path = input("Куда? (полный путь): ")
            copy_file(source_path, dest_path)
        elif choice == 5:
            source_path = input("Какой файл переносим? (полный путь): ")
            dest_path = input("Куда? (полный путь): ")
            move_file(source_path, dest_path)
        elif choice == 6:
            path = input("Где искать? (полный путь): ")
            mask = input("Маска: ")
            result = search_file(path, mask)
            print(f"\nНайдено файлов: {len(result)}")
            for res in result:
                print(res)
        elif choice == 7:
            save_current_path(current_path)
            print("До свидания!")
            break

if __name__ == "__main__":
    clear()
    main()

