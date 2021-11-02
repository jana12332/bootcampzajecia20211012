"""
 Rekurencja i funkcje
"""
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