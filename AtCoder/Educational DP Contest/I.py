def coins(a,n,heads):
    dp=[[0 for i in range(heads+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,heads+1):
        dp[0][i]=0
    for i in range(1,n+1):
        for j in range(1,heads+1):
            dp[i][j]=a[i-1]*dp[i-1][j-1]+(1-a[i-1])*dp[i-1][j]
    return dp[n][heads]

n=int(input())
a=list(map(float, input().split()))
print(coins(a,n,(n+1)//2))