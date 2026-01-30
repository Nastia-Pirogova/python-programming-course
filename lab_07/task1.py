import re

def Open(file_name, mode, encoding="utf-8"):

    try:
        f = open(file_name, mode, encoding=encoding)
    except OSError as e:
        print(f"File {file_name} wasn't opened! ({e})")
        return None
    else:
        print(f"File {file_name} was opened!")
        return f

file1_name = "TF4_1.txt"
file2_name = "TF4_2.txt"


lines = [
    "Я люблю Python, але інколи бувають помилки: try, except, finally!",
    "Слова різної довжини: a, bb, ccc, dddd, eeeee, ffffff.",
    "Перевіримо розділові знаки... і тире - та лапки 'тест' (!).",
    "Ще один рядок для статистики слів у файлі."
]

f1w = Open(file1_name, "w")
if f1w is not None:
    for line in lines:
        f1w.write(line + "\n")
    print(f"Information was successfully added to {file1_name}!")
    f1w.close()
    print(f"File {file1_name} was closed!")


f1r = Open(file1_name, "r")
f2w = Open(file2_name, "w")

if f1r is not None and f2w is not None:
    text = f1r.read()

    words = re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ']+", text)

    length_counts = {}
    for w in words:
        lw = len(w)
        if lw <= 16:
            length_counts[lw] = length_counts.get(lw, 0) + 1


    for length in sorted(length_counts):
        f2w.write(f"Довжина {length}: {length_counts[length]}\n")

    f1r.close()
    f2w.close()
    print("Files were closed!")


print("Result (TF4_2):")
f2r = Open(file2_name, "r")
if f2r is not None:
    for line in f2r:
        print(line.rstrip("\n"))
    f2r.close()
    print(f"File {file2_name} was closed!")
