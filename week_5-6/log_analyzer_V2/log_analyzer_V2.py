from datetime import datetime as dt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

stats = {"INFO": 0, "WARNING": 0, "ERROR": 0, "DEBUG": 0, "CRITICAL": 0}

def parse_line(line):
    """Преобразует строку лога в словарь {'date': ..., 'level': ..., 'message': ...}"""
    # Использовать split() и datetime.strptime()
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        return None
    
    date_str = f"{parts[0]} {parts[1]}"
    date = dt.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return {
        "date": date,
        "level": parts[2],
        "message": parts[3]
    }

def main():
    with open("log.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    parsed = list(map(parse_line, lines))
    parsed = [p for p in parsed if p is not None]

    target = input("Введите дату (ГГГГ-ММ-ДД): ")
    target_date = dt.strptime(target, "%Y-%m-%d").date()

    filtered = list(filter(lambda x: x["date"].date() == target_date, parsed))

    stats = {"INFO": 0, "WARNING": 0, "ERROR": 0, "DEBUG": 0, "CRITICAL": 0}
    for entry in filtered:
        stats[entry["level"]] += 1

    print(f"\n=== СТАТИСТИКА ЗА {target}")
    for level, count in stats.items():
        print(f"{level}: {count}")
    
    print(f"\n=== ЗАПИСИ ({len(filtered)} шт) ===")
    for entry in filtered:
        print(f'{entry["date"]} - {entry["level"]} - {entry["message"]}')

if __name__ == "__main__":
    main()