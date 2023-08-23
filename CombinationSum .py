# https://leetcode.com/problems/combination-sum/description/

from itertools import combinations_with_replacement
class Solution:

    def combinationSum(self, candidates, target):
        l=[]
        no_of_iter=(target//min(candidates))+1
        for i in range(1,no_of_iter+1):
            l1=combinations_with_replacement(candidates,i)
            l+=l1
        l2=[i for i in l if sum(i)==target]
        return l2



obj=Solution()
print(obj.combinationSum(candidates,target))

# Examples:
# 1) candidates = [2,3,5]
# target = 8

# print(obj.combinationSum(candidates,target))
# # Output: [[2,2,2,2],[2,3,3],[3,5]]

# 2) candidates = [2,3,6,7]
# target = 7

# print(obj.combinationSum(candidates,target))
# # Output: [[2,2,3],[7]]

# 3) candidates = [2]
# target = 1

# print(obj.combinationSum(candidates,target))
# # Output: []