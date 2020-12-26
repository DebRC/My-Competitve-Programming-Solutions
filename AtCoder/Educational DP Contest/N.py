import sys
sys.setrecursionlimit(10**6)
dp=[[-1 for _ in range(401)] for _ in range(401)]
prefix_sum=[0]*(401)
def slimes(a, n):
    prefix_sum[0]=a[0]
    for i in range(1,n):
        prefix_sum[i]=prefix_sum[i-1]+a[i]
    #print(prefix_sum)
    return solve(a,0,n-1)

def solve(a,i,j):
    if i==j:
        return 0
    if dp[i][j]>-1:
        return dp[i][j]
    ways=sys.maxsize
    for k in range(i,j):
        if i==0:
            ways=min(ways,(solve(a,i,k)+solve(a,k+1,j)+prefix_sum[k]+prefix_sum[j]-prefix_sum[k]))
        else:
            ways=min(ways,(solve(a,i,k)+solve(a,k+1,j)+(prefix_sum[k]-prefix_sum[i-1])+prefix_sum[j]-prefix_sum[k]))
    dp[i][j]=ways
    return dp[i][j]
    
n=int(input())
a=list(map(int, input().split()))
print(slimes(a,n))