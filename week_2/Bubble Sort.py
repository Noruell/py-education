arr = list(map(int, input("Введите числа (через пробел): ").split()))\

print(f"Начальный список: {arr}\n")

l = len(arr)

for i in range(l):
    swap = False
    for j in range(0, l-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap = True
    print(f"Шаг {i+1}: {arr}")

    if not swap:
        break
print(f"\nОтсортировано: {arr}")
