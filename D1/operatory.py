a = 5
b = 4

# operatory porównania
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)

# operatory przypisania
a = b
print(a)
b = 6
print(a)
a += 1
print(a)

tekst = 'ala ma '
tekst += 'kota'
print(tekst)
a -= 1
print(a)
a *= 4
print(a)
tekst *= 4
print(tekst)
a //= 2
print(a)
a %= 3
print(a)
a **= 3
print(a)
a = True
b = False

print(a & b)
print(a | b)

numer = 12
a = bin(numer)
print(bin(numer))

c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = 4
print(b in c)
print(b not in c)

c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 1
b = 1
c = d
d[0] = 2
print(a is b)
print(c is d)
print(c)
print(d)
