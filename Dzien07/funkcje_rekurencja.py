"""
 Rekurencja i funkcje
"""
import time

def silnia_iter(n): # silnia iteracyjne
    wynik = 1
    for x in range(1, n+1):
        wynik *= x # wynik = wynik * x
    return wynik

# n>1 - n*silnia(n-1)
# n=1 - 1
def silnia_rek(n): # silnia rekurencyjnie
    if n>1:
        return n*silnia_rek(n-1)
    else:
        return 1

print(silnia_iter(5), silnia_rek(5))

LICZBA_ITER = 10_000 # liczba iteracji
N = 300 # liczba dla ktorej licze silnie

# badanie szybkosci wykonania funkcji
t1 = time.time() # zwraca tzw. unix timestamp w formie liczby float
for _ in range(LICZBA_ITER): silnia_rek(N)
t2 = time.time()
print(f"Czas wykonania silnia_rek = {t2-t1} sek.")

t1 = time.time() # zwraca tzw. unix timestamp w formie liczby float
for _ in range(LICZBA_ITER): silnia_iter(N)
t2 = time.time()
print(f"Czas wykonania silnia_iter = {t2-t1} sek.")