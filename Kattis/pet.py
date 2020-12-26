best=0
i=1
while(i<=5):
    a=list(map(int, input().split()))
    total=sum(a)
    if total>=best:
        best=total
        index=i
    i+=1
print(index,best)