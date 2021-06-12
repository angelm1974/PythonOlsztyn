osoba = {
    "name": "Jan",
    "last_name": "Kowalski",
    "age": 37,
    "abc": "Jurek"
}
samochod = {
    "marka": "Fiat",
    "model": "Punto",
    "rocznik": 2019
}

print(osoba, type(osoba))

print(osoba["age"])  # wyświetlenie wartości dla danego klucza
# print(osoba[2])
osoba["height"] = 1.84  # dodanie nowej pary klucz wartość
print(osoba)
osoba["height"] = 1.54  # aktualizacja pary klucz wartość
print(osoba)
del osoba["height"]  # usuwanie pary
print(osoba)
osoba.update(samochod)
print(osoba)
print(osoba.pop("height", "nie ma takiego klucza"))

mojazmienna = osoba.get("age", 25)
print(mojazmienna)
# osoba.clear()
# print(osoba)
print(osoba.keys())

# pobrać listę
lista_kluczy = osoba.keys()
# przeiterować za pomocą pętli for
osoba.pop("age")
print(lista_kluczy)
for i in lista_kluczy:
    # wyświetlić wartości słownika dla poszczególnych kluczy :)
    print(osoba[i])
    print(osoba.get(i, "brak klucza"))

print(osoba.items())

for k, w in osoba.items():
    print(f'mój klucz: {k}, moja wartość: {w}')


lista_wartosci = osoba.values()
print(lista_wartosci)

for k in sorted(osoba.keys()):
    print(k)

osoba["samochod"] = samochod


b = ['słoń', 'kot', 23, 34, True, 44.56, 'rybki']

osoba["rzeczy"] = b
print(osoba)
