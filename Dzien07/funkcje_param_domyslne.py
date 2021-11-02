"""
Funkcja z parametrami domyślnymi
"""
def nowy_pracownik(imie, nazwisko, telefon="22123456", email="info@firma.com"):
    pracownik = {
        "imie" : imie, "nazwisko" : nazwisko,
        "telefon": telefon, "email": email
    }
    return pracownik

# przykłady użycia
print(nowy_pracownik("Jan","Kowalski","601602063", "jk@firma.com"))
print(nowy_pracownik("Jan","Kowalski"))
print(nowy_pracownik("Jan","Kowalski", "502505507"))
print(nowy_pracownik("Jan","Kowalski", email="jk@firma.com" ))
print(nowy_pracownik("Jan","Kowalski", email="jk@firma.com", telefon="606123456" ))
