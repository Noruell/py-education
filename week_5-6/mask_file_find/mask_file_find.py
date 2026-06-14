import os
import fnmatch as fnm

ignore = [".git", "__pycache__"]
count = 0

def search(path, mask):
    global count
    for item in os.listdir(path):
        FULL_PATH = os.path.join(path, item)
        if item in ignore:
            continue
        if os.path.isdir(FULL_PATH):
            search(FULL_PATH, mask)
        else:
            if fnm.fnmatch(item, mask):
                print(FULL_PATH)
                count += 1

def main():
    print("=== ПОИСК ФАЙЛОВ ПО МАСКЕ ===")
    path = input("Путь для поиска: ")
    mask = input("Маска для поиска: ")

    print("\nНайденные пути:")
    search(path, mask)

    print(f"\nВсего найденных путей - {count}")

if __name__ == "__main__":
    main()
