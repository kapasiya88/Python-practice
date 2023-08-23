# implement the function to print the count of each element in the given list.
l=[1,4,8,9,10,40,22,1,4,7,8,1]
l_set=set(l)
for i in l_set:
    print(i,l.count(i))


Output:
1 3
4 2
7 1
8 2
9 1
10 1
40 1
22 1