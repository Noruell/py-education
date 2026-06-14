import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "input.txt")
OUTPUT_PATH = os.path.join(BASE_DIR, "unique_words.txt")

# Очистка слов от знаков препинания
def clean_word(word):
    return word.strip(".,!?;:()\"'-").lower()

# Получение списка слов из input.txt
def words_read():
    global input_words
    input_words = []

    if not os.path.exists(INPUT_PATH):
        print("Файл 'input.txt' не найден!")
        return input_words
    
    with open(INPUT_PATH, "r", encoding="utf-8") as file:
        for line in file:
            raw_words = line.strip().split()
            for raw_word in raw_words:
                clean = clean_word(raw_word)
                if clean:
                    input_words.append(clean)
    return input_words

# Получение уникальныйх слов
def get_unique_words(words):
    return set(words)


# Запись уникальных слов в файл
def save_unique_words(unique_words):
    try:
        with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
            for word in unique_words:
                file.write(f"{word}\n")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    words = words_read()

    if not words:
        print("Нет слов для обработки!")
        return
    
    unique_words = get_unique_words(words)

    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(unique_words)}")
    print(f"Слова: {', '.join(sorted(unique_words))}")

    save_unique_words(unique_words)
    print(f"\nУникальные слова сохранены в '{OUTPUT_PATH}'")



if __name__ == "__main__":
    main()