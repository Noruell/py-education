login = "Admin"
password = "admin123"

user_login = input("Введите логин: ")
user_password = input("Введите пароль: ")

if user_login != login:
    print("Неверный логин!")
elif user_password != password:
    print("Неверный пароль!")
else:
    print("-" * 20)
    print("Вы вошли в систему")
    print("-" * 20)