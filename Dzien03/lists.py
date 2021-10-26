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
list1.extend([9,8,7])
print(list1)


liczby = [1, 2, 3, 4, 5, 6, 10, 20, 0]
liczby[4]
liczby[1] = 22
print(liczby)