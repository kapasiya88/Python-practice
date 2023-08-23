# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class solution:
    def validate_occurance(self,nums,target):
        if target in nums:
            return (nums.index(target))
        else:
            return -1
        

# example:
# Input: 
# nums = [4,5,6,7,0,1,2]
# target = 0

# nums = [4,5,6,7,0,1,2]
# target = 8
# obj=solution()
# param1=obj.validate_occurance(nums,target)
# print(param1)