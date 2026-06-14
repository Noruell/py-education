remove = str.maketrans("", "", "+(),/- ") # Список очисти ввода

# Склонение вывода
def plural_form(n, form1, form2, form5):
    if 10 <= n % 100 <= 20:
        return form5
    if n % 10 == 1:
        return form1
    if 2 <= n % 10 <= 4:
        return form2
    return form5

in_secs = input("Введите количество секунд: ").translate(remove)

# Проверка на корректность ввода
if not in_secs:
    print("Ввод не может быть пустым!")
    exit()
elif in_secs.isdigit():
    in_secs = int(in_secs)
else: 
    print("Введите секунды цифрами!")
    exit()

# Рассчет времени
hours = in_secs // 3600
minutes = (in_secs // 60) % 60
secs = in_secs % 60

# Корректировка отображения
if hours >= 24:
    days = hours // 24
    hours = hours % 24
    print(f"Время: {days} {plural_form(days, 'день', 'дня', 'дней')}"
          f" {hours} {plural_form(hours, 'час', 'часа', 'часов')}"
          f" {minutes} {plural_form(minutes, 'минута', 'минуты', 'минут')}"
          f" {secs} {plural_form(secs, 'секунда', 'секунды', 'секунд')} ")
else:
    print(f"Время: {hours} {plural_form(hours, 'час', 'часа', 'часов')}"
          f" {minutes} {plural_form(minutes, 'минута', 'минуты', 'минут')}"
          f" {secs} {plural_form(secs, 'секунда', 'секунды', 'секунд')} ")