import nltk
import string
import matplotlib.pyplot as plt

from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist

nltk.download("gutenberg")
nltk.download("punkt")
nltk.download("stopwords")

file_id = "austen-sense.txt"

tokens = gutenberg.words(file_id)

words_only = [w for w in tokens if w.isalpha()]
print("Кількість слів у тексті (тільки алфавітні токени):", len(words_only))

words_lower = [w.lower() for w in words_only]
freq = FreqDist(words_lower)

top10 = freq.most_common(10)
print("\nТОП-10 слів (до видалення стоп-слів):")
for word, count in top10:
    print(word, "->", count)

plt.figure(figsize=(10, 5))
plt.bar([w for w, _ in top10], [c for _, c in top10])
plt.title("ТОП-10 найчастіших слів (без видалення стоп-слів)")
plt.xlabel("Слова")
plt.ylabel("Кількість")
plt.grid(axis="y")


stop_words = set(stopwords.words("english"))

clean_words = [
    w.lower()
    for w in tokens
    if w.isalpha() and w.lower() not in stop_words
]

freq_clean = FreqDist(clean_words)
top10_clean = freq_clean.most_common(10)

print("\nТОП-10 слів (після видалення стоп-слів та пунктуації):")
for word, count in top10_clean:
    print(word, "->", count)

plt.figure(figsize=(10, 5))
plt.bar([w for w, _ in top10_clean], [c for _, c in top10_clean])
plt.title("ТОП-10 найчастіших слів (після видалення стоп-слів і пунктуації)")
plt.xlabel("Слова")
plt.ylabel("Кількість")
plt.grid(axis="y")
plt.show()
