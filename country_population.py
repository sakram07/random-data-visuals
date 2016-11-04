import matplotlib.pyplot as plt
import unicodecsv as csv

x = []
y = []

country_code = "LTU" # For different graph, change this variable

for j in range (1960, 2016):
    x.append(j)

with open('data.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if (row['Country Code'] == country_code):
            for h in range (1960, 2016):
                y.append(row[str(h)])
            break

# matplotlib things
plt.plot(x, y, linewidth=3.0)

plt.xlabel("Year")
plt.ylabel("Population")

plt.title("Population change")

plt.show()
