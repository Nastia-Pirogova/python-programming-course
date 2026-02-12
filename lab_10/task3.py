import json
import matplotlib.pyplot as plt


json_data = '''
[
  {"name":"Ukraine","area_km2":603700,"population":36000000,"part":"Europe"},
  {"name":"Turkey","area_km2":783356,"population":85000000,"part":"Asia"},
  {"name":"Egypt","area_km2":1002450,"population":110000000,"part":"Africa"},
  {"name":"Nigeria","area_km2":923768,"population":223000000,"part":"Africa"},
  {"name":"Japan","area_km2":377975,"population":124000000,"part":"Asia"},
  {"name":"Canada","area_km2":9984670,"population":40000000,"part":"North America"},
  {"name":"Brazil","area_km2":8515767,"population":203000000,"part":"South America"},
  {"name":"Germany","area_km2":357022,"population":83000000,"part":"Europe"},
  {"name":"India","area_km2":3287263,"population":1420000000,"part":"Asia"},
  {"name":"Australia","area_km2":7692024,"population":26000000,"part":"Australia/Oceania"}
]
'''

countries = json.loads(json_data)


population_by_part = {}
for c in countries:
    part = c["part"]
    population_by_part[part] = population_by_part.get(part, 0) + c["population"]

labels = list(population_by_part.keys())
sizes = list(population_by_part.values())


fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Розподіл населення за частинами світу (у %)")
ax.axis("equal")
plt.show()
