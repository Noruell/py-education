# Точка входа, управление программой
from alphabets import ALPHABETS_DICT
from chipher_methods import (
    CHIPHER_METHODS, caesar, atbash,
    flip, xor_encrypt, xor_decrypt
)
from utils import (
    choose_language, choose_action, choose_chipher,
    get_text, get_shift, get_xor_key,
    save_result, auto_log, safe_input
)
from datetime import datetime as dt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

def main():
    while True:
        print("===== ШИФРАТОР =====")
        language = choose_language(ALPHABETS_DICT)
        action = choose_action()
        method = choose_chipher(CHIPHER_METHODS)
        
        text = get_text()

        key = None
        result = None

        if method == "цезарь":
            shift = get_shift()
            key = shift
            result = caesar(text, shift, ALPHABETS_DICT, language)
        elif method == "атбаш":
            result = atbash(text, ALPHABETS_DICT, language)
        elif method == "переворот строки":
            result = flip(text)
        elif method == "xor":
            key = get_xor_key()
            if action == "encrypt":
                result = xor_encrypt(text, key)
            else:
                if isinstance(text, str) and " " in text:
                    text_list = list(map(int, text.split()))
                else:
                    text_list = text  
                result = xor_decrypt(text_list, key)

        print(f"\nРезультат: {result}")

        timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        auto_log(timestamp, method, text, result, key=key)

        choice = safe_input("\nСохранить результат в файл? (да/нет): ", {"да", "нет"}, str)
        if choice == "да":
            save_result(method, text, result, key=key)
            print("Сохранено в 'history.txt'")
        
        again = safe_input("\nПовторить? (да/нет) ", {"да", "нет"}, str)
        if again != "да":
            print("До свидания!")
            break


if __name__ == "__main__":
    main()