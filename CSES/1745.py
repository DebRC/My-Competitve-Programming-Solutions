def moneysum(a,n):
    bal=sum(a)
    dp=[[False for i in range(bal+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,bal+1):
            if j-a[i-1]<0:
                dp[i][j]=(dp[i-1][j])
            else:
                dp[i][j]=(dp[i-1][j] or dp[i-1][j-a[i-1]])
    #print(dp)
    m=set()
    for i in range(n+1):
        for j in range(1,bal+1):
            if dp[i][j]:
                m.add(j)
    m=list(m)
    print(len(m))
    print(*sorted(m))
 
n=int(input())
a=list(map(int, input().split()))
moneysum(a,n)