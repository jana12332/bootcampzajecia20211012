"""
Funkcje w Pythonie
"""
import math

# pusta funkcja
def foo():
    pass

def oblicz_pole(r):
    # pole = 3.14159*(r**2)
    # return pole
    return math.pi*(r**2)

def oblicz_obwod(r):
    return 2*math.pi*r

# zwraca pole i obwod koła
def oblicz_kolo(r):
    pole = oblicz_pole(r)
    obwod = oblicz_obwod(r)
    return pole, obwod

# test funkcji
print(oblicz_pole(2))
print(oblicz_obwod(2))
print(oblicz_kolo(3))

# ta funkcja nie zwraca wartości
def wypisz_duze_litery(s):
    print(s.upper())

wypisz_duze_litery("aBc")
