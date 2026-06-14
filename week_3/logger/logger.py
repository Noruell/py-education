from datetime import datetime as dt

def log_message():
    while True:
        message = input("Введите текст (или 'выход'): ").strip().lower()
        timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")

        if message == "выход":
            print("До свидания!")
            break
        elif not message:
            print("Ошибка: невозможно записать пустую строку!\n")
        else:
            try:
                with open("log.txt", "a", encoding="utf-8") as file:
                    file.write(f"{timestamp} - {message}\n")
                    print("Записано\n")
            except Exception as e:
                print(f"Ошибка при записи в файл: {e}")

if __name__ == "__main__":
    log_message()


