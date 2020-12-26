mod=10**9+7
def candies(a, n, k):
    dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        prefix_sum=[0]*(k+1)
        prefix_sum[0]=dp[i-1][0]
        for j in range(1,k+1):
            prefix_sum[j]=(prefix_sum[j-1]+dp[i-1][j])%mod
        for j in range(1,k+1):
            if j<=a[i-1]:
                dp[i][j]=prefix_sum[j]%mod
            else:
                dp[i][j]=(prefix_sum[j]-prefix_sum[j-a[i-1]-1])%mod
    return dp[n][k]%mod
n,k=map(int, input().split())
a=list(map(int, input().split()))
print(candies(a,n,k))