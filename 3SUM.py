#3SUM
#https://leetcode.com/problems/3sum/description/
from itertools import combinations
j_list=[]
# nums = [-1,0,1,2,-1,-4]
# nums=[0,1,1]
nums=[0,0,0]
s_comb=list(combinations(nums,3))
s_comb_sum=[sorted(i) for i in s_comb if sum(i)==0]
for j in s_comb_sum:
    if j in j_list:
        continue 
    else:
        j_list.append(j)
print(j_list)
