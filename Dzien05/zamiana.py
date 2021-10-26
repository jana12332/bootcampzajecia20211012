# sposob 1

print(list("123"))
list_ = [2, 1, 3, 5, 4]

index_min = 0
index_max = 0

# podejscie po wartosciach
for el in list_:
    if el < list_[index_min]:
        index_min = list_.index(el)
    if el > list_[index_max]:
        index_max = list_.index(el)
# podejscie po indeksach

# list_len = len(list_)
# for i in range(list_len):
#     el = list_[i]
#     if el < list_[index_min]:
#         index_min = i
#     if el > list_[index_max]:
#         index_max = i

tmp = list_[index_min]
list_[index_min] = list_[index_max]
list_[index_max] = tmp

a, b = 1, 2

a, b = b, a  # a, b = 2, 1

# rownowazne podejscie:
# list_[index_min], list_[index_max] = list_[index_max], list_[index_min]


# range(3) -> 0, 1, 2
# print(list("123"))
# [2, 1, 3, 5, 4]("123")

min_v = min(list_)
max_v = max(list_)


i_min_v = list_.index(min_v)  # list_.index(min(list_))
i_max_v = list_.index(max(list_))  # list_.index(max_v)


list_[i_min_v], list_[i_max_v] = list_[i_max_v], list_[i_min_v]