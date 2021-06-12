import time
# odczyt pliku
with open('opis.txt', 'r', encoding='utf8') as plik:
    tresc = plik.read()
print(tresc)

# odczyt pliku linia po linii
with open('opis.txt', 'r', encoding='utf8') as plik:
    lines = plik.readlines()
    for line in lines:
        time.sleep(2)
        print(line.rstrip())

zwierzeta = ['struś', 'pelikan', 'koliber', 'wrona']

# zapis do pliku w trybie dodawania
with open('lista.txt', 'a', encoding='utf8') as plik:
    for ptak in zwierzeta:
        plik.write(ptak + '\n')

# odczyt z pliku i przekazanie danych do listy
zwierzeta = []
with open('lista.txt', 'r', encoding='utf8') as plik:
    lines = plik.readlines()
    for line in lines:
        zwierzeta.append(line.rstrip())
print(zwierzeta)

# zadanie z osobami - utwórz program w którym użytkownik wprowadza imiona z klawiatury
# każde wprowadzone imię zapisuje się do pliku
# program kończy się kiedy użytkownik wprowadzi pusty ciąg

with open('imiona.txt', 'a', encoding='utf8') as plik:
    while True:
        imie = input("podaj imię, (lub naciśnij enter aby wyjść): ")
        if not imie:
            break
        plik.write(imie + '\n')
    print("Program zakończył wpisywanie!")
