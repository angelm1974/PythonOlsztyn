import abc


class Ptak(abc.ABC):
    @abc.abstractmethod
    def leć(self):
        pass


class Papuga(Ptak):
    def leć(self):
        super(Papuga, self).__init__()
        print('poleciała!')


p1 = Papuga()
p1.leć()


class człowiek(abc.ABC):
    @abc.abstractmethod
    def PodajImie(self, strImie):
        pass

    @abc.abstractmethod
    def PodajNazwisko(self, strNazwisko):
        pass


class Kierownik(człowiek):
    def __init__(self):
        self.Imie = ''
        self.Nazwisko = ''

    def PodajImie(self, strImie):
        self.Imie = strImie
        super(Kierownik, self).__init__()
        print(strImie)

    def PodajNazwisko(self, strNazwisko):
        self.Nazwisko = strNazwisko
        super(Kierownik, self).__init__()
        print(strNazwisko)


Rafal = Kierownik()
Rafal.PodajImie('Adam')
Rafal.PodajNazwisko('Kowalski')
