import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_NAME = os.path.basename(__file__)
os.getcwd()

# Получение списка всех файлов в папке с проектом
def get_files():
    filename = []
    for i in os.listdir(os.path.abspath(BASE_DIR)):
        path = os.path.join(BASE_DIR, i)
        if os.path.exists(path): 
            if os.path.isfile(path) and i != SCRIPT_NAME:
                filename.append(i)
    return filename

# Получения расширений
# def get_extension(filename):
#     ext = []
#     for file in filename:
#         extension = os.path.splitext(file)
#         ext.append(extension[-1].replace(".", ""))
#     return ext
def get_extension(filename):
    extension = os.path.splitext(filename)
    return extension[-1].replace(".", "")

# Создание папок для каждого расширения
def create_folder(folder_name):
    for folder in folder_name:
        if os.path.exists(os.path.join(BASE_DIR, folder)) and os.path.isdir(os.path.join(BASE_DIR, folder)):
            print(f"Папка с названием {folder} уже есть")
            continue
        else:
            os.makedirs(os.path.join(BASE_DIR, folder))
            print(f"Папка {folder} созданна")

def file_move(file):
    shutil.move(os.path.join(BASE_DIR), os.path.join(BASE_DIR, get_extension(file)))

def organize_files():
    for file in get_files():
        if get_extension(file) == "csv":
            file_move(file)
        elif get_extension(file) == "txt":
            file_move(file)
        elif get_extension(file) == "jpg":
            file_move(file)
        elif get_extension(file) == "png":
            file_move(file)
        elif get_extension(file) == "py":
            file_move(file)
        


if __name__ == "__main__":
    # organize_files()
