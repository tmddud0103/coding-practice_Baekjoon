import sys
n = int(sys.stdin.readline())
dp = [0]*1000001
dp[0] = 1000000
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    a, b = 0, 0

    if i % 2 == 0:
        a = i // 2

    if i % 3 == 0:
        b = i // 3

    dp[i] = min(dp[i-1]+1,dp[a]+1,dp[b]+1)
dp[1] = 0
print(dp[n])