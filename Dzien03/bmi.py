"""

 Skrypt obliczający BMI

 BMI = waga (kg) / wzrost (m^2)
 Uwaga! - wzrost podajemy w cm
"""
weight = input("Podaj wagę w kg:")
height = input("Podaj wzrost w cm:")

weight = int(weight) # konwertujemy z napisu na int
height = int(height) # konwertujemy z napisu na int

# liczenie formuły
# bmi = weight / pow( height/100 , 2)
# print(bmi)

bmi = weight / (height/100)**2
#print("Twoje BMI = "+str( round(bmi,2) ))
print(f"Twoje BMI = {bmi:.2f}")

# import math
# bmi = weight / math.pow(  height/100 , 2 )
# print(bmi)

"""
<18.5 - zjedz coś
>=18.5 i <25 - ok
>= 25 - ogranicz kebaby
"""

# if bmi>=25:
#     print("ogranicz kebaby")
#     print("ogranicz monsterki")
# elif bmi<18.5:
#     print("zjedz coś")
# else:
#     print("OK")

if bmi>=18.5 and bmi<25:
    print("OK")
elif bmi>=25:
    print("ogranicz kebaby")
    print("ogranicz monsterki")
    if bmi>35:
        print("Do lekarza")
elif bmi<18.5:
    print("zjedz coś")
else:
    pass # celuloza w Pythonie

#print(weight, height)
