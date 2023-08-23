# implement a function to find the maximum subarray total in a given list.
from itertools import combinations
from functools import reduce
l=[1,2,3,5,6,7,8]
iter_init=0
for i in range (1,len(l)+1):
    l1=[]
    l1=list(combinations(l,i))
    print(l1)
    l2=[list(i) for i in list(l1)]
    print(l2)
    max_sublist = reduce(lambda x, y: x if sum(x) > sum(y) else y, l2)
    print(sum(max_sublist))
    iter_init=max(sum(max_sublist),iter_init)
    print('-----------------------')
print(iter_init)