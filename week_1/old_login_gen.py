name = input("Введите имя: ").replace(" ", "")
surname = input("Введите фамилию: ").replace(" ", "")
study_card = input("Введите номер студенческого билета: ").replace(" ", "")

if not name:
    print("Заполните поле: Имя")
elif not surname:
    print("Заполните поле: Фамилия")
elif not study_card:
    print("Заполните поле: Номер студ билета")
elif not study_card.isdigit():
    print("Номер билета должен состоять из цифр!")
else:
    login = (name[0] + surname[:5] + study_card[-2:]).lower()
    print(f"Ваш логин: {login}")