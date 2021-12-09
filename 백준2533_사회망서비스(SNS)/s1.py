import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline())
mat = [[] for _ in range(N + 1)]
check = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    mat[u].append(v)
    mat[v].append(u)
dp = [[0, 0] for _ in range(N + 1)]

check = [True for _ in range(N + 1)]


def dfs(cur):
    check[cur] = False
    dp[cur][0] = 1
    dp[cur][1] = 0
    for i in mat[cur]:
        if check[i]:
            dfs(i)
            dp[cur][0] += dp[i][1]
            dp[cur][1] += max(dp[i][0], dp[i][1])


dfs(1)
print(N - max(dp[1][0], dp[1][1]))