n=int(input())
if n==1:
    print(1)
elif n==2 or n==3:
    print("NO SOLUTION")
else:
    n1=[]
    n2=[]
    for i in range(1,n+1):
        if i%2==0:
            n1.append(i)
        else:
            n2.append(i)
    n1=n1+n2
    print(*n1)