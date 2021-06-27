a = 20  # deklarujemy zmienną a
b = 10  # deklarujemy zmienną b

suma = a+b  # deklarujemy zmienną suma oraz przypisujemy jej wartość a+b
print(suma)  # wyświetlamy wartość suma
print(suma, type(suma))  # wyświetlamy wartość oraz wyświetlamy typ danych

a = 1.23
b = 33.44
suma = a/b
print(suma, type(suma))


a = 20
print(a, type(a))  # typ int

a = 10.5
print(a, type(a))  # typ float

a = -10
print(a, type(a))  # typ int

a = False
print(a, type(a))  # typ bool

a = "dwadzieścia"
print(a, type(a))  # typ str

# suma = a/b  # - ten fragment powoduje błąd ze wględu na brak operacji dzielenia str/float
print(suma)

b = 10
suma = a*b
print(suma)

# definicja zmiennych (złożona definicja)
a, b, c = 3, 3.5, "Hello"  # nadawanie nazw zmiennym po kolei
ab = cd = ef = gi = 8  # przypisywanie tej samej wartości do różnych zmiennych

var = None # definicja pustej wartości

if var is None: # polecenie if z warunkiem czy var jest puste
    print("typ pusty", type(var)) #wykonanie kodu jeżeli jest puste
else: #w innym przypadku kiedy var jest niepuste
    print("nie puste") # wydruk tekstu

