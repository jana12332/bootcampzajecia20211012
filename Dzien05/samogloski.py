
SAMOGLOSKI = "aeiouy"

napis = input("Podaj napis: ")

ilosc_samoglosek = 0
# sp. 1

for litera in napis.lower():
    if litera in SAMOGLOSKI:
        ilosc_samoglosek += 1  # ilosc_samoglosek = ilosc_samoglosek + 1

print(f"Ilosc: {ilosc_samoglosek}")

# sp 2

ilosc_samoglosek = 0

for samogloska in SAMOGLOSKI:
    ilosc_samoglosek += napis.count(samogloska)
print(f"Ilosc sp 2: {ilosc_samoglosek}")