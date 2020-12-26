def frog2(a, n, k):
    dp=[99999999999999]*n
    dp[0]=0
    dp[1]=abs(a[1]-a[0])
    for i in range(2,n):
        for j in range(1,k+1):
            if j>i:
                break
            dp[i]=min(dp[i], abs(a[i]-a[i-j])+dp[i-j])
    return dp[n-1]
n,k=map(int, input().split())
jump=list(map(int, input().split()))
print(frog2(jump, n, k))