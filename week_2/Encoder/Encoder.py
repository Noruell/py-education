from encoder_lang import ru_lang, en_lang

# Переменные
encoded = []
language_list = ["Русский", "Английский"]

# Безопасный ввод чисел
def safe_input_number(prompt, data_type):
    while True:
        user_input = input(prompt).strip()
        if user_input and (user_input[0] == '-' and user_input[1:].isdigit() or user_input.isdigit()):
            return data_type(user_input)
        print("Некорректный ввод!\n")

# Безопасный ввод слова
def safe_input_word(prompt):
    alphabet_set = set(language)

    while True:
        user_input = input(prompt).lower().strip()
        
        if user_input and set(user_input).issubset(alphabet_set):
                return user_input
        print("Некорректный ввод!\n")


# Вывод доступных языков
print("=== Список языков ===")
for i, lang in enumerate(language_list, start=1):
    print(f"{i}. {lang}")

# Выбор языка
lang_chose = safe_input_number("Выберите язык: ", int)

if lang_chose == 1:
    language = ru_lang
    print("Выбран: Русский\n")

elif lang_chose == 2:
    language = en_lang
    print(f"Выбран: Английский\n")

# Ввод слова и сдвига
user_word = safe_input_word("Введите слово: ")
user_shift = safe_input_number("Введите сдвиг: ", int)


# Шифратор
for letter in user_word:
    old_index = language.index(letter)
    new_index = (old_index + user_shift) % len(language)

    encoded.append(language[new_index])

print(f"\nЗашифрованное слово: {''.join(encoded)}")
