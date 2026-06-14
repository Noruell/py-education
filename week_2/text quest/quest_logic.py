# ======== ИМПОРТ БИБЛИОТЕК И СЦЕНАРИЯ ========
from random import randint
from rich import print
from quest_screenplay import *


# ======== ИГРОК =========
player_alive = True
player_health = 100
player_damage = 50
has_key = False

# ======== МОНСТР ========
monster_health = 100
monster_damage = 50

# ======== ЛОВУШКИ ========
trap_damage = 100


# ======== ПРОВЕРКА БЕЗОПАСНОСТИ ВВОДА ========
def safe_input(prompt, options):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) in options:
            return int(user_input)
        print(f"Ошибка! Введите {options}")

# ======= ВЫБОР СЛОЖНОСТИ =======
def difficulty_selection():
    global monster_damage
    global trap_damage
    global game_diff

    game_diff = safe_input("\nВыберите уровень сложности (1/2):", {1, 2})
    print_separator()
    if game_diff == 1:
        monster_damage = 25
        trap_damage = 50

        print("Выбранная сложность: [bold green]ЛЕГКАЯ[/bold green]")
    elif game_diff == 2:
        print("Выбранная сложность: [bold yellow]НОРМАЛЬНАЯ[/bold yellow]")

    

# ======== БИТВА =========
def fight_health_display():
    print_separator()
    print(f"Ваше здоровье: {player_health}")
    print(f"Здоровье монстра: {monster_health}")
    print_separator()

def fight():
    global player_damage, player_health, monster_damage, monster_health

    while player_health > 0 and monster_health > 0:
        print_separator()
        input("\nНажмите Enter, что бы бросить кубик...\n")

        player_dice = randint(1, 6)
        monster_dice = randint(1, 6)

        print(f"Монстру выпало число: {monster_dice}")
        print(f"Вам выпало число: {player_dice}")
        print_separator()

        if player_dice > monster_dice:
            monster_health -= player_damage
            print("- Вы проводите успешную атаку!")
            print(f"Монстр теряет {player_damage} здоровья!")
        elif monster_dice > player_dice:
            player_health -= monster_damage
            print("- Монстр проводит успешную атаку!")
            print(f"Вы теряете {monster_damage} здоровья!")
        else:
            print("Ничья! Никто не реяет здоровья.")
    
    if player_health <= 0:
        scene_defeat_goblin()
        return False
    elif monster_health <= 0:
        scene_victory_with_treasure()
        return True

# ======== ИГРА ========
def main():
    player_welcome()
#    difficulty_info()
#    difficulty_selection()
    scene_intro()

    # Первая локация
    scene_first_room()
    choice = safe_input("Ваши действия (1/2): ", {1, 2})
    print_separator()
    
    if choice == 1:
        print("На столе лежит ржавый ключ, взять?")
        print("1. Да")
        print("2. Нет")
        choice = safe_input("Взять ключ? ", {1, 2})
        
        if choice == 1:
            has_key = True
            key_found()
            scene_corridor()
            choice = safe_input("Куда пойдете? ", {1, 2, 3})

            if choice == 1:
                scene_goblin_room()
                choice = safe_input("Ваши действия? ", {1, 2})

                if choice == 1:
                    scene_goblin_escape()
                    choice = safe_input("Куда теперь? ", {1, 2})

                    if choice == 1:
                        scene_trap()

                    elif choice == 2:
                        scene_good_ending()

                elif choice == 2:
                    scene_goblin_fight()
                    fight_rules()
                    fight_health_display()
                    fight()

            elif choice == 2:
                scene_trap()

            elif choice == 3:
                scene_good_ending()

        elif choice == 2:
            scene_bad_ending_no_key()

    elif choice == 2:
        scene_bad_ending_do_nothing()
        

main()