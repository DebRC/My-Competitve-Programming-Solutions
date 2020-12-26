mod=10**9+7
def twoset_tab(n,bal):
    dp=[[0 for i in range(bal+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,bal+1):
            if j-i<0:
                dp[i][j]=(dp[i-1][j])
            else:
                dp[i][j]=(dp[i-1][j]%mod+dp[i-1][j-i]%mod)
    return dp[n][bal]
 
n=int(input())
if (n*(n+1)//2)&1:
    print(0)
else:
    print(((twoset_tab(n,(n*(n+1))//4))//2)%mod)