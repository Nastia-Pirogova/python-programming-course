n = int(input("Введіть N: "))

print(f"Введіть {n} дійсних елементів масиву (по одному в рядок):")
arr = [float(input()) for _ in range(n)]

negatives = [x for x in arr if x < 0]

print("Масив:", arr)

if len(negatives) == 0:
    print("Від’ємних елементів немає, середнє арифметичне обчислити неможливо.")
else:
    avg_neg = sum(negatives) / len(negatives)
    print("Від’ємні елементи:", negatives)
    print("Середнє арифметичне від’ємних елементів:", avg_neg)
