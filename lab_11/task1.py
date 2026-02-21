import pandas as pd

countries = {
    "Ukraine": {"continent": "Europe", "area": 603628, "population": 37000000, "gdp": 160000},
    "Germany": {"continent": "Europe", "area": 357022, "population": 84000000, "gdp": 4450000},
    "France": {"continent": "Europe", "area": 551695, "population": 68000000, "gdp": 3050000},
    "Egypt": {"continent": "Africa", "area": 1002450, "population": 112000000, "gdp": 475000},
    "Nigeria": {"continent": "Africa", "area": 923768, "population": 223000000, "gdp": 477000},
    "China": {"continent": "Asia", "area": 9596961, "population": 1409000000, "gdp": 17900000},
    "Japan": {"continent": "Asia", "area": 377975, "population": 123000000, "gdp": 4230000},
    "Canada": {"continent": "North America", "area": 9984670, "population": 40000000, "gdp": 2140000},
    "Brazil": {"continent": "South America", "area": 8515767, "population": 203000000, "gdp": 2170000},
    "Australia": {"continent": "Australia", "area": 7692024, "population": 27000000, "gdp": 1700000},
}

print("Словник countries:")
print(countries)

df = pd.DataFrame.from_dict(countries, orient="index")

df.reset_index(inplace=True)
df.rename(columns={"index": "country"}, inplace=True)

print("\nDataFrame:")
print(df)

print("\nПерші 3 рядки (df.head(3)):")
print(df.head(3))

print("\nТипи даних (df.dtypes):")
print(df.dtypes)

print("\nКількість рядків і стовпців (df.shape):")
print(df.shape)

print("\nОписова статистика (df.describe()):")
print(df.describe())

df["population_density"] = df["population"] / df["area"]

print("\nDataFrame з новим стовпцем population_density:")
print(df)

filtered = df[df["population"] > 100_000_000]
print("\nФільтрація: країни з населенням понад 100 млн:")
print(filtered)

sorted_df = df.sort_values(by="population", ascending=False)
print("\nСортування за спаданням населення:")
print(sorted_df)

group_mean = df.groupby("continent")["population_density"].mean()
print("\nСередня густота населення по континентах:")
print(group_mean)

max_gdp = df.groupby("continent")["gdp"].max()
print("\nМаксимальний ВВП (gdp) у кожному континенті:")
print(max_gdp)

unique_countries = df["country"].nunique()
print("\nКількість унікальних країн:", unique_countries)
