from Education.week_8.coffee.coffee_machine import Menu, CoffeeMaker, MoneyMachine

def main():
    menu = Menu()
    maker = CoffeeMaker()
    money = MoneyMachine()
    
    while True:
        print("\n" + "=" * 40)
        print("Добро пожаловать в кофемашину!")
        print(f"Меню: {menu.get_items()}")
        print("Команды: отчёт / выключить")
        
        choice = input("Ваш выбор: ").lower().strip()
        print("\n")
        # Твоя логика здесь
        if choice == "выключить":
            print("До свидания!")
            break

        elif choice == "отчёт":
            maker.report()
            money.report()

        else:
            drink = menu.find_drink(choice)
    
            if drink is None:
                print("❌ Такого напитка нет в меню")
            else:
                if maker.is_sufficient(drink):
                    if money.process_coins(drink.cost):
                        maker.make_coffee(drink)

if __name__ == "__main__":
    main()