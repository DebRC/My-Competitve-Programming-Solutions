mod=10**9+7
def gridpath_tab(s,n):
    dp=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        if s[i][0]=="*":
            break
        dp[i][0]=1
    for i in range(n):
        if s[0][i]=="*":
            break
        dp[0][i]=1
    for i in range(1,n):
        for j in range(1,n):
            if s[i][j]==".":
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
    #print(dp,sep="\n")
    return dp[n-1][n-1]%mod
n=int(input())
s=[]
for i in range(n):
    s.append(list(input()))
#print(s)
#print(gridpath(s,0,0,n))
print(gridpath_tab(s,n)%mod)