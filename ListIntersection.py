# print common elements between two lists
l1=[1,2,3,5,6,7,2,3,8,8]
l2=[3,5,2,8,9]
l1_set=set(l1)
l2_set=set(l2)
print(l1_set.intersection(l2_set))