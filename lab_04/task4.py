def five_min_elements():
    A = list(map(int, input("Введіть елементи списку через пробіл: ").split()))
    print("Початковий список:", A)

    if len(A) < 5:
        print("У списку менше 5 елементів.")
        result = sorted(A)
    else:
        result = sorted(A)[:5]

    print("П’ять мінімальних елементів:", result)
    return result


five_min_elements()
