krotka = ()
print(krotka, type(krotka))
krotka1 = ('Olek',)
print(krotka1, type(krotka1))

imiona = ('Ala', 'Ola', 'Jan')
imiona1 = 'Tadeusz', 'Jonasz',

for imie in imiona:
    print(imie)

mojalista = list(imiona)
mojalista[1] = 'Ania'
print(mojalista)
imiona = tuple(mojalista)
print(imiona)
im1, im2, im3 = imiona
print(im1, im2, im3)
imiona=(im1, im2, im3)