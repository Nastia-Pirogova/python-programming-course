"""
task1.py — командна робота з текстовим файлом.

Запуск:
  Student 1:
    python task1.py --role student1 --surname "Pyrohova"
  Student 2:
    python matask1.py --role student2 --surname "Petrenko"
  Student 3:
    python task1.py --role student3 --surname "Shevchenko"

Файл: team_file.txt (створює Student 1, всі інші лише дописують).
"""

from __future__ import annotations

import argparse
import os

FILE_NAME = "team_file.txt"


def safe_open(file_name: str, mode: str, encoding: str = "utf-8"):
    """
    Безпечне відкриття файлу з обробкою винятків.
    Повертає файловий об'єкт або None.
    """
    try:
        return open(file_name, mode, encoding=encoding)
    except FileNotFoundError as e:
        print(f"[ERROR] Файл/шлях не знайдено: {e}")
        return None
    except PermissionError as e:
        print(f"[ERROR] Немає прав доступу до файлу '{file_name}': {e}")
        return None
    except OSError as e:
        print(f"[ERROR] Не вдалося відкрити файл '{file_name}' у режимі '{mode}'. Причина: {e}")
        return None


def write_block(header: str, lines: list[str]) -> None:
    """
    Дозаписує блок у кінець файлу.
    Усі дії над файлом — програмно, з обробкою винятків.
    """
    f = safe_open(FILE_NAME, "a")
    if f is None:
        return

    try:
        f.write(header + "\n")
        for line in lines:
            f.write(line + "\n")
        f.write("\n")
    except OSError as e:
        print(f"[ERROR] Помилка запису у файл: {e}")
    finally:
        try:
            f.close()
        except OSError as e:
            print(f"[ERROR] Помилка закриття файлу: {e}")


def create_or_clear_file() -> None:
    """
    Student 1: створює або очищує файл.
    Важливо: це робить тільки Student 1, щоб не стерти внесок інших студентів.
    """
    f = safe_open(FILE_NAME, "w")
    if f is None:
        return

    try:
        f.write("")
    except OSError as e:
        print(f"[ERROR] Не вдалося створити/очистити файл: {e}")
    finally:
        try:
            f.close()
        except OSError as e:
            print(f"[ERROR] Помилка закриття файлу: {e}")


def print_file() -> None:
    """Друкує вміст файлу в консоль."""
    f = safe_open(FILE_NAME, "r")
    if f is None:
        return

    try:
        print("----- Вміст файлу -----")
        print(f.read())
        print("-----------------------")
    except OSError as e:
        print(f"[ERROR] Помилка читання файлу: {e}")
    finally:
        try:
            f.close()
        except OSError as e:
            print(f"[ERROR] Помилка закриття файлу: {e}")


# ============================
# Частина 1 — Student 1
# ============================
def run_student1(surname: str) -> None:

    create_or_clear_file()

    question1 = "Що таке список (list) у Python і чим він відрізняється від кортежу (tuple)?"

    write_block("=== Student 1 ===", [
        f"Surname: {surname}",
        f"Question: {question1}",
    ])


# ============================
# Частина 2 — Student 2
# ============================
def run_student2(surname: str) -> None:

    if not os.path.exists(FILE_NAME):
        print("[ERROR] Спільний файл не знайдено. Спочатку Student 1 має створити файл.")
        return

    answer1_lines = [
        "List (список) — це змінювана (mutable) впорядкована колекція елементів у Python.",
        "Елементи можна додавати, видаляти та змінювати після створення списку.",
        "Tuple (кортеж) — незмінювана (immutable) впорядкована колекція: змінювати елементи не можна.",
        "Списки використовують, коли дані треба змінювати, кортежі — коли потрібна фіксованість та захист від змін."
    ]

    question2 = "Поясни, що робить конструкція try-except-finally у Python?"

    write_block("=== Student 2 ===", [
        f"Surname: {surname}",
        "Answer:",
        *answer1_lines,
        f"Question: {question2}",
    ])


# ============================
# Частина 3 — Student 3
# ============================
def run_student3(surname: str) -> None:

    if not os.path.exists(FILE_NAME):
        print("[ERROR] Спільний файл не знайдено. Переконайся, що працюєш з репозиторієм команди.")
        return

    answer2_lines = [
        "try-except-finally використовується для обробки помилок (виключень).",
        "Код у try виконується звичайно; якщо виникає помилка — виконання переходить у except.",
        "У except можна обробити виняток (наприклад, показати повідомлення і не падати аварійно).",
        "Блок finally виконується завжди — незалежно від того, була помилка чи ні.",
        "Його часто застосовують для закриття файлів або звільнення ресурсів."
    ]

    question3 = "Що таке контекстний менеджер with open(...) і чому він зручний?"

    write_block("=== Student 3 ===", [
        f"Surname: {surname}",
        "Answer:",
        *answer2_lines,
        f"Question: {question3}",
    ])


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--role", choices=["student1", "student2", "student3"], required=True)
    p.add_argument("--surname", required=True)
    p.add_argument("--print", action="store_true", help="Показати вміст файлу після запису")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    if args.role == "student1":
        run_student1(args.surname)
    elif args.role == "student2":
        run_student2(args.surname)
    elif args.role == "student3":
        run_student3(args.surname)

    if args.print:
        print_file()


if __name__ == "__main__":
    main()
