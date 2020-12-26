n=int(input())
count=0
for i in range(n):
    temp=list(map(int, input().split()))
    if temp.count(1)>1:
        count+=1
print(count)