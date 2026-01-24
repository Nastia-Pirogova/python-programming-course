sentence = input("Введіть речення: ").strip()

while len(sentence) == 0:
    sentence = input("Введіть речення ще раз (не може бути порожнім): ").strip()

punct = ".,!?;:-—()[]{}\"'«»“”„…"

words = sentence.split()
count_n = 0

for w in words:
    w_clean = w.strip(punct).lower()
    if w_clean.startswith("н"):
        count_n += 1

print("Кількість слів, що починаються з літери «н»:", count_n)
