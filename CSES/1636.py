mod=10**9+7
def count(a,n,bal):
    dp=[0 for i in range(bal+1)] 
    dp[0]=1
    for i in range(0,n):
        for j in range(a[i],bal+1): 
            dp[j] = (dp[j] + dp[j-a[i]])%mod 
    return dp[bal]%mod
n,bal=map(int, input().split())
a=list(map(int, input().split()))
print((count(a,n,bal))%mod)