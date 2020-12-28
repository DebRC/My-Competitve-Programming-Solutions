# cook your dish here
n,k=map(int, input().split())
a=[0]*n
for i in range(k):
    t=list(input().split())
    if t[0]=="CLICK":
        c=int(t[1])
        if(a[c-1]==0):
            a[c-1]+=1
        else:
            a[c-1]=0
    else:
        a=[0]*n
    print(sum(a))