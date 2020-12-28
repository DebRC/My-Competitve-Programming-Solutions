# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    m=0
    while(k>0):
        ans=n%k
        if(ans>m):
            m=ans
        k-=1
    print(m)