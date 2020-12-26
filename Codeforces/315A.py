n=int(input())
count=0
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i]=map(int, input().split())
for i in range(n):
    for j in range(n):
        if a[i]==b[j] and j!=i:
            count+=1
            break
print(n-count)