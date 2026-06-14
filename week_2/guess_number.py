from random import randint

guessed_numb = randint(1, 20)
attempts_count = 1

def correct_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print("Некорректный ввод!")
 
print("Угадай число от 1 до 20 (5 попыток)")

while attempts_count <= 5:
    user_input = correct_input(f"\nПопытка {attempts_count}: ")
    
    if user_input == guessed_numb:
        print("Поздравляю! Вы угадали!")
        break        
    elif user_input > guessed_numb:
        print("Загаданное число меньше!")
    elif user_input < guessed_numb:
        print("Загаданное число больше!")

    attempts_count += 1
else:
    print(f"\nПопытки кончились. Было загадано: {guessed_numb}")      
