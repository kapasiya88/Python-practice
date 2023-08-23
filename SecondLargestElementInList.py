# write a program to find the second largest element in a list.
l=[1,4,8,9,10,40,22,1,4,7,8,1]
l_set=set(l)
list_l_set=list(l_set)
list_l_set.sort(reverse=True)
print(list_l_set[1])
# NOTE:if you directly print the sort command,it will print None. eg: print(list_l_set.sort(reverse=True))