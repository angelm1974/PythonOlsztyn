str1 = "to jest ciąg 1"
str2 = "to jest ciąg 2"

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
