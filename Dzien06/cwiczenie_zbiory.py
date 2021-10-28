liczby = set()

while True:
    liczba = input("Podaj liczbe lub k by zakonczyc")
    if liczba == "k":
        break
    liczby.add(int(liczba))

print(liczby)

print(f"Unikalnych {len(liczby)}")

l_parzyste_od_2_100 = set(range(2, 101, 2))

print(len(liczby & l_parzyste_od_2_100), "parzystych z zakresu 2-100")