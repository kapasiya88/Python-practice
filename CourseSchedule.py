# Course Schedule
# https://leetcode.com/problems/course-schedule/
from collections import Counter
numCourses = 2
prerequisites = [[1,0]]

pre_sorted=[str(sorted(i)) for i in prerequisites]
print(pre_sorted)
freq=Counter(pre_sorted)
print(freq)
freq_val=[val for key,val in freq.items()]
print(freq_val)
max_val=max(freq_val)
if max_val > 1:
    print (False)
else:
    print (True)