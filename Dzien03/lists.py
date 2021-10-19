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