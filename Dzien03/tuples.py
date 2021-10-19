"""

Krotki czyli a'la struktura

"""
tuple1 = (200, "OK")
tuple2 = (200, "OK", False, (-1,1), -123.45 )
tuple3 = (200,) # krotka 1-elementowa

# wypisz "OK" z tuple2
print( tuple2[1] )
#tuple2[1] = "ERROR" # próba zmiany zawartości elementu tuple2
tuple2 = (200, "ERROR", False, (-1,1), -123.45 )

print(tuple2[3][0])
# var1 = tuple2[0]
# var2 = tuple2[1]
# var3 = tuple2[2]
# var4 = tuple2[3]
var1, var2, var3, var4, _ = tuple2 # _ = ślepa zmienna
x, y, z = 10, 20, 30
x=10; y=10; z=10; # jako działająca ciekawostka

print(var1, var2, var3, var4)