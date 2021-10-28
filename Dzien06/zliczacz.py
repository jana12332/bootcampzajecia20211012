
# Rozwiazanie 1

text = "Ala ma <kota>."
counter = 0
zliczaj = False
for znak in text:
    if znak == "<": # chce zaczac zliczac
        zliczaj = True
        continue
    elif znak == ">":
        zliczaj = False

    if zliczaj == True:
        counter += 1

print(counter)

# Rozwiazanie 2

print(text.index("<"))
print(text.index(">"))
print(text.index(">") - text.index("<") - 1)

print(len(range(text.index("<"), text.index(">"))) - 1)