

text = "Ala ma kota"

# licznik = {}
licznik = dict()

for znak in text.lower():
    # if znak in licznik:
    #     licznik[znak] += 1
    # else:
    #     licznik[znak] = 1

    licznik[znak] = licznik.get(znak, 0) + 1

print(licznik)

from collections import defaultdict


licznik = defaultdict(int)

for znak in text.lower():
    licznik[znak] += 1
print(licznik)