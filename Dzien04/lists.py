"""
 Listy w Pythonie
"""
list1 = list() # pusta lista
list1 = [] # pusta lista
list1 = [1, "Ala ma kota", True, 999.99, (1,), ["A","B"], None ] # deklaracja listy z wartosciami inicjalnymi
print(list1)

# dodaj element na koniec listy
list1.append(2)
print(list1)

# dodaj listę na koniec listy
list1.extend([9,8,7, 1])
print(list1)

# wstawianie elementów w listę
list1.insert(1, 6789)
print(list1)

# usuwanie elementow z listy
list1.remove("Ala ma kota")
print(list1)

list1.remove(1)
print(list1)

# detekcja liczby elementow o podanej wartosci w liscie
print(list1.count(1))

# przed usunieciem, sprawdzam ile czy są wartości do usunięcia
# if list1.count("Alka ma kota"):
#     list1.remove("Alka ma kota")
if "Alka ma kota" in list1:
    list1.remove("Alka ma kota")

# Ile jest elementów?
print(f"Liczba elementów = {len(list1)}")

print(f"Pozycja liczby 999.99 to {list1.index(999.99)}")

# usuwanie 1-go elementu w liscie
del(list1[0])

# modyfikacja wartości elementu listy
list1[0] = "ABC"
print(list1)

# kopiowanie list
list2 = list1.copy()
list2[0] = "XYZ"
print(f"List1 = {list1}")
print(f"List2 = {list2}")
print(f"list1={id(list1)}, list2={id(list2)}")



x = [1, 2, 3]
z = x
y = [4, 5, x]
yy = y.copy()
print(x)
print(y)

x.append(7)

print(x)
print(y)
print(yy)

import copy
yy = copy.deepcopy(y)


lista = [1, 2, 3]
print(id(lista))
lista.append(4)
lista.pop()
print(id(lista))

krotka = (1, 2, 3)
print(id(krotka))
krotka = krotka + (1, )
print(id(krotka))