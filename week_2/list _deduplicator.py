user_input = list(map(int, input("Введите числа: ").split()))

result = []
for i in user_input:
    if i not in result:
        result.append(i)
         
print(f"Оригинал: {', '.join(map(str, user_input))}")
print(f"Без дулей: {', '.join(map(str, result))}")
