"""
 Dokumentowanie funkcji
"""

# zwraca delte dla rown. kwadr.
def delta(a,b,c):
    '''Funkcja obliczająca delte dla rown. kwadratowego'''
    return b**2 - 4*a*c

def delta2(a,b,c):
    '''
    Funkcja obliczająca delte dla rown. kwadratowego

    Parametry:
        a - wspl. A
        b - wspl. B
        c - wspl. C

    Wynik:
        zwraca wartość delty
    '''
    return b**2 - 4*a*c

print(delta.__doc__)
print("="*50)
print(delta2.__doc__)

# Adnotacje dla zmiennych (type hint)
def utworz_pracownika(imie : str, nazwisko : str, rok_urodzenia : int) -> str:
    # własna walidacja typów argumentów
    if (type(imie) is str) \
            and (type(nazwisko) is str) \
            and (type(rok_urodzenia) is int):
        s = f"Imie i nazwisko: {imie} {nazwisko}\nRok urodzenia: {rok_urodzenia}"
        return s
    else:
        return None


print("="*50)
print(utworz_pracownika("Jan","Kowalski", 1991))
print(utworz_pracownika(9876, [1,2], "Kowalski"))
