import figury

# Pole kwadratu
a = float(input('Podaj bok kwadratu: '))
print('Pole kwadratu o boku ', a, ' wynosi: ', figury.pole_kwadratu(a))

# Pole prostokąta
a = float(input('Podaj dłuższy bok prostokąta: '))
b = float(input('Podaj krótszy bok prostokąta: '))
print('Pole prostokąta o bokach ', a, ' i ',
      b, ' wynosi: ', figury.pole_prostokata(a, b))

# Pole trójkąta
a = float(input('Podaj podstawę trójkąta: '))
h = float(input('Podaj wysokość trójkąta: '))
print('Pole trójkąta o podstawie ', a, ' i wysokości ',
      h, ' wynosi: ', figury.pole_trojkata(a, h))

# Pole koła
r = float(input('Podaj promień koła: '))
print('Pole koła o promieniu ', r, ' wynosi ', figury.pole_kola(r))
