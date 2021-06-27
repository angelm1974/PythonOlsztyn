x = 1
y = 3.14

x = int(2)  # castowanie wartości 2 na typ int
y = int(3.14)  # castowanie wartości 3,14 na typ int
print('zmienna x =', x, type(x))
print('zmienna y =', y, type(y))
x = float(2)
print('zmienna x =', x, type(x))

y = str(3.14)
print('zmienna y =', y, type(y))

u = 3.14
print(round(u), type(round(u)))  # zaokrąglanie do liczb naturalnych
print(round(u, 1), type(round(u, 1)))  # zaokrąglanie do 1 miejsca po przecinku
