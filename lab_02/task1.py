import math

def expression(m):
    z = 1 / math.sqrt(m + 2)
    return z

def total_distance(n):
    distance = 10
    total = 0

    for i in range(n):
        total += distance
        distance *= 1.1

    return total


m = float(input("Введіть значення m: "))
print("Значення виразу z =", expression(m))

n = int(input("Введіть кількість днів n: "))
print("Сумарний шлях за", n, "днів:", total_distance(n), "км")
