n=int(input())
a=list(map(int, input().split()))
a.sort()
print((n-1)//2)
for i in range(0,n,2):
    if i==n-1:
        break
    a[i],a[i+1]=a[i+1],a[i]
print(*a)