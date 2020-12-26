def frog1(a, n):
    dp=[-1]*n
    dp[0]=0
    dp[1]=abs(a[1]-a[0])
    for i in range(2,n):
        dp[i]=min(abs(a[i]-a[i-1])+dp[i-1], abs(a[i]-a[i-2])+dp[i-2])
    return dp[n-1]
n=int(input())
jump=list(map(int, input().split()))
print(frog1(jump, n))