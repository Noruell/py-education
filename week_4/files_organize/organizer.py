import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.basename(__file__)
fold = []

# =========== ТЕСТИЛ СМЕНУ ДИРЕКТОРИИ ===========
# print(f"Начальная дирректория: {os.getcwd()}")
os.chdir(BASE_DIR)
# print(f"Поменяная дирректория: {os.getcwd()}")
# ===============================================

# Получаем все файлы в директории кроме нашего скрипта
def get_files():
    files = []
    for file in os.listdir():
        if file == SCRIPT_PATH:
            continue
        elif os.path.exists(file) and not os.path.isdir(file):
            files.append(file)
    return files

# Получаем расширение файлаы
def get_extansion(filename):
    name, ext = os.path.splitext(filename)
    return ext[1:]

# Создать папку для конкретного расширения
def create_folder(folder_name):
    if os.path.exists(folder_name):
        return folder_name
    else:
        fold.append(folder_name)
        os.makedirs(folder_name)
        return folder_name
    
# Основная логика
def organize_files():
    files = get_files()
    moved = []
    for file in files:
        PATH_TO_MOVE = os.path.join(BASE_DIR, create_folder(get_extansion(file)))
        shutil.move(file, PATH_TO_MOVE)
        moved.append(file)
    return files, moved

def main():
    files, moved = organize_files()

    print("=== ОРГАНАЙЗЕР ФАЙЛОВ ===")
    print(f"Найдено файлов: {len(files)}")
    print(f"Перемещено: {len(moved)}")
    print(f"Созданы папки: {', '.join(fold)}")

    print("\nГотово!")


if __name__ == "__main__":
    main()


        


