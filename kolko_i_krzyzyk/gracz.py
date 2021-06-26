class Gracz:

    def __init__(self, imie):  # konstruktor klasy
        self.imie = imie
        self.punkty = 0
        self.figura = 0

    def dodaj_punkt(self):
        self.punkty += 1
