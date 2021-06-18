class Osoba:
    wspolczynnik_wyplaty = 1.5

    def __init__(self, imie, nazwisko, **kwargs):  # konstruktor klasy
        self.imie = imie
        self.nazwisko = nazwisko
        self.dodatkowy = 12
        self.stanowisko = kwargs.get('stanowisko', 'brak')
        self.wynagrodzenie = float(kwargs.get('wynagrodzenie', 1200))


class Maszyna():
    def __init__(self, pobor_energii, **kwargs):  # konstruktor klasy
        self.pobor_energii = pobor_energii
        self.oprogramowanie = float(kwargs.get('soft', 1.2))


class Cyborg(Osoba, Maszyna):
    def __init__(self, pobor_energii, nr_seryjny ** kwargs):  # konstruktor klasy
        self.pobor_energii = pobor_energii
        self.nr_seryjny = nr_seryjny


arnold = Cyborg(1200, 3.4)
arnold.imie = 'Arnold'
