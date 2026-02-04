import csv

INPUT_FILE = "Lab9.csv"
OUTPUT_FILE = "new_lab9.csv"

def parse_number(value: str):
    if value is None:
        return None

    value = value.strip()
    if value == "" or value == "..":
        return None

    value = value.replace(",", ".")
    try:
        return float(value)
    except ValueError:
        return None


def print_csv_contents():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f, delimiter=",")
            print("Country Name : 2016 [YR2016]")
            for row in reader:
                country = row.get("Country Name", "").strip()
                val_raw = row.get("2016 [YR2016]", "").strip()
                print(f"{country} : {val_raw}")
    except FileNotFoundError:
        print(f"Файл {INPUT_FILE} не знайдено!")
    except Exception as e:
        print(f"Помилка читання файлу {INPUT_FILE}: {e}")


def filter_and_save(threshold: float):
    found = False

    try:
        with open(INPUT_FILE, "r", encoding="utf-8-sig", newline="") as f_in:
            reader = csv.DictReader(f_in, delimiter=",")

            with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f_out:
                writer = csv.writer(f_out, delimiter=";")
                writer.writerow(["Country Name", "2016 [YR2016]"])

                print("\nРезультати пошуку (значення більше введеного):")
                for row in reader:
                    country = row.get("Country Name", "").strip()
                    value = parse_number(row.get("2016 [YR2016]", ""))

                    if value is None:
                        continue

                    if value > threshold:
                        found = True
                        print(f"{country} : {value}")
                        writer.writerow([country, value])

        if not found:
            print(f"\nПоказників, які більші, ніж {threshold} — немає.")

    except FileNotFoundError:
        print(f"Файл {INPUT_FILE} не знайдено!")
    except Exception as e:
        print(f"Помилка обробки файлу {INPUT_FILE}: {e}")


def read_threshold_from_user() -> float:
    while True:
        s = input("\nВведіть значення (число), щоб знайти показники більші за нього: ").strip()
        s = s.replace(",", ".")
        try:
            return float(s)
        except ValueError:
            print("Некоректне значення. Введіть число ще раз.")


def main():
    print_csv_contents()
    threshold = read_threshold_from_user()
    filter_and_save(threshold)


if __name__ == "__main__":
    main()
