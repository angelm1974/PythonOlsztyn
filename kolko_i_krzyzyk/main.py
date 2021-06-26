# from random import choice
# Uruchom interfejs gry
# Podaj imię gracza - OK
# Wybierz figurę -o lub x - OK
# wylosuj kto rozpoczyna grę
# gracze=['czlowiek', 'komputer']
# print(choice(gracze))
# plansza
# plansza=[0,0,0,0,0,0,0,0,0]
# plansza2={1:'A1'}

# Rozpoczynający wybiera pole z planszy
# Powyborze następuje procedura sprawdzenia wyniku
# tablica wygranych
# wygrane=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
# ruch komputera
# z planszy wybieramy indeksy wolne i tworzymy z nich listę
# z listy za pomocą metody random choise wybieramy dowolny index
# zapisujemy wynik na planszę
# sprawdzamy tablice wygranych
# wyświetlamy planszę po zmianach
# w przypadku kiedy zwycięstwo jednego z graczy to ogłaszamy

from kolko_i_krzyzyk.kolko_krzyzyk import Kolko_Krzyzyk


moja_gra = Kolko_Krzyzyk()
moja_gra.run()