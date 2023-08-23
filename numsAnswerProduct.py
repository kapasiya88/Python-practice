# Given an integer array nums, return an array answer such that answer[i] is equal to the product of 
# all the elements of nums except nums[i].

from itertools import combinations
import math
# nums = [1,2,3,4]
# answer=[24,12,8,6]
nums = [-1,1,0,-3,3]
answer=[0, 0, 9, 0, 0]
nums_sub=[]

for i in range (0,len(nums)):
    nums_sub1=[nums[j] for j in range(0,len(nums)) if j!=i]
    nums_sub.append(nums_sub1)
l=[math.prod(i) for i in nums_sub]
print(l)