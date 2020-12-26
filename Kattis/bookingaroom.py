r,n=map(int,input().split())
a=[1]*r
for i in range(n):
    temp=int(input())
    a[temp-1]=0
flag=0
i=0
while(i<r):
    if a[i]==1:
        flag=1
        index=i+1
        break
    i+=1
if flag:
    print(index)
else:
    print("too late")