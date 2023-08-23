# Given string S and C is the list of cost of 
# removing a particular letter from S.Remove any consecutive letter from S having minimum cost.
# S='abccbd'
# C=[0,1,2,3,4,5]
# output_cost=2
# output_string='abcbd'
# s='aabbcc'
# c=[1,2,1,2,1,2]
# s='aaaa'
# c=[3,4,5,6]
s='ababa'
c=[10,5,10,5,10]
a=0
for i in range(0,(len(s)-1)):
    if s[i]==s[i+1]:
        if c[i] > c[i+1]:
            a+=c[i+1]
        else:
            a+=c[i]
    else:
        continue
print(a)