import matplotlib.pyplot as plt


godziny = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperatura = [30, 32, 34, 36, 38, 36, 33, 31, 28, 26]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()

ax.scatter(godziny, temperatura)
ax.set_title("Temperatury w ciągu dnia", fontsize=18)
ax.set_xlabel("Godzina", fontsize=12)
ax.set_ylabel("Temperatura", fontsize=12)
ax.tick_params(axis='both', labelsize=10)


plt.show()
