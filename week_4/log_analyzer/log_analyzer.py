import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "log.txt")
STATS_PATH = os.path.join(BASE_DIR, "stats.txt")
os.chdir(BASE_DIR)

stats = {"INFO": 0, 
         "WARNING": 0, 
         "ERROR": 0}

def parse_log_line(line):
    line = line.split()
    return line[2]

def analyz_logs():
    lines = 0
    with open(LOG_PATH, "r", encoding="utf-8") as file:
        for line in file:
            lines += 1
            if line:
                level = parse_log_line(line)
                if level == "INFO": stats["INFO"] += 1
                elif level == "ERROR": stats["ERROR"] += 1
                elif level == "WARNING": stats["WARNING"] += 1
        return stats, lines

def print_stats(stats, lines):
    print("=== АНАЛИЗ ЛОГОВ ===")
    print(f"Всего строк: {lines}\n")
    print("Статистика по уровням:")
    for key, value in stats.items():
        print(f"{key}: {value}")

def save_stats(stats, lines):
    with open(STATS_PATH, "w", encoding="utf-8") as file:
        file.write(f"Строк обработано: {lines}\n")
        for key, value in stats.items():
            file.write(f"{key}: {value}\n")
    print("Данные сохранены в 'stats.txt'")

def main():
    stats, lines = analyz_logs()

    print_stats(stats, lines)
    save_stats(stats, lines)

if __name__ == "__main__":
    main()




