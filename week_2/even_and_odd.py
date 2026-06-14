odd = []
even = []


while True:
    number = input("\nВведите N: ")
    
    if not number:
        print("Ввод не может быть пустым!")
    elif number.isdigit():
        number = int(number)
        break
    else:
        print("Число может состоять только из цифр!")

for i in range(2, number + 1, 2):
    even.append(i)
    
for i in range(1, number + 1, 2):
    odd.append(i)

print(f"Четные: {', '.join(map(str, even))}")
print(f"Нечетные: {', '.join(map(str, odd))}")
