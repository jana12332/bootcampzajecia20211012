slownik = {}
print(slownik, type(slownik))

slownik = {"a": 1, "b": "cos tam"}
print(slownik)

print(slownik.keys())
print(slownik.values())
print(slownik.items())
(1, 2,)
(1,)
# klucze to unikalne i hashowalne obiekty
# {[1, 2]: "x"}  # TypeError: unhashable type: 'list'

print(slownik["a"])
slownik["a"] = "Ala"
print(slownik["a"])

# dodanie pary:
slownik["c"] = "czas"
print(slownik)

lista = [["a", 1],["b", "cos tam"],["z", 12]]
# szukam wartosci dla z:

for el in lista:
    if el[0] == "z":
        print(el[1])


{"a":10, "e":8}

"aaaaaa"

{"a":6}

"aabbaa"
{"a":4, "b":2}