n=int(input())
a=list(map(int, input().split()))
total=0
for i in range(n):
    if a[i]<0:
        total+=abs(a[i])
print(total)