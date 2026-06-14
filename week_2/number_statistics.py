user_input = list(map(int, input("Введите числа: ").split()))

numb_count = len(user_input)
numb_sum = sum(user_input)
numb_mean = sum(user_input) / len(user_input)
numb_max = max(user_input)
numb_min = min(user_input)
numb_odd = [] 
numb_even = []

for i in range(2, user_input + 1, 2):
    numb_even.append(i)

for i in range(1, user_input + 1, 2):
    numb_odd.append(i)

print(numb_count)
print(numb_sum)
print(numb_mean)
print(numb_max)
print(numb_min)
print(*numb_odd)
print(*numb_even)