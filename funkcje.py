#import mojmodul
from mojmodul import drukuj_sowe_m as dm

print(chr(78))
print(ord('N'))
print(eval('2+2'))

kraje = ['Pakistan', 'Jordania', 'Liban', 'Argentyna']
for i, kraj in enumerate(kraje):
    print(i, kraj)

st1 = 'A'
st2 = 'b'


def drukuj_sowe():
    imie = input("Podaj imię: ")
    print(f"{imie} - Jesteś sową!")


def sumuj(liczba1, liczba2):
    suma = int(liczba1) + int(liczba2)
    print(f'Suma {liczba1} i {liczba2} wynosi: {suma}')


# drukuj_sowe()
#sumuj(input("x: "), input("y: "))


def dodawanie(w1=5, w2=4):
    suma = w1+w2
    print(suma)


dodawanie()
dodawanie(2)
dodawanie(2, 1)


def dodawanie2(w1, w2=10):
    suma = w1+w2
    print(suma)


dodawanie2(2)


def odejmowanie(x):
    return x-1

    liczba3 = odejmowanie(5)
    print(liczba3*3)

# dowolna liczba argumentów


def moja_funkcja1(x, *args):
    print(f'To pierwszy argument- {x}')
    for arg in args:
        print(f'kolejny argument: {arg}')


moja_funkcja1(12)
moja_funkcja1(12, 34, 'olek', 11, 2, 8)


def make_pizza(wielkość, *args):
    print(f'wielkość pizzy - {wielkość}')
    for i, arg in enumerate(args):
        print(f'Składnik nr {i+1} pizzy {arg}')


make_pizza(50, 'cebula', 'czosnek', 'ketchup', 'kielbasa')


def nazwane_arg(w, **kwargs):
    print(kwargs.get('kosc', 'brak argumentu'))


nazwane_arg(1, kosc=23, slon=22)

# mojmodul.dodawanie_m(4,6)
# mojmodul.drukuj_sowe_m()
dm()