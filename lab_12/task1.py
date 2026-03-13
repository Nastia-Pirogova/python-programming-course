import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = None
stats = {}
current_file = ""


def show_error(message: str) -> None:
    messagebox.showerror("Помилка", message)


def load_csv() -> None:
    """Завантажити CSV і оновити список доступних стовпців."""
    global df, current_file

    file_path = filedialog.askopenfilename(
        title="Виберіть CSV файл",
        filetypes=[("CSV файли", "*.csv"), ("Всі файли", "*.*")]
    )
    if not file_path:
        return

    try:
        df = pd.read_csv(file_path)
        current_file = file_path
    except Exception as e:
        show_error(f"Не вдалося прочитати файл:\n{e}")
        return

    file_label.config(text=f"Файл: {os.path.basename(file_path)}")

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_cols:
        show_error("У файлі немає числових стовпців для аналізу.")
        return

    column_combo["values"] = numeric_cols
    column_combo.set(numeric_cols[0])

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(
        tk.END,
        "Файл успішно завантажено.\n"
        "Оберіть стовпець і натисніть 'Розрахувати статистику'.\n"
    )
    result_text.config(state="disabled")


def calculate_stats() -> None:
    """Обчислити статистику для вибраного в комбобоксі стовпця."""
    global df, stats

    if df is None:
        show_error("Спочатку завантажте CSV-файл.")
        return

    col_name = column_var.get()
    if not col_name:
        show_error("Будь ласка, оберіть стовпець для аналізу.")
        return

    try:
        series = df[col_name].dropna()
        if series.empty:
            show_error("Вибраний стовпець не містить даних.")
            return

        stats = {
            "column": col_name,
            "min": float(series.min()),
            "max": float(series.max()),
            "mean": float(series.mean()),
            "median": float(series.median()),
            "std": float(series.std())
        }
    except Exception as e:
        show_error(f"Помилка під час обчислення статистики:\n{e}")
        return

    text = (
        f"Статистика для стовпця '{col_name}':\n"
        f"Мінімум: {stats['min']:.3f}\n"
        f"Максимум: {stats['max']:.3f}\n"
        f"Середнє: {stats['mean']:.3f}\n"
        f"Медіана: {stats['median']:.3f}\n"
        f"Стандартне відхилення: {stats['std']:.3f}\n"
    )

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, text)
    result_text.config(state="disabled")
    messagebox.showinfo("Результати", text)


def plot_histogram() -> None:
    """Побудувати гістограму для вибраного стовпця."""
    global df

    if df is None:
        show_error("Спочатку завантажте CSV-файл.")
        return

    col_name = column_var.get()
    if not col_name:
        show_error("Будь ласка, оберіть стовпець для аналізу.")
        return

    try:
        series = df[col_name].dropna()
        if series.empty:
            show_error("Вибраний стовпець не містить даних.")
            return

        plt.figure(figsize=(7, 4))
        plt.hist(series, bins=5, color="skyblue", edgecolor="black")
        plt.title(f"Гістограма стовпця '{col_name}'")
        plt.xlabel(col_name)
        plt.ylabel("Частота")
        plt.grid(axis="y", alpha=0.3)
        plt.tight_layout()

        img_name = f"hist_{col_name}.png"
        plt.savefig(img_name)
        plt.show()

        messagebox.showinfo("Гістограма", f"Гістограма збережена у файл: {img_name}")
    except Exception as e:
        show_error(f"Помилка під час побудови гістограми:\n{e}")


def save_results() -> None:
    """Зберегти обчислену статистику у файл CSV або TXT."""
    if not stats:
        show_error("Немає результатів для збереження. Спочатку розрахуйте статистику.")
        return

    file_path = filedialog.asksaveasfilename(
        title="Збереження результатів",
        defaultextension=".csv",
        filetypes=[("CSV файл", "*.csv"), ("Текстовий файл", "*.txt"), ("Всі файли", "*.*")]
    )
    if not file_path:
        return

    try:
        if file_path.lower().endswith(".txt"):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Стовпець: {stats['column']}\n")
                f.write(f"Мінімум: {stats['min']}\n")
                f.write(f"Максимум: {stats['max']}\n")
                f.write(f"Середнє: {stats['mean']}\n")
                f.write(f"Медіана: {stats['median']}\n")
                f.write(f"Стандартне відхилення: {stats['std']}\n")
        else:
            stats_df = pd.DataFrame([stats])
            stats_df.to_csv(file_path, index=False)

        messagebox.showinfo("Збереження", f"Результати успішно збережено у файл:\n{file_path}")
    except Exception as e:
        show_error(f"Не вдалося зберегти результати:\n{e}")


def main() -> None:
    global file_label, result_text, column_var, column_combo

    root = tk.Tk()
    root.title("Аналіз даних з CSV (tkinter + pandas)")
    root.geometry("750x420")

    top_frame = tk.Frame(root)
    top_frame.pack(fill=tk.X, padx=10, pady=10)

    btn_open = tk.Button(top_frame, text="Відкрити CSV", command=load_csv)
    btn_open.pack(side=tk.LEFT)

    file_label = tk.Label(top_frame, text="Файл: не обрано", anchor="w")
    file_label.pack(side=tk.LEFT, padx=10)

    middle_frame = tk.Frame(root)
    middle_frame.pack(fill=tk.X, padx=10, pady=5)

    tk.Label(middle_frame, text="Стовпець:").pack(side=tk.LEFT)

    column_var = tk.StringVar()
    column_combo = ttk.Combobox(middle_frame, textvariable=column_var, state="readonly", width=30)
    column_combo.pack(side=tk.LEFT, padx=5)

    btn_stats = tk.Button(middle_frame, text="Розрахувати статистику", command=calculate_stats)
    btn_stats.pack(side=tk.LEFT, padx=5)

    btn_plot = tk.Button(middle_frame, text="Побудувати гістограму", command=plot_histogram)
    btn_plot.pack(side=tk.LEFT, padx=5)

    btn_save = tk.Button(middle_frame, text="Зберегти результати", command=save_results)
    btn_save.pack(side=tk.LEFT, padx=5)

    bottom_frame = tk.Frame(root)
    bottom_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    result_text = tk.Text(bottom_frame, wrap="word", state="disabled")
    result_text.pack(fill=tk.BOTH, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()