def insert_element():
    A = list(map(int, input("Введіть елементи списку через пробіл: ").split()))
    print("Початковий список:", A)

    x = int(input("Введіть елемент для вставки: "))
    k = int(input("Введіть позицію для вставки: "))

    if k < 0 or k > len(A):
        print("Неправильна позиція!")
        return A

    A.insert(k, x)

    print("Список після вставки:", A)
    return A


insert_element()

