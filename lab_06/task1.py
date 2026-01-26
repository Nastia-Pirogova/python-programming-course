from typing import Dict, Any, Optional, List

journal: Dict[str, Any] = {
    "group_number": "IPZ-21",
    "students": []
}


def normalize_name(name: str) -> str:
    return " ".join(name.strip().split()).lower()


def find_student(journal_data: Dict[str, Any], full_name: str) -> Optional[Dict[str, Any]]:
    target = normalize_name(full_name)
    for student in journal_data["students"]:
        if normalize_name(student["full_name"]) == target:
            return student
    return None


def calc_average(student: Dict[str, Any]) -> float:
    subjects = student.get("subjects", {})
    if not subjects:
        return 0.0
    total = sum(subjects.values())
    return total / len(subjects)

def add_student(journal_data: Dict[str, Any], full_name: str, course: int) -> None:

    if find_student(journal_data, full_name) is not None:
        print(f"Студент '{full_name}' вже є в журналі.")
        return

    journal_data["students"].append({
        "full_name": full_name.strip(),
        "course": int(course),
        "subjects": {}
    })
    print(f"Студента '{full_name}' додано.")


def remove_student(journal_data: Dict[str, Any], full_name: str) -> None:
    target = normalize_name(full_name)
    before = len(journal_data["students"])
    journal_data["students"] = [
        s for s in journal_data["students"]
        if normalize_name(s["full_name"]) != target
    ]
    after = len(journal_data["students"])

    if after < before:
        print(f"Студента '{full_name}' видалено.")
    else:
        print(f"Студента '{full_name}' не знайдено.")


def add_or_update_grade(journal_data: Dict[str, Any], full_name: str, subject: str, grade: int) -> None:
    student = find_student(journal_data, full_name)
    if student is None:
        print(f"Студента '{full_name}' не знайдено.")
        return

    if not (0 <= grade <= 100):
        print("Некоректна оцінка. Введи число від 0 до 100.")
        return

    subj = subject.strip()
    student["subjects"][subj] = int(grade)
    print(f"Оцінку з '{subj}' для '{student['full_name']}' збережено: {grade}")


def sort_students(journal_data: Dict[str, Any], by: str = "full_name", reverse: bool = False) -> None:

    if by == "full_name":
        journal_data["students"].sort(key=lambda s: normalize_name(s["full_name"]), reverse=reverse)
    elif by == "course":
        journal_data["students"].sort(key=lambda s: s["course"], reverse=reverse)
    elif by == "average":
        journal_data["students"].sort(key=lambda s: calc_average(s), reverse=reverse)
    else:
        print("Невідомий параметр сортування.")
        return

    print(f"Відсортовано за '{by}' {'(спадання)' if reverse else '(зростання)'}.")


def print_journal(journal_data: Dict[str, Any]) -> None:
    print(f"\nЖУРНАЛ УСПІШНОСТІ | Група: {journal_data['group_number']}")
    print("-" * 60)

    if not journal_data["students"]:
        print("Поки що студентів немає.")
        print("-" * 60)
        return

    for i, student in enumerate(journal_data["students"], start=1):
        avg = calc_average(student)
        print(f"{i}. {student['full_name']} | курс: {student['course']} | середній: {avg:.2f}")
        if student["subjects"]:
            for subj, grade in student["subjects"].items():
                print(f"   - {subj}: {grade}")
        else:
            print("   - (предметів ще немає)")
    print("-" * 60)


def search_students(journal_data: Dict[str, Any], query: str) -> List[Dict[str, Any]]:

    q = query.strip().lower()
    return [s for s in journal_data["students"] if q in s["full_name"].lower()]


def menu() -> None:

    while True:
        print("""
1) Додати студента
2) Видалити студента
3) Додати/оновити оцінку
4) Показати журнал
5) Сортувати студентів
6) Пошук студентів
0) Вийти
""")

        choice = input("Обери дію: ").strip()

        if choice == "1":
            name = input("ПІБ: ")
            course = input("Курс (число): ")
            if not course.isdigit():
                print("Курс має бути числом.")
                continue
            add_student(journal, name, int(course))

        elif choice == "2":
            name = input("ПІБ для видалення: ")
            remove_student(journal, name)

        elif choice == "3":
            name = input("ПІБ: ")
            subject = input("Предмет: ")
            grade_str = input("Оцінка (0..100): ")
            if not grade_str.isdigit():
                print("Оцінка має бути числом.")
                continue
            add_or_update_grade(journal, name, subject, int(grade_str))

        elif choice == "4":
            print_journal(journal)

        elif choice == "5":
            by = input("Сортувати за (full_name/course/average): ").strip()
            rev = input("reverse? (y/n): ").strip().lower() == "y"
            sort_students(journal, by=by, reverse=rev)

        elif choice == "6":
            q = input("Введи частину ПІБ для пошуку: ")
            results = search_students(journal, q)
            if not results:
                print("Нічого не знайдено.")
            else:
                print("Знайдено:")
                for s in results:
                    print(f"- {s['full_name']} (курс {s['course']}, середній {calc_average(s):.2f})")

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невірний вибір.")


if __name__ == "__main__":


    menu()
