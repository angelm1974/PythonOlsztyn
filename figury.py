# Pola figur
import math


def pole_kwadratu(a):
    pole = a * a
    return pole


def pole_prostokata(a, b):
    pole = a * b
    return pole


def pole_trojkata(a, h):
    pole = 1/2 * a * h
    return pole


def pole_kola(r):
    pole = math.pi * r**2
    return pole


def pole_figury(**kwargs):
    # figura
    # a,b,h,r
    return 3


def pole_figury(**kwargs):
    figura = (kwargs.get('figura', 'brak argumentu'))
    a = float(kwargs.get('a', 'brak argumentu'))
    b = float(kwargs.get('b', 'brak argumentu'))
    h = float(kwargs.get('h', 'brak argumentu'))
    r = float(kwargs.get('r', 'brak argumentu'))
    if figura == 'kwadrat':
        return pow(a, 2)
    elif figura == 'prostokąt':
        return a*b
    elif figura == 'trójkąt':
        return 0.5*a*b
    elif figura == 'koło':
        pole = math.pi * pow(r, 2)
        return pole
    else:
        print("wyswietli się w każdym innym przypadku")
