# find sum of all digits of a number
from functools import reduce
n=str(956)
final_sum=reduce(lambda x,y:int(x)+int(y),n)
print(final_sum)
