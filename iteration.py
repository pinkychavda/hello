from itertools import combinations 
from itertools import islice
name = str(input())
name = sorted(name)
for i in islice(name,1):
    print(name[i],end="")
    