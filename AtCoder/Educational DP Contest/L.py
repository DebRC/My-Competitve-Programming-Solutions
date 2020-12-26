import sys
sys.setrecursionlimit(10**6)
def removal_game_memo(a, i, j, dp):
    if i > j:
        return 0
    if i == j:
        return a[i]
    if dp[i][j]!=-1:
        return dp[i][j]
    dp[i][j]=max(a[i] + min(removal_game_memo(a, i + 2, j, dp), removal_game_memo(a, i + 1, j - 1, dp)),
               a[j] + min(removal_game_memo(a, i + 1, j - 1, dp), removal_game_memo(a, i, j - 2, dp)))
    return dp[i][j]
n=int(input())
a=list(map(int, input().split()))
dp=[[-1 for i in range(n)] for i in range(n)]
x=removal_game_memo(a,0,n-1,dp)
#print(x)
y=sum(a)-x
print(x-y)