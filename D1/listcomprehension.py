liczby = []
for liczba in range(30):
    if liczba % 2 == 0:
        liczby.append(liczba**2)
print(f'Liczby parzyste podniesione do potęgi 3: {liczby}')

liczba = []
liczby = [x ** 2 for x in range(30) if x % 2 == 0]
print(f'Liczby parzyste podniesione do potęgi 3: {liczby}')

# postać rozszerzona

lista2 = [(x, y) for x in range(1, 5) for y in range(4, 0, -1)]
print(lista2)

lista3 = [(x, y) for x in range(1, 5) for y in range(6, 3, -1) if x < y]
print(lista3)
mojalista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
tekst = "ABCDEFGH"
lista3 = [(x, y) for x in tekst for y in range(1, 9)]
print(lista3)
print(['*' for j in range(20)])
lista_zagniezdzona = [[j for j in range(2)] for i in range(3)]
print(lista_zagniezdzona)

set = {x for x in range(0, 10)}
print(set)

tekst = "W małym białym domku, mieszkał mały biały miś. Był cały biały. Mieszka. miś"
slowa = tekst.lower().replace('.', '').split()
print(slowa)
unikalne = {slowo for slowo in slowa}
print(unikalne)
unikalne = {slowo for slowo in slowa if len(slowo) > 3}
print(unikalne)

imiona = {0: 'Adam', 1: 'Jola', 2: 'Edmund',
          3: 'Robert', 4: 'Ryszard', 5: 'Adam'}

imiona_set = {(key, value) for(key, value) in imiona.items()}
print(imiona_set, type(imiona_set))


imiona_set = {y: x for(x, y) in imiona.items()}
print(imiona_set, type(imiona_set))

imiona_set = {}
for x, y in imiona.items():
    imiona_set[y] = x
print(imiona_set)


imiona_set = []
for x, y in imiona.items():
    imiona_set.insert(x, y)
print(imiona_set)

stocks = {'Boombit': 22, 'CD Project': 295, 'Playway': 350}
stock1 = {x: y for (x, y) in stocks.items() if y > 100}
print(stock1, type(stock1))
