import random
from rich import print


# Игрок
player_alive = True
player_health = 100
has_key = False
has_treaser = False

# Монстр
monster_alive = True
monster_health = 100

# Текстовые делители, сообщения
gameover = "[bold red]ИГРА ОКОНЧЕНА[/bold red]"
victory = "[bold green]ПОБЕДА![/bold green]"
separator = "=" * 33
trap_death_msg = (f"{separator}\n"
                   "- Вы входите в комнату\n"
                   "- Пока вы осматриваетесь на вас с потолка обрушивается плита с шипами\n" 
                   "- Не успев испугаться вы умирате\n"
                  f"{separator}\n")
key = "[green]Теперь у вас есть ключ![/green]"
fight_rules = ("[bold yellow]Подсказка[/bold yellow]:\n"
              "1. Враг подбрасывает кубик, затем вы\n"
              "2. Если ваше число оказалось больше, вы проводите успешную атаку\n"
              "3. Если ваше число оказалось меньше, успешную атаку проводит враг\n"
              "4. [bold red]БИТВА ВЕДЁТСЯ ДО ЧЬЕЙ ЛИБО СМЕРТИ[/bold red]\n"
              "   [bold red]УДАЧИ[/bold red]\n")
              
# Приветствие с игроком
print("=" * 55)
print("Добро пожаловать в текстовый квест: [bold red]ПОДЗЕМЕЛЬЕ ГОБЛИНОВ[/bold red]")
print("=" * 55)

# Предыстория
print("=" * 10, "[bold red]ПРЕДЫСТОРИЯ[/bold red]", "=" * 10)
print("- Ты пошел исследовать шахту")
print("- Бродя по тёмным изгибам спотыкаешь и падаешь в глубокую яму...")
print("- ...")
print("- Когда ты очнулся тебя окружала мрачная комната с каменными стенами")
print("- В углу комнаты ты заметил старый деревянный стол")
print("- В дальней части комнаты находится дверь")
print(separator)

# Начало игры
print("1. Подойти и осмотреть стол")
print("2. Ничего не делать")
choice = int(input("Ваши действия (1/2): "))
print(separator)

# Первая локация
if choice == 1:
    print("На столе лежит ржавый ключ, взять?")
    print("1. Да")
    print("2. Нет")
    choice = int(input("Взять ключ? (1/2): "))
    print(separator)
    
    # Переход в локацию Коридор
    if choice == 1:
        has_key = True
        print(key)
        print(separator)

        print("- Вы подходите к двери, вставляете ключ в замочную скважину и проворачиваете")
        print("- Дверь с режущим уши скрипом отворяется")
        print("- Вы поподаете в коридор и видите три прохода:")
        print("1. Налево")
        print("2. Прямо")
        print("3. Направо")
        choice = int(input("Куда пойдешь: (1/2/3): "))

        # Локация с гоблином
        if choice == 1:
            print(separator)
            print("- Вы аккуратно заходите в комнату")
            print("- Из за угла выходит старый гоблин охраняющий сокровища")
            print("[bold green]Гоблин[/bold green]: Кто ты?! Проваливай!! Иначе я тебя убью!!!")
            print("1. Сбежать")
            print("2. Вступить в битву")
            choice = int(input("Ваш выбор (1/2): "))

            # Избегание битвы
            if choice == 1:
                print(separator)
                print("- Переполненные страхом вы возвращаетесь в коридор")
                print("- У вас осталось два пути")
                print("1. Прямо")
                print("2. Направо")
                choice = int(input("В каком направлении пойдёшь (1/2): "))

                # Комната с ловушкой
                if choice == 1:
                    print(separator)
                    print(trap_death_msg)
                    print(gameover)
                    exit()
                
                # Первая концовка
                elif choice == 2:
                    print(separator)
                    print("- Пройдя в комнату вы видите лестницу и слабый свет")
                    print("- Вы поднимаетесь по лестнице")
                    print("- Свет становится ярче и ближе")
                    print("- Вас охватывает чувство эйфории")
                    print("- Вы выбрались и жили долго и счастливо")
                    print(separator)
                    print(victory)
                    exit()

            # Битва с гоблином
            elif choice == 2:
                print(separator)
                print("- Вы собрались с силами и решились вступить в битву!")
                print(separator)
                print(fight_rules)
                print(separator)
                print("[bold red]БИТВА С[/bold red]: [bold green]СТАРЫЙ ГОБЛИН[/bold green]")
                print(f"Ваше здоровье: {player_health}")
                print(f"Здоровье гоблина: {monster_health}")

                # Битва
                while player_health > 0 and monster_health > 0:
                    input("\nНажмите Enter, что бы бросить кубик...")

                    player_dice = random.randint(1, 6)
                    monster_dice = random.randint(1, 6)

                    print(f"Число на кубике монстра: {monster_dice}")
                    print(f"Число на вашем кубике: {player_dice}")

                    if player_dice > monster_dice:
                        damage = 50
                        monster_health -= damage
                        print(f"Вы атакуете! Монстр теряет {damage} здоровья!")
                        print(separator)
                    elif monster_dice > player_dice:
                        damage = 50
                        player_health -= damage
                        print(f"Атакует монстр! Вы теряете {damage} здоровья!")
                        print(separator)
                    else:
                        print("Ничья! Никто не теряет здоровья")
                        print(separator)

                # Проверка победителя   
                if player_health <= 0:
                    print("- Беда, вас загрыз гоблин!")
                    print(separator)
                    print(gameover)
                    player_alive = False
                    exit()
                elif monster_health <= 0:
                    print("- Поздравляю! Вы одолели гоблина, забрали сокровища которые он охранял")
                    print("- И жили долго, счастливо и богато!")
                    print(separator)
                    print(victory)
                    exit()
        
        # Комната с ловушкой
        elif choice == 2:
            print(trap_death_msg)
            print(separator)
            print(gameover)
            exit()
        
        # Первая концовка
        elif choice == 3:
            print(separator)
            print("- Пройдя в комнату вы видите лестницу и слабый свет")
            print("- Вы поднимаетесь по лестнице")
            print("- Свет становится ярче и ближе")
            print("- Вас охватывает чувство эйфории")
            print("- Вы выбрались и жили долго и счастливо")
            print(separator)
            print(victory)
            exit()

    # Плохая концовка
    elif choice == 2:
        print("- Вы не решаетесь брать ключ")
        print("- В полном отчаянии вы сходите с ума, замерзаете и умираете от голода")
        print(separator)
        print(gameover)
        player_alive = False
        exit()
elif choice == 2:
    print(separator)
    print("- Вы не решаетесь что то делать")
    print("- В полном отчаянии вы сходите с ума, замерзаете и умираете от голода")
    print(separator)
    print(gameover)
    player_alive = False
    exit()