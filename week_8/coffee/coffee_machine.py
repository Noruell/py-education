class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("Эспрессо", 50, 0, 18, 150),
            MenuItem("Латте", 200, 150, 24, 250),
            MenuItem("Капучино", 250, 100, 24, 200)
        ]
    
    def get_items(self):
        names = [item.name for item in self.menu]
        return ', '.join(names)
    
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name.lower() == order_name.lower():
                return item 
        return None

class CoffeeMaker:
    def __init__(self):
        self.res = {
            "water": 1000,
            "milk": 500,
            "coffee": 200
        }
    
    def report(self):
        print(f"Вода: {self.res.get('water')} мл")
        print(f"Молоко: {self.res.get('milk')} мл")
        print(f"Кофе: {self.res.get('coffee')} г")

    def is_sufficient(self, drink):
        if self.res["water"] < drink.water:
            print("❌ Недостаточно воды")
            return False
        if self.res["milk"] < drink.milk:
            print("❌ Недостаточно молока")
            return False
        if self.res["coffee"] < drink.coffee:
            print("❌ Недостаточно кофе")
            return False
        return True
    
    def make_coffee(self, drink):
        self.res["water"] -= drink.water
        self.res["milk"] -= drink.milk
        self.res["coffee"] -= drink.coffee
        print(f"☕ Ваш {drink.name} готов! Приятного аппетита!")

class MoneyMachine:
    def __init__(self):
        self.profit = 0   
        self.coins = [1, 2, 5, 10]
    def report(self):
        print(f"💰 Выручка: {self.profit} руб.")

    def process_coins(self, cost):
        print(f"Стоимость напитка: {cost} руб.")
        print("Вносите монеты номиналом 1, 2, 5, 10 рублей.")

        total = 0
        for coin in self.coins:
            count = int(input(f"Сколько монет по {coin} руб.? "))
            total += coin * count

        if total < cost:
            print("❌ Недостаточно средств. Деньги возвращены.")
            return False
        if total > cost:
            change = total - cost
            print(f"✅ Сдача: {change} руб.")
        
        self.profit += cost
        print("💰 Оплата принята!")
        return True

