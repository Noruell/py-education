from random import choices, shuffle

# Переменные
alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
characters = list("!@#$%^&*")

# Генератор
def password_generator(length=8, use_digits=True, use_symbols=False):
    if length <= 0:
        raise ValueError("Длина пароля не может быть 0 или меньше")

    pool = list(alphabet)

    if use_digits == True:
        pool.extend(numbers)
    if use_symbols == True:
        pool.extend(characters)
    
    password = choices(pool, k=length)
    shuffle(password)

    return "".join(password)

# Тесты
if __name__ == "__main__":
    print("=" * 33)
    print("Тестирование генератора паролей:")
    print(f"Пароль по умолчанию: {password_generator()}")
    print(f"12 символов с символами: {password_generator(6, use_symbols=True)}")
    print(f"10 символов без цифр: {password_generator(10, use_digits=False)}")
    print(f"12 символов со всем: {password_generator(12, use_digits=True, use_symbols=True)}")
    print(f"0 символов: {password_generator(0)}")
    print("=" * 33)