
from gracz import Gracz
from random import choice

# Możliwe Figury True=kółko, False=Krzyżyk
# Człowiek to gracz nr 1 a komputer to gracz nr 2


class Kolko_Krzyzyk():
    def __init__(self):  # konstruktor klasy
        self.czlowiek = Gracz(input('Podaj imię: '))
        self.komputer = Gracz('Ai')
        self.runda = 0
        self.czyj_ruch = 0
        self.pozostalo_ruchow = 9
        self.plansza = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.wygrane = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                        [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def run(self):
        self.runda += 1
        self.czyj_ruch = choice([self.czlowiek, self.komputer])
        print(self.czyj_ruch.imie)
        self.wybor_figury()

        while True:
            # przebieg gry
            if self.czyj_ruch == self.komputer:
                self.wylosuj_ruch_za_komputer()
            else:
                self.ruch_czlowieka()

            self.pozostalo_ruchow -= 1
            if self.pozostalo_ruchow == 0:
                self.wyswietl_wynik()
                self.wyczysc_gre()
                break

            sprawdzenie = self.sprawdzenie_wygranej()
            if sprawdzenie == True:
                self.czyj_ruch.dodaj_punkt()
                self.wyswietl_wynik()
                self.wyczysc_gre()
                break

            if self.czyj_ruch == self.komputer:
                self.czyj_ruch = self.czlowiek
            else:
                self.czyj_ruch = self.komputer

    def sprawdzenie_wygranej(self):
        lista_do_sprawdzenia = []
        a = -1
        for x in self.plansza:
            a += 1
            if self.czyj_ruch == self.komputer:
                if x == 2:
                    lista_do_sprawdzenia.append(a)
            else:
                if x == 1:
                    lista_do_sprawdzenia.append(a)

        for x in self.wygrane:
            set1 = set(x)
            set2 = set(lista_do_sprawdzenia)

            if(set1.issubset(set2)):
                return True

    def wyswietl_wynik(self):
        wynik_komputera = self.komputer.punkty
        wynik_czlowieka = self.czlowiek.punkty
        print(wynik_czlowieka, wynik_komputera)

    def wybor_figury(self):
        if self.czyj_ruch == self.komputer:
            self.komputer.figura = choice([True, False])
            self.czlowiek.figura = not(self.komputer.figura)
            print(self.komputer.figura)
        else:
            wybor_z_okna = True
            self.czlowiek.figura = wybor_z_okna
            self.komputer.figura = not(self.czlowiek.figura)
            print(self.czlowiek.figura)

    def wylosuj_ruch_za_komputer(self):
        lista_do_losowania = []
        a = -1
        for x in self.plansza:
            a += 1
            if x == 0:
                lista_do_losowania.append(a)

        wylowana_pozycja = choice(lista_do_losowania)
        self.plansza[wylowana_pozycja] = 2
        print('po ruchu komputera', self.plansza)

    def ruch_czlowieka(self):
        wybor_z_interfejsu = int(input("Podaj indeks pozycji: "))

        if self.plansza[wybor_z_interfejsu] != 0:
            print('Nie możesz w ten sposób zagrać!')
        else:
            self.plansza[wybor_z_interfejsu] = 1

        print('po ruchu czlowieka', self.plansza)

    def wyczysc_gre(self):
        self.pozostalo_ruchow = 9
        self.plansza = [0, 0, 0, 0, 0, 0, 0, 0, 0]
