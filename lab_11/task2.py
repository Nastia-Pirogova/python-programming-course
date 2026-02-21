import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("comptage_velo_2011.csv", sep=",", parse_dates=["Date"], dayfirst=True)

df.drop(columns=["Unnamed: 1"], inplace=True)

print("Перші рядки:")
print(df.head())

print("\nІнформація про датафрейм:")
print(df.info())

print("\nОписова статистика (тільки числові колонки):")
print(df.select_dtypes(include="number").describe())

tracks = df.select_dtypes(include="number").fillna(0)

total_all_tracks_year = tracks.to_numpy().sum()
print("\nЗагальна кількість велосипедистів за 2011 рік (усі доріжки):", int(total_all_tracks_year))

total_per_track_year = tracks.sum(axis=0).sort_values(ascending=False)
print("\nЗагальна кількість велосипедистів за 2011 рік по кожній велодоріжці:")
print(total_per_track_year.astype(int))

top3_tracks = list(total_per_track_year.head(3).index)
print("\nОбрані 3 велодоріжки (топ-3 за сумою за рік):", top3_tracks)

df["Month"] = df["Date"].dt.month
monthly = df.groupby("Month")[top3_tracks].sum()

popular_months = monthly.idxmax()
print("\nНайпопулярніший місяць (номер місяця) для кожної з 3 доріжок:")
print(popular_months)

track_to_plot = top3_tracks[0]
plt.figure(figsize=(12, 6))
monthly[track_to_plot].plot(marker="o")
plt.title(f"Завантаженість велодоріжки '{track_to_plot}' по місяцях за 2011 рік")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.xticks(range(1, 13))
plt.grid(True)
plt.show()