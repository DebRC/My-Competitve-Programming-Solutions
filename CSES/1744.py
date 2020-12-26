import sys
def cutting_tab(l,b):
    dp=[[0 for _ in range(b+1)] for _ in range(l+1)]
    for i in range(1,l+1):
        for j in range(1,b+1):
            if i==j:
                continue
            else:
                ans=sys.maxsize
                for k in range(1,i):
                    ans=min(ans,1+dp[i-k][j]+dp[k][j])
                for k in range(1,j):
                    ans=min(ans,1+dp[i][j-k]+dp[i][k])
                dp[i][j]=ans
    return dp[l][b]
    
l,b=map(int, input().split())
print(cutting_tab(l, b))