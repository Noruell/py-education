from datetime import datetime, timedelta


def get_month_name(month):
    month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                   "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    return month_names[month - 1]

def get_days_in_month(year, month):
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    first_day = datetime(year, month, 1)
    return (next_month - first_day).days

def main():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц (1-12): "))
    
    first_day = datetime(year, month, 1)
    start_weekday = first_day.weekday()
    days_in_month = get_days_in_month(year, month)
    
    # Генератор списка дней
    days = [f"{day:2}" for day in range(1, days_in_month + 1)]
    calendar = ["  "] * start_weekday + days
    
    print(f"\n     {get_month_name(month)} {year}")
    print("Пн Вт Ср Чт Пт Сб Вс")
    
    for i in range(0, len(calendar), 7):
        week = calendar[i:i+7]
        print(" ".join(week))

if __name__ == "__main__":
    main()