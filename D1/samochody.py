class samochod():
    def __init__(self, marka, model, kolor, **kwargs):  # konstruktor klasy
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.ilosc_paliwa = 100

    def zatankuj_paliwo(self):
        pass


class benzynowy(samochod):
    def __init__(self, pojemnosc_baku, **kwargs):  # konstruktor klasy
        self.pojemnosc_baku = pojemnosc_baku

    def zatankuj_paliwo(self):
        print(
            f'pojemnoć baku {self.pojemnosc_baku}, maksymalnie zatankujesz {self.pojemnosc_baku-self.ilosc_paliwa} litrów benzyny')


class ropniak(samochod):
    def __init__(self, pojemnosc_baku, **kwargs):  # konstruktor klasy
        self.pojemnosc_baku = pojemnosc_baku

    def zatankuj_paliwo(self):
        print(
            f'pojemnoć baku {self.pojemnosc_baku}, maksymalnie zatankujesz {self.pojemnosc_baku-self.ilosc_paliwa} litrów ropy.')


class elektyczny(samochod):
    def __init__(self, pojemnosc_baterii, **kwargs):  # konstruktor klasy
        self.pojemnosc_baterii = pojemnosc_baterii

    def zatankuj_paliwo(self):
        print(
            f'pojemnoć baterii {self.pojemnosc_baterii}, maksymalnie naładujesz {self.pojemnosc_baterii-self.ilosc_paliwa} kWh.')


samochod1 = benzynowy(120)
samochod2 = ropniak(200)
samochod3 = elektyczny(400)

samochod1.marka = 'Opel'
samochod1.ilosc_paliwa = 60
samochod1.zatankuj_paliwo()

samochod2.marka = 'Ford'
samochod2.ilosc_paliwa = 60
samochod2.zatankuj_paliwo()

samochod3.marka = 'Tesla'
samochod3.ilosc_paliwa = 60
samochod3.zatankuj_paliwo()
