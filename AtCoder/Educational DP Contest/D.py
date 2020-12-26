def knapsack1(n, c, w, v):
    dp=[[0 for i in range(c+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,c+1):
            if j<w[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(v[i-1]+dp[i-1][j-w[i-1]],dp[i-1][j])
    return dp[n][c]
n,c=map(int, input().split())
w=[0]*n
v=[0]*n
for i in range(n):
    w[i],v[i]=map(int, input().split())
print(knapsack1(n, c, w, v))