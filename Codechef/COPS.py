# cook your dish here
for _ in range(int(input())):
    m,x,y=map(int,input().split())
    cops=list(map(int,input().split()))
    a=[0]*100
    p=x*y
    c=0
    for i in range(m):
        upper=cops[i]+p-1
        if upper>99:
            upper=99
        lower=cops[i]-p-1
        if lower<0:
            lower=0
        for j in range(lower,upper+1):
            a[j]+=1
    for i in range(100):
        if a[i]==0:
            c+=1
    print(c)