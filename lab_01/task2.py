a = 0
b = 1
s = a + b

print(a)
print(b)

for i in range(6):
    c = a + b
    print(c)
    s += c

    a = b
    b = c

print("Сума:", s)
