str1 = "to jest ciąg 1"
str2 = "to jest ciąg 2"
str3 = 'abc test'
str_multiline = '''
Dzięki specjalnie stworzonemu algorytmowi wyliczono szanse poszczególnych drużyn na Euro 2020
Polacy mają wyjść z grupy kosztem Szwecji. Dalej jednak nie będzie tak kolorowo
Za faworytów imprezy uchodzą Francuzi, obecni mistrzowie świata
Więcej takich historii znajdziesz na stronie głównej Onet.pl
Faworytami są reprezentacje Francji, Belgii, Niemiec i Portugalii, ale niczego tak naprawdę nie możemy być pewni. Z pomocą w przewidywaniu tego, kto wygra Euro 2020 oraz tego, jak daleko zajdą poszczególne reprezentacje przyszedł algorytm nazwany "Superkomputerem".
'''

nested = 'elastyczne zagnieżdzanie - "tylko w pythonie"'
print(nested)

print("Python\njest\nfajny")
print("Python\tjest\tfajny")
print(str1 + str2)
print(str1, str2, sep='-')
print(str1, str2, sep='\n')

imie = "Jan"
nazwisko = "Kowalski"
# literka f przed znakiem apostrofu lub cudzysłowia informuje, ze w ciągu podane w klamrowym nawiasie nazwy zmiennych mają pobierać jej wartość
imie_nazwisko = f'{imie} 23, {nazwisko} to fajny gość'
print(imie_nazwisko)

pierwsza_litera = imie_nazwisko[0]  # pobranie 1 litery z stringa
print(pierwsza_litera)

zakres_liter = imie_nazwisko[0:3]  # pobranie pierwszych 3 liter
print(zakres_liter)

zakres_liter = imie_nazwisko[4:]  # bez Jana do końca
print(zakres_liter)

zakres_ostatnich_4_liter = imie_nazwisko[-4:]  # pobieramy 4 ostatnie
print(zakres_ostatnich_4_liter)
co_druga = imie_nazwisko[::2]
print(co_druga)

zwierze = 'biały słoń z kłami'
print(zwierze.capitalize())
print(zwierze.title())
substring = 'a'
zlicz = zwierze.count(substring)
print(zlicz)
zwierze.upper()
zwierze.lower()
