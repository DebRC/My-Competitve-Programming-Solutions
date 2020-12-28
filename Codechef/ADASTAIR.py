for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=0
    a.sort()
    a.insert(0,0)
    for j in range(1,n+1):
        if k//(a[j]-a[j-1])<1:
            m+=(a[j]-a[j-1])//k
            if (a[j]-a[j-1])%k==0:
                m-=1
    print(m)