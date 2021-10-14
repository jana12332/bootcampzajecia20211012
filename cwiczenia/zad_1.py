imie = input("Podaj imię: ")
wzrost = input("Podaj wzrost: ")
bmi = 34.25

raport = f"""
Imię:   {imie:3}  xxx
Wzrost: {wzrost:^25} yyy
BMI: {bmi:25.1f}
"""

# https://pyformat.info/

print(raport)
