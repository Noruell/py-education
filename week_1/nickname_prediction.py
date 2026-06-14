name = input("Введите имя: ").lower()
surname = input("Введите фамилию: ").lower()
age = input("Введите год рождения: ")


if not name:
    print("Имя не может быть пустым")
elif not surname:
    print("Фамилия не может быть пустой")
elif not age:
    print("Год рождения не может быть пустой")
else: 
    if int(age) <= 2008:
        task = "Вам завтра на работу!!!"
    else:
        task = "Вы проспите до обеда!"
    nickname = (name[0]+name[-1]+surname[0]+surname[-1]+age[-2:]).title()
    print(f"Я предсказываю что ваше супергеройское имя {nickname}. {task}")