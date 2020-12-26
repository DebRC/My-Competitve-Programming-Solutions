import sys
sys.setrecursionlimit(10**6)
mod=10**9+7
def grid(a,h,w,dp):
    if h==1 and w==1:
        return 1
    if h<1 or w<1:
        return 0
    if a[h-1][w-1]=="#":
        return 0
    if dp[h][w]>-1:
        return dp[h][w]%mod
    dp[h][w] = (grid(a,h-1,w,dp)+grid(a,h,w-1,dp))%mod
    return dp[h][w]%mod
h,w=map(int, input().split())
a=[]
for i in range(h):
    a.append(list(input()))
dp=[[-1 for i in range(w+1)] for i in range(h+1)]
#print(a)
print(grid(a,h,w,dp))