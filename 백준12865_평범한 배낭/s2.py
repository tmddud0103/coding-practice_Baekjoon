import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
nlist = [[0,0]] +[ list(map(int, sys.stdin.readline().split())) for _ in range(N)]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = nlist[i][0]
        value = nlist[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])