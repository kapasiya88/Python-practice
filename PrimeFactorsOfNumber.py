# Write a program to find the prime factors of a given number.
n=18
a=[]

for i in range(2,n+1):
    if n%i==0 and i!=2:
        prime=1
        for j in range(2,(i//2)+1):
            if i%j==0:
                prime=0
                break
            else:
                prime=1
        if prime==1:
            a.append(i)
    elif i==2:
        a.append(i)
print(a)