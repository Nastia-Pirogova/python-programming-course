def print_all(countries):
    print("\nУсі записи словника:")
    for name, info in countries.items():
        print(f"{name} – частина світу: {info['continent']}, "
              f"площа: {info['area']} км², населення: {info['population']} осіб")


def add_country(countries):
    try:
        name = input("Введіть назву країни: ")
        continent = input("Введіть частину світу: ")
        area = float(input("Введіть площу (км²): "))
        population = int(input("Введіть населення: "))

        countries[name] = {
            "continent": continent,
            "area": area,
            "population": population
        }
        print("Країну додано успішно.")
    except ValueError:
        print("Помилка введення даних!")


def delete_country(countries):
    name = input("Введіть назву країни для видалення: ")
    try:
        del countries[name]
        print("Країну видалено.")
    except KeyError:
        print("Помилка: такої країни не існує у словнику.")


def print_sorted(countries):
    print("\nСловник за відсортованими ключами:")
    for key in sorted(countries.keys()):
        info = countries[key]
        print(f"{key} – {info['continent']}, {info['area']} км², {info['population']} осіб")


def find_africa_asia(countries):
    print("\nКраїни, що знаходяться в Африці або Азії:")
    found = False
    for name, info in countries.items():
        if info["continent"].lower() in ["africa", "asia"]:
            print(name)
            found = True
    if not found:
        print("Таких країн не знайдено.")


def menu():
    countries = {
        "Ukraine": {"continent": "Europe", "area": 603628, "population": 37000000},
        "Germany": {"continent": "Europe", "area": 357022, "population": 84000000},
        "France": {"continent": "Europe", "area": 551695, "population": 68000000},
        "Egypt": {"continent": "Africa", "area": 1002450, "population": 112000000},
        "Nigeria": {"continent": "Africa", "area": 923768, "population": 223000000},
        "China": {"continent": "Asia", "area": 9596961, "population": 1409000000},
        "Japan": {"continent": "Asia", "area": 377975, "population": 123000000},
        "Canada": {"continent": "North America", "area": 9984670, "population": 40000000},
        "Brazil": {"continent": "South America", "area": 8515767, "population": 203000000},
        "Australia": {"continent": "Australia", "area": 7692024, "population": 27000000},
    }

    while True:
        print("\nМеню:")
        print("1 – Вивести словник")
        print("2 – Додати країну")
        print("3 – Видалити країну")
        print("4 – Перегляд за відсортованими ключами")
        print("5 – Країни Африки або Азії")
        print("0 – Вихід")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            print_all(countries)
        elif choice == "2":
            add_country(countries)
        elif choice == "3":
            delete_country(countries)
        elif choice == "4":
            print_sorted(countries)
        elif choice == "5":
            find_africa_asia(countries)
        elif choice == "0":
            print("Завершення роботи.")
            break
        else:
            print("Невірний вибір!")


menu()
