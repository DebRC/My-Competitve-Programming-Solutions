INF=10**10
def knapsack2(n, c, w, v):
    max_value=sum(v)
    dp=[[INF for i in range(max_value+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
    for i in range(1,n+1):
        for j in range(1,max_value+1):
            if j<v[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=min(w[i-1]+dp[i-1][j-v[i-1]],dp[i-1][j])
    res=0
    for i in range(max_value+1):
        if dp[n][i]<=c:
            res=i
    return res
n,c=map(int, input().split())
w=[0]*n
v=[0]*n
for i in range(n):
    w[i],v[i]=map(int, input().split())
print(knapsack2(n, c, w, v))