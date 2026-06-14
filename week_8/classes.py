class User:
    def __init__(self, name, greeting_word):
        self.name = name
        self.greeting_word = greeting_word

    def greeting(self):
        print(f"{self.greeting_word}, {self.name}!")

me = User("Максим", "Здравствуйте")

me.greeting()
print("\n")

# Задание для закрепления
# Создай класс Animal с атрибутами name и методом make_sound() (просто pass пока).
# Затем создай классы Dog и Cat, которые наследуют Animal. Переопредели make_sound() так, чтобы Dog выводил "Гав!", а Cat — "Мяу!".
# Создай объекты и вызови их методы.

class Animal():
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Какой-то звук")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name}: Гаф!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name}: Мяу!")

dog = Dog("Шарик")
cat = Cat("Соня")

dog.make_sound()
cat.make_sound()
print("\n")

# Создай класс BankAccount:
# Приватный атрибут __balance (начальный баланс 0)
# Метод deposit(amount) — увеличивает баланс (нельзя внести ≤ 0)
# Метод withdraw(amount) — уменьшает баланс (нельзя снять больше, чем есть)
# Метод get_balance() — возвращает баланс
# Создай объект, попробуй положить и снять деньги, выведи баланс.

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         if amount <= 0:
#             return
#         self.__balance += amount
#         print(f"Ваш баланс пополнен на: {amount} руб.")

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("На вашем счёте недостаточно средств")
#             return
#         self.__balance -= amount
#         print(f"Вы сняли: {amount} руб.")

#     def get_balance(self):
#         print(f"Ваш баланс: {self.__balance} руб.")
#         return self.__balance
    

# user1 = BankAccount()

# user1.deposit(1000)
# user1.withdraw(1100)
# user1.withdraw(500)
# user1.get_balance()

# Допиши в класс BankAccount из предыдущего задания:
# __str__ — возвращает строку "Баланс: X руб."
# __eq__ — два счёта равны, если у них одинаковый баланс
# Создай два счёта, пополни их до одинакового баланса и проверь account1 == account2.

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            return
        self.__balance += amount
        print(f"Ваш баланс пополнен на: {amount} руб.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("На вашем счёте недостаточно средств")
            return
        self.__balance -= amount
        print(f"Вы сняли: {amount} руб.")

    def get_balance(self):
        print(f"Ваш баланс: {self.__balance} руб.")
        return self.__balance
    
    def __str__(self):
        return f"Баланс: {self.__balance} руб."

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return self.__balance == other.__balance
    
account1 = BankAccount()
account2 = BankAccount()

account1.deposit(1000)
account2.deposit(1000)

print(account1 == account2)
print(account1)

# Создай класс Temperature:
# Атрибут класса _celsius (приватный)
# @classmethod from_celsius(cls, value) — создаёт объект
# @classmethod from_fahrenheit(cls, value) — переводит фаренгейты в цельсии и создаёт объект
# Обычный метод to_fahrenheit() — возвращает температуру в фаренгейтах
# __str__ для красивого вывода

# Формулы:
# F = C * 9/5 + 32
# C = (F - 32) * 5/9

class Temperature:
    def __init__(self, value):
        self._celsius = value
    
    @classmethod
    def from_celsius(cls, value):
        return cls(value)
    
    @classmethod
    def from_fahrenheit(cls, value):
        celsius = (value - 32) * 5 / 9
        return cls(celsius)
    
    def to_fahrenheit(self):
        f = self._celsius * 9 / 5 + 32
        return round(f, 2)
    
    def __str__(self):
        return f"{round(self._celsius, 2)}°C"

t1 = Temperature.from_celsius(25)
t2 = Temperature.from_fahrenheit(77)

print("\n")
print(t1)   # 25°C
print(t2)   # 25°C
print(t1.to_fahrenheit())   # 77.0