word = input("Введіть слово (має містити повторювані літери): ").strip()

while len(word) == 0:
    word = input("Введіть слово ще раз (не може бути порожнім): ").strip()

counts = {}
for ch in word:
    counts[ch] = counts.get(ch, 0) + 1

duplicates = [ch for ch, cnt in counts.items() if cnt >= 2]

if duplicates:
    print("Однакові літери (повторюються 2+ рази):")
    for ch in duplicates:
        print(f"'{ch}' — {counts[ch]} раз(и)")
else:
    print("У слові немає літер, що повторюються 2+ рази.")
