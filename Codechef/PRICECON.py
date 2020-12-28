# cook your dish here
t=int(input())
while(t>0):
    t-=1
    n,k=map(int, input().split())
    p=list(map(int, input().split()))
    rev=0
    for i in range(n):
        if(p[i]>k):
            rev+=(p[i]-k)
    print(rev)