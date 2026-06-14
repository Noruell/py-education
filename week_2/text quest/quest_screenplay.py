from rich import print

# ============ КОНСТАНТЫ ============
LONG_SEPARATOR = "=" * 55
SEPARATOR = "=" * 33
GAMEOVER = "[bold red]ИГРА ОКОНЧЕНА[/bold red]"
VICTORY = "[bold green]ПОБЕДА![/bold green]"
KEY_FOUND = "[green]Теперь у вас есть ключ![/green]"

# ============ФУНКЦИИ ДЛЯ ВЫВОДА СЦЕН ========
def print_separator():
    print(SEPARATOR)

def print_long_separator():
    print(LONG_SEPARATOR)

def print_gameover():
    print(GAMEOVER)

def print_victory():
    print(VICTORY)

# =========== ОПИСАНИЕ СЛОЖНОСТИ ==========
def difficulty_info():
    print_separator()
    print("[bold yellow]ОПИСАНИЕ СЛОЖНОСТИ[/bold yellow]\n")
    print("1. [bold green]ЛЕГКАЯ[/bold green]:")
    print("- Монстры наносят меньше урона")
    print("- Вы не умираете от ловушек моментально\n")
    print("2. [bold yellow]НОРМАЛЬНАЯ[/bold yellow]:")
    print("- Нормальный урон монстра")
    print("- Вы умираете от ловушек")

# =========== СЦЕНЫ ===========
def player_welcome():
    print_long_separator()
    print("Добро пожаловать в текстовый квест: [bold red]ПОДЗЕМЕЛЬЕ ГОБЛИНОВ[/bold red]")
    print_long_separator()

def scene_intro():
    print_separator()
    print("=" * 10, "[bold red]ПРЕДЫСТОРИЯ[/bold red]", "=" * 10)
    print("- Ты пошел исследовать шахту")
    print("- Бродя по тёмным изгибам спотыкаешь и падаешь в глубокую яму...")
    print("- ...")
    print("- Когда ты очнулся тебя окружала мрачная комната с каменными стенами")
    print("- В углу комнаты ты заметил старый деревянный стол")
    print("- В дальней части комнаты находится дверь")
    print_separator()

def scene_first_room():
    print("1. Подойти и осмотреть стол")
    print("2. Ничего не делать")

def key_found():
    print(KEY_FOUND)
    print_separator()

def scene_corridor():
    print("- Вы подходите к двери, вставляете ключ в замочную скважину и проворачиваете")
    print("- Дверь с режущим уши скрипом отворяется")
    print_separator()
    print("- Вы поподаете в коридор и видите три прохода:")
    print("1. Налево")
    print("2. Прямо")
    print("3. Направо")

def scene_goblin_room():
    print_separator()
    print("- Вы аккуратно заходите в комнату")
    print("- Из за угла выходит старый гоблин охраняющий сокровища")
    print("[bold green]Гоблин[/bold green]: Кто ты?! Проваливай!! Иначе я тебя убью!!!")
    print("1. Сбежать")
    print("2. Вступить в битву")

def scene_goblin_escape():
    print_separator()
    print("- Переполненные страхом вы возвращаетесь в коридор")
    print("- У вас осталось два пути")
    print("1. Прямо")
    print("2. Направо")

def scene_trap_safe():
    print_separator()
    print("- Вы входите в пустую комнату...")
    print("- Осматриваясь вы замечаете шипы на потолке")
    print("- Вы почти успеваете выбежать из комнаты, но шипы задевают вашу ногу...")

def fight_rules():
    print("[bold yellow]Подсказка[/bold yellow]:")
    print("1. Враг подбрасывает кубик, затем вы")
    print("2. Если ваше число оказалось больше, вы проводите успешную атаку")
    print("3. Если ваше число оказалось меньше, успешную атаку проводит враг")
    print("4. [bold red]БИТВА ВЕДЁТСЯ ДО ЧЬЕЙ ЛИБО СМЕРТИ[/bold red]")
    print("5. [bold red]УДАЧИ[/bold red]")

def scene_goblin_fight():
    print_separator()
    print("- Вы собрались с силами и решились вступить в битву!")
    print_separator()
    
# ========== ХОРОШИЕ КОНЦОВКИ ============
def scene_good_ending():
    print_separator()
    print("- Пройдя в комнату вы видите лестницу и слабый свет")
    print("- Вы поднимаетесь по лестнице")
    print("- Свет становится ярче и ближе")
    print("- Вас охватывает чувство эйфории")
    print("- Вы выбрались и жили долго и счастливо")
    print_separator()
    print_victory()

def scene_victory_with_treasure():
    print_separator()
    print("- Поздравляю! Вы одолели гоблина, забрали сокровища которые он охранял")
    print("- И жили долго, счастливо и богато!")
    print_separator()
    print_victory()

# ========== ПЛОХИЕ КОНЦОВКИ =============
def scene_trap():
    print_separator()
    print("- Вы входите в комнату")
    print("- Пока вы осматриваетесь на вас с потолка обрушивается плита с шипами")
    print("- Не успев испугаться вы умирате")
    print_separator()
    print_gameover()

def scene_bad_ending_no_key():
    print_separator()
    print("- Вы не решаетесь брать ключ")
    print("- В полном отчаянии вы сходите с ума, замерзаете и умираете от голода")
    print_separator()
    print_gameover()

def scene_bad_ending_do_nothing():
    print_separator()
    print("- Вы не решаетесь что то делать")
    print("- В полном отчаянии вы сходите с ума, замерзаете и умираете от голода")
    print_separator()
    print_gameover()

def scene_defeat_goblin():
    print_separator()
    print("- Беда, вас загрыз гоблин!")
    print_separator()
    print_gameover()