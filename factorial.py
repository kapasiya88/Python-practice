# print factorial of a number
n=6
fact=1
if (n==0 or n==1):
    fact=1
else:
    for i in range(n,0,-1):
        fact*=i
print(fact)