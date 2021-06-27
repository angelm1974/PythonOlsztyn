# lambda x: x*2+3

def y(x): return x * 2 + 3


print(y(30), type(y(30)))


def af_2(w): return w.upper()


print(af_2('python'))

kwadraty = map(lambda x: x ** 2, range(10))
print(list(kwadraty), type(list(kwadraty)))


def apply_function(x, fn):
    return fn(x)


print(apply_function(5, lambda x: x**2))
print(apply_function([45, 32], lambda x: sum(x)))

numbers = [-3, -2, -1, 0, 1, 2, 3]

print(sorted(numbers, key=lambda x: abs(x)))