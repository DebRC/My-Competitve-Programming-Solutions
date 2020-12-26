def sushi(p, n):
    x = p.count(1)
    y = p.count(2)
    z = p.count(3)
    dp = [[[0] * (n + 2) for i in range(n + 2)] for j in range(n + 2)]
    for i in range(z + 1):
        for j in range(n - x - i + 1):
            for k in range(n - i - j + 1):
                if i + j + k:
                    dp[i][j][k] = (n + (k * dp[i][j][k - 1]) + (j * dp[i][j - 1][k + 1]) + (
                                i * dp[i - 1][j + 1][k])) / (i + j + k)
    return dp[z][y][x]


n = int(input())
p = list(map(int, input().split()))
print(sushi(p, n))
