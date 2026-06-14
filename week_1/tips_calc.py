people = int(input("Сколько вас человек: "))

if people <= 0: # Защита от ошибки
    print("Кол-во человек должно быть больше 0!")
    exit()

check_sum = float(input("Сумма вашего счёта: "))
tips = float(input("Сколько процентов чаевых хотите оставить: "))

tips_sum = round((check_sum / 100) * tips, 2)
on_people = round(tips_sum / people, 2)
total_sum = round(tips_sum + check_sum, 2)

print (f"Общая сумма счета с чаевыми - {total_sum} рублей")
print (f"Сумма чаевых - {tips_sum} рублей")
print (f"Скинтесь по {on_people} рублей с человека")
