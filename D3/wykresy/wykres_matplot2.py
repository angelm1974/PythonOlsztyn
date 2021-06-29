import matplotlib.pyplot as plt

dane = [1, 4, 9, 16, 25, 36]
fig, ax = plt.subplots()
ax.plot(dane, linewidth=3)  # grubość linii wykresu
ax.set_title("Kwadraty liczb", fontsize=18)
ax.set_xlabel("Wartość",fontsize=12)
ax.set_ylabel("Kwadraty wartości",fontsize=12)
ax.tick_params(axis='both',labelsize=10)


plt.show()
