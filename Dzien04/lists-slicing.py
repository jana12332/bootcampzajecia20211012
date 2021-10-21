"""
 "Krojenie" list
"""
#        0    1   2   3  4   5    6   7  8    9
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#       -10  -9  -8  -7  -6  -5  -4  -3  -2   -1
print(list1[8], list1[-2])

# Zasada 3xS
# [ START : STOP : STEP ]

#30, 40, 50, 60, 70,
print(list1[2:7])  # = <2,7)

# 40, 50, 60, 70, 80, 90, 100
#print(list1[3:10])
print(list1[3:])

# 10, 20, 30
#print(list1[0:3])
print(list1[:3])

# [10,  30,  50,  70,  90]
print(list1[::2])

# lista odwrócona
#list1.reverse()
print(list1[::-1])

# sortowanie
lista2 = [9, -10, 11, -100, 20, 0, 0.1, -1234]
lista2.sort(reverse=True)
print(lista2)

def sort_tuple(x):
    return x[1]

lista3 = [ ("Marek",2), ("Julian", 4), ("Zenek",1) ]
lista3.sort(key=sort_tuple)
print(lista3)