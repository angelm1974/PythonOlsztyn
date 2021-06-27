# czlowiek
# imie
# nazwisko
# wzrost
# plec
# wiek
# pesel
# stanowisko
# telefon
# kot
# waga
# wysokosc
# dlugosc
# rasa
# wiek
# plec
# siersc
# ubarwienie
# kondycja
# wlasciciel
# dlugosc_wibrysów
# Ola=czlowiek

# Garfield=Kot
# waga=62
# wysokosc=30
# dlugosc=60.33
# rasa=dachowiec
# wiek=12
# plec=samiec
# siersc=krótka
# ubarwienie=rude
# kondycja=ok
# wlasciciel=Ola
# dlugosc_wibrysów=25

# wyswietl garfield.wlasciciel.telefon

lista_plci = ('K', 'M', 'N',)


class czlowiek:
    imie = ''
    nazwisko = ''
    wzrost = -1
    plec = ''
    wiek = -1
    pesel = -1
    stanowisko = ''
    telefon = -1


Adam = czlowiek()
Mariusz = czlowiek()

Adam.imie = 'Adam'
Adam.nazwisko = 'Kowalski'
Adam.wzrost = 185
Adam.plec = lista_plci[1]
Adam.wiek = 32
Adam.pesel = 1264616546
Adam.stanowisko = 'Kierownik'
Adam.telefon = 453348641

print(Adam.plec)
print(Mariusz.plec)


class kot:
    waga = 62
    wysokosc = 30
    dlugosc = 60.33
    rasa = 'dachowiec'
    wiek = 12
    plec = 'samiec'
    siersc = 'krótka'
    ubarwienie = 'rude'
    kondycja = 'ok'
    wlasciciel = None
    dlugosc_wibrysów = 25


garfield = kot()
garfield.wlasciciel = Adam

print(garfield.wlasciciel.nazwisko)


class Osoba:
    wspolczynnik_wyplaty = 1.5

    def __init__(self, imie, nazwisko, **kwargs):  # konstruktor klasy
        self.imie = imie
        self.nazwisko = nazwisko
        self.dodatkowy = 12
        self.stanowisko = kwargs.get('stanowisko', 'brak')
        self.wynagrodzenie = float(kwargs.get('wynagrodzenie', 1200))

    def podaj_imie_nazwisko(self):
        print(self.nazwisko, self.imie)

    def pobierz_wynagrodzenie(self):
        return self.wynagrodzenie * self.wspolczynnik_wyplaty


Ola = Osoba('Aleksandra', 'Kot', stanowisko='dyrektor', wynagrodzenie=3100.32)
print(Ola.nazwisko)
print(Ola.wspolczynnik_wyplaty)
print(Ola.stanowisko)
print(Ola.dodatkowy)
Ola.podaj_imie_nazwisko()
wynagrodzenie_Oli = Ola.pobierz_wynagrodzenie()
print(wynagrodzenie_Oli)


class Administrator(Osoba):
    wspolczynnik_wyplaty = 3.0

    def __init__(self, imie, nazwisko, user, password, **kwargs):  # konstruktor klasy
        self.imie = imie
        self.nazwisko = nazwisko
        self.user = user
        self.password = password
        self.wynagrodzenie = float(kwargs.get('wynagrodzenie', 1200))

    def resetuj_system(self):
        print(self.user+self.password+str(324))


Kuba = Administrator('Jakub', 'Nowak', 'jakub', 'Ha5l0', wynagrodzenie=2400)
print(Kuba.pobierz_wynagrodzenie())
Kuba.resetuj_system()


class Administrator2(Osoba):
    wspolczynnik_wyplaty = 3.0

    def __init__(self, imie, nazwisko, user, password, **kwargs):  # konstruktor klasy
        super().__init__(imie, nazwisko)
        self.user = user
        self.password = password
        self.wynagrodzenie = float(kwargs.get('wynagrodzenie', 1200))
        print('Utworzono Admina 2')
        print(f'Wynagrodzenie  brutto - {super().pobierz_wynagrodzenie()}')  # wywołanie metody z klasy nadrzednej

    def pobierz_wynagrodzenie(self):
        return (self.wynagrodzenie * self.wspolczynnik_wyplaty)/1.23


Tomasz = Administrator2('Tomasz', 'Adamski', 'user', 'Haslo1')
print(f'Wynagrodzenie netto - {Tomasz.pobierz_wynagrodzenie()}')
Tomasz.podaj_imie_nazwisko()

