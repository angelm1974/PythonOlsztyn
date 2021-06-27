mojset = set()
mojset2 = {1, 432, 3, 5, 2, 1, 1, 1, 1, 2, 2}
print(mojset, mojset2)

tekst = set('"Superkomputer" zdecydował. Jak daleko na Euro 2020 zajdą Polacy? Euro 2020 wreszcie się rozpoczyna. Podopieczni Paulo Sousy rozpoczną przygodę z mistrzostwami Europy jednak dopiero w poniedziałek od starcia Polska - Słowacja. Kibice, specjaliści i dziennikarze prześcigają się w typowaniu ostatecznych wyników reprezentacji Polski.')
print(tekst)

# Działania na zbiorach

A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = ["Adam", 1, 4, 6, 3, 7, 5, 1, 9]
print("Suma:", A | B)  # suma zbiorów
print("Suma:", A.union(B))  # suma zbiorów
print("Suma:", A.union(C))  # suma zbiorów

# część wspólna
print("Część wspólna:", A & B)
print("Część wspólna:", A.intersection(B))
print("Część wspólna:", A.intersection(C))

# różnice zbiorów
print("Różnica A-B: ", A-B)
print("Różnica B-A: ", B-A)
print("Różnica symetryczna:", A ^ B)
print("Różnica: ", A.difference(B))
print("Różnica symetryczna:", A.symmetric_difference(B))

A = {0, 1, 2, 3}
B = {1, 2, 8}
print("Czy zbiór B jest podzbiorem zbioru A:", B.issubset(A))
print("Czy zbiór B jest zbiorem nadrzędnym zbioru A:", A.issuperset(B))

A.add(4)
print(A)
A.update(B)
print(A)
A.discard(8)
print(A)
# A.clear()
print(A.pop())
print(A.pop())
print(A)
