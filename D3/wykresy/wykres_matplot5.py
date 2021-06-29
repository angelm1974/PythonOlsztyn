import matplotlib.pyplot as plt
from random import randrange

godziny = range(1,10)
temperatura = [x**2 for x in godziny]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()

ax.pie(godziny)
ax.set_title("Temperatury w ciągu dnia", fontsize=18)
ax.set_xlabel("Godzina", fontsize=12)
ax.set_ylabel("Temperatura", fontsize=12)
ax.tick_params(axis='both', labelsize=10)


plt.show()
