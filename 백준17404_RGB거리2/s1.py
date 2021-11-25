import sys
sys.stdin = open('input.txt')
n = int(sys.stdin.readline().lstrip())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 100000000
for color in range(3):
    dp = [[0 for _ in range(3)] for _ in range(n)]
    for i in range(3):
        if i == color:
            dp[0][i] = mat[0][i]
        else:
            dp[0][i] = 100000000
    for i in range(1, n):
        dp[i][0] = mat[i][0] + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = mat[i][1] + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = mat[i][2] + min(dp[i-1][1],dp[i-1][0])
    for i in range(3):
        if i != color:
            result = min(result, dp[-1][i])
print(result)
