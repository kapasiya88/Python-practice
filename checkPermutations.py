# print all permutations of a text
from itertools import permutations
a1="abc"
 
# Finding all permutation
permutation = ["".join(p) for p in permutations(a1)]
print(permutation)