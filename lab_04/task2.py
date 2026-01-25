n = 7
a = []

for i in range(n):
    row = []
    for j in range(n):
        if j <= n - i - 2:
            row.append(0)
        else:
            row.append(j - (n - i - 2))
    a.append(row)

for row in a:
    print(*row)
