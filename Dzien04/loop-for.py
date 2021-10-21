"""

Pętla iterująca

"""
list1 = [9, -10, 11, -100, 20, 0, 0.1, -1234]
list_res = []
ix = 1
# for x in list1:
#     #print(x)
#     if x>0:
#         list_res.append(x)
#         print(f"Wartość {x} jest na pozycji {ix}")
#     ix += 1 # ix = ix + 1

for ix, value in enumerate(list1, 1):
    if value==-10:
        continue

    if value==0.1:
        break
    if value>0:
        list_res.append(value)
        print(f"Wartość {value} jest na pozycji {ix}")

print(list_res)
