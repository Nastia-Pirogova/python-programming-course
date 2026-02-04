import json
import os

DATA_FILE = "countries.json"
RESULT_FILE = "result.json"


def save_json(path: str, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def init_data_if_missing():
    """Створює файл countries.json з 10 країнами, якщо файлу ще немає."""
    if os.path.exists(DATA_FILE):
        return

    countries = [
        {"name": "Ukraine", "area_km2": 603700, "population": 36000000, "part": "Europe"},
        {"name": "Turkey", "area_km2": 783356, "population": 85000000, "part": "Asia"},
        {"name": "Egypt", "area_km2": 1002450, "population": 110000000, "part": "Africa"},
        {"name": "Nigeria", "area_km2": 923768, "population": 223000000, "part": "Africa"},
        {"name": "Japan", "area_km2": 377975, "population": 124000000, "part": "Asia"},
        {"name": "Canada", "area_km2": 9984670, "population": 40000000, "part": "North America"},
        {"name": "Brazil", "area_km2": 8515767, "population": 203000000, "part": "South America"},
        {"name": "Germany", "area_km2": 357022, "population": 83000000, "part": "Europe"},
        {"name": "India", "area_km2": 3287263, "population": 1420000000, "part": "Asia"},
        {"name": "Australia", "area_km2": 7692024, "population": 26000000, "part": "Australia/Oceania"},
    ]

    save_json(DATA_FILE, countries)


def view_data():
    """Виведення на екран вмісту JSON файлу."""
    try:
        data = load_json(DATA_FILE)
        print("\nВміст countries.json:\n")
        for item in data:
            print(item)
    except FileNotFoundError:
        print(f"Файл {DATA_FILE} не знайдено!")
    except json.JSONDecodeError:
        print("Помилка: файл JSON пошкоджений або порожній.")
    except Exception as e:
        print(f"Помилка читання: {e}")


def add_record():
    """Додавання нового запису у JSON файл."""
    try:
        data = load_json(DATA_FILE)
    except FileNotFoundError:
        data = []

    name = input("Назва країни: ").strip()
    part = input("Частина світу (Africa/Asia/Europe...): ").strip()

    while True:
        try:
            area = float(input("Площа (км²): ").strip().replace(",", "."))
            break
        except ValueError:
            print("Помилка! Введіть число для площі.")

    while True:
        try:
            population = int(input("Населення: ").strip())
            break
        except ValueError:
            print("Помилка! Введіть ціле число для населення.")

    data.append({"name": name, "area_km2": area, "population": population, "part": part})
    save_json(DATA_FILE, data)
    print("Запис додано.")


def delete_record():
    """Видалення запису з JSON файлу за назвою країни."""
    name = input("Введіть назву країни для видалення: ").strip().lower()

    try:
        data = load_json(DATA_FILE)
        new_data = [x for x in data if x.get("name", "").strip().lower() != name]

        if len(new_data) == len(data):
            print("Країну не знайдено.")
            return

        save_json(DATA_FILE, new_data)
        print("Запис видалено.")

    except FileNotFoundError:
        print(f"Файл {DATA_FILE} не знайдено!")
    except Exception as e:
        print(f"Помилка: {e}")


def search_by_field():
    """Пошук даних у JSON файлі за одним із полів."""
    field = input("Поле для пошуку (name / part / area_km2 / population): ").strip()
    value = input("Значення для пошуку: ").strip()

    try:
        data = load_json(DATA_FILE)
        result = []

        for item in data:
            if field not in item:
                continue
            if str(item[field]).strip().lower() == value.strip().lower():
                result.append(item)

        if result:
            print("\nЗнайдено записи:\n")
            for r in result:
                print(r)
        else:
            print("Нічого не знайдено.")

    except FileNotFoundError:
        print(f"Файл {DATA_FILE} не знайдено!")
    except Exception as e:
        print(f"Помилка: {e}")


def task_africa_or_asia():
    """
    Завдання варіанту:
    визначити, чи є країни, що знаходяться в Африці або Азії.
    Якщо є — надрукувати їх назви.
    Результат записати у result.json
    """
    try:
        data = load_json(DATA_FILE)

        result = [x for x in data if x.get("part", "").strip().lower() in ("africa", "asia")]

        if result:
            print("\nКраїни, що знаходяться в Африці або Азії:")
            for x in result:
                print("-", x["name"])
        else:
            print("\nНемає країн в Африці або Азії серед заданих.")

        save_json(RESULT_FILE, result)
        print(f"\nРезультат записано у файл: {RESULT_FILE}")

    except FileNotFoundError:
        print(f"Файл {DATA_FILE} не знайдено!")
    except Exception as e:
        print(f"Помилка: {e}")


def main():
    init_data_if_missing()

    while True:
        print("\nМеню:")
        print("1 - Вивести вміст JSON файлу")
        print("2 - Додати запис")
        print("3 - Видалити запис")
        print("4 - Пошук за полем")
        print("5 - Завдання: країни в Африці або Азії + запис у result.json")
        print("0 - Вихід")

        choice = input("Оберіть пункт: ").strip()

        if choice == "1":
            view_data()
        elif choice == "2":
            add_record()
        elif choice == "3":
            delete_record()
        elif choice == "4":
            search_by_field()
        elif choice == "5":
            task_africa_or_asia()
        elif choice == "0":
            print("Вихід.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
