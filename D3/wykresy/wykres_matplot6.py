import csv
from datetime import datetime
import matplotlib.pyplot as plt

file = 'dane.csv'
with open(file) as f:
    reader = csv.reader(f)
    naglowek = next(reader)

    daty, temperatury = [], []

    for row in reader:
        dat1 = datetime.fromisoformat(row[0])
        temp = float(row[1])
        daty.append(dat1)
        temperatury.append(temp)

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()

ax.scatter(daty, temperatury, c='red')
ax.set_title("Temperatury w ciągu miesiąca", fontsize=18)
ax.set_xlabel(naglowek[0], fontsize=12)
ax.set_ylabel(naglowek[1], fontsize=12)
ax.tick_params(axis='both', labelsize=10)


plt.show()
