weight = float(input("Введите свой вес (кг): "))
height = float(input("Введите свой рост (метры): "))

if weight <= 0:
    print("Вес не может быть меньше 0!")
    exit()
elif height <= 0:
    print("Рост не может быть меньше 0!")
    exit()

imt = round(weight / height ** 2, 2)

if imt < 18.5:
    index = ("Недостаточная масса тела.")
elif imt >= 18.5 and imt < 25:
    index = ("Нормальная масса тела.")
elif imt >= 25 and imt < 30:
    index = ("Избыточная масса тела.")
else:
    index = ("У вас ожирение.")   

print(f"Ваш индекс равен: {imt} \n{index}")