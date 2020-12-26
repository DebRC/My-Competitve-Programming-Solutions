mod=10**9+7
def matching(a,n):
    # creating dp table
    # dp[i][j] = no of ways to make pairs
    # where i = no of men
    # where j = permutation of 2^j binary numbers to represent
    #           number of woman selected as set bit and
    #           number of woman not yet selected as unset bit

    # (1<<n)=2^n
    dp=[[0]*((1<<n)+1) for _ in range(n+1)]

    # when there is no men and women then no of ways to make pairs is 0!=1
    dp[0][0]=1

    # i = no of men
    for i in range(n):
        # j = creating permuutation of women selected/not selected as a binary number with n bit
        # 0 means not selected and 1 means selected
        # Ex - 010 means 1st and 3rd women is not selected and 2nd woman is already selected
        for j in range(1<<n):
            if dp[i][j]==0:
                continue
            for k in range(n):
                # creating a mask with only the kth bit as set
                mask=1<<k
                # checking j with the mask to know which of the bits are unset and available for selection
                # using and operator to 'and' mask with j to know which bits are unset/not yet selected 
                if not(mask&j) and a[i][k]:
                    # j 'or' mask sets the kth bit which marks the kth bit as selected
                    dp[i+1][j|mask]+=dp[i][j]
    # return the dp state where n men and every women is available
    return dp[n][(1<<n)-1]%mod


n=int(input())
a = [list(map(int,input().split())) for _ in range(n)]
print(matching(a,n))