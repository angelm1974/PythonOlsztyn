# Sklepy
class siec:
    def __init__(self,  **kwargs):
        self.wlasciciel = None


class odziezowy(siec):
    def __init(self, sprzedaz, **kwargs):
        self.sprzedaz = sprzedaz

    def podaj_sprzedaz(self):
        return self.sprzedaz


class obuwniczy(siec):
    def __init(self, sprzedaz, **kwargs):
        self.sprzedaz = sprzedaz

    def podaj_sprzedaz(self):
        return self.sprzedaz


class drogeria(siec):
    def __init(self, sprzedaz, **kwargs):
        self.sprzedaz = sprzedaz

    def podaj_sprzedaz(self):
        return self.sprzedaz





class wlasciciel():
    sprzedaz_dr = 0
    sprzedaz_ob = 0
    sprzedaz_od = 0

Tomasz=wlasciciel()

sklep1 = odziezowy()
sklep2 = obuwniczy()
sklep3 = drogeria()
sklep4 = drogeria()


sklep1.sprzedaz = 10
sklep2.sprzedaz = 20
sklep3.sprzedaz = 30

sklep1.wlasciciel=Tomasz
sklep2.wlasciciel=Tomasz
sklep3.wlasciciel=Tomasz
sklep4.wlasciciel=Tomasz

sklep1.wlasciciel.sprzedaz_od+=10
sklep1.wlasciciel.sprzedaz_od+=30
sklep2.wlasciciel.sprzedaz_ob+=20
sklep3.wlasciciel.sprzedaz_dr+=40
sklep4.wlasciciel.sprzedaz_dr+=50

print(
    f'Sieć sklepów sprzedała {sklep1.podaj_sprzedaz() + sklep2.podaj_sprzedaz() + sklep3.podaj_sprzedaz()} sztuk towaru')

print(
    f'drogerie{ Tomasz.sprzedaz_dr }, obuwnicze {Tomasz.sprzedaz_ob}, odzieżowe {Tomasz.sprzedaz_od} ')
