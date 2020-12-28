# cook your dish here
t=int(input())
while(t>0):
    n=int(input())
    if(n==0):
        print(0)
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        print(fact)
    t-=1