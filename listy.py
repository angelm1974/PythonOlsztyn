a = []
b = ['słoń', 'kot', 23, 34, True, 44.56, 'rybki']
print(a, b)
print(b[-3:])
print(str(b[4]).upper())
b[0] = 'krokodyl'
b.append('kangur')  # dodanie na ostatniej pozycji elementu do listy
print(b)
b.insert(3, 'pies')  # wstawienie w dowolnym miejscu
print(b)
del b[-4]  # skasowanie elementu o wybranym indeksie
print(b)
print(b.pop())  # skasowanie ostatniego elementu
print(b)
b.remove('kot')  # skasowanie elementu o wskazanej nazwie
print(b)

# sortowanie
samochody = ['Fiat1', 'Ford', 'Renault3432', 'Peugeot', 'BMW', 'Mercedes']
samochody.sort()
print(samochody)
print(samochody.reverse())  # odwracanie listy - zwraca none
print(samochody)  # wydruk odwróconej listy

# własna funkcja sortująca


def moja_funkcja_sortujaca(e):
    return len(e)


# sortowanie z wykorzystaniem własnej listy sortującej
samochody.sort(key=moja_funkcja_sortujaca)
print(samochody)

# zliczenie wystąpień wybranego typu elementu listy
print(b.count('słoń'))

# pętla po wszystkich elementach listy
for x in [1, 2, 3, 4, 5]:  # definicja pętli i lista na której pętla jest wykonywana
    print(x)  # ciało pętli


for x in samochody:  # pętla na nazwanej liście
    print(x)

for x in samochody:  # pętla z warunkiem
    if x == 'Ford':  # definicja warunku
        print(f'{x} - to super samochód')
    else:
        print(x)

lista = []
for x in range(10):
    gosc = input('Podaj imię: ')
    lista.append(gosc)
lista.sort()
print(lista)
