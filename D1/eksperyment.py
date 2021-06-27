lista = [2, 2, 2, 1, 2, 1, 2, 0, 0]
wygrane = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
           [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

lista_do_sprawdzenia = []


def sprawdzenie_wygranej():
    a = -1
    for x in lista:
        a += 1
        if x == 2:
            lista_do_sprawdzenia.append(a)


sprawdzenie_wygranej()
print(lista_do_sprawdzenia)

for x in wygrane:
    set1=set(x)
    set2=set(lista_do_sprawdzenia)
    
    if(set1.issubset(set2)):
        print("wygrałeś")
