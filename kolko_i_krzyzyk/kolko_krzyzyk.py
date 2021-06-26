
from kolko_i_krzyzyk.gracz import Gracz
from random import choice

# Możliwe Figury True=kółko, False=Krzyżyk
# Człowiek to gracz nr 1 a komputer to gracz nr 2


class Kolko_Krzyzyk():
    def __init__(self):  # konstruktor klasy
        self.czlowiek = Gracz('Imię z UI')
        self.komputer = Gracz('Ai')
        self.runda = 0
        self.czyj_ruch = 0
        self.pozostalo_ruchow = 9
        self.plansza = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.wygrane = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                        [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def run(self):
        self.czyj_ruch = choice[self.czlowiek, self.komputer]
        self.wybor_figury()

        while True:
            # przebieg gry
            if self.czyj_ruch == self.komputer:
                self.wylosuj_ruch_za_komputer()
            else:
                self.ruch_czlowieka()

            self.pozostalo_ruchow -= 1
            sprawdzenie = self.sprawdzenie_wygranej()
            if sprawdzenie:
                self.wyswietl_wynik()
                break

    def sprawdzenie_wygranej(self):
        # sprawdzenie kto wygrał
        return True

    def wyswietl_wynik(self):
        wynik_komputera = self.komputer.punkty
        wynik_czlowieka = self.czlowiek.punkty

    def wybor_figury(self):
        if self.czyj_ruch == self.komputer:
            self.komputer.figura = choice[True, False]
            self.czlowiek.figura = not(self.komputer.figura)
        else:
            wybor_z_okna = True
            self.czlowiek.figura = wybor_z_okna
            self.komputer.figura = not(self.czlowiek.figura)

    def wylosuj_ruch_za_komputer(self):
        lista_do_losowania = []
        a = -1
        for x in self.plansza:
            a += 1
            if x == 0:
                lista_do_losowania.append(a)

        wylowana_pozycja = choice(lista_do_losowania)
        self.plansza[wylowana_pozycja] = 2

    def ruch_czlowieka(self):
        wybor_z_interfejsu = 8

        if self.plansza[wybor_z_interfejsu] != 0:
            print('Nie możesz w ten sposób zagrać!')
        else:
            self.plansza[wybor_z_interfejsu] = 1
