# Operatoions list
oper_list = ["Сложение", "Вычитание", "Умножение", "Деление", "Степень"]

# Operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): 
    if b == 0:
        raise ZeroDivisionError("Ошибка: деление на ноль!")
    else:
        return a / b
def power(a, b): return pow(a, b)


# Tests
if __name__ == "__main__":
    print(f"Сложение: {add(5, 10)}")
    print(f"Вычитание: {subtract(10, 10)}")
    print(f"Умножение: {multiply(7, 10)}")
    print(f"Деление: {divide(10, 5)}")
    print(f"Степень: {power(3, 2)}")