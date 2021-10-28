
# https://github.com/rkorzen/bootcampzajecia20211012

cena_za_kg = dict(
    marchew=1.22,
    pietruszka=2.34
)

magazyn = dict(
    marchew=20,
    pietruszka=20
)


while True:
    print("Witaj w naszym zielniku.")
    print("Jaki tryb programu? z - zakupym, m - magazyn")
    tryb = input()
    if tryb == "z":
        print()
        for product, cena in cena_za_kg.items():
            print(f" - {product} ({magazyn[product]}) w cenie {cena} PLN za kg")

        prod = input("Co chcesz kupic (wpisz 'nic' by zakonczyc): ")
        if prod == 'nic': break
        if prod not in cena_za_kg:
            print("Sorry nie mam tego")
            continue

        ile_kg = float(input("Ile kg: "))
        if ile_kg < magazyn[prod]:
            magazyn[prod] -= ile_kg  # magazyn[prod] = magazyn[prod] - ile_kg
        else:
            print("Sorry - nie mam tyle tego towaru")
            continue
        koszt = cena_za_kg[prod] * ile_kg

        print(f"Za {ile_kg} kg {prod} zaplacisz {koszt}")
        print()
    elif tryb == "m":
        print("Witaj w Trybie magazynowym")
        co = input("Co chcesz dodac? ")
        ile = input("Ile chcesz dodac? ")
        magazyn[co] = magazyn.get(co, 0) + int(ile)
        if co not in cena_za_kg:
            cena = float(input("Cena za kg? "))
            cena_za_kg[co] = cena

    else:
        print("Zly tryb")