def stones(k,a):
    dp=[False]*(k+1)
    for i in range(1,k+1):
        for j in a:
            if i-j>=0 and dp[i-j]==False:
                dp[i]=True
                break
    return dp[k]
n,k=map(int, input().split())
p=list(map(int, input().split()))
print("First" if stones(k,p) else "Second")