import numpy as np
import matplotlib.pyplot as plt

x = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024])

ukraine = np.array([-0.43, -0.50, -0.57, -0.83, -7.59, -8.35, 0.42])

usa = np.array([0.44, 0.33, 0.24, 0.17, 0.61, 0.88, 1.04])

plt.plot(x, ukraine, label='Ukraine', linewidth=3)
plt.plot(x, usa, label='USA', linewidth=3)

plt.title('Urban population growth (annual %)', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Indicator (%)', fontsize=12)

plt.legend()
plt.grid(True)
plt.show()

data = {
    "Ukraine": ukraine,
    "USA": usa
}

country = input("Введіть назву країни (Ukraine або USA): ")

if country in data:
    plt.bar(x, data[country])
    plt.title(f'Urban population growth (annual %) — {country}', fontsize=15)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Indicator (%)', fontsize=12)
    plt.grid(True, axis='y')
    plt.show()
else:
    print("Невірна назва країни")
