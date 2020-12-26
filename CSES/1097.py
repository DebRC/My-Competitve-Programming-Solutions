def removal_game_tab(a, n):
    dp=[[0 for i in range(n)] for i in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if i==j:
                dp[i][i]=a[i]
            else:
                dp[i][j] = max(a[i]-dp[i+1][j],a[j]-dp[i][j-1])
    return dp[0][n-1]
    
n = int(input())
a = list(map(int, input().split()))
print((sum(a)+removal_game_tab(a,n))//2)