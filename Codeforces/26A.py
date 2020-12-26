n=int(input())
x=[0]*(n+1)
for i in range (2,n+1):
    if x[i]==0:
        for j in range(2*i,n+1,i):
            x[j]+=1
print(x.count(2))