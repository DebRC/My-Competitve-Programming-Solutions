n=int(input())
a=list(map(int, input().split()))
total=0
i=0
while(1):
    total+=a[i]
    if total>=n:
        break
    i+=1
    if i==7:
        i=0
print(i+1)