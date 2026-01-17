a = float(input("Введіть a: "))
while a <= 0:
    print("Помилка: число a повинно бути додатнім")
    a = float(input("Введіть a ще раз: "))

b = float(input("Введіть b: "))
while b <= 0:
    print("Помилка: число b повинно бути додатнім")
    b = float(input("Введіть b ще раз: "))

if a < b:
    X = a / b + 5
    print("Перша умова")
elif a == b:
    X = -5
    print("Друга умова")
else:
    X = (a * a - b) / b
    print("Третя умова")

print("Результат:", X)
