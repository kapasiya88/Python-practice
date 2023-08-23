# check if given number is prime?
n=15
l=[i for i in range(2,n) if n%i==0]
if len(l)>0:
    print("Not prime")
else:
    print("Prime")