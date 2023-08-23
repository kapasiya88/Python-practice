# print the numbers indices from the array whose sum equals to target.
# chain is the class from itertools to flatten 2d array to 1 d array.
from itertools import combinations,chain
nums = [2,7,11,15]
target = 18
l=combinations(nums,2)
l1=list(list(i) for i in l if sum(i)==target)
print(l1)
flatten_list = list(chain.from_iterable(l1))
print(flatten_list)
print([nums.index(i) for i in flatten_list])