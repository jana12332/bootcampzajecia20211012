"""
 Funkcje o dowolnej liczbie parametrów
"""
def wiele_argumentow(*args): # * -> namiar na adres początkowy struktury w RAM z parametrami
    suma = 0
    for arg in args:
        if type(arg) is int:
            suma += arg # suma = suma + arg
    return suma

print(wiele_argumentow(1, "Ala ma kota", False, None, [], (1,2,3), -1, 10 ))

def min_dwa_parametry(arg1, arg2, *args):
    suma = 0
    for arg in args:
        if type(arg) is int:
            suma += arg # suma = suma + arg
    return suma

print(min_dwa_parametry(1, "Ala ma kota", False, None, [], (1,2,3), -1, 10 ))

# przykład użycia print
print(3, "Ala ma kota", [2,3,4], sep="|", end="@@")
print(3, "Ala ma kota", [2,3,4], sep="|")

## funkcja z kwargs
def funkcja_kwargs(**kwargs):
    print("="*50)
    print(f"imie={kwargs.get('imie')}")
    print(f"nazwisko={kwargs.get('nazwisko','--brak nazwiska--')}")
    print(f"wiek={kwargs.get('wiek','--nie podano wieku--')}")

funkcja_kwargs(imie="Jan",nazwisko="Kowalski", wiek=45, staz=10, wynagrodzenie=12345)
funkcja_kwargs(imie="Jan",staz=10, wynagrodzenie=12345)
funkcja_kwargs(imie="Jan",nazwisko="Kowalski", wiek=45, staz=10, wynagrodzenie=12345, kierownik=True)
