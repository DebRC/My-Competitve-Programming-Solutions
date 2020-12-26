n=int(input())
na=list(map(int, input().split()))
m=int(input())
ma=list(map(int, input().split()))
na.sort()
ma.sort()
count=0
for i in range(n):
    for j in range(m):
        if abs(na[i]-ma[j])<=1:
            count+=1
            ma[j]=1000
            break
print(count)