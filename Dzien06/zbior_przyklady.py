

zbior = {1, 2, 3}

print(zbior, type(zbior))

zbior2 = set([3, 4, 5])
print(zbior2)

print(dir(zbior2))
"""
[... 'add', 'clear', 'copy', 
'difference', 'difference_update', 'discard',
 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
 'issuperset', 'pop', 'remove', 'symmetric_difference', 
 'symmetric_difference_update', 'union', 'update']

"""

zbior2.add(6)
zbior2.add(4)
print(zbior2)


print(zbior | zbior2)  # suma
print(zbior & zbior2)  # iloczyn
print(zbior - zbior2)  # roznica
print(zbior2 - zbior)
print(zbior ^ zbior2)  # roznica symetryczna  {1, 2, 3} ^ {3 , 4, 5} ==> {1, 2, 4, 5}  suma - iloczyn

#
