# "Madam, I'm Adam"
# “A man, a plan, a canal—Panama,”
# “Able was I ere I saw Elba”
from itertools import combinations
s_list=[]
s="A man, a plan, a canal—Panama,"
for i in range(1,len(s)+1):
    s_comb=list(combinations(s,i))
    s_list.append(s_comb)
print(s_list)