# binary search algorithm to find a target into a sorted list.
nums=[1,5,8,10,29,34,67]
target=2

def binary_search(nums,target,low,high):
    if high >= low:
        mid=(low+high)//2
        if target==nums[mid]:
            return (mid)
        elif target < nums[mid]:
            return (binary_search(nums,target,low,mid-1))
        else:
            return (binary_search(nums,target,mid+1,high))
    else:
        return (-1)
        
final_search=binary_search(nums,target,0,len(nums)-1)
print('final_search is {}'.format(final_search))