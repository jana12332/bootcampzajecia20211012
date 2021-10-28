cena_za_kg = {
    "marchew": 1.22,
    "pietruszka": 2.34
}

cena_za_kg = dict(
    marchew=1.22,
    pietruszka=2.34
)


while True:
    print("Witaj w naszym zielniku. Oferujemy: ")
    print()
    # for product in cena_za_kg:
    #     print(f" - {product} w cenie {cena_za_kg[product]} PLN za kg")

    for product, cena in cena_za_kg.items():
        print(f" - {product} w cenie {cena} PLN za kg")

    prod = input("Co chcesz kupic (wpisz 'nic' by zakonczyc): ")
    if prod == 'nic': break
    if prod not in cena_za_kg:
        print("Sorry nie mam tego")
        continue
    ile_kg = float(input("Ile kg: "))

    koszt = cena_za_kg[prod] * ile_kg

    print(f"Za {ile_kg} kg {prod} zaplacisz {koszt}")
