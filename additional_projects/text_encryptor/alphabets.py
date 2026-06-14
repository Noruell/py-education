# Алфавиты

ALPHABETS_DICT = {
    "русский": {
        "normal": "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
        "revers": "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"
        },
    "английский": {
        "normal": "abcdefghijklmnopqrstuvwxyz",
        "revers": "zyxwvutsrqponmlkjihgfedcba"
    }  
}


# Тесты
if __name__ == "__main__":
    print("=" * 7, "СПИСОК ЯЗЫКОВ И АЛФАВИТОВ", "=" * 7, "\n")
    for outer_key, inner_dict in ALPHABETS_DICT.items():
        print(f"Язык: {outer_key}")

        for key, value in inner_dict.items():
            print(f"{key}: {value}")
        print("\n", '=' * 40, "\n")

