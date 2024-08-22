import sys
import itertools 

a_list = str(input())
a_tuple = tuple()
b_list = sorted(a_list)
# HACa_list = [1,2,3,4,5]
a_tuple = (1,2,3,4,5)

print(a_list)
print(a_tuple)
for i in a_list:
    if i <= 0:
        print(*b_list, sep="\n")
    elif:
        print(listcombina((a_list,2)), sep = "\n")