'''
# kontrola przepływu programu
x = int(input("Podaj aktualną prędkość w terenie zabudowanym (km/h): "))
if x > 50:
    # instrukcje kiedy warunek jest prawdziwy
    print("Twoja prędkość jest zbyt duża!!!")
elif x == 50:
    print("Twoja prędkość jest maksymalną dozwoloną prędkością!!!")
else:
    print("Twoja prędkość jest prawidłowa :D!")
    # instrukcje kiedy warunek jest fałszywy

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
if a == b:
    print(f"a:{a} jest równe b:{b}")
elif a > b:
    print(f'a:{a} jest większe od b:{b}')
else:
    print(f"a:{a} jest mniejsze od b:{b}")
'''

zwierzeta = ['zając', 'słoń', 'koń', 'pies', 'kot']
for zwierze in zwierzeta:
    print(f'ilość znaków w {zwierze.upper()} to {len(zwierze)}')

for value in range(1, 30):
    print(value)

nazwa = "Python"
for x in nazwa:
    if x == "h":
        break
    print(x)

for x in nazwa:
    if x == "h":
        continue
    print(x)

liczba = 1
while liczba < 30:
    if liczba % 2 == 0:
        print(liczba)
    else:
        print("liczba nieparzysta!")
    liczba += 1


kawdraty = []
pozostale = []

for a in range(20, 0, -1):
    if a % 3 == 0:
        kawdraty.append(a**2)
    else:
        pozostale.append(a)
print(kawdraty)
pozostale.reverse()
print(pozostale)


# pierwszy program
liczba = 10
for x in range(0, 10):
    liczba = liczba - 1
    if x == 4:
        break
print(liczba)


# drugi program
lista = [4, 5, 9, 3, 5, 3, 7, 1]
liczba = 0
for x in lista:
    if x == 3 or x == 5:
        continue
    else:
        liczba = liczba + x
print(liczba)
