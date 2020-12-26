def vacation(a, n):
    dp=[[-1 for i in range(3)] for i in range(n)]
    for i in range(3):
        dp[0][i]=a[0][i]
    for i in range(1,n):
        for j in range(3):
            dp[i][j]=a[i][j]+max(dp[i-1][(j+1)%3],dp[i-1][(j+2)%3])
    return max(dp[n-1])
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int, input().split())))
#print(a)
print(vacation(a, n))